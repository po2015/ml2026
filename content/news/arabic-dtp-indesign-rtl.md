---
title: "Arabic DTP: Right-to-Left Layout in InDesign"
date: 2026-12-02T20:46:00+08:00
publishDate: 2026-12-02T20:46:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["DTP", "Arabic", "RTL", "InDesign"]
keywords: ["arabic dtp indesign", "right to left layout", "arabic typesetting"]
cover: "/images/news/arabic-dtp-indesign-rtl.jpg"
author: "MediaLocalize Team"
summary: "Arabic DTP is not 'mirror the English file.' Fonts, digits, table direction, and InDesign's own RTL machinery each have failure modes that only show up in the final PDF — here is how to avoid them."
---

A European manufacturer sends their product catalog for Arabic DTP. The English layout is mirrored, the Arabic text is pasted in — and the PDF comes back with disconnected letters, Latin numerals where the client expected Eastern Arabic ones, a table of contents that reads left-to-right, and a logo lockup that now sits awkwardly against flipped body text. Each problem is small; together they announce that nobody involved had done Arabic typesetting before.

Arabic DTP is a specialization, not a checkbox. Here is what actually changes and how to run an InDesign RTL project cleanly.

## The text itself: shaping, ligatures, and direction

**Arabic is cursive by construction.** Each letter has up to four positional forms (isolated, initial, medial, final), and correct rendering requires the layout engine to shape them. Paste Arabic into a document using a font without Arabic glyphs — or with a composer that doesn't shape — and you get the classic symptom: letters rendered in isolated forms, readable but obviously broken to any native eye, like English printed with spaces between every letter. In InDesign this means: use the **World-Ready Composer** (paragraph-level setting) and a font with real Arabic support — never assume.

**Bidirectional text runs both ways in one line.** Arabic sentences with embedded Latin terms, model numbers, or URLs contain left-to-right islands inside right-to-left flow. The bidi algorithm handles most of it, but edge cases — a model number at the start of a line, punctuation between two scripts, parentheses around a Latin term — need manual inspection and occasionally explicit directional marks. Budget review time for every mixed line; there is no reliable automation.

**Digits are a decision, not a default.** Arabic-Indic digits (٠١٢٣٤٥٦٧٨٩) are standard in Gulf print materials; Western digits (0–9) dominate in technical documentation and in North Africa. Your client must choose per document type — and "match the source" is not a policy, it's a coin flip. Put it in the project brief alongside the [pronunciation and terminology decisions](/news/ai-voice-pronunciation-lexicon/) that govern their audio content.

## The layout: mirroring is the start, not the job

Flipping a page layout to RTL is 20% of the work. The other 80%:

- **Reading-order elements**: tables of contents, numbered steps, breadcrumbs, and multi-column text must flow right-to-left — column one is on the *right*. A two-column product spec table keeps its labels right, values left... unless the values are Latin model numbers, in which case consistency beats purity.
- **Tables**: mirror column order so the label column sits right — but keep LTR order for tables of Latin content (part-number lists). Mixed tables are normal; document the rule per table type.
- **Images**: photos with directional composition (a machine's workflow shown left-to-right, an arrow in a diagram) may need mirrored versions. Never mirror images containing readable text, clocks, maps, or brand marks — the same rule as [visual localization](/news/image-icon-color-localization/) generally.
- **Icons and bullets**: directional icons (arrows, chevrons, play triangles) flip; symmetric ones don't. Bullets migrate to the right margin with their text.
- **Page furniture**: page numbers, running headers, and spine position all mirror — a perfect-bound Arabic book's spine is on the right, which affects cover spreads and printer imposition.

## The InDesign machinery

Working setup for an RTL project:

1. **Start from the ME-capable version** — any current InDesign supports RTL, but the Middle East features (RTL paragraph direction controls, Arabic/Hebrew type options) must be enabled; they ship with the standard install in current versions.
2. **Paragraph direction is the master switch** — set it to RTL at the *style* level, never by overriding paragraphs ad hoc. Character direction handles the LTR islands.
3. **World-Ready Composer on every Arabic style.** This is the shaping engine; the Adobe Paragraph Composer will produce the disconnected-letters symptom.
4. **Fonts with genuine Arabic coverage**: Noto Naskh Arabic / Noto Kufi Arabic, Adobe Arabic, or licensed foundry faces (GE SS, Boutros, Sakkal Majalla for corporate work). Check kashida behavior if the design justifies text — Arabic justification elongates letters rather than spacing words, and bad kashida is as ugly as bad tracking. The same [pairing discipline](/news/cjk-latin-font-pairing/) applies to the Latin runs in the document: choose a Latin companion face, don't inherit the Arabic font's built-in Latin.
5. **Story and table direction settings** exist separately from paragraph direction — an RTL paragraph inside an LTR table is a classic source of "why is column one on the left."

## Numbers, dates, and units in mixed documents

Technical catalogs are the common case, and they're number-dense. Set the rules before layout starts: digit set (per above), date format (Arabic month names vs numerals; Hijri dates only when the client asks), units (kW stays Latin; translations of unit *names* in prose), and decimal separators (Arabic uses the Arabic decimal separator ٫ in fully-localized documents, Western conventions in technical ones). These decisions interact with everything — a spec table mixing ٠.٥ and 0.5 in adjacent rows looks like an error because it is one.

## QA: what to check before the PDF ships

- Zoom to 100% and read every line containing a number, Latin term, or punctuation mark — the bidi failures live there.
- Check justification for stretched or colliding kashida.
- Verify cross-references, TOC, and index regenerated *after* direction changes — stale TOCs keep LTR page ordering.
- One full native-speaker read-through of the final PDF, not the translation file. Shaping and direction bugs are invisible outside the layout.
- Preflight font embedding: Arabic fonts with licensing restrictions on embedding will bite at the printer, not on your screen.

Arabic DTP done well is invisible — the catalog simply looks like it was designed in Arabic. Done casually, every page says otherwise. Our [DTP team](/services/localization/dtp/) runs RTL projects with native review built into the QA pass. [Send us your English original](/contact/) and we will return a print-ready Arabic edition — shaping, digits, and spine all correct.
