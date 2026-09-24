---
title: "Localizing Charts, Diagrams, and Infographics"
date: 2026-12-22T16:37:00+08:00
publishDate: 2026-12-22T16:37:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["DTP", "infographics", "charts", "visual localization"]
keywords: ["infographic localization", "chart translation", "diagram localization"]
cover: "/images/news/infographic-chart-localization.jpg"
author: "MediaLocalize Team"
summary: "A chart is not a picture with words on it — it's text, numbers, axes, colors, and reading order fused into one argument. How to localize data graphics without breaking the argument or the layout."
---

The datasheet is perfectly translated. Then the buyer reaches page three: a performance curve with English axis labels, a comparison table baked into a PNG, and an infographic whose callouts now point at the wrong things because someone translated the text layer and nothing else. Data graphics are where translation projects quietly break — because a chart is not a picture with words on it. It's an argument made of text, numbers, position, and color, and localizing it means rebuilding that argument per market.

## First decision: which graphics actually need work

Triage before touching anything:

- **No text, universal imagery** (product photos, icons-only diagrams): ship as-is.
- **Text-bearing but regenerable** (charts from Excel/Tableau/web charting libraries): regenerate from source with translated labels — cheapest and cleanest.
- **Text baked into pixels** (exported PNGs, screenshots, scanned diagrams): must be rebuilt or retouched in DTP. This is where budgets go to die, and why we tell clients to [keep text out of images](/news/image-icon-color-localization/) at authoring time.
- **Screenshots of software**: decide per market — localized UI screenshots if the product ships in that language, annotated originals if it doesn't.

## The mechanics: text, numbers, axes

**Text expansion hits graphics harder than prose.** German runs ~30% longer than English; a tight callout box that fit "Torque" must now fit "Drehmoment" — fine — but "Max. operating pressure" becoming "Maximaler Betriebsdruck" breaks the layout. The standard [text-expansion playbook](/news/text-expansion-translation-layout/) applies with one amplification: charts have no fluid layout to absorb growth. Budget redraw time, shorten labels aggressively (abbreviations, legends instead of inline labels), and never shrink fonts below legibility to make it fit.

**Numbers and axes follow the market.** Decimal commas (3,14 vs 3.14), thousand separators, date formats on time axes, units on axis titles — all of it localizes, per the conventions in our [date and number formats guide](/news/date-currency-format-localization/). A chart regenerated with translated labels but US number formats is half-localized and reads as such.

**Reading order flips for RTL.** A process diagram flowing left-to-right in English must flow right-to-left in Arabic — arrows, sequence numbers, and all. Simply mirroring the image breaks charts (mirrored axis values are wrong); the correct move is rebuilding the layout RTL with the data intact. The same bidi discipline as [Arabic DTP](/news/arabic-dtp-indesign-rtl/), applied to graphics.

**Font support decides legibility.** CJK, Arabic, and Thai labels need fonts that render them properly at small sizes — see the [font-pairing guide](/news/cjk-latin-font-pairing/). A beautiful English infographic typeset in a fallback font for its Chinese version looks broken to exactly the readers it was made for.

## Color and symbolism are data too

Color encodes meaning in charts — red for losses, green for growth in Western convention; red is positive in China and Japan's stock markets. A red/green performance chart may invert its message for some audiences. Check the [color conventions](/news/image-icon-color-localization/) per market, and when in doubt use redundant encoding (color *plus* icons or labels), which is better for accessibility everywhere anyway.

## A workflow that scales

1. **Author in layers.** Keep every chart's source (spreadsheet, vector file) with text on its own layer. Graphics authored flat cost 5–10× more to localize.
2. **Extract text like any other content.** Chart labels go into the same translation workflow and [translation memory](/news/translation-memory-dtp-efficiency/) as body text — axis titles and callouts repeat across documents more than you'd think.
3. **Regenerate, don't retouch, where source exists.** A scripted chart library (even a simple matplotlib/D3 template) turns per-language rebuilds into a build step.
4. **Retouch only what's stranded.** For pixel-only graphics, a DTP specialist rebuilds the text layers in Photoshop or Illustrator — schedule it, don't discover it at delivery.
5. **Review in context with native reviewers.** Numbers get misread when moved: a swapped decimal separator is a factual error, not a typo. Chart QA belongs in the [DTP checklist](/news/technical-manual-translation-dtp-checklist/), with the numbers checked against source data, not just the labels against the glossary.

## The cost picture

Localizing a graphic properly costs anywhere from near-zero (regenerated from layered source) to more than the surrounding page's translation (pixel-baked infographic, ten languages, RTL variants). The leverage is entirely upstream: teams that author localizable graphics once localize every subsequent document cheaply. Teams that don't pay the redraw tax forever.

Charts persuade where paragraphs don't — a buyer comparing torque curves is closer to an RFQ than one reading marketing copy. Our [DTP team](/services/localization/dtp/) localizes data graphics as part of every document project: extraction, regeneration, RTL rebuilds, and numeric QA included. [Send us a sample document](/contact/) and we'll show you which of your graphics are localizable as-is and which are time bombs.
