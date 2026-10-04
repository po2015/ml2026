---
title: "SSML (Lenguaje de marcado de síntesis de voz)"
definition: "El lenguaje de marcado que dirige a los motores de texto a voz: pronunciación, pausas, énfasis y cómo se leen en voz alta números y abreviaturas."
description: "El lenguaje de marcado que dirige a los motores de texto a voz: pronunciación, pausas, énfasis y cómo se leen en voz alta números y abreviaturas."
date: 2026-10-04
related:
  - ["Doblaje con IA", "/services/localization/dubbing/"]
  - ["TTS neuronal", "/news/neural-tts-ai-voice-localization/"]
---

SSML (Speech Synthesis Markup Language) es la capa de control del texto a voz. El texto plano dice al motor TTS qué decir; SSML le dice cómo: dónde pausar, qué enfatizar, a qué velocidad hablar y cómo pronunciar las palabras que de otro modo pronunciaría mal.

Para la locución corporativa y de producto, las funciones críticas son la pronunciación y la interpretación. Una etiqueta <phoneme> puede hacer que tu marca se diga bien en todos los idiomas. <say-as> indica al motor que lea «2026» como año, «B2B» como letras y «3/4» como fracción y no como fecha. <break> y <emphasis> modelan el ritmo para que las listas de especificaciones suenen habladas, no leídas.

Sin SSML, las voces de IA se delatan exactamente ahí: referencias leídas como galimatías, unidades destrozadas, énfasis en la palabra equivocada. Con él —más un léxico de pronunciación personalizado— la narración de IA supera la revisión de hablantes nativos.

SSML es parte central del flujo de doblaje con IA de MediaLocalize: cada guion recibe marcado SSML ajustado por idioma y cada proyecto construye un léxico con tus marcas, referencias y terminología, verificado por nativos antes de la entrega.
