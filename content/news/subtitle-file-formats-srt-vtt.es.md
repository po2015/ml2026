---
title: "SRT, VTT, ASS: los formatos de archivos de subtítulos explicados"
date: 2027-04-12T21:14:00+08:00
publishDate: 2027-04-12T21:14:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["Subtitulado", "localización de video", "formatos de archivo", "captioning"]
keywords: ["formatos de archivos de subtítulos", "diferencia srt vtt ass", "formatos de subtítulos localización de video"]
cover: "/images/news/subtitle-file-formats-srt-vtt.jpg"
author: "MediaLocalize Team"
summary: "Sus subtítulos en chino vuelven como un SRT que no se importa en su reproductor web; el archivo en árabe muestra cada línea en orden inverso; la plataforma de formación exige VTT y usted tiene SRT. Los archivos de subtítulos parecen triviales — texto más códigos de tiempo — hasta que se rompen. Qué hacen realmente los tres formatos que importan, cuándo usar cada uno y las trampas de codificación que arruinan las entregas multilingües."
---

Una gerente de marketing recibe los subtítulos terminados de un video de producto: doce idiomas, todos entregados como archivos `.srt`. El reproductor del equipo web los rechaza — necesita WebVTT. Alguien renombra la extensión, y ahora la mitad de los videos se reproducen sin subtítulos. Mientras tanto, el archivo en árabe se abre en el Bloc de notas como un galimatías invertido, y el japonés muestra signos de interrogación donde deberían ir los caracteres. Nada de esto es exótico: los archivos de subtítulos son texto plano con códigos de tiempo, pero esa simplicidad esconde exactamente los detalles — capacidades del formato, codificación, dirección del texto — que deciden si sus [subtítulos multilingües](/es/news/subtitle-translation-best-practices/) realmente se reproducen. Esta es la guía práctica de los tres formatos que encontrará y las trampas entre ellos.

## SRT: el caballo de batalla universal

SubRip (`.srt`) es el formato más antiguo y más compatible: un número de secuencia, una línea de códigos de tiempo, el texto, una línea en blanco — nada más.

```srt
1
00:00:02,500 --> 00:00:05,000
The PVG-32 valve handles flows up to 130 l/min.

2
00:00:05,200 --> 00:00:08,400
Commissioning takes under ten minutes.
```

Los códigos de tiempo usan `horas:minutos:segundos,milisegundos` — fíjese en la **coma**. SRT casi no admite estilos (algunos reproductores respetan etiquetas básicas `<i>`/`<b>`/`<u>`, muchos no), ni posicionamiento, ni metadatos. Esa limitación es su fortaleza: todos los editores, reproductores, plataformas y herramientas CAT del planeta leen SRT. Úselo como su **formato de intercambio de traducción** — lo que envía a los traductores y lo que recibe de vuelta — y para las plataformas que lo aceptan (YouTube, LinkedIn y la mayoría de las plataformas sociales lo hacen).

## WebVTT: el estándar web

WebVTT (`.vtt`) es lo que exigen los elementos `<track>` de HTML5 y la mayoría de los reproductores web. Se parece a SRT con una cabecera y diferencias que importan:

```vtt
WEBVTT

00:02.500 --> 00:05.000
The PVG-32 valve handles flows up to 130 l/min.

NOTE
Reviewed by native speaker, 2027-04-10

00:05.200 --> 00:08.400
Commissioning takes under ten minutes.
```

- El archivo **debe empezar con `WEBVTT`** — un SRT renombrado sin la cabecera es un VTT inválido, razón por la que el truco de renombrar falla.
- Los códigos de tiempo usan un **punto** para los milisegundos (`00:02.500`), y las horas son opcionales.
- Admite **ajustes de cue** (posición, alineación, saltos de línea), **etiquetas de hablante** (`<v Anna>`), **comentarios** (bloques `NOTE`) y estilos basados en CSS mediante `::cue` en la hoja de estilos de la página.

Use VTT para todo lo incrustado en su propio sitio web y para plataformas de e-learning (los [reproductores LMS](/es/news/multilingual-lms-deployment/) esperan VTT de forma abrumadora). El flujo práctico: traduzca en SRT (compatibilidad de herramientas), convierta a VTT para la entrega web — con un conversor de verdad, no renombrando.

## ASS/SSA: cuando el estilo es el punto

Advanced SubStation Alpha (`.ass`) es el formato del subtitulado con estilo: fuentes, tamaños, colores, contornos, sombras por cue, posicionamiento preciso en pantalla, incluso animación. Lo encontrará cuando los subtítulos deban *verse diseñados* — la cultura del anime y los fan-subs lo construyó, pero es igualmente la forma de incrustar subtítulos de marca y posicionados en un video de marketing, o de colocar texto chino para evitar cubrir la interfaz de la demostración en el tercio inferior.

El costo: complejidad y compatibilidad. ASS lleva una sección de estilos completa y una lista de eventos; los reproductores web generalmente no lo leen, y los traductores pueden romper fácilmente sus etiquetas de sustitución (`{\an8}`, `{\pos(320,40)}`). Trate ASS como un **formato de acabado**: la traducción ocurre en SRT/VTT, luego un subtitulador reconstruye el estilo en ASS para la incrustación, y el video con subtítulos incrustados es el entregable. Cuando los subtítulos se [incrustan en lugar de entregarse como archivos](/es/news/burned-in-subtitles-vs-caption-files/), ASS pertenece a la rama de incrustación.

## Las trampas que realmente rompen las entregas

1. **Codificación: UTF-8, con o sin BOM, y nada más.** SRT no tiene declaración de codificación; los archivos guardados como Latin-1 o GB2312 convierten el japonés y el árabe en mojibake. Entregue y exija **UTF-8**. Un BOM ayuda a las herramientas de Windows a detectar la codificación correctamente; la mayoría de los reproductores modernos lo aceptan.
2. **Dirección del texto para árabe y hebreo.** El *archivo* de subtítulos está ordenado lógicamente; el *reproductor* aplica la renderización bidireccional. Las líneas de dirección mixta — una oración en árabe que contiene el nombre de su producto en caracteres latinos — se renderizan mal si la puntuación cae en los bordes de línea. Pruebe los subtítulos en árabe en el reproductor de destino real, no en un editor de texto, y prefiera reproductores con soporte bidi adecuado.
3. **La longitud de línea y la velocidad de lectura sobreviven mal a la traducción.** El alemán es ~30 % más largo que el inglés; un cue de dos líneas en inglés puede convertirse en cuatro líneas en alemán que ningún espectador puede leer en el tiempo en pantalla. La planificación de la [expansión del texto](/es/news/subtitle-text-expansion-contraction/) ocurre en la traducción, pero la verificación de *formato* es la pasada de QA de subtítulos: caracteres por línea, líneas por cue, duración mínima en pantalla.
4. **Desfase de códigos de tiempo tras las ediciones.** Si el video se re-corta después del subtitulado, cada cue se desplaza. Los archivos de subtítulos referencian códigos de tiempo absolutos — cualquier edición los invalida. Bloquee la imagen antes de subtitular, o presupueste una pasada de resincronización.
5. **Manejo de saltos de línea en la conversión.** Los conversores SRT→VTT ocasionalmente destrozan los cues de varias líneas o eliminan los separadores de línea en blanco; revise a mano los archivos convertidos antes de subirlos.

## Las recomendaciones prácticas

- **Un máster por idioma, en SRT, UTF-8**, archivado junto al video — su fuente de verdad para ediciones futuras y conversiones de plataforma.
- **Convierta por destino**: VTT para su sitio web y LMS, SRT para YouTube/redes sociales, ASS→incrustación para piezas de marketing diseñadas. Las conversiones son mecánicas y automatizables.
- **Especifique el formato en el brief del proveedor** ("entregar SRT UTF-8 + VTT") en lugar de descubrir los requisitos del reproductor después de la entrega — la misma disciplina que [especificar entregables en los briefs de localización](/es/news/localization-vendor-brief-template/) en general.
- **Mantenga cortos los conteos de líneas CJK**: el chino/japonés/coreano transmiten más por carácter, así que los cues traducidos a menudo se acortan — una oportunidad de aumentar la comodidad de lectura, según las [notas de subtitulado CJK](/es/news/chinese-video-subtitling-guide/).

Los formatos son la capa aburrida del subtitulado — hasta que un video de lanzamiento se publica sin subtítulos porque un archivo se renombró en lugar de convertirse. Nuestro [equipo de localización de video](/es/services/localization/video/) entrega subtítulos en cada formato de destino con la pasada de QA (codificación, bidi, métricas de línea, sincronización) ya hecha. [Envíenos su video y las plataformas de destino](/es/contact/) y nos ocuparemos de toda la cadena, de la transcripción a los archivos listos para el reproductor.
