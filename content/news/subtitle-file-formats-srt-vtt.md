---
title: "SRT, VTT, ASS: Subtitle File Formats Explained"
date: 2027-04-12T21:14:00+08:00
publishDate: 2027-04-12T21:14:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["Subtitling", "video localization", "file formats", "captioning"]
keywords: ["subtitle file formats", "srt vtt ass difference", "caption formats video localization"]
cover: "/images/news/subtitle-file-formats-srt-vtt.jpg"
author: "MediaLocalize Team"
summary: "Your Chinese subtitles come back as an SRT that won't import into your web player; the Arabic file shows every line in reverse order; the training platform demands VTT and you have SRT. Subtitle files look trivial — text plus timestamps — until they break. What the three formats that matter actually do, when to use each, and the encoding traps that ruin multilingual deliveries."
---

A marketing manager receives the finished subtitles for a product video: twelve languages, all delivered as `.srt` files. The web team's player rejects them — it needs WebVTT. Someone renames the extension, and now half the videos play with no captions at all. Meanwhile the Arabic file opens in Notepad as backwards gibberish, and the Japanese one shows question marks where characters should be. None of this is exotic: subtitle files are plain text with timestamps, but that simplicity hides exactly the details — format capabilities, encoding, text direction — that decide whether your [multilingual subtitles](/news/subtitle-translation-best-practices/) actually play. This is the working guide to the three formats you'll meet and the traps between them.

## SRT: the universal workhorse

SubRip (`.srt`) is the oldest and most compatible format: a sequence number, a timestamp line, the text, a blank line — nothing else.

```srt
1
00:00:02,500 --> 00:00:05,000
The PVG-32 valve handles flows up to 130 l/min.

2
00:00:05,200 --> 00:00:08,400
Commissioning takes under ten minutes.
```

Timestamps use `hours:minutes:seconds,milliseconds` — note the **comma**. SRT supports almost no styling (a few players honor basic `<i>`/`<b>`/`<u>` tags, many don't), no positioning, no metadata. That limitation is its strength: every editor, player, platform, and CAT tool on earth reads SRT. Use it as your **translation exchange format** — what you send to translators and get back — and for platforms that accept it (YouTube, LinkedIn, most social platforms do).

## WebVTT: the web standard

WebVTT (`.vtt`) is what HTML5 `<track>` elements and most web players require. It looks like SRT with a header and differences that matter:

```vtt
WEBVTT

00:02.500 --> 00:05.000
The PVG-32 valve handles flows up to 130 l/min.

NOTE
Reviewed by native speaker, 2027-04-10

00:05.200 --> 00:08.400
Commissioning takes under ten minutes.
```

- The file **must start with `WEBVTT`** — a renamed SRT without the header is an invalid VTT, which is why the rename trick fails.
- Timestamps use a **period** for milliseconds (`00:02.500`), and hours are optional.
- It supports **cue settings** (position, alignment, line breaks), **speaker labels** (`<v Anna>`), **comments** (`NOTE` blocks), and CSS-based styling via `::cue` in the page stylesheet.

Use VTT for anything embedded on your own website and for e-learning platforms ([LMS players](/news/multilingual-lms-deployment/) overwhelmingly expect VTT). The practical pipeline: translate in SRT (tool compatibility), convert to VTT for web delivery — with a real converter, not a rename.

## ASS/SSA: when styling is the point

Advanced SubStation Alpha (`.ass`) is the format of styled subtitling: per-cue fonts, sizes, colors, outlines, shadows, precise screen positioning, even animation. You'll meet it when subtitles must *look designed* — anime and fan-sub culture built it, but it's equally how you burn branded, positioned captions into a marketing video, or place Chinese text to avoid covering the demo UI in the lower third.

The cost: complexity and compatibility. ASS carries a full style section and event list; web players generally don't read it, and translators can easily break its override tags (`{\an8}`, `{\pos(320,40)}`). Treat ASS as a **finishing format**: translation happens in SRT/VTT, then a subtitler rebuilds styling in ASS for burn-in, and the burned video is the deliverable. When captions are [burned in vs. delivered as files](/news/burned-in-subtitles-vs-caption-files/), ASS belongs to the burn-in branch.

## The traps that actually break deliveries

1. **Encoding: UTF-8, with or without BOM, and nothing else.** SRT has no encoding declaration; files saved as Latin-1 or GB2312 turn Japanese and Arabic into mojibake. Deliver and demand **UTF-8**. A BOM helps Windows tools detect encoding correctly; most modern players accept it.
2. **Text direction for Arabic and Hebrew.** The subtitle *file* is logically ordered; the *player* applies bidirectional rendering. Mixed-direction lines — an Arabic sentence containing your Latin product name — render wrong if punctuation lands at line edges. Test Arabic subtitles in the actual target player, not in a text editor, and prefer players with proper bidi support.
3. **Line length and reading speed survive translation badly.** German runs ~30% longer than English; a two-line English cue can become four German lines that no viewer can read in the on-screen time. [Text expansion](/news/subtitle-text-expansion-contraction/) planning happens at translation, but the *format* check is the subtitle QA pass: characters per line, lines per cue, minimum display duration.
4. **Timestamp drift after edits.** If the video is re-cut after subtitling, every cue shifts. Subtitle files reference absolute timecodes — any edit invalidates them. Lock picture before subtitling, or budget a re-sync pass.
5. **Line-break handling in conversion.** SRT→VTT converters occasionally mangle multi-line cues or drop blank-line separators; spot-check converted files before upload.

## The practical recommendations

- **One master per language, in SRT, UTF-8**, archived alongside the video — your source of truth for future edits and platform conversions.
- **Convert per destination**: VTT for your website and LMS, SRT for YouTube/social, ASS→burn-in for designed marketing pieces. Conversions are mechanical and scriptable.
- **Specify the format in the vendor brief** ("deliver SRT UTF-8 + VTT") rather than discovering player requirements after delivery — the same discipline as [specifying deliverables in localization briefs](/news/localization-vendor-brief-template/) generally.
- **Keep CJK line counts short**: Chinese/Japanese/Korean convey more per character, so translated cues often shrink — an opportunity to raise reading comfort, per the [CJK subtitling notes](/news/chinese-video-subtitling-guide/).

Formats are the boring layer of subtitling — until a launch video publishes with no captions because a file was renamed instead of converted. Our [video localization team](/services/localization/video/) delivers subtitles in every destination format with the QA pass (encoding, bidi, line metrics, sync) already done. [Send us your video and target platforms](/contact/) and we'll handle the whole chain from transcript to player-ready files.
