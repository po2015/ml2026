---
title: "PDF Translation Workflows: Editable vs. Flattened"
date: 2027-01-11T19:45:00+08:00
publishDate: 2027-01-11T19:45:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["DTP", "PDF", "document translation", "workflow"]
keywords: ["pdf translation workflow", "translate pdf document", "pdf localization editable"]
cover: "/images/news/pdf-translation-workflow-editable.jpg"
author: "MediaLocalize Team"
summary: "\"Can you translate this PDF?\" is the most expensive sentence in document localization. Why the answer depends on what's inside the file — and the workflow that stops paying the PDF tax."
---

A distributor asks for your catalog in Portuguese. Marketing exports the PDF and sends it to a translation vendor. Two weeks later the quote comes back at triple the expected price, with a note about "DTP reconstruction." What happened? The PDF was the *only* source — and a PDF is not a document. It's a printout. Whether translating it costs $500 or $5,000 depends entirely on what kind of printout it is. Here is how to tell, and the workflow that makes the problem disappear.

## The three kinds of PDF

**1. Editable-source PDFs.** Exported directly from InDesign, Word, FrameMaker, or a web page. Text is real text: selectable, extractable, in reading order. These translate cleanly — extract, translate, reimport, adjust layout. The catch: you rarely want to translate the PDF itself; you want to translate the *source file* it came from, which leads to the golden rule below.

**2. Flattened PDFs.** Text converted to outlines, or pages exported as images wrapped in a PDF container. Common when a designer "finalizes" a file for print or when the PDF passed through a print shop. Nothing is extractable; every page must be rebuilt — retyped or OCR'd, re-laid-out, re-proofed. This is where "DTP reconstruction" line items come from.

**3. Scanned PDFs.** Photographs of paper. OCR quality varies from decent (clean scan, standard fonts) to hopeless (skews, stamps, handwriting, low resolution). Tables and multi-column layouts OCR worst — exactly the content datasheets are made of.

The 30-second diagnostic: open the PDF, try to select a sentence of body text. Selects cleanly → kind 1. Selects as an image or not at all → kind 2 or 3. Then check file size against page count: a 20-page "catalog" that's 80 MB is probably images in a trench coat.

## The golden rule: never translate the PDF

A PDF is an output, like a printed brochure. Translating it directly means paying to reverse-engineer a layout that already exists somewhere upstream. The rule:

> **Translate the source file; regenerate the PDF.**

If your catalog lives in InDesign, translate the .indd (or its exported IDML) — the translation drops into the existing layout, styles intact, and only expansion adjustments remain, per the standard [DTP checklist](/news/technical-manual-translation-dtp-checklist/). The PDF you send the distributor is then just a fresh export. Companies that internalize this rule stop paying the PDF tax forever; companies that don't pay it on every document, every language, every revision.

## When the source file is genuinely gone

It happens — the agency folded, the employee left, the file is from 2009. The recovery workflow, in order of preference:

1. **OCR + rebuild into a proper tool.** Extract text via OCR, rebuild the document in Word or InDesign, and translate *that* — paying the reconstruction cost **once**. From then on the document has a real source and every future language and revision is cheap. This is almost always the right call for living documents (catalogs, manuals, price lists).
2. **Translate as text, deliver bilingual or simplified layout.** For one-off, low-stakes documents (an old certificate, a legacy report), skip layout reconstruction entirely: deliver translated text in a clean simple document. Not beautiful — adequate.
3. **Overlay patching** for the rare case where the original layout must be preserved exactly but the source is gone: blank out source text regions and typeset translations on top. Slow, brittle, and the text expansion problem ([+30% for German](/news/text-expansion-translation-layout/)) makes a mess of tight layouts. Last resort.

Whichever path: graphics with baked-in text need their own treatment, per the [chart and infographic workflow](/news/infographic-chart-localization/) — they're the other half of the reconstruction bill.

## Building the upstream pipeline

The permanent fix is procedural, and costs nothing but a decision:

- **Archive source files as deliverables.** Every document project — internal or agency — ends with source files in your repository, not just the PDF. Make it a contract clause with design agencies.
- **Choose tools with translation in mind.** InDesign exports IDML; FrameMaker is built for structured multilingual docs (the trade-offs in [InDesign vs FrameMaker](/news/indesign-vs-framemaker-multilingual/)); even Word documents translate cleanly when built with real styles instead of manual formatting. Markdown-based docs with generated PDFs are the dream case — translate text, rebuild PDF in the build step.
- **Keep text out of images** and fonts embedded with licensing that permits editing, so extraction and re-typesetting stay legal and possible.
- **Feed the translation memory.** Every translated document adds segment pairs to your [TM](/news/translation-memory-dtp-efficiency/) — revision 3 of the catalog in language 5 then costs a fraction of revision 1, because only changed segments translate. This is where the real compounding happens.

## The decision in one table

| Situation | Path | Relative cost |
|---|---|---|
| Source file exists | Translate source, re-export PDF | 1× |
| Editable PDF, no source | Extract → translate → rebuild once → now you have source | 1.5–3× once, then 1× |
| Flattened/scanned, living document | OCR + rebuild → translate | 2–4× once, then 1× |
| Flattened/scanned, one-off | Translate as text, simple layout | ~1×, no layout fidelity |

The pattern: the expensive options are all *one-time* expensive if you rebuild properly, and *permanently* expensive if you keep translating the PDF.

Your documents should be assets that get cheaper to localize over time, not artifacts you ransom from a layout program every quarter. Our [DTP team](/services/localization/dtp/) handles the full chain — extraction, translation, reconstruction, and the typography QA in [every script](/news/multilingual-dtp-typography-guide/) — and hands you back the source files, always. [Send us your most painful PDF](/contact/) and we'll tell you exactly which row of the table it's in.
