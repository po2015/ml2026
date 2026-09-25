---
title: "Control de calidad de audio para contenido doblado: una lista de verificación para el oyente"
date: 2027-01-25T13:10:00+08:00
publishDate: 2027-01-25T13:10:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["doblaje", "control de calidad", "QA de audio", "voz IA"]
keywords: ["control de calidad de doblaje", "lista de verificación de audio", "revisión de audio doblado"]
cover: "/images/news/dubbing-audio-qa-checklist.jpg"
author: "MediaLocalize Team"
summary: "El estudio de doblaje entregó 40 archivos. Nadie de su equipo habla vietnamita. Los aprobó de todos modos, y el nombre del producto está mal pronunciado en los 40. El QA de audio es una disciplina propia, con su propia lista de verificación; así puede ejecutarla incluso sin lingüistas internos."
---

Un proveedor de capacitación entrega un curso doblado en seis idiomas. Dos semanas después, el cliente alemán reporta que el narrador dice un nombre de producto equivocado en el módulo tres, que en la versión en español la música de fondo baja bajo la voz de forma tan agresiva que suena como un latido, y que los archivos en árabe están a 44.1 kHz mientras todo lo demás está a 48 kHz, lo que rompe la importación a su LMS. Ninguno de estos es un problema de traducción. Ninguno se detectó porque nadie ejecutó un QA de *audio*: la pasada independiente que escucha lo que se entregó, contra una lista de verificación, antes de publicarlo. Aquí está esa lista, organizada para que un project manager sin conocimientos del idioma pueda ejecutar la mayor parte, y sepa exactamente qué partes necesitan un oído nativo.

## Por qué el QA de audio es una pasada independiente

Los proyectos de doblaje suelen recibir dos revisiones: la del guion (antes de grabar) y una revisión final superficial de «suena bien». Entre ambas queda un hueco donde vive la mayoría de los defectos. Un guion perfectamente traducido puede grabarse con el léxico de pronunciación equivocado, mezclarse con música que enmascara las consonantes, editarse con pausas de 200 ms que hacen que cada frase suene vacilante, o exportarse con la sonoridad incorrecta para la plataforma de destino. Como vimos en [la adaptación del guion y los tiempos](/es/news/dubbing-script-adaptation-timing/), los problemas de sincronización nacen en el guion, pero *afloran* en el audio, y solo un oyente los detectará. El doblaje con IA cambia la mezcla de errores, no la necesidad de QA: las [voces de IA](/es/news/how-ai-dubbing-works/) rara vez tropiezan a mitad de frase, pero pronuncian mal el mismo término, con total confianza, 200 veces seguidas.

## La lista de verificación, en orden de escucha

Ejecute las pasadas en este orden: cada una es más barata que la siguiente, y las primeras detectan los errores bloqueantes antes de que desperdicie el tiempo de un revisor nativo en un archivo que de todos modos se va a rehacer.

1. **Conformidad técnica (sin escuchar, 5 minutos).** Frecuencia de muestreo, profundidad de bits, canales, formato, sonoridad (según la plataforma de destino: −16 LUFS para la mayoría de los LMS/web, −23/−24 para especificaciones de broadcast), nomenclatura de archivos y conteo contra el manifiesto de entrega. Un tercio de los «problemas de audio» son discrepancias de especificación que se encuentran aquí.
2. **Pasada de integridad (recorra cada archivo).** Reproduzca cada archivo a 1.5–2× de velocidad, observando la forma de onda. Verifica: que no haya finales truncados, que no hayan quedado tomas dobles, que no haya silencios largos, y que la duración esté dentro de la tolerancia de la fuente (±5–10 % según cuánta [adaptación](/es/news/dubbing-script-adaptation-timing/) se planificó).
3. **Pasada de mezcla (muestree cada archivo, escuche completo un subconjunto).** Relación voz-música, suavidad del ducking, niveles consistentes entre archivos, sin clipping. Escuche en bocinas de laptop *y* en audífonos: los usuarios usan ambos, y una mezcla que suena bien en audífonos puede sepultar la voz en la bocina de un teléfono.
4. **Pronunciación y terminología (oyente nativo + glosario).** La pasada de mayor valor. El oyente verifica cada término del glosario, nombre de producto y marca contra el [léxico de pronunciación](/es/news/ai-voice-pronunciation-lexicon/), y señala cualquier cosa que suene mal aunque *no* esté en el glosario. Un solo nombre de producto mal pronunciado en una demo estrella socava toda la [inversión en localización de video](/es/news/product-demo-video-localization/).
5. **Interpretación y ajuste (oyente nativo).** El ritmo coincide con la acción en pantalla, el énfasis cae en las palabras correctas, el [estilo de narración](/es/news/elearning-voiceover-narration-styles/) es consistente con lo seleccionado en el casting y, en contextos de lip-sync, las líneas caen sobre los movimientos visibles de la boca dentro de la tolerancia.
6. **Consistencia del conjunto.** Mismo personaje, misma voz, misma energía en el módulo 12 que en el módulo 1; términos pronunciados de forma idéntica en todos los archivos; intros y outros idénticos donde deben serlo.

## La taxonomía de defectos (y lo que cuesta cada uno)

Clasifique los hallazgos en cuatro categorías: mantiene racional la conversación sobre las correcciones:

| Clase de defecto | Ejemplo | Severidad | Costo típico de corrección |
|---|---|---|---|
| **Bloqueante** | Nombre de producto equivocado; frase faltante; el archivo no se importa | Detiene la publicación | Regrabar/re-renderizar las líneas afectadas |
| **Mayor** | Término del glosario mal pronunciado; el balance voz/música sepulta palabras; artefactos de edición audibles | Corregir antes del lanzamiento | Líneas de pickup o remezcla |
| **Menor** | Una interpretación plana en 40 archivos; ligero desfase de ritmo en una transición | Corregir si es barato | Normalmente, notas para el próximo proyecto |
| **Estilo** | «Yo habría enfatizado otra palabra» | Documentar, no corregir | Agregar al léxico/guía de estilo |

La disciplina importa: sin clases de severidad, cada nota se convierte en «hay que corregirlo», el estudio se resiste, y el ciclo de revisión se come el calendario que ahorró al doblar en lugar de subtitular. Con ellas, una revisión de 40 archivos converge en una o dos rondas.

## Quién escucha qué

No necesita seis lingüistas internos. La división que funciona:

- **PM / productor**: pasadas 1–3 y 6: técnica, integridad, mezcla, consistencia. Estas necesitan oídos y un cronómetro, no conocimientos del idioma.
- **Oyente nativo por idioma**: pasadas 4–5. Puede ser un empleado del lado del cliente, un distribuidor o un revisor contratado por horas, pero debe ser alguien con interés en el resultado, informado con el glosario y el léxico *antes* de escuchar, y con una plantilla de retroalimentación con marcas de tiempo (archivo, timecode, esperado, escuchado, severidad).
- **El estudio o el responsable del pipeline de IA**: cierra el ciclo. En el doblaje con IA, la mayoría de las correcciones de pronunciación son entradas de léxico: una corrección se propaga a todas partes, razón por la cual la [disciplina del léxico](/es/news/ai-voice-pronunciation-lexicon/) se paga sola desde el segundo proyecto.

## Cómo abaratarlo la próxima vez

Cada hallazgo de las pasadas 4–5 debe fluir de vuelta hacia tres activos: el léxico de pronunciación, el glosario de traducción y la guía de estilo. Hágalo, y la pasada de QA de cada proyecto se acorta: el segundo curso en alemán tiene una fracción de los hallazgos del primero. Omita este paso, y pagará el mismo costo de revisión para siempre.

El QA de audio suele representar entre el 5 y el 10 % del presupuesto de doblaje y detecta los defectos que cuestan el 100 % de la confianza de un cliente. Nuestro [equipo de doblaje](/es/services/localization/dubbing/) incorpora las pasadas de QA anteriores en cada proyecto, tanto en pipelines humanos como de IA, con léxicos y glosarios que persisten en toda su biblioteca de contenido. [Envíenos un proyecto ya entregado](/es/contact/) y le aplicaremos la lista de verificación a modo de auditoría.
