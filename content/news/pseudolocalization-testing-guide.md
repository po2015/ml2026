---
title: "Pseudo-Localization: Test Before You Translate"
date: 2026-11-09T11:59:00+08:00
publishDate: 2026-11-09T11:59:00+08:00
category: "industry"
category_label: "Industry"
tags: ["localization", "pseudolocalization", "testing", "internationalization"]
keywords: ["pseudolocalization testing", "pseudo-localization", "i18n testing"]
cover: "/images/news/pseudolocalization-testing-guide.jpg"
author: "MediaLocalize Team"
summary: "Fake-translate your UI before paying for real translation. Pseudo-localization catches layout breaks, hardcoded strings, and encoding bugs while they cost nothing to fix."
---

Here is an uncomfortable truth about multilingual projects: most of the bugs are not in the translation. They are in your code and layouts — hardcoded English strings, buttons that clip German text, forms that reject accented names, templates that garble Arabic. Discovering these after paying for five languages of translation means fixing them five times.

Pseudo-localization exists to find these bugs first, for free. It is a fake translation: your English text is mechanically transformed to simulate what real translation will do — lengthened, accented, wrapped in brackets — and run through your actual UI. What breaks now would have broken in production.

## What pseudo-localization actually does

A typical pseudo-localization transform turns:

`Save changes` → `[Šàṽé çħàñğéš~~~ ąć]`

Three things happen in that one string:

1. **Character substitution**: vowels get accented versions (à, ṽ, é). This instantly exposes encoding problems — if your stack mishandles UTF-8, these characters render as `Ã©` or `?`.
2. **Expansion**: the string grows 30–40%, simulating German/Russian/Spanish text length. Buttons, menus, tables, and dialog boxes show immediately whether they have room.
3. **Boundary markers**: brackets (here `[` and `ąć]`) wrap each string. Truncated text loses its closing marker, so clipped strings are visible at a glance. Concatenated strings — two separately translated fragments jammed together — show two markers in one label, exposing strings that will be impossible to translate correctly.

Some setups also add a **mirroring mode** that reverses layout direction to smoke-test right-to-left rendering for Arabic and Hebrew before you have any Arabic text.

## What it catches (with real examples)

- **Hardcoded strings**: any text that stays in English during a pseudo-localized run was never externalized — translators will never see it, and it will ship in English in your German product. This is the single most common find.
- **Clipped and overlapping text**: fixed-height list items, fixed-width nav, tables sized to English headers.
- **Concatenation**: `"Your order" + status + "was received"` produces word order that works only in English; pseudo markers reveal every instance.
- **Encoding failures**: accented characters turning into mojibake in emails, PDFs, exports, or database round-trips.
- **Font gaps**: missing glyphs show as boxes (tofu) long before a real CJK or Cyrillic string hits the screen.
- **Locale-blind formatting**: dates, currencies, and numbers hardcoded to one format.
- **String ID confusion**: duplicate or reused string keys where one English source string serves two contexts — fine in English, wrong in languages that need two different translations.

## How to run it

1. **Generate the pseudo-locale.** Most stacks have tooling: pseudo-locale options in i18n libraries (i18next, FormatJS), built-in pseudo-localization in Crowdin/Phrase/Lokalise, or simple transform scripts for static sites. For a [Hugo-style static site](/news/website-localization-workflow/), a script that transforms your content files works fine.
2. **Add it as a real locale** (`en-XA` is the conventional pseudo-locale code) so your entire language pipeline — routing, fallbacks, formatting — gets exercised, not just the strings.
3. **Click through real user journeys.** Signup, checkout, forms, error states, emails, PDF exports, search with pseudo input. Screenshots per page beat spot checks.
4. **Log every defect in two buckets**: code issues (hardcoded, concatenated, encoding) and layout issues (clipping, overflow, direction). They get fixed by different people.
5. **Fix and re-run.** Pseudo-localization is cheap enough to run in CI — some teams gate releases on it.

## When to run it

The earlier the better, but three moments matter most:

- **Before the first translation project**: fixes here are single-language fixes. After translation starts, every code fix risks invalidating translated strings.
- **After major UI changes**: new screens and components reintroduce hardcoded strings constantly.
- **Before adding a new script or direction**: first CJK language, first RTL language — run pseudo first, always.

The teams that skip pseudo-localization do not skip the bugs; they discover them during linguistic QA, when fixes cost translation rework, or in production, when they cost customers. A pseudo-localization pass on a typical B2B website takes one engineer a day or two and routinely surfaces dozens of issues — every one of which would have been more expensive later.

If you are planning a multilingual rollout and want to know what will break before you spend on translation, our [localization team](/services/localization/) includes internationalization review in every website project — [start with an audit](/contact/) and we will run pseudo-localization on your site as part of scoping.
