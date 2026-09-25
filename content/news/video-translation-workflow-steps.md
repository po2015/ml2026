---
title: "Video Translation Workflow: From Transcript to Burn-In"
date: 2027-02-15T09:32:00+08:00
publishDate: 2027-02-15T09:32:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["video localization", "workflow", "subtitling", "dubbing"]
keywords: ["video translation workflow", "video localization process", "subtitle burn in workflow"]
cover: "/images/news/video-translation-workflow-steps.jpg"
author: "MediaLocalize Team"
summary: "Transcribe, translate, time, review, deliver — video localization looks linear until a part number gets mistranscribed and propagates into five languages. The production-grade workflow, with the checkpoints that stop errors from compounding."
---

Every video localization disaster story has the same plot: an early error — a mistranscribed number, a missing on-screen text list — sailed through every downstream stage and got multiplied by the language count. "210 bar" heard as "two ten bar" became a wrong subtitle in English, then a wrong subtitle in five more languages, then a wrong *voiceover* in three — discovered by a distributor after publication. Video localization is a pipeline, and pipelines don't forgive errors; they replicate them. Here is the production-grade workflow, stage by stage, with the checkpoints that keep one mistake from becoming eighteen deliverables.

## Stage 0 — Asset collection (before anything starts)

Half of all workflow pain is missing inputs. Collect before kickoff:

- **The final video file** (not a re-encode of a re-encode) plus the **clean audio mix or stems** if dubbing is planned — voice separate from music/effects.
- **The project file or graphics sources** for any [on-screen text](/news/on-screen-text-video-localization/) — lower thirds, titles, callouts. Recreating OST from a flattened video means rebuilding graphics; having the sources makes it a text swap.
- **The glossary and product documentation.** The transcript will be judged against your spec sheet, so give the team the spec sheet up front.
- **The deliverables matrix**: which languages, which formats (subtitles, dubbing, or both), which platforms (YouTube, LMS, WeChat), which aspect ratios. This decides everything downstream — as covered in our [corporate training video guide](/news/video-localization-corporate-training-guide/).

## Stage 1 — Transcription and spotting

Transcribe the source language and spot the timecodes. Today this is AI-assisted by default — but for technical content, treat the AI transcript as a *draft*, per our [subtitling accuracy benchmarks](/news/ai-subtitling-accuracy-benchmarks/): numbers, units, part numbers, and standards get verified against documentation before anything proceeds.

**Checkpoint 1: the source transcript is signed off.** This is the single highest-leverage checkpoint in the whole pipeline. Every later stage consumes this text; an error here costs one fix, the same error found after translation costs one fix *per language*.

## Stage 2 — Translation and adaptation

The signed-off transcript goes to translation — with the glossary, the style guide, and a note about the destination format, because it changes the job:

- **For subtitles**: translators work to reading-speed and line-length constraints from day one ([formatting rules](/news/subtitle-formatting-rules/) — characters per line, CPS limits), not as a post-fix.
- **For dubbing**: the translation is an [adaptation for timing and register](/news/dubbing-script-adaptation-timing/) — spoken language, sentence lengths matched to the original's rhythm.

**Checkpoint 2: terminology review of the translation *before* timing/rendering.** A wrong term is a one-line edit in a text file; after burn-in or recording, it's a re-render or a pickup session.

## Stage 3 — Production, per format

**Subtitle track**: cue timing, line breaking, and positioning per platform rules; SDH elements (speaker IDs, sound cues) if accessibility is in scope — see the [SDH requirements](/news/sdh-accessibility-subtitles/).

**Dubbing track**: casting (human or [AI voice selection](/news/choosing-ai-voice-brand/)), recording/rendering, then mixing against the original audio bed, then [audio QA](/news/dubbing-audio-qa-checklist/) — technical conformance, pronunciation against the lexicon, mix balance.

**On-screen text**: translated graphics re-rendered from source files, matched to the original's fonts (with the [CJK/RTL font decisions](/news/cjk-latin-font-pairing/) where relevant), timed to the same in/out points.

## Stage 4 — In-context review

Native reviewers watch the *actual output* — not the subtitle file, not the script. A subtitled MP4 and a dubbed MP4 per language, reviewed for: sync, readability at real playback size, terminology in context, and anything culturally off that text review missed. One finding round, severity-triaged, is usually enough if checkpoints 1–2 were real.

## Stage 5 — Delivery, burn-in or sidecar

The last decision is packaging:

- **Sidecar files** (SRT/VTT alongside the video, separate audio tracks where the platform supports them) — preferred whenever the platform allows: editable, accessible, indexable. YouTube and most LMS platforms want sidecar; [multi-language audio tracks](/news/youtube-multi-language-audio/) keep one video URL serving all markets.
- **Burned-in subtitles / mixed dub** — required where sidecar isn't supported (WeChat channels, many trade-show screens, some social platforms) or where you need guaranteed rendering. Burn-in is a one-way door: every future text fix is a re-render, so it happens *last*, after review sign-off.

Deliver with the project assets: final subtitle files, the adapted scripts, the updated glossary, and the pronunciation lexicon. Those are the [translation-memory equivalents](/news/translation-memory-dtp-efficiency/) for video — they make video 2 cheaper than video 1.

## The timeline, realistically

For a 10-minute corporate video, one language, clean inputs: transcript+sign-off 1 day, translation 1–2 days, subtitle production 1 day, review 1–2 days, delivery — roughly a week; dubbing adds 2–5 days depending on format. Each *additional* language adds 2–3 days, not another week, because stages 1 and 5 amortize. The multipliers that break schedules are all in stage 0: missing sources, no glossary, undecided deliverables.

The workflow is linear; the discipline is in the checkpoints. Sign off the transcript, review terminology before production, watch the real output before burn-in — and errors die where they're cheap. Our [video localization team](/services/localization/video/) runs exactly this pipeline, from AI-assisted transcription with human number-verification to platform-specific delivery. [Send us a video and your target markets](/contact/) — we'll map the workflow and the timeline before you commit.
