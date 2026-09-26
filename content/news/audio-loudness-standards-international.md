---
title: "Loudness Standards for International Audio Delivery"
date: 2027-04-26T08:14:00+08:00
publishDate: 2027-04-26T08:14:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["Dubbing", "audio production", "loudness", "delivery specs"]
keywords: ["loudness standards ebu r128", "audio delivery specs", "lufs normalization dubbing"]
cover: "/images/news/audio-loudness-standards-international.jpg"
author: "MediaLocalize Team"
summary: "Your corporate video plays whisper-quiet on YouTube, blasts on LinkedIn, and gets rejected by a European broadcaster for exceeding -23 LUFS. Loudness — not peak level, but perceived volume measured over time — is regulated, platform-specific, and invisible until it breaks. The standards that matter (EBU R128, ATSC A/85, platform specs), what the numbers mean, and how to spec multilingual audio deliveries that pass everywhere."
---

A marketing team delivers their newly-dubbed product video: English, German, Japanese. On their editing monitors all three sound identical. Then reality: YouTube turns the English version down but not the German (now they differ), LinkedIn's feed makes the Japanese one sound crushed, and a German trade-fair organizer running it on the hall's broadcast system reports distortion. The mix engineer insists the peaks never clipped — and he's right, because peaks were never the problem. The problem is **loudness**: perceived volume measured as an integrated average (LUFS), not instantaneous peaks (dBFS). Every broadcast market and platform has its own loudness target, deliverables that miss it get rejected or auto-adjusted (badly), and multilingual programs multiply the risk — N languages, each needing to hit the same spec, on every platform. Here's what the numbers mean and how to spec deliveries once, correctly.

## Loudness 101: the terms that matter

- **LUFS (or LKFS)** — the unit of perceived loudness; 1 LU ≈ 1 dB. Three measurements exist: **Integrated** (average over the whole program — the number specs care about), **Short-term** (3-second window), **Momentary** (400 ms).
- **True Peak (dBTP)** — the actual peak of the reconstructed analog signal, which can exceed the digital sample peak; specs cap it (typically -1 or -2 dBTP) to prevent distortion after encoding. "My meter showed no clipping" usually means sample peaks were fine while true peaks weren't.
- **LRA (Loudness Range)** — the dynamic spread of the program, in LU. Broadcast specs sometimes cap it; podcasts and web video mostly don't, but wildly varying LRA (whispered intro, shouted demo) makes any single normalization sound wrong.

The key mental shift from the peak-meter era: **normalization is now loudness-based, not peak-based.** Two files can both peak at -1 dBFS and differ in loudness by 10 LU — that's your "YouTube turned one down" scenario.

## The standards map

| Target | Integrated loudness | True Peak | Where it applies |
|---|---|---|---|
| **EBU R128** (Europe broadcast) | -23 LUFS ±0.5 | -1 dBTP | European broadcasters, trade-fair/hall broadcast systems, many corporate AV specs |
| **ATSC A/85 (CALM Act)** | -24 LUFS ±2 | -2 dBTP | US broadcast |
| **YouTube** | ~-14 LUFS normalization target | — | Turns louder content *down* (quiet content is left alone) |
| **Spotify** | -14 LUFS | -1 dBTP | Podcast/audio platforms broadly similar |
| **Apple Podcasts** | -16 LUFS | -1 dBTP | Audio-first deliverables |
| **Social feeds (Meta/LinkedIn/TikTok)** | ~-14 LUFS de facto | — | Heavy compression of dynamics on playback |

Note the structure: **broadcast is quiet (-23/-24), online platforms are loud (-14 to -16)**. One master cannot be optimal for both — which is why "we have one audio file" is a delivery problem, not simplicity.

## Why multilingual programs fail at this

1. **Each language is mixed separately** — often by different vendors — and "sounds the same on my speakers" varies by studio. Language A lands at -18 LUFS, language B at -26: after platform normalization, they play at different volumes *and* the quieter one reveals noise.
2. **AI/human hybrid tracks drift.** AI-generated segments and studio-recorded segments have different dynamics; without a unified [loudness pass at the mix stage](/news/hybrid-ai-human-voiceover-workflow/), the seams are audible as volume jumps.
3. **Deliverable proliferation.** 5 languages × 3 targets (broadcast -23, web -14, podcast -16) = 15 loudness variants — unless the pipeline renders them from one mix systematically, someone normalizes by hand and files diverge.
4. **Encoding reveals true peaks.** A file at 0 dBFS sample peak distorts after AAC/Opus encoding even if it looked clean — true-peak limiting at -1 dBTP is the fix, applied before delivery, not discovered by the platform.

## The practical delivery spec (steal this)

Put this in every audio/voiceover brief — your [vendor brief template](/news/localization-vendor-brief-template/) should carry it verbatim:

1. **Master mix**: dialogue-normalized, music and effects mixed to taste, then the whole program measured — not eyeball-matched.
2. **Web/video master**: -14 LUFS integrated, true peak ≤ -1 dBTP, one file per language. (Covers YouTube, LinkedIn, website embeds, [product videos](/news/product-demo-video-localization/) generally.)
3. **Broadcast/fair master** (if ever played on broadcast infrastructure): -23 LUFS integrated ±0.5, true peak ≤ -1 dBTP, EBU R128 compliant — and confirm the target's actual spec sheet, since some halls and broadcasters publish their own.
4. **Every language measured and documented**: a one-line loudness report per file (integrated LUFS, true peak, LRA) from a real meter (EBU-mode loudness meter, or ffmpeg's `loudnorm` printout) — not "engineer says it sounded right."
5. **Consistency across languages**: all languages within ±0.5 LU of each other for the same target — so the language switcher never changes perceived volume.

## The workflow that makes this boring

Mix once per language → measure → correct with a loudness-normalization pass (transparent limiting, not brute gain) → render the per-target variants from the mastered mix → verify the render, not the session. ffmpeg's two-pass `loudnorm` does this reliably and scriptably, which means the 15-variant problem is a batch job, not 15 mixing sessions. For ongoing programs — [course libraries](/news/batch-video-localization-course-libraries/), video series — build the loudness spec into the delivery checklist so every future file passes by default.

Loudness is the least glamorous spec in audio and the one most likely to get your video rejected, turned down, or played at three different volumes in three languages. Our [dubbing team](/services/localization/dubbing/) delivers every language with measured, documented loudness — R128 for broadcast targets, -14 LUFS for the web, consistent across your whole language set. [Send us your platform list](/contact/) and we'll spec the deliverables once, correctly.
