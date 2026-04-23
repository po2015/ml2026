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

  const { name, email, company, service, message, _hp, _t0 } = body;

  // Bot guards (server-side mirror of client checks)
  if (_hp) {
    return new Response(JSON.stringify({ ok: true }), { headers }); // silently accept bots
  }
  if (!name || !email || !service || !message) {
    return new Response(JSON.stringify({ ok: false, error: 'missing_fields' }), { status: 400, headers });
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return new Response(JSON.stringify({ ok: false, error: 'invalid_email' }), { status: 400, headers });
  }

  const webhookUrl = env.FEISHU_WEBHOOK;
  if (!webhookUrl) {
    return new Response(JSON.stringify({ ok: false, error: 'server_config' }), { status: 500, headers });
  }

  const text = [
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
