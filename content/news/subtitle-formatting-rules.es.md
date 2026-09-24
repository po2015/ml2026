---
title: "Formato de subtítulos: longitud de línea, velocidad y tiempos"
date: 2026-10-26T18:44:00+08:00
publishDate: 2026-10-26T18:44:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["Localización de video", "subtítulos", "subtitulado", "traducción"]
keywords: ["reglas de formato de subtítulos", "longitud de línea de subtítulos", "velocidad de lectura cps"]
cover: "/images/news/subtitle-formatting-rules.jpg"
author: "MediaLocalize Team"
summary: "Los subtítulos malos hacen que los buenos videos sean imposibles de ver. Las reglas profesionales de longitud de línea, velocidad de lectura y tiempos, y cómo cambian cuando los subtítulos se traducen."
---

Dos pistas de subtítulos pueden contener traducciones idénticas y producir experiencias de visualización completamente distintas. Una es invisible: los espectadores la absorben sin darse cuenta. La otra los hace retroceder, pausar y, finalmente, cerrar el video. La diferencia está en el formato: reglas de longitud de línea, velocidad de lectura y tiempos que los subtituladores profesionales tratan como restricciones, no como sugerencias.

Estas reglas importan el doble en localización, porque la traducción cambia la longitud del texto y la velocidad de lectura de maneras que rompen los flujos de trabajo de subtitulado ingenuos. Esto es lo que dicen realmente los estándares, y qué cambia cuando los subtítulos cruzan idiomas.

## Longitud de línea: el techo de 42 caracteres

El estándar profesional casi universal:

- **Máximo ~42 caracteres por línea** (incluidos los espacios) para escrituras latinas; algunas cadenas de televisión usan 37–40.
- **Máximo dos líneas por evento de subtítulo.** Tres líneas obligan al ojo a desplazarse y cubren demasiada imagen.
- **Los idiomas CJK son más cortos**: aproximadamente 13–16 caracteres por línea para chino y japonés, dos líneas como máximo; los glifos CJK son más anchos y se leen más rápido por carácter.
- **El árabe** sigue presupuestos de caracteres similares a los del alfabeto latino, pero requiere verificaciones de renderizado de derecha a izquierda: la colocación de la puntuación y los números de dirección mixta son los puntos clásicos de fallo.

Corte las líneas en los límites lingüísticos naturales: entre oraciones, después de las preposiciones, manteniendo unidos los sintagmas nominales. Una línea que termina "la nueva bomba / hidráulica ofrece" obliga al lector a retener una frase incompleta; "la nueva / bomba hidráulica ofrece" se lee con limpieza.

## Velocidad de lectura: la restricción que moldea la traducción

Los subtítulos viven o mueren por los caracteres por segundo (CPS): la velocidad a la que los espectadores deben leer para mantener el ritmo:

| Audiencia | CPS máximo (latino) | Notas |
|---|---|---|
| Adultos, contenido estándar | 17–20 CPS | La conocida directriz de Netflix es 20; el broadcast suele ser 17 |
| Contenido infantil | 13–15 CPS | Los lectores más jóvenes necesitan bastante más tiempo |
| SDH / accesibilidad | 17–20 CPS | Incluye identificadores de hablante y descripciones de sonido |
| CJK | ~6–8 caracteres/seg | Menos caracteres transmiten la misma información |

Aquí está la trampa de la localización: **la traducción del inglés al alemán expande el texto entre un 20 y un 35 %**, pero la duración del video no cambia. Un subtítulo sincronizado cómodamente a 18 CPS en inglés se convierte en 23 CPS en alemán: físicamente imposible de leer. Los flujos de trabajo profesionales resuelven esto en la etapa de traducción, no en la de sincronización: los traductores trabajan con las restricciones de CPS visibles y condensan el texto alemán para que quepa. Por eso la traducción de subtítulos es una especialización: un traductor que trabaja a partir de un guion plano, sin datos de tiempo, producirá texto que no se puede mostrar.

## Tiempos: las reglas que los espectadores sienten pero nunca ven

- **Duración mínima de ~1 segundo** (5/6 de segundo es el límite mínimo absoluto en las grandes plataformas de streaming). Cualquier cosa más corta pasa en un destello sin ser leída; fusiónela con un evento vecino o elimínela.
- **Duración máxima de ~6–7 segundos** por evento. Si dura más, los espectadores releen el subtítulo pensando que cambió.
- **Entrada y salida con precisión de fotograma**: los subtítulos deben comenzar y terminar en los cambios de plano siempre que sea posible. Un subtítulo que sobrevive a un corte hace que los espectadores crean que se perdieron algo y retrocedan.
- **Separación entre eventos encadenados**: deje 2 o más fotogramas entre subtítulos consecutivos para que el cerebro registre el cambio; los eventos pegados se leen como una sola línea larga.
- **Tolerancia de sincronización**: entrada dentro de unos pocos fotogramas del inicio del habla; la salida puede retrasarse hasta medio segundo respecto al habla si el texto necesita tiempo de lectura.

## Qué cambia en la traducción: los tres puntos de presión

1. **Idiomas expansivos (alemán, ruso, árabe, español)**: condense en la traducción, verifique el CPS por evento y divida los eventos largos en dos bien cortados, en lugar de reducir la fuente o aumentar el CPS.
2. **Idiomas contractivos (chino)**: un texto más corto tienta a extender los tiempos de visualización y a colapsar todo en menos eventos; resista la tentación de fusionar a través de cambios de plano solo porque los caracteres quepan.
3. **La lógica de corte de línea difiere según la escritura**: el japonés prohíbe ciertas posiciones de corte (puntuación al inicio de línea), el árabe corta solo entre palabras e invierte la dirección de la puntuación, y el chino evita cortar dentro de una palabra o de un número. El ajuste automático de línea de estilo latino rompe estas reglas silenciosamente.

## Detalles de formato y posicionamiento que se olvidan en la localización

- **Posición**: abajo al centro es lo predeterminado; los subtítulos se mueven arriba o a un lado solo para evitar cubrir texto incrustado o rostros. Los videos traducidos suelen tener gráficos incrustados *distintos* de los del original: revise el posicionamiento por idioma, no por video.
- **Cursivas y etiquetas de hablante**: el habla fuera de pantalla, la narración y los identificadores de hablante SDH siguen convenciones propias de cada casa que deben reaplicarse, no traducirse literalmente. Los formatos tipo "- [HABLANTE]" difieren según el mercado.
- **Números y unidades**: el estilo de los dígitos, los separadores decimales y las unidades se localizan (1,500 rpm frente a 1.500 U/min), y cuentan contra su presupuesto de caracteres en su forma expandida.
- **Fuente**: las fuentes de subtítulos incrustadas deben contener los glifos de la escritura de destino: una fuente solo latina convierte los subtítulos chinos en cuadrados. Los subtítulos incrustados en la imagen necesitan renderizarse de nuevo por idioma; los archivos separados (SRT/VTT) heredan la fuente del reproductor.

## Una lista de verificación de QC previa a la entrega

1. Ningún evento supera las 2 líneas / ~42 caracteres (o el equivalente CJK/árabe)
2. Cada evento dentro de los límites de CPS de su idioma y audiencia
3. Ningún subtítulo cruza un cambio de plano; separaciones de ≥ 2 fotogramas entre eventos
4. Cortes de línea en límites lingüísticos, correctos según la escritura
5. Números, unidades y puntuación localizados, no solo traducidos
6. Ningún texto choca con los gráficos en pantalla en *ninguna* versión de idioma

Los subtítulos son la parte de mayor volumen y menor margen de la localización de video, y lo primero que juzgan los espectadores. Nuestro [equipo de localización de video](/es/services/localization/video/) produce subtítulos con especificaciones de broadcast, con traducción, sincronización y QC bajo un mismo techo. Para la cuestión estratégica de cuándo los subtítulos superan al doblaje en un mercado determinado, consulte nuestra [comparación mercado por mercado](/es/news/subtitles-vs-dubbing-by-market/), o [envíenos un video](/es/contact/) y le devolveremos una pista de subtítulos de muestra en su idioma objetivo.
