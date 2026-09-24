---
title: "Localizing On-Screen Text and Motion Graphics"
date: 2026-11-11T08:15:00+08:00
publishDate: 2026-11-11T08:15:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["Video Localization", "motion graphics", "on-screen text", "DTP"]
keywords: ["on screen text localization", "motion graphics translation", "video text replacement"]
cover: "/images/news/on-screen-text-video-localization.jpg"
author: "MediaLocalize Team"
summary: "Voiceover is only half of video localization. What it takes to translate on-screen text, titles, and motion graphics — and why project files matter more than the video itself."
---

A product video comes back from "localization": the voiceover is German, the subtitles are German — and every on-screen title, callout, and chart label is still English. Viewers notice immediately. On-screen text is where the information density lives in modern corporate video, and leaving it untranslated tells your German audience the video was not made for them.

Localizing on-screen text (OST) and motion graphics is a distinct discipline between translation and video editing. Here is what it involves, what it costs, and how to scope it correctly.

## The inventory: what counts as on-screen text

Before quoting anything, inventory every text element in the video:

- **Titles and lower thirds**: speaker names, chapter cards, section headers
- **Callouts and annotations**: labels pointing at product features, dimension callouts
- **Charts and diagrams**: axis labels, legends, data callouts
- **Screen recordings**: software UI captures, dashboard walkthroughs
- **Burned-in captions and social-style text overlays**
- **Logos with taglines, end cards, CTAs** — often forgotten until delivery

Each category has a different workflow and cost. A 3-minute product video typically carries 20–60 discrete text elements.

## Workflow A: with project files (the sane path)

If you have the After Effects / Premiere / motion graphics project files, OST localization is systematic:

1. **Extract all text layers** to a spreadsheet with timecodes and context screenshots. Translators work from this, not from the video.
2. **Translate with length constraints.** German runs 20–35% longer; text that animates on for two seconds must still fit and remain readable — the same [expansion rules](/news/text-expansion-translation-layout/) that govern print apply here, with tighter budgets.
3. **Replace text in the project.** This is where font support gets checked (CJK, Arabic, Cyrillic glyphs), where expansion breaks layouts, and where RTL languages need animation direction reconsidered — an element that sweeps in from the left may read wrong in Arabic.
4. **Re-time animations.** Longer translated text needs longer on-screen time; keyframes shift, and anything synced to voiceover re-syncs to the new audio.
5. **Re-render per language** and QC frame by frame for clipped text, encoding artifacts, and orphaned English elements.

## Workflow B: without project files (the expensive path)

No project files means re-creating graphics from the rendered video:

- **Simple text over clean backgrounds**: masked out, background patched, new text composited. Feasible and affordable.
- **Text over moving footage or complex animations**: effectively re-animation. Often 3–5× the cost of Workflow A, sometimes approaching the cost of re-shooting.
- **Screen recordings**: usually re-recorded with the localized software UI — there is no shortcut that looks professional.

This is why we tell every client the same thing: **archive your project files with the same care as the master video.** The request "just localize the video we had made two years ago" turns from a two-day job into a two-week job precisely when project files are lost. If an agency made the video, get the project files in the contract.

## The translation-specific traps

- **Expansion breaks timed reveals.** Bullet points that animate in one-by-one are timed to text length; translated bullets need re-choreography, not just re-typing.
- **Fonts change the design.** Your brand font may not cover Chinese or Arabic; the fallback font changes weight and width, and suddenly the title layout needs redesign. Decide per language: adapt the layout to the font or license a script-appropriate brand alternative.
- **Numbers and units need localization too**: decimal separators, date formats, units (kW vs. PS, inches vs. mm) — and they are inside graphics, invisible to text extraction.
- **Arabic flips reading order inside animations**: multi-element reveals should sequence right-to-left, and progress indicators fill right-to-left. Half-measures here read as broken to native eyes.

## Scoping and pricing logic

| Scenario | Typical effort per language |
|---|---|
| Titles/callouts only, project files available | 0.5–1 day |
| Full motion graphics, project files available | 1–3 days |
| No project files, moderate complexity | 3–10 days (re-creation) |
| Screen recordings | Re-shoot with localized UI + edit |

Per-language costs drop fast after the first: the adaptation decisions (fonts, layout rules, timing adjustments) are made once, and languages two through eight ride on that template. Combined with [localized voiceover](/news/how-ai-dubbing-works/) and [subtitles](/news/subtitle-formatting-rules/), OST localization completes the package that makes a video feel produced *for* a market rather than adapted *to* it.

If your video library is heading to new markets, our [video localization team](/services/localization/video/) handles the full stack — voiceover, subtitles, and motion graphics — from project files or without. [Send us one video](/contact/) and we will inventory its text elements and quote the whole library from it.
