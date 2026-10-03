export async function onRequestPost(context) {
  const { request, env } = context;

  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  };

  let body;
  try {
    body = await request.json();
  } catch {
    return new Response(JSON.stringify({ ok: false, error: 'Invalid request body' }), { status: 400, headers });
  }

  const { form_type, name, email, company, service, message, voice_type, voice_name, text: voiceText, chars, price_usd, tier_rate, _hp, _t0 } = body;

  // Bot guards (server-side mirror of client checks)
  if (_hp) {
    return new Response(JSON.stringify({ ok: true }), { headers }); // silently accept bots
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email || '')) {
    return new Response(JSON.stringify({ ok: false, error: 'invalid_email' }), { status: 400, headers });
  }

  const webhookUrl = env.FEISHU_WEBHOOK;
  if (!webhookUrl) {
    return new Response(JSON.stringify({ ok: false, error: 'server_config' }), { status: 500, headers });
  }

  let text;
  if (form_type === 'voice_request') {
    // Self-serve TTS request from the dubbing voice catalog. The message carries
    // everything needed to execute the job: voice ID + text + char count + quote.
    if (!voice_type || !voiceText) {
      return new Response(JSON.stringify({ ok: false, error: 'missing_fields' }), { status: 400, headers });
    }
    text = [
      '🎙️ Voice Dubbing Request — MediaLocalize',
      '',
      `Email:     ${email}`,
      `Voice:     ${voice_name || '—'}`,
      `Voice ID:  ${voice_type}`,
      `Engine:    Volcano Engine Doubao TTS 2.0 (cluster: volcano_tts)`,
      `Chars:     ${chars ?? '—'}`,
      `Quote:     $${price_usd ?? '—'} (tier $${tier_rate ?? '—'}/5k chars)`,
      '',
      '--- Text to synthesize ---',
      String(voiceText).slice(0, 5000),
    ].join('\n');
  } else {
    if (!name || !service || !message) {
      return new Response(JSON.stringify({ ok: false, error: 'missing_fields' }), { status: 400, headers });
    }
    text = [
      '📬 New Inquiry — MediaLocalize',
      '',
      `Name:    ${name}`,
      `Email:   ${email}`,
      `Company: ${company || '—'}`,
      `Service: ${service}`,
      '',
      'Message:',
      message,
    ].join('\n');
  }

  try {
    const res = await fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ msg_type: 'text', content: { text } }),
    });
    const data = await res.json();
    if (data.code === 0 || data.StatusCode === 0) {
      return new Response(JSON.stringify({ ok: true }), { headers });
    }
    return new Response(JSON.stringify({ ok: false, error: 'webhook_error', detail: data.msg }), { status: 502, headers });
  } catch (err) {
    return new Response(JSON.stringify({ ok: false, error: 'network_error' }), { status: 502, headers });
  }
}

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}
