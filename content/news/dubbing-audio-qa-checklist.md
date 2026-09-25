---
title: "Audio QA for Dubbed Content: A Listener's Checklist"
date: 2027-01-25T13:10:00+08:00
publishDate: 2027-01-25T13:10:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["dubbing", "quality assurance", "audio QA", "AI voice"]
keywords: ["dubbing quality assurance", "audio qa checklist", "dubbed audio review"]
cover: "/images/news/dubbing-audio-qa-checklist.jpg"
author: "MediaLocalize Team"
summary: "The dubbing studio delivered 40 files. Nobody on your team speaks Vietnamese. You approved them anyway — and the product name is mispronounced in all 40. Audio QA is a distinct discipline with its own checklist; here's how to run it even without in-house linguists."
---

A training provider ships a dubbed course in six languages. Two weeks later the German client reports that the narrator says the wrong product name in module three, the Spanish version's background music ducks under the voice so aggressively it sounds like a pumping heartbeat, and the Arabic files are 44.1 kHz while everything else is 48 kHz — which breaks their LMS import. None of these are translation problems. None were caught because nobody ran *audio* QA: the distinct pass that listens to what was delivered, against a checklist, before it ships. Here is that checklist, organized so a project manager without language skills can run most of it — and knows exactly which parts need a native ear.

## Why audio QA is its own pass

Dubbing projects usually get two reviews: script review (before recording) and a final "sounds fine" spot check. Between those two sits a gap where most defects live. A perfectly translated script can still be recorded with the wrong pronunciation lexicon, mixed with music that masks consonants, edited with 200 ms gaps that make every sentence sound hesitant, or exported with the wrong loudness for the target platform. As we covered in [script adaptation timing](/news/dubbing-script-adaptation-timing/), timing problems start at the script — but they *surface* in the audio, and only a listener will catch them. AI dubbing changes the error mix, not the need for QA: [AI voices](/news/how-ai-dubbing-works/) rarely stumble mid-sentence, but they confidently mispronounce the same term 200 times in a row.

## The checklist, in listening order

Run the passes in this order — each is cheaper than the next, and early passes catch showstoppers before you waste a native reviewer's time on a file that will be redone anyway.

1. **Technical conformance (no listening, 5 minutes).** Sample rate, bit depth, channels, format, loudness (target platform: −16 LUFS for most LMS/web, −23/−24 for broadcast specs), file naming, and count against the delivery manifest. A third of "audio problems" are spec mismatches found here.
2. **Completeness pass (scrub every file).** Play each file at 1.5–2× speed, watching the waveform. You're checking: no truncated endings, no double-takes left in, no long dead air, duration within tolerance of the source (±5–10% depending on how much [adaptation](/news/dubbing-script-adaptation-timing/) was planned).
3. **Mix pass (sample every file, full-listen a subset).** Voice-to-music ratio, ducking smoothness, consistent levels across files, no clipping. Listen on laptop speakers *and* headphones — learners use both, and a mix that's fine on headphones can bury the voice on a phone speaker.
4. **Pronunciation and terminology (native listener + glossary).** The single highest-value pass. The listener checks every glossary term, product name, and brand against the [pronunciation lexicon](/news/ai-voice-pronunciation-lexicon/) — and flags anything that sounds wrong even if it's *not* in the glossary. One mispronounced product name in a flagship demo undermines the whole [video localization investment](/news/product-demo-video-localization/).
5. **Performance and fit (native listener).** Pace matches the on-screen action, emphasis lands on the right words, [narration style](/news/elearning-voiceover-narration-styles/) is consistent with what was cast, and — for lip-sync contexts — lines land on visible mouth movements within tolerance.
6. **Consistency across the set.** Same character, same voice, same energy in module 12 as in module 1; terms pronounced identically across all files; intros/outros identical where they should be.

## The defect taxonomy (and what each costs)

Triage findings into four buckets — it keeps the fix conversation rational:

| Defect class | Example | Severity | Typical fix cost |
|---|---|---|---|
| **Blocking** | Wrong product name pronounced; missing sentence; file won't import | Ship-stopper | Re-record/re-render affected lines |
| **Major** | Glossary term mispronounced; voice/music balance buries words; audible edit artifacts | Fix before release | Pickup lines or remix |
| **Minor** | One flat delivery in 40 files; slight pace mismatch on a transition | Fix if cheap | Usually notes for next project |
| **Style** | "I'd have emphasized a different word" | Document, don't fix | Add to the lexicon/style guide |

The discipline matters: without severity classes, every note becomes "must fix," the studio pushes back, and the review cycle eats the schedule you saved by dubbing instead of subtitling. With them, a 40-file review converges in one or two rounds.

## Who listens to what

You don't need six in-house linguists. The split that works:

- **PM / producer**: passes 1–3 and 6 — technical, completeness, mix, consistency. These need ears and a stopwatch, not language skills.
- **Native listener per language**: passes 4–5. This can be a client-side employee, a distributor, or a reviewer hired by the hour — but it must be someone with stake in the outcome, briefed with the glossary and lexicon *before* they listen, and given a timestamped feedback template (file, timecode, expected, heard, severity).
- **The studio or AI pipeline owner**: closes the loop. For AI dubbing, most pronunciation fixes are lexicon entries — one correction propagates everywhere, which is why the [lexicon discipline](/news/ai-voice-pronunciation-lexicon/) pays for itself by the second project.

## Making it cheaper next time

Every finding from pass 4–5 should flow back into three assets: the pronunciation lexicon, the translation glossary, and the style guide. Do that, and each project's QA pass gets shorter — the second German course has a fraction of the findings of the first. Skip it, and you pay the same review cost forever.

Audio QA is typically 5–10% of a dubbing budget and catches the defects that cost 100% of a client's trust. Our [dubbing team](/services/localization/dubbing/) builds the QA passes above into every project — human and AI pipelines alike — with lexicons and glossaries that persist across your content library. [Send us a delivered project](/contact/) and we'll run the checklist on it as an audit.
