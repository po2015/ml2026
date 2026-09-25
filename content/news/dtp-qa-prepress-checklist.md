---
title: "DTP QA: The Pre-Press Checklist for Translated Files"
date: 2027-03-24T10:36:00+08:00
publishDate: 2027-03-24T10:36:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["DTP", "quality assurance", "pre-press", "print production"]
keywords: ["dtp quality assurance", "prepress checklist translation", "translated files print qa"]
cover: "/images/news/dtp-qa-prepress-checklist.jpg"
author: "MediaLocalize Team"
summary: "The Arabic catalog came back from print with the phone numbers mirrored. The German manual's index pointed to pages that no longer existed. Both files had been 'checked' — by someone who looked at the screen, not the print-ready PDF. Pre-press QA for translated documents is its own discipline: the checklist that catches what translation review never sees."
---

A distributor emails a photo: 5,000 printed catalogs, and on the Arabic pages every phone number reads backwards — the DTP operator pasted LTR numbers into RTL paragraphs and InDesign's paragraph direction flipped the digit order. The file had passed two reviews: the translator checked the text (correct), the account manager checked the look (plausible, if you don't read Arabic). What nobody ran was a pre-press QA pass — the systematic check of a translated document as a *print production file*, where a whole category of defects lives that neither linguistic review nor a casual flip-through can see. Translated files fail pre-press in translated-file-specific ways. Here's the checklist, in the order a professional runs it.

## Why translated files need their own QA pass

Standard pre-press checks (fonts embedded, images at resolution, bleed, color space) apply to every document. Translation adds a second failure layer:

- **Text changed after the design was finalized** — expansion, contraction, and script changes stress every layout assumption ([expansion rules](/news/text-expansion-translation-layout/)).
- **Multiple languages multiply the file count** — a 6-language catalog is 6 chances for the wrong version of an image, price list, or legal line to ship.
- **Scripts the production team can't read** — nobody on your team can tell mirrored Arabic from correct Arabic by eye, which is exactly why the checklist must be *mechanical* (compare values, check settings) rather than visual judgment.

## The checklist

**1. Version and completeness parity.** Open source and target side by side: same page count (or a documented reason for difference), every section present, no untranslated text left in frames — including the classic hiding spots: master pages, footers, layer-locked frames, text in tables, and text converted to outlines in graphics. Search the PDF for common source-language words ("the", "and") to catch stragglers mechanically.

**2. Typography and fonts.** Correct fonts for the script, embedded and licensed (the [font licensing map](/news/font-licensing-multilingual-publishing/) applies at exactly this moment); no missing-glyph boxes (□) or fallback-font substitutions — in InDesign, preflight reports flag them, and the [typography conventions](/news/multilingual-dtp-typography-guide/) per language (quotation marks, dashes, spacing rules) verified against the style guide.

**3. Numbers, units, and untranslatables.** Mechanically compare every number in source and target: part numbers, dimensions, tolerances, phone numbers, prices. They should match digit-for-digit, except where [locale formatting](/news/date-currency-format-localization/) deliberately changes them (decimal commas, thousand separators, date formats). Phone numbers in RTL documents: verified digit order by *calling the printed number mentally* — the catalog story above is this check skipped.

**4. Layout integrity.** Text overflow (the red plus in InDesign, truncated text in the PDF), widows/orphans, headings separated from their body, table rows split across pages, line breaks that change meaning in tables and spec sheets. Warnings and safety notices verified against their procedure steps, per the [manual DTP rules](/news/technical-document-dtp-rules/) — keep-with-next constraints don't always survive translation reflow.

**5. Cross-references, TOC, and index.** "See page 38" — does page 38 still hold that content in the target language? Click every cross-reference in the PDF; regenerate and verify the table of contents; confirm the index was *rebuilt* for translated sort order, not translated entry-by-entry (locale collation differs — ä sorts differently in German and Swedish).

**6. Graphics and images.** Correct localized image versions placed (screenshots, diagrams with translated callouts — and *not* the English screenshots in the German manual); [culturally appropriate imagery](/news/image-icon-color-localization/); image resolution and color space per print spec, unchanged by the localization round-trip.

**7. Language-specific mechanical checks.** RTL documents: paragraph direction, digit direction, mirrored page geometry where required ([Arabic DTP](/news/arabic-dtp-indesign-rtl/) has its own full checklist). CJK: no fake-bold/fake-italic synthesized styles, correct line-breaking rules (kinsoku), proper [CJK-Latin font pairing](/news/cjk-latin-font-pairing/). Hyphenation enabled and correct per language — German compound words hyphenated by English rules produce spectacular errors.

**8. Output verification.** Preflight the final PDF against the printer's spec (fonts embedded, images 300 dpi, CMYK, bleed, overprint settings) — and *proof from the final PDF*, never from the layout file. The PDF is what prints; only the PDF shows what the rip will do.

## The process notes that make QA stick

- **QA per language, not per project.** The checklist runs on every language file individually; "we checked the German one" says nothing about the Arabic one, which fails in different places.
- **A reader per language for the meaning checks.** Mechanical checks (numbers, versions, preflight) need no language skill; layout-integrity and line-break checks need a native reader — budget one hour per language for a native-speaker flip-through of the proof PDF.
- **Sign-off trail.** Who ran the checklist, on which file version, when. At 6 languages × 3 document types, you'll need it by the second project — and regulated industries require it outright, same as [compliance training records](/news/compliance-training-translation-accuracy/).
- **Feed defects back to templates.** Every overflow, every broken cross-reference is a template lesson — character budgets, keep-rules, and frame sizing get adjusted once, and the next language inherits the fix, per the [template economics](/news/translation-memory-dtp-efficiency/).

Pre-press QA is an hour or two per language against five-figure reprints and distributor-confidence damage — the cheapest insurance in the entire localization budget. Our [DTP team](/services/localization/dtp/) runs this checklist as standard on every translated file, with native readers per language and a signed QA report per deliverable. [Send us your next print project](/contact/) and we'll show you what the report catches before the printer does.
