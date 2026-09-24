---
title: "Dates, Currency, Units: Small Details That Break Trust"
date: 2026-12-15T20:59:00+08:00
publishDate: 2026-12-15T20:59:00+08:00
category: "industry"
category_label: "Industry"
tags: ["localization", "formats", "i18n", "user experience"]
keywords: ["date format localization", "currency localization", "units conversion website"]
cover: "/images/news/date-currency-format-localization.jpg"
author: "MediaLocalize Team"
summary: "03/04/2026 means April 3rd to a German and March 4th to an American. Formatting errors are small, constant, and corrosive — a field guide to getting dates, currency, numbers, and units right per market."
---

A German buyer reads your delivery promise "03/04/2026" as April 3rd; you meant March 4th. An Argentine buyer sees "$1.500" and can't tell whether it's fifteen hundred dollars or one and a half. A Japanese engineer finds torque specs in foot-pounds and closes the datasheet. None of these are translation errors — every word was correct. They're *format* errors, and they do quiet, compounding damage: each one tells the reader this document wasn't made for them.

Formats are the most neglected layer of localization because they look like details. Here is the field guide.

## Dates: the ambiguity trap

The core problem: numeric dates are ambiguous across markets. `03/04/2026` is March 4 in the US, April 3 in most of Europe and Latin America, and April 3rd again in a different order (2026/04/03) in Japan and China. There is no safe numeric-only format except ISO 8601 (`2026-04-03`), which is unambiguous but reads as technical.

Practical rules:

- **In prose, spell the month**: "3 April 2026" or "April 3, 2026" per locale convention. Unambiguous everywhere and it reads naturally.
- **In tables and tight UI, use ISO 8601** or a locale-aware formatter — never hardcode `MM/DD/YYYY`.
- **Weekday and month names must come from the locale**, not string replacement ("Mon" → "Mon" in German is "Mo"; May is "May" in English, "mai" in French, "Mai" in German, "mayo" in Spanish — naive truncation breaks).
- **Calendars**: Gulf documents sometimes pair Gregorian with Hijri dates; Japan has era years (Reiwa 8 = 2026) in official contexts. B2B web content can stay Gregorian, but know the contexts where your buyers' paperwork won't.

## Numbers: separators are not decoration

| Market | 1,500,000.50 written as |
|---|---|
| US / UK / China / Japan | 1,500,000.50 |
| Germany / Spain / Brazil | 1.500.000,50 |
| France | 1 500 000,50 (narrow spaces) |
| Switzerland | 1'500'000.50 |
| India | 15,00,000.50 (lakh grouping) |

The failure modes: your English site shows "1.500 kg" (a German reads one and a half kilos, you meant 1,500), or a form validates `1,5` as invalid because it expects a dot. Two rules fix most of it: **render numbers through a locale-aware formatter** (every modern framework has one; Hugo sites can format at build time), and **accept both separators in form input**, normalizing server-side. For measurements, always append the unit — a bare number forces the reader to guess the system.

## Currency: symbol, position, and which dollar

- **"$" is five currencies** (US, Canadian, Australian, Singapore, Hong Kong dollars — and "peso" shares the symbol in Mexico and Argentina). In international contexts write `USD 1,500` or `US$1,500`, never bare `$`.
- **Symbol position varies**: `$1,500` but `1 500 €` in French, `1.500 €` in German, `¥150,000`. The formatter knows; hardcoded templates don't.
- **Which currency to show**: for cross-border B2B, USD or EUR with a note is standard and honest. Showing local currency converted at an unstated rate creates a different problem — quotes that don't match. Whatever you choose, state it: "Prices in USD, EXW Shenzhen."
- **Large numbers**: Indian buyers think in lakhs and crores (1 crore = 10 million); Chinese in 万 (10,000) and 亿 (100 million). A "million-unit capacity" claim may land better restated in local magnitude for those markets.

## Units: pick a system per audience, show both when critical

The industrial world is metric, with one giant exception: US customary units, and their persistence in aerospace, oil & gas (API specs), and some fastener/thread standards. Rules that prevent the worst errors:

- **Default to metric for international audiences**; add imperial in parentheses for US-facing content, not the reverse.
- **Never convert silently in technical specs.** A 25.4 mm dimension that started life as 1 inch should say `1″ (25.4 mm)` — the converted value alone loses the information that it's a standard size, and rounding (25 mm ≠ 25.4 mm) has caused real manufacturing disputes.
- **Pressure, torque, energy have market favorites**: bar vs psi vs MPa, Nm vs ft-lb, kW vs hp (and PS in Germany, where 1 PS ≠ 1 hp). Match the market's convention and keep the original in parentheses.
- **Temperature**: °C everywhere except the US. In recipes-for-industry (curing, annealing specs), give both.

## Phone numbers, addresses, names

- **Phone**: E.164 (`+86 755 1234 5678`) in display and `tel:` links; input fields must accept `+`, spaces, and leading zeros. A form that rejects non-US formats is an inquiry filter — the same class of friction we flagged in [trust signals](/news/b2b-website-trust-signals/).
- **Addresses**: field order varies (Japan: large-to-small, postal code first; Germany: street then number). One rigid "Address 1 / City / State / ZIP" form misfits most of the world — "State" alone excludes half your markets.
- **Names**: single "Full name" field beats "First/Last" (Chinese and Japanese order, Spanish double surnames, Indonesian mononyms). And let UTF-8 through: a form rejecting "José" or "Müller" is failing the same encoding test that [pseudo-localization](/news/pseudolocalization-testing-guide/) exists to catch.

## Making it systematic

Formats go wrong in code and templates, so fix them there:

1. **One formatter per stack**, used everywhere — no hand-built date strings.
2. **Locale drives format, language drives words** — an English page for German readers (en-de thinking) formats German-style; don't couple format to translation language blindly.
3. **Test with pseudo-locales and real ones**: set your browser to de-DE and ar-EG and click every page type once.
4. **Add formats to the localization style guide** next to fonts and terminology, so every new market inherits the decisions.

None of this is expensive; all of it is visible. Buyers forgive an imperfect sentence; they don't forgive a delivery date they can't parse. Our [localization team](/services/localization/) audits formatting as part of every website project — [send us your URL](/contact/) and we'll list what your dates and numbers are really saying.
