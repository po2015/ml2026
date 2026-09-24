---
title: "Subtitle Formatting: Line Length, Speed, and Timing"
date: 2026-10-26T18:44:00+08:00
publishDate: 2026-10-26T18:44:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["Video Localization", "subtitles", "captioning", "translation"]
keywords: ["subtitle formatting rules", "subtitle line length", "reading speed cps"]
cover: "/images/news/subtitle-formatting-rules.jpg"
author: "MediaLocalize Team"
summary: "Bad subtitles make good videos unwatchable. The professional rules for line length, reading speed, and timing — and how they change when subtitles are translated."
---

Two subtitle tracks can contain identical translations and produce completely different viewing experiences. One is invisible — viewers absorb it without noticing. The other has them rewinding, pausing, and eventually closing the video. The difference is formatting: line length, reading speed, and timing rules that professional subtitlers treat as constraints, not suggestions.

These rules matter twice over in localization, because translation changes text length and reading speed in ways that break naive subtitle workflows. Here is what the standards actually say, and what changes when subtitles cross languages.

## Line length: the 42-character ceiling

The near-universal professional standard:

- **Maximum ~42 characters per line** (including spaces) for Latin scripts; some broadcasters use 37–40.
- **Maximum two lines per subtitle event.** Three lines force the eye to travel and cover too much of the picture.
- **CJK languages run shorter**: roughly 13–16 characters per line for Chinese and Japanese, two lines maximum — CJK glyphs are wider and read faster per character.
- **Arabic** follows similar character budgets to Latin but requires right-to-left rendering checks — punctuation placement and mixed-direction numbers are the classic breakage points.

Break lines at natural linguistic boundaries — between clauses, after prepositions, keeping noun phrases together. A line that ends "the new hydraulic / pump delivers" forces the reader to hold an incomplete phrase; "the new / hydraulic pump delivers" reads cleanly.

## Reading speed: the constraint that shapes translation

Subtitles live or die on characters per second (CPS) — how fast viewers must read to keep up:

| Audience | Maximum CPS (Latin) | Notes |
|---|---|---|
| Adults, standard content | 17–20 CPS | Netflix's well-known guideline is 20; broadcast often 17 |
| Children's content | 13–15 CPS | Younger readers need substantially more time |
| SDH / accessibility | 17–20 CPS | Includes speaker IDs and sound descriptions |
| CJK | ~6–8 characters/sec | Fewer characters carry the same information |

Here is the localization trap: **English-to-German translation expands text 20–35%**, but the video's duration does not change. A subtitle timed comfortably at 18 CPS in English becomes 23 CPS in German — physically impossible to read. Professional workflows solve this in the translation step, not the timing step: translators work with CPS constraints visible and condense the German text to fit. This is why subtitle translation is a specialization — a translator working from a plain script without timing data will produce text that cannot be displayed.

## Timing: the rules viewers feel but never see

- **Minimum duration ~1 second** (5/6 of a second is the hard floor at major streamers). Anything shorter flashes by unread; merge it with a neighbor or cut it.
- **Maximum duration ~6–7 seconds** per event. Longer and viewers re-read the subtitle thinking it changed.
- **Frame-accurate in/out**: subtitles should start and end on shot changes where possible. A subtitle that survives a cut makes viewers think they missed something and rewind.
- **Chaining gap**: leave 2+ frames between consecutive subtitles so the brain registers the change; abutting events read as one long line.
- **Sync tolerance**: in-time within a few frames of speech start; out-time can trail speech by up to half a second if the text needs reading time.

## What changes in translation: the three pressure points

1. **Expansion languages (German, Russian, Arabic, Spanish)**: condense in translation, verify CPS per event, and split long events into two well-broken ones rather than shrinking font or raising CPS.
2. **Contraction languages (Chinese)**: shorter text tempts longer display times collapsing into fewer events — resist merging across shot changes just because the characters fit.
3. **Line-breaking logic differs by script**: Japanese forbids certain line-break positions (line-start punctuation), Arabic breaks between words only and flips punctuation direction, Chinese avoids breaking within a word or a number. Auto-wrapping Latin-style breaks these rules silently.

## Formatting and positioning details that get forgotten in localization

- **Position**: bottom-center is the default; subtitles move top or side only to avoid covering burned-in text or faces. Translated videos often have *different* burned-in graphics than the source — re-check positioning per language, not per video.
- **Italics and speaker labels**: off-screen speech, narration, and SDH speaker IDs follow house conventions that must be re-applied, not translated literally. "- [SPEAKER]" formats differ by market.
- **Numbers and units**: digit style, decimal separators, and units localize (1,500 rpm vs 1.500 U/min), and they count against your character budget in expanded form.
- **Font**: embedded subtitle fonts must contain the target script's glyphs — a Latin-only font turns Chinese subtitles into boxes. Burned-in subtitles need re-rendering per language; sidecar files (SRT/VTT) inherit the player font.

## A pre-delivery QC checklist

1. No event exceeds 2 lines / ~42 characters (or the CJK/Arabic equivalent)
2. Every event within CPS limits for its language and audience
3. No subtitle crosses a shot change; gaps ≥ 2 frames between events
4. Line breaks at linguistic boundaries, script-correct
5. Numbers, units, and punctuation localized, not just translated
6. No text collides with on-screen graphics in *any* language version

Subtitles are the highest-volume, lowest-margin part of video localization — and the first thing viewers judge. Our [video localization team](/services/localization/video/) produces broadcast-spec subtitles with translation, timing, and QC under one roof. For the strategic question of when subtitles beat dubbing in a given market, see our [market-by-market comparison](/news/subtitles-vs-dubbing-by-market/) — or [send us a video](/contact/) and we will return a sample subtitle track in your target language.
