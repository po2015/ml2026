---
title: "SCORM, xAPI, and Localization: What Actually Changes"
date: 2026-10-12T13:58:00+08:00
publishDate: 2026-10-12T13:58:00+08:00
category: "industry"
category_label: "Industry"
tags: ["E-Learning", "SCORM", "xAPI", "localization", "corporate training"]
keywords: ["scorm localization", "xapi translation", "elearning localization"]
cover: "/images/news/scorm-xapi-localization.jpg"
author: "MediaLocalize Team"
summary: "Translating course text is only half of e-learning localization. What actually changes inside SCORM and xAPI packages — and what breaks if you miss it."
---

A training team finishes their English compliance course, sends the SCORM package to a translation vendor, and gets back what looks like a finished German course. Three weeks later the LMS report shows learners stuck at 87% completion, quiz feedback displays in English, and the navigation buttons overflow their labels in Polish. None of these are translation problems — they are packaging problems. The e-learning standard your course is built on determines what localization actually has to touch.

This article maps what changes inside SCORM and xAPI packages when you localize them, so you can scope the work correctly and ask vendors the right questions.

## What SCORM and xAPI actually package

Both standards define how a course talks to a learning management system (LMS): how it reports completion, scores, time spent, and bookmarks. But they package content very differently, and that difference drives localization effort.

| Standard | What it contains | Where learner-facing text lives | Tracking model |
|---|---|---|---|
| SCORM 1.2 | Zipped HTML/JS + `imsmanifest.xml` | Inside course files; some in manifest | Completion, score, suspend data |
| SCORM 2004 | Same structure, richer sequencing | Same, plus sequencing rules | Adds objectives, interactions |
| xAPI (Tin Can) | Content anywhere; statements sent to an LRS | Course files + statement display strings | "Actor did verb object" events |
| cmi5 | xAPI statements wrapped in a launchable package | Same as xAPI | xAPI with LMS launch rules |

The key insight: **SCORM keeps everything inside the ZIP**, so localization means opening, editing, and repackaging course files. **xAPI moves reporting into statements**, so localization also has to consider what those statements say — they often contain human-readable strings that end up in reports your German HR team will read.

## What changes when you localize a SCORM package

### The manifest and metadata

`imsmanifest.xml` holds the course title and organization labels that some LMSs display in their catalogs. A surprising number of localized courses still carry English titles here, so learners see "Fire Safety Training 2026" in an otherwise fully German course catalog. The manifest must be translated and re-validated — a malformed manifest means the course will not import at all.

### Text expansion inside fixed layouts

Course authoring tools (Storyline, Captivate, Lectora) place text in fixed-size boxes. German runs 20–35% longer than English; Chinese contracts but changes line breaking; Arabic mirrors the reading direction. Buttons, tabs, progress bars, and drag-and-drop labels all need resizing or reflow — this is layout work, not translation work, and it is why e-learning localization quotes include an engineering line item.

### Completion and reporting strings

SCORM status values (`completed`, `passed`, `failed`) are fixed English tokens — never translate them, or tracking breaks silently. But feedback text, result slide messages, and "You must score 80%" instructions are learner-facing and must be translated. Vendors who work from a raw text export routinely mix these two categories up.

### Audio, video, and on-screen text

Narrated courses multiply the work: translated scripts, [AI or human voice recording](/news/how-ai-dubbing-works/), re-syncing to animations, and re-editing any on-screen text burned into videos or screenshots. A course with 20 minutes of narration and annotated screenshots can double the engineering effort of a text-only course.

### Quizzes and interactions

Drag-and-drop targets, dropdown options, hotspot labels, and feedback layers are often stored as separate objects in the authoring file, not as running text — which means they get missed by text-extraction workflows. Randomized answer shuffling can also break translated "All of the above" options. Every interaction type needs a functional pass in the target language.

## What changes with xAPI

xAPI shifts the problem from packaging to reporting. Statements like `"Zhang Wei completed Fire Safety Module 3"` carry display strings defined in the activity definitions and the statements themselves.

Three localization decisions are unique to xAPI:

1. **Activity definition language**: xAPI activity definitions support multiple `display` language maps. Done properly, your LRS can render the same activity as "Brandschutz Modul 3" for German viewers and keep English for headquarters. Done lazily, every locale's report shows English activity names.
2. **Verb consistency**: Translate display names of custom verbs, never their IRIs. Two courses using different IRIs for the same concept ("completed" vs "finished") will fragment your reporting across languages.
3. **Result readability**: If your LRS feeds dashboards that regional managers read, decide up front which language statements display in — and keep it consistent across all localized course versions.

## The workflow that avoids rework

The order of operations matters more than the tools:

1. **Extract from the source project file** (Storyline `.story`, Captivate `.cptx`), not from the published SCORM ZIP. Published files are compiled; text extraction from them loses context and object structure.
2. **Translate with context** — translators need to see where each string appears (button, feedback layer, alt text) to keep within space limits.
3. **Reimport and rebuild** in the authoring tool, fixing text expansion object by object.
4. **Re-record and re-sync audio/video**, then replace localized images and screenshots.
5. **Publish and validate the package** — run it through a SCORM conformance test (e.g., SCORM Cloud) before it goes near your LMS.
6. **Functional QA in the target language** — a native speaker clicks through every interaction and checks completion reporting on the real LMS.

Skipping step 1 is the single most expensive mistake: we regularly see projects re-scoped after a vendor discovers they cannot edit compiled output. Our [e-learning localization overview](/news/elearning-localization-global-audiences/) covers the broader process; this article is the technical half of it.

## Questions to ask before you get a quote

- Can you deliver the **source project files**, or only the published package?
- Which standard and version does the course use (SCORM 1.2 / 2004, xAPI, cmi5)?
- Does the course contain narration, video, or screenshots with text?
- How many interactions and quiz types does it use?
- Will the vendor run functional QA on your LMS, or only deliver files?

A vendor who quotes from the ZIP file alone is guessing. One who asks these questions has done this before — and their quote will hold.

If you are planning multilingual training rollout and want the engineering scoped correctly from the start, our [e-learning localization team](/services/localization/elearning/) works directly in Storyline, Captivate, and Lectora project files — [send us a sample module](/contact/) and we will tell you exactly what localization will change in it.
