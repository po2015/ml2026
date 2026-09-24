---
title: "Articulate Storyline Localization: Step by Step"
date: 2026-10-28T17:43:00+08:00
publishDate: 2026-10-28T17:43:00+08:00
category: "industry"
category_label: "Industry"
tags: ["E-Learning", "Articulate Storyline", "SCORM", "localization"]
keywords: ["articulate storyline translation", "storyline localization workflow", "storyline xlf export"]
cover: "/images/news/articulate-storyline-translation-workflow.jpg"
author: "MediaLocalize Team"
summary: "Storyline's translation export looks simple until slide layers, triggers, and variable text come back broken. The complete workflow that survives real courses."
---

Articulate Storyline has a built-in translation feature: export text, translate, import back. Vendors who have never done it quote from that menu item's existence. Then the imported course has truncated button labels in German, quiz feedback showing variable placeholders instead of learner names, and a text-to-speech track still reading English — and three rounds of rework begin.

Storyline localization works smoothly when you know where the traps are. Here is the workflow we run, step by step, with the checks that catch problems while they are still cheap.

## Step 1: Prepare the source file (before any export)

Half the quality of a Storyline localization is decided before translation starts:

- **Use the source .story file, never the published output.** If the client only has the published SCORM package, stop — text extraction from published files loses slide structure and context.
- **Update to the latest Storyline version** and save a versioned copy of the file per target language from the start (`course_de.story`, `course_es.story`). Working in one file and "importing languages in" is how overwritten masters happen.
- **Replace text-in-images.** Screenshots with callouts, diagrams with labels, and button graphics containing words must be rebuilt as editable text or flagged for re-creation per language.
- **Standardize fonts.** Choose fonts that exist for every target script — a Latin-only font silently falls back on Chinese or Arabic slides. Check our [typography guide](/news/multilingual-dtp-typography-guide/) for script-safe font choices.
- **Note every dynamic text source**: variable references (`%UserName%`), number-to-text triggers, and JavaScript-generated strings do not appear in translation exports.

## Step 2: Export for translation

Storyline offers two export formats:

- **Word (.docx)**: one row per text segment with slide/layer references. Fine for small courses and clients reviewing in Word; weaker for translation memory workflows.
- **XLIFF (.xlf)**: the professional route. Imports into any CAT tool (memoQ, Trados), preserves segment IDs, and round-trips cleanly. Use this whenever a translation vendor is involved.

Critical settings: export **with the original text as source**, and make sure "include text from all slides, layers, notes, and question banks" is covered — question banks and feedback masters are separate objects in Storyline and the most commonly missed content.

## Step 3: Translate with context

Storyline exports segment text without visual context. Translators seeing "Submit" cannot know whether the button fits 20 characters or 6. Two practices prevent the guesswork:

1. **Provide slide screenshots or a published review link** alongside the XLIFF, so translators see where each segment lives.
2. **Set length constraints** for UI segments — buttons, tabs, and menu items. In a CAT tool these become character limits that flag overflow during translation rather than after import.

German runs 20–35% longer than English; for button-heavy courses, agree up front whether overflow gets solved by shorter wording or by resizing. Our [text expansion article](/news/text-expansion-translation-layout/) explains why this decision belongs here, not in QA.

## Step 4: Rebuild audio, video, and dynamic elements

The translation export only covers text. In parallel with translation:

- **Re-record narration** — [AI voices](/news/how-ai-dubbing-works/) make this dramatically cheaper for training libraries; document the voice choice in a style guide so future modules match.
- **Localize videos and animations**: re-time captions, re-record voiceover, and re-edit burned-in text. Storyline's closed captions are attached per slide and must be re-uploaded per language.
- **Update Storyline's built-in text-to-speech**: it does not switch language automatically. Each language file needs TTS regenerated with a matching-language voice, or replaced with recorded audio.
- **Handle variable text**: strings assembled by triggers (score messages, name insertion) exist partly in the export and partly in trigger logic. Test every variable-driven screen manually.

## Step 5: Import and fix the layout

Import the translated XLIFF into the language copy of the .story file. Then budget real time for what import does not fix:

- **Text overflow**: resized boxes, shrunk fonts (within legibility limits), or reworded labels — slide by slide.
- **Right-to-left languages**: Storyline supports Arabic text entry, but bullet alignment, indentation, and mixed-direction punctuation need slide-level review.
- **Player text labels**: the player UI (Prev/Next buttons, menu, glossary, resources tab) is translated separately in the player's Text Labels settings — a fully German course with an English "NEXT" button is the signature of an amateur job.

## Step 6: Publish and validate

Publish each language as its own SCORM/xAPI package and validate before delivery:

1. **SCORM Cloud or equivalent conformance test** — catches manifest and packaging errors. The packaging-level issues (manifest titles, completion strings) are covered in our [SCORM and xAPI localization article](/news/scorm-xapi-localization/).
2. **Functional QA on the real LMS** — a native speaker completes the course: every quiz submitted, every branch taken, completion and score reporting verified in the LMS report.
3. **Linguistic QA in context** — translators review the running course, not the XLIFF; truncated strings and wrong-context translations are only visible on screen.

## Realistic effort and timeline

For a typical 30-minute corporate module:

| Task | Effort |
|---|---|
| Prep + export | 2–4 hours |
| Translation (per language) | 1–2 days |
| Layout fixes post-import | 3–8 hours (more for interaction-heavy courses) |
| Audio re-record + sync | 1–2 days (AI) / 3–5 days (studio) |
| QA + LMS validation | 2–4 hours |

Multiply by languages, and parallelize — layout and audio work in one language does not block another. First-time projects should add 30% for the learning curve; it disappears by the third module.

If you have Storyline courses headed for multilingual rollout, our [e-learning localization team](/services/localization/elearning/) works directly in .story files and delivers validated SCORM packages per language — [send us one module](/contact/) and we will quote the whole library from it.
