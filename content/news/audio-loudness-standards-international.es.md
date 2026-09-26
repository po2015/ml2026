---
title: "Estándares de sonoridad para la entrega internacional de audio"
date: 2027-04-26T08:14:00+08:00
publishDate: 2027-04-26T08:14:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["Doblaje", "producción de audio", "sonoridad", "especificaciones de entrega"]
keywords: ["estándares de sonoridad ebu r128", "especificaciones de entrega de audio", "normalización lufs doblaje"]
cover: "/images/news/audio-loudness-standards-international.jpg"
author: "MediaLocalize Team"
summary: "Su video corporativo se escucha susurrado en YouTube, retumba en LinkedIn y es rechazado por un broadcaster europeo por exceder -23 LUFS. La sonoridad — no el nivel de pico, sino el volumen percibido medido en el tiempo — está regulada, es específica de cada plataforma e invisible hasta que falla. Los estándares que importan (EBU R128, ATSC A/85, especificaciones de plataformas), qué significan los números y cómo especificar entregas de audio multilingües que pasen en todas partes."
---

Un equipo de marketing entrega su video de producto recién doblado: inglés, alemán, japonés. En sus monitores de edición los tres suenan idénticos. Entonces llega la realidad: YouTube baja la versión en inglés pero no la alemana (ahora difieren), el feed de LinkedIn hace que la japonesa suene aplastada, y un organizador de feria alemán que la reproduce en el sistema de difusión del pabellón reporta distorsión. El ingeniero de mezcla insiste en que los picos nunca saturaron — y tiene razón, porque los picos nunca fueron el problema. El problema es la **sonoridad**: el volumen percibido medido como un promedio integrado (LUFS), no los picos instantáneos (dBFS). Cada mercado de difusión y plataforma tiene su propio objetivo de sonoridad, las entregas que no lo alcanzan son rechazadas o ajustadas automáticamente (mal), y los programas multilingües multiplican el riesgo — N idiomas, cada uno necesitando cumplir la misma especificación, en cada plataforma. Esto es lo que significan los números y cómo especificar las entregas una vez, correctamente.

## Sonoridad 101: los términos que importan

- **LUFS (o LKFS)** — la unidad de sonoridad percibida; 1 LU ≈ 1 dB. Existen tres mediciones: **Integrated** (promedio de todo el programa — el número que importa a las especificaciones), **Short-term** (ventana de 3 segundos), **Momentary** (400 ms).
- **True Peak (dBTP)** — el pico real de la señal analógica reconstruida, que puede exceder el pico de muestra digital; las especificaciones lo limitan (típicamente a -1 o -2 dBTP) para prevenir distorsión tras la codificación. "Mi medidor no mostró saturación" suele significar que los picos de muestra estaban bien mientras los true peaks no.
- **LRA (Loudness Range)** — la amplitud dinámica del programa, en LU. Las especificaciones de difusión a veces la limitan; los podcasts y el video web mayormente no, pero un LRA salvajemente variable (intro susurrada, demo gritada) hace que cualquier normalización única suene mal.

El cambio mental clave respecto a la era del medidor de picos: **la normalización ahora se basa en sonoridad, no en picos.** Dos archivos pueden ambos alcanzar picos de -1 dBFS y diferir en sonoridad por 10 LU — ese es su escenario de "YouTube bajó uno".

## El mapa de estándares

| Objetivo | Sonoridad integrada | True Peak | Dónde aplica |
|---|---|---|---|
| **EBU R128** (difusión europea) | -23 LUFS ±0.5 | -1 dBTP | Broadcasters europeos, sistemas de difusión de ferias/pabellones, muchas especificaciones AV corporativas |
| **ATSC A/85 (CALM Act)** | -24 LUFS ±2 | -2 dBTP | Difusión en EE. UU. |
| **YouTube** | objetivo de normalización ~-14 LUFS | — | Baja el contenido más alto de volumen (el contenido silencioso se deja igual) |
| **Spotify** | -14 LUFS | -1 dBTP | Plataformas de podcast/audio en general similares |
| **Apple Podcasts** | -16 LUFS | -1 dBTP | Entregables orientados a audio |
| **Feeds sociales (Meta/LinkedIn/TikTok)** | ~-14 LUFS de facto | — | Compresión intensa de la dinámica en la reproducción |

Note la estructura: **la difusión es silenciosa (-23/-24), las plataformas en línea son altas (-14 a -16)**. Un solo máster no puede ser óptimo para ambos — por eso "tenemos un archivo de audio" es un problema de entrega, no simplicidad.

## Por qué los programas multilingües fallan en esto

1. **Cada idioma se mezcla por separado** — a menudo por proveedores distintos — y "suena igual en mis altavoces" varía por estudio. El idioma A queda en -18 LUFS, el idioma B en -26: tras la normalización de la plataforma, suenan a volúmenes distintos *y* el más silencioso revela ruido.
2. **Las pistas híbridas IA/humano derivan.** Los segmentos generados por IA y los grabados en estudio tienen dinámicas distintas; sin una [pasada de sonoridad unificada en la etapa de mezcla](/es/news/hybrid-ai-human-voiceover-workflow/), las costuras se oyen como saltos de volumen.
3. **Proliferación de entregables.** 5 idiomas × 3 objetivos (difusión -23, web -14, podcast -16) = 15 variantes de sonoridad — a menos que el pipeline las renderice desde una sola mezcla sistemáticamente, alguien normaliza a mano y los archivos divergen.
4. **La codificación revela los true peaks.** Un archivo con pico de muestra a 0 dBFS distorsiona tras la codificación AAC/Opus aunque se viera limpio — la limitación de true peak a -1 dBTP es la solución, aplicada antes de la entrega, no descubierta por la plataforma.

## La especificación práctica de entrega (róbela)

Ponga esto en cada brief de audio/voz en off — su [plantilla de brief para proveedores](/es/news/localization-vendor-brief-template/) debería llevarlo textualmente:

1. **Mezcla máster**: diálogo normalizado, música y efectos mezclados a gusto, luego el programa completo medido — no igualado a ojo.
2. **Máster web/video**: -14 LUFS integrado, true peak ≤ -1 dBTP, un archivo por idioma. (Cubre YouTube, LinkedIn, incrustaciones en sitio web, [videos de producto](/es/news/product-demo-video-localization/) en general.)
3. **Máster para difusión/feria** (si alguna vez se reproduce en infraestructura de difusión): -23 LUFS integrado ±0.5, true peak ≤ -1 dBTP, conforme a EBU R128 — y confirme la hoja de especificaciones real del destino, ya que algunos pabellones y broadcasters publican la suya propia.
4. **Cada idioma medido y documentado**: un informe de sonoridad de una línea por archivo (LUFS integrado, true peak, LRA) desde un medidor real (medidor de sonoridad en modo EBU, o la salida de `loudnorm` de ffmpeg) — no "el ingeniero dice que sonaba bien".
5. **Consistencia entre idiomas**: todos los idiomas dentro de ±0.5 LU entre sí para el mismo objetivo — de modo que el selector de idioma nunca cambie el volumen percibido.

## El flujo de trabajo que vuelve esto aburrido

Mezcle una vez por idioma → mida → corrija con una pasada de normalización de sonoridad (limitación transparente, no ganancia bruta) → renderice las variantes por objetivo desde la mezcla masterizada → verifique el render, no la sesión. El `loudnorm` de dos pasadas de ffmpeg hace esto de forma fiable y scriptable, lo que significa que el problema de las 15 variantes es un trabajo por lotes, no 15 sesiones de mezcla. Para programas continuos — [bibliotecas de cursos](/es/news/batch-video-localization-course-libraries/), series de video — incorpore la especificación de sonoridad en la lista de verificación de entrega para que cada archivo futuro pase por defecto.

La sonoridad es la especificación menos glamorosa del audio y la más propensa a hacer que su video sea rechazado, bajado de volumen o reproducido a tres volúmenes distintos en tres idiomas. Nuestro [equipo de doblaje](/es/services/localization/dubbing/) entrega cada idioma con sonoridad medida y documentada — R128 para objetivos de difusión, -14 LUFS para la web, consistente en todo su conjunto de idiomas. [Envíenos su lista de plataformas](/es/contact/) y especificaremos los entregables una vez, correctamente.
