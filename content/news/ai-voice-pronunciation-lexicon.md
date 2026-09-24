---
title: "AI Voice Pronunciation: Getting Brand Names Right"
date: 2026-11-10T12:35:00+08:00
publishDate: 2026-11-10T12:35:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["AI Dubbing", "TTS", "pronunciation", "SSML"]
keywords: ["tts pronunciation control", "ai voice brand names", "pronunciation lexicon"]
cover: "/images/news/ai-voice-pronunciation-lexicon.jpg"
author: "MediaLocalize Team"
summary: "Your TTS voice will mispronounce your company name, your product names, and your industry's acronyms. How pronunciation lexicons fix it — and how to build one that scales."
---

Every text-to-speech engine reads text by statistical guesswork. Feed it "Xinwei's XW-4500 meets IP67 per ISO 20653" and you will hear your brand name mangled, your model number read as a word, and "ISO" spelled out or not depending on the engine's mood. In a 30-second product video this is embarrassing; in a 200-module training library it is brand damage at scale.

The fix is a pronunciation lexicon — a documented, reusable mapping from your written terms to how they must sound. This article covers how TTS pronunciation control works and how to build a lexicon that survives growth.

## Why default pronunciation fails on business content

TTS engines learn pronunciation from general text. Your content is not general text:

- **Invented brand names** have no dictionary entry. "Zontec," "Huayu," "Wilo" — the engine guesses from spelling, and guesses wrong in ways that differ per language.
- **Model numbers and codes**: "XW-4500" might come out as "X W minus four thousand five hundred" or "exwuh forty-five hundred." Neither is what your sales team says.
- **Acronyms with conventions**: "SQL" is "sequel" in some teams and "S-Q-L" in others; "ISO" is usually spelled out; "API" always is. The engine cannot know your convention.
- **Homographs**: "lead" (metal vs. verb), "read" (present vs. past), "live" (adjective vs. verb). Context usually resolves these — until it doesn't, mid-sentence in your compliance training.
- **Foreign words inside another language's narration**: a German voice reading your English product name, or an English voice reading "Porsche" or "Hannover Messe." Cross-language pronunciation is where engines are weakest.

## The three control mechanisms

### 1. SSML inline markup

Speech Synthesis Markup Language embeds pronunciation instructions in the text:

```xml
<phoneme alphabet="ipa" ph="ˈzɒn.tɛk">Zontec</phoneme>
<say-as interpret-as="characters">XW</say-as>-<say-as interpret-as="number">4500</say-as>
```

Precise and supported by all major engines (Amazon Polly, Google Cloud TTS, Azure, ElevenLabs with varying dialects). The catch: inline SSML lives inside each script, so the same fix gets pasted into hundreds of files — and updated hundreds of times when it changes.

### 2. Custom lexicons (the scalable route)

Most platforms let you upload a pronunciation dictionary that applies to every request: term → phonetic spelling or IPA. One file, centrally maintained, applies to all current and future scripts. This is the only approach that scales past a handful of videos.

### 3. Respellings in the source text

Writing "Zon-tek" or "eye-ess-oh" directly in scripts. Works in a pinch, but pollutes your scripts, confuses translators, and breaks when you change engines. Use only for one-off emergencies.

## Building your lexicon: the practical process

**Step 1: Harvest terms.** Extract candidates from your existing scripts, product catalogs, and style guide: company name, product names, model numbers, acronyms, technical terms, personnel names, place names. A typical manufacturer ends up with 50–300 entries.

**Step 2: Record the truth.** Have the people who own each term say it: your CEO says the company name, product managers say product names, engineers say technical terms. Disagreements here are real (two divisions pronouncing the same product differently) and the lexicon forces a decision — that is a feature.

**Step 3: Encode per engine and language.** The same term needs separate entries per TTS engine (their phoneme sets differ) and per language (your German voice pronounces "Bosch" correctly already; your English voice does not). IPA where supported, platform-specific phoneme alphabets where not.

**Step 4: Test with minimal pairs.** Render each entry in a short sentence, listen, adjust. Budget for two or three iterations on the tricky 10% — usually names with unusual vowel sequences.

**Step 5: Version it like code.** The lexicon lives in version control, gets reviewed when products launch, and ships with every project brief. Our [vendor brief template](/news/localization-vendor-brief-template/) includes it for exactly this reason.

## Lexicon maintenance rules

- **One owner.** Pronunciation decisions by committee produce drift; assign the lexicon to whoever owns brand or product marketing.
- **New product = lexicon entry before launch**, not after the first mispronounced video.
- **Re-validate when changing engines or voices.** Lexicons are not portable; a voice upgrade can change how your entries render.
- **Log every override.** Inline SSML exceptions should be rare, documented, and migrated into the lexicon when they repeat.

## What this costs and saves

A first lexicon for a typical B2B company takes two to four days including stakeholder recording and testing. It then eliminates the single most common source of revision requests on AI-dubbed content — and it is the difference between AI narration that sounds mass-produced and narration that sounds like *your* company. For how this fits into voice selection overall, see our guide to [choosing an AI voice](/news/choosing-ai-voice-brand/).

Our [dubbing team](/services/localization/dubbing/) builds and maintains pronunciation lexicons as part of every AI voice project, across all major TTS platforms. [Send us your product list](/contact/) and we will return a tested starter lexicon with sample renderings.
