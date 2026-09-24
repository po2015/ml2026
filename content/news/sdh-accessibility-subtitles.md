---
title: "SDH and Accessibility: Subtitles Beyond Translation"
date: 2026-12-01T11:10:00+08:00
publishDate: 2026-12-01T11:10:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["Video Localization", "SDH", "accessibility", "subtitles"]
keywords: ["sdh subtitles", "accessibility captions", "subtitles for deaf hard of hearing"]
cover: "/images/news/sdh-accessibility-subtitles.jpg"
author: "MediaLocalize Team"
summary: "Translated subtitles assume the viewer can hear the audio. SDH assumes they can't — speaker labels, sound cues, and different reading rules. What changes, what it costs, and when you need it."
---

Your product video has perfect German subtitles — a faithful translation of everything the narrator says. Then a deaf German engineer watches it: a second voice answers a question she didn't know was a question, a crucial alarm sound goes unmentioned, and the off-screen presenter demonstrates something while the subtitles describe something else. The translation was fine; the subtitle *type* was wrong. What she needed was SDH — Subtitles for the Deaf and Hard of Hearing.

SDH is not a translation concern; it's an information-completeness concern. Here is what distinguishes it, when it's required, and how to produce it without doubling your budget.

## What SDH adds beyond dialogue

Standard translated subtitles carry one channel: speech, rendered in the target language. SDH carries three:

**1. Speaker identification.** Who is talking matters when you can't hear voices change. Conventions: a name label (`MARIA:`), a dash per speaker in alternating dialogue, or color/position coding (position is the most robust — colors die in grayscale playback and projectors). Off-screen speech gets marked too, usually with italics or a label.

**2. Non-speech audio.** `[alarm sounds]`, `[phone ringing]`, `[machinery stops]` — anything a hearing viewer uses to follow the content. The test: mute the video, read only your subtitles, and check whether any on-screen action becomes inexplicable. Sound cues get brackets and lowercase; meaningful music gets a mention (`[tense music]`), background Muzak doesn't.

**3. Reading accommodation.** SDH audiences read *all* the information, so pace and chunking matter more: line breaks at phrase boundaries, two-line maximum, adequate display time per line, and no subtitles disappearing mid-sentence because the shot changed. The [formatting rules](/news/subtitle-formatting-rules/) from standard subtitling apply with tighter margins.

## When SDH is required vs optional

- **Legal requirements**: broadcast and public-sector content in the US (FCC/ADA), EU (European Accessibility Act, applying to streaming services and e-commerce video from 2025), and similar regimes elsewhere. If your videos sit on government, education, or large-enterprise procurement portals, assume accessibility documentation will be requested.
- **Platform norms**: e-learning platforms and corporate LMS deployments increasingly treat SDH as table stakes; WCAG 2.1 AA (the standard most policies cite) requires captions for prerecorded audio in synchronized media.
- **The silent-majority argument**: most social-feed video is watched muted — SDH-style captions (with sound cues) serve that audience too. Accessibility work doubles as engagement work.

Even where nothing is legally required, the honest question is simpler: *can every target viewer follow this video with the sound off?* If not, you're shipping less than your content.

## SDH and translation: which comes first

The efficient pipeline:

1. **Author SDH in the source language** — one pass that identifies speakers, sound cues, and reading-pace issues.
2. **Translate the SDH file**, keeping the cue conventions (labels, brackets) and re-checking line lengths per language. German speaker labels and sound descriptions expand like everything else; a `[hydraulic pressure release]` cue needs the same [expansion awareness](/news/text-expansion-translation-layout/) as dialogue.

The expensive pipeline is the reverse: translate dialogue-only subtitles, then retrofit SDH per language. Every cue gets added four times instead of once, and the timing decisions get relitigated per language. Author once in the source; localize the complete file.

## The production details that bite

- **Positioning**: SDH moves subtitles to avoid covering on-screen text and speakers' mouths — a translated subtitle file that always sits bottom-center fails the SDH bar. This interacts with [localized on-screen text](/news/on-screen-text-video-localization/): if your German lower thirds moved, the German subtitles' safe zones moved too.
- **Reading speed limits**: standard targets are ~17 characters per second for adults, lower for children's content. Dialogue-dense videos (panel discussions, fast explainers) sometimes need *edited* subtitles — condensed, not verbatim — to stay readable. SDH standards explicitly permit this; note it in your style guide so translators condense consistently.
- **File formats**: the cue conventions live in the subtitle file, but their rendering depends on format and player — WebVTT and TTML carry positioning and styling; SRT carries almost nothing. For SDH deliverables, specify the format per platform, not "whatever exports."
- **Music and lyrics**: if a song's lyrics matter (a brand jingle), subtitle them with a ♪ convention; if it's mood music, one cue at onset is enough.

## What it costs

SDH authoring adds roughly 20–40% on top of a standard subtitle pass for the source language — the increment is listening for cues and positioning, not translation. Localizing the SDH file costs nearly the same as localizing standard subtitles. Compliance-ready accessibility (plus a conformance statement, if you need one for procurement) is where professional QC earns its fee.

Our [video localization team](/services/localization/video/) produces SDH as a first-class deliverable — source-authored once, localized with cue conventions intact, delivered per-platform format. [Send us a video](/contact/) and we will tell you whether your current subtitles pass the mute test.
