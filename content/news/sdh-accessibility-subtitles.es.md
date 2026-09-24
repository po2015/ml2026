---
title: "SDH y accesibilidad: subtítulos más allá de la traducción"
date: 2026-12-01T11:10:00+08:00
publishDate: 2026-12-01T11:10:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["Localización de vídeo", "SDH", "accesibilidad", "subtítulos"]
keywords: ["subtítulos sdh", "subtítulos de accesibilidad", "subtítulos para personas sordas y con discapacidad auditiva"]
cover: "/images/news/sdh-accessibility-subtitles.jpg"
author: "MediaLocalize Team"
summary: "Los subtítulos traducidos dan por sentado que el espectador puede oír el audio. El SDH da por sentado que no puede: etiquetas de hablante, indicaciones sonoras y reglas de lectura diferentes. Qué cambia, cuánto cuesta y cuándo lo necesita."
---

Su vídeo de producto tiene subtítulos en alemán perfectos: una traducción fiel de todo lo que dice el narrador. Entonces una ingeniera alemana sorda lo ve: una segunda voz responde a una pregunta que ella no sabía que era una pregunta, un sonido de alarma crucial no se menciona, y el presentador fuera de pantalla demuestra algo mientras los subtítulos describen otra cosa. La traducción estaba bien; el *tipo* de subtítulo era el equivocado. Lo que ella necesitaba era SDH: subtítulos para personas sordas y con discapacidad auditiva (Subtitles for the Deaf and Hard of Hearing).

El SDH no es una cuestión de traducción; es una cuestión de completitud de la información. Esto es lo que lo distingue, cuándo es obligatorio y cómo producirlo sin duplicar el presupuesto.

## Qué añade el SDH más allá del diálogo

Los subtítulos traducidos estándar transmiten un solo canal: el habla, reproducida en el idioma de destino. El SDH transmite tres:

**1. Identificación del hablante.** Quién habla importa cuando no se pueden oír los cambios de voz. Convenciones: una etiqueta con el nombre (`MARIA:`), un guion por hablante en diálogos alternados, o codificación por color o posición (la posición es la más robusta: los colores desaparecen en reproducciones en escala de grises y proyectores). El habla fuera de pantalla también se marca, normalmente con cursivas o una etiqueta.

**2. Audio no verbal.** `[suena una alarma]`, `[teléfono sonando]`, `[la maquinaria se detiene]`: cualquier cosa que un espectador oyente use para seguir el contenido. La prueba: silencie el vídeo, lea solo sus subtítulos y compruebe si alguna acción en pantalla se vuelve inexplicable. Las indicaciones sonoras llevan corchetes y minúsculas; la música significativa se menciona (`[música tensa]`), la música ambiental de fondo no.

**3. Adaptación de lectura.** Las audiencias de SDH leen *toda* la información, así que el ritmo y la segmentación importan más: saltos de línea en los límites de las frases, máximo de dos líneas, tiempo de visualización adecuado por línea y ningún subtítulo que desaparezca a mitad de frase porque cambió el plano. Las [reglas de formato](/es/news/subtitle-formatting-rules/) del subtitulado estándar se aplican con márgenes más estrictos.

## Cuándo el SDH es obligatorio y cuándo opcional

- **Requisitos legales**: contenidos de radiodifusión y del sector público en Estados Unidos (FCC/ADA), la UE (Ley Europea de Accesibilidad, aplicable a servicios de streaming y vídeo de comercio electrónico desde 2025) y regímenes similares en otros lugares. Si sus vídeos están en portales de contratación de gobiernos, educación o grandes empresas, dé por sentado que le pedirán documentación de accesibilidad.
- **Normas de plataforma**: las plataformas de e-learning y los despliegues corporativos en LMS tratan cada vez más el SDH como requisito básico; WCAG 2.1 AA (el estándar que citan la mayoría de las políticas) exige subtítulos para el audio pregrabado en medios sincronizados.
- **El argumento de la mayoría silenciosa**: la mayor parte del vídeo en redes sociales se ve sin sonido; los subtítulos estilo SDH (con indicaciones sonoras) también sirven a esa audiencia. El trabajo de accesibilidad funciona también como trabajo de engagement.

Incluso donde nada es legalmente obligatorio, la pregunta honesta es más simple: *¿puede cada espectador objetivo seguir este vídeo con el sonido apagado?* Si no, está publicando menos que su contenido.

## SDH y traducción: qué va primero

El flujo eficiente:

1. **Cree el SDH en el idioma de origen**: una sola pasada que identifica hablantes, indicaciones sonoras y problemas de ritmo de lectura.
2. **Traduzca el archivo SDH**, manteniendo las convenciones de indicaciones (etiquetas, corchetes) y revisando de nuevo las longitudes de línea por idioma. Las etiquetas de hablante y las descripciones de sonidos en alemán se expanden como todo lo demás; una indicación `[liberación de presión hidráulica]` necesita la misma [conciencia de la expansión](/es/news/text-expansion-translation-layout/) que el diálogo.

El flujo caro es el inverso: traducir subtítulos de solo diálogo y luego añadir el SDH a posteriori por idioma. Cada indicación se añade cuatro veces en lugar de una, y las decisiones de sincronización se vuelven a discutir por idioma. Cree una vez en el origen; localice el archivo completo.

## Los detalles de producción que muerden

- **Posicionamiento**: el SDH desplaza los subtítulos para no tapar el texto en pantalla ni las bocas de los hablantes; un archivo de subtítulos traducido que siempre se queda abajo en el centro no supera el listón del SDH. Esto interactúa con el [texto en pantalla localizado](/es/news/on-screen-text-video-localization/): si sus rótulos inferiores en alemán se movieron, las zonas seguras de los subtítulos en alemán también se movieron.
- **Límites de velocidad de lectura**: los objetivos estándar son ~17 caracteres por segundo para adultos, menos para contenido infantil. Los vídeos densos en diálogo (mesas redondas, vídeos explicativos rápidos) a veces necesitan subtítulos *editados* (condensados, no literales) para seguir siendo legibles. Los estándares SDH lo permiten explícitamente; anótelo en su guía de estilo para que los traductores condensen de forma consistente.
- **Formatos de archivo**: las convenciones de indicaciones viven en el archivo de subtítulos, pero su renderizado depende del formato y del reproductor: WebVTT y TTML llevan posicionamiento y estilos; SRT no lleva casi nada. Para entregables SDH, especifique el formato por plataforma, no "lo que exporte la herramienta".
- **Música y letras**: si la letra de una canción importa (un jingle de marca), subtitúlela con la convención ♪; si es música de ambiente, una indicación al inicio es suficiente.

## Cuánto cuesta

La creación de SDH añade aproximadamente un 20–40 % sobre una pasada de subtítulos estándar para el idioma de origen; el incremento está en escuchar las indicaciones y posicionar, no en traducir. Localizar el archivo SDH cuesta casi lo mismo que localizar subtítulos estándar. La accesibilidad lista para cumplimiento (más una declaración de conformidad, si la necesita para un proceso de contratación) es donde el control de calidad profesional se gana su honorario.

Nuestro [equipo de localización de vídeo](/es/services/localization/video/) produce SDH como un entregable de primera clase: creado una sola vez en el origen, localizado con las convenciones de indicaciones intactas, entregado en el formato de cada plataforma. [Envíenos un vídeo](/es/contact/) y le diremos si sus subtítulos actuales superan la prueba del silencio.
