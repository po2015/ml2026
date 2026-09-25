---
title: "Text Expansion in Course UI: Buttons and Menus"
date: 2027-01-12T19:36:00+08:00
publishDate: 2027-01-12T19:36:00+08:00
category: "industry"
category_label: "Industry"
tags: ["E-Learning", "UI localization", "text expansion", "course design"]
keywords: ["elearning ui localization", "text expansion buttons", "course interface translation"]
cover: "/images/news/elearning-ui-text-expansion.jpg"
author: "MediaLocalize Team"
summary: "\"Submit\" fits its button. \"Absenden\" almost does. \"Envoyer la réponse\" doesn't. Text expansion breaks course interfaces before learners ever reach the content — how to design course UI that survives translation."
---

A corporate academy launches in eight languages. The content is beautifully translated; the course is unusable. The Submit button overflows its pill shape in German, the navigation menu wraps onto two lines in French, the "Next" arrow in the Arabic version points the wrong way, and a progress label reading "Question 3 of 10" collides with the score display in Russian. None of this is a translation error — it's a design assumption: that interface text is a fixed size. It never is. English is one of the most compact languages on earth, and every course UI designed around English string lengths is a layout incident waiting for its second language.

## The numbers behind the breakage

The expansion factors are consistent enough to design against:

| Language | Typical expansion vs English | Classic casualty |
|---|---|---|
| German | +25–35% | Compound nouns that can't hyphenate gracefully |
| French | +15–25% | Articles and prepositions everywhere |
| Russian | +15–25% | Long words, no short synonyms for UI terms |
| Spanish | +15–25% | "Next" → "Siguiente" is the gentle case |
| Arabic | +25% *and* RTL | Layout mirrors; strings also grow |
| CJK | −20–40% (shorter) | The opposite problem: UI looks empty, hit targets shrink |

The UI zones that break first, in order: **buttons** (short English verbs become long phrases), **fixed-width menus and tabs**, **labels paired with values** ("Score: 85" — the label grows, the pair collides), **toast/popup messages** sized for one line, and **table headers**. Our general [text expansion guide](/news/text-expansion-translation-layout/) covers the document side; course UI is harsher because there's no fluid page flow to absorb growth — every element sits in a pixel-fixed player.

## Design rules that prevent it

- **Budget 40% extra width for every string container.** If "Submit" defines your button width, the German version is already broken. Size buttons for the longest expected translation, or make them auto-width with sensible max-widths.
- **Never use text-as-image in the player UI.** A button baked into a PNG means graphic rework per language — the same tax as [text baked into charts](/news/infographic-chart-localization/). Live text or it doesn't ship.
- **Separate labels from values.** "Question 3 of 10" as three data-driven components ("Question", 3, "of 10") reassembles per language grammar; as one hardcoded string it mangles in languages with different word order — and some languages need entirely different phrasing ("10 题中的第 3 题").
- **Prefer icons with tooltips for repeat controls**, but never icon-only for critical actions — icon ambiguity across cultures is its own [localization problem](/news/image-icon-color-localization/).
- **Design the Arabic version at the start, not the end.** RTL mirrors the whole player: navigation direction, progress bar fill, "next" arrow direction, as detailed in [RTL web design](/news/rtl-website-design-arabic/). Retrofitting RTL into a finished course costs more than the original UI build.

## The authoring-tool angle

Modern tools help if you use them properly:

- **Storyline/Rise**: player UI text (buttons, messages, menu labels) lives in the *player text labels* set, exported and translated as one unit — per the [Storyline workflow](/news/articulate-storyline-translation-workflow/). Translating slide content but forgetting player labels ships a bilingual Frankenstein: German slides, English buttons.
- **Custom HTML5 players**: strings belong in a resource file (JSON/properties), never inline in code or — worst — in the course content itself.
- **The LMS chrome is also UI**: completion messages, enrollment emails, certificate templates. They expand too.

Whatever the tool, the verification step is the same: **pseudolocalization**. Run the course with a pseudo-locale that pads every string by 40% and flips direction, per the [pseudolocalization testing guide](/news/pseudolocalization-testing-guide/) — every overflow, truncation, and hardcoded string reveals itself in one pass, before a single word is translated. It is the cheapest QA step in the entire localization budget.

## The content-side mitigations

Some expansion problems are better solved in the writing than in the layout:

- **Write shorter source UI text.** "Submit" not "Submit your response"; "Retry" not "Try this question again". Source brevity is the single biggest lever — every word you cut saves space in all eight languages.
- **Keep a UI glossary.** Course interfaces reuse a few dozen strings; translating them consistently (and choosing naturally short equivalents — a native translator's job, not a dictionary's) prevents both overflow and the "three translations of Submit across one course" problem.
- **Numbers and formats stay locale-correct** in scores, dates, and durations — the [formats discipline](/news/date-currency-format-localization/) applies inside courses exactly as on websites.

## A pre-flight checklist

1. All player strings externalized and included in the translation package
2. Every string container tested at +40% width (pseudolocale pass)
3. Labels and values separate; no grammar baked into code
4. RTL variant of the player verified, not assumed
5. Buttons, menus, popups, table headers visually QA'd in the *longest* language (usually German)
6. Certificates and LMS messages checked — learners see those too

Course UI is the frame around your training content; learners forgive an awkward sentence, but a button they can't read or tap costs you the completion rate the whole project exists for. Our [e-learning localization team](/services/localization/elearning/) audits course UI for expansion and RTL as a standard project step — before translation starts, not after it breaks. [Send us a course](/contact/) and we'll run the pseudolocale audit on it.
