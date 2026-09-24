---
title: "SCORM, xAPI y localización: qué cambia realmente"
date: 2026-10-12T13:58:00+08:00
publishDate: 2026-10-12T13:58:00+08:00
category: "industry"
category_label: "Industria"
tags: ["E-Learning", "SCORM", "xAPI", "localización", "formación corporativa"]
keywords: ["localización scorm", "traducción xapi", "localización elearning"]
cover: "/images/news/scorm-xapi-localization.jpg"
author: "MediaLocalize Team"
summary: "Traducir el texto del curso es solo la mitad de la localización de e-learning. Qué cambia realmente dentro de los paquetes SCORM y xAPI — y qué se rompe si lo pasa por alto."
---

Un equipo de formación termina su curso de cumplimiento en inglés, envía el paquete SCORM a un proveedor de traducción y recibe de vuelta lo que parece un curso alemán terminado. Tres semanas después, el informe del LMS muestra a los alumnos atascados en un 87 % de finalización, la retroalimentación de los cuestionarios aparece en inglés y los botones de navegación desbordan sus etiquetas en polaco. Ninguno de estos es un problema de traducción: son problemas de empaquetado. El estándar de e-learning sobre el que está construido su curso determina qué debe tocar realmente la localización.

Este artículo detalla qué cambia dentro de los paquetes SCORM y xAPI cuando se localizan, para que pueda delimitar el trabajo correctamente y hacer las preguntas adecuadas a los proveedores.

## Qué empaquetan realmente SCORM y xAPI

Ambos estándares definen cómo un curso se comunica con un sistema de gestión de aprendizaje (LMS): cómo reporta la finalización, las puntuaciones, el tiempo dedicado y los marcadores. Pero empaquetan el contenido de formas muy diferentes, y esa diferencia determina el esfuerzo de localización.

| Estándar | Qué contiene | Dónde reside el texto visible para el alumno | Modelo de seguimiento |
|---|---|---|---|
| SCORM 1.2 | HTML/JS comprimido en ZIP + `imsmanifest.xml` | Dentro de los archivos del curso; parte en el manifiesto | Finalización, puntuación, datos de suspensión |
| SCORM 2004 | Misma estructura, secuenciación más rica | Igual, más reglas de secuenciación | Añade objetivos e interacciones |
| xAPI (Tin Can) | Contenido en cualquier lugar; declaraciones enviadas a un LRS | Archivos del curso + cadenas de visualización de las declaraciones | Eventos "actor hizo verbo objeto" |
| cmi5 | Declaraciones xAPI envueltas en un paquete lanzable | Igual que xAPI | xAPI con reglas de lanzamiento del LMS |

La clave: **SCORM mantiene todo dentro del ZIP**, por lo que localizar significa abrir, editar y reempaquetar los archivos del curso. **xAPI traslada el reporte a las declaraciones**, así que la localización también debe considerar qué dicen esas declaraciones: a menudo contienen cadenas legibles por humanos que terminarán en informes que leerá su equipo de RR. HH. en Alemania.

## Qué cambia al localizar un paquete SCORM

### El manifiesto y los metadatos

`imsmanifest.xml` contiene el título del curso y las etiquetas de organización que algunos LMS muestran en sus catálogos. Una cantidad sorprendente de cursos localizados sigue llevando títulos en inglés aquí, así que los alumnos ven "Fire Safety Training 2026" en un catálogo de cursos por lo demás completamente en alemán. El manifiesto debe traducirse y revalidarse: un manifiesto malformado significa que el curso no se importará en absoluto.

### Expansión del texto en diseños fijos

Las herramientas de autoría de cursos (Storyline, Captivate, Lectora) colocan el texto en cuadros de tamaño fijo. El alemán es entre un 20 y un 35 % más largo que el inglés; el chino se contrae pero cambia los saltos de línea; el árabe invierte la dirección de lectura. Botones, pestañas, barras de progreso y etiquetas de arrastrar y soltar necesitan redimensionarse o refluirse: esto es trabajo de maquetación, no de traducción, y es la razón por la que los presupuestos de localización de e-learning incluyen una partida de ingeniería.

### Cadenas de finalización y reporte

Los valores de estado de SCORM (`completed`, `passed`, `failed`) son tokens fijos en inglés: nunca los traduzca, o el seguimiento se romperá silenciosamente. Pero el texto de retroalimentación, los mensajes de la diapositiva de resultados y las instrucciones tipo "Debe obtener un 80 %" son visibles para el alumno y deben traducirse. Los proveedores que trabajan a partir de una exportación de texto en bruto confunden habitualmente estas dos categorías.

### Audio, vídeo y texto en pantalla

Los cursos narrados multiplican el trabajo: guiones traducidos, [grabación de voz con IA o humana](/es/news/how-ai-dubbing-works/), resincronización con las animaciones y reedición de cualquier texto en pantalla incrustado en vídeos o capturas. Un curso con 20 minutos de narración y capturas de pantalla anotadas puede duplicar el esfuerzo de ingeniería de un curso de solo texto.

### Cuestionarios e interacciones

Los destinos de arrastrar y soltar, las opciones de menús desplegables, las etiquetas de zonas interactivas y las capas de retroalimentación suelen almacenarse como objetos separados en el archivo de autoría, no como texto continuo, lo que significa que los flujos de extracción de texto los pasan por alto. La aleatorización de respuestas también puede romper las opciones traducidas tipo "Todas las anteriores". Cada tipo de interacción necesita una pasada funcional en el idioma de destino.

## Qué cambia con xAPI

xAPI desplaza el problema del empaquetado al reporte. Declaraciones como `"Zhang Wei completed Fire Safety Module 3"` llevan cadenas de visualización definidas en las definiciones de actividad y en las propias declaraciones.

Tres decisiones de localización son exclusivas de xAPI:

1. **Idioma de la definición de actividad**: las definiciones de actividad de xAPI admiten múltiples mapas de idioma en `display`. Bien hecho, su LRS puede mostrar la misma actividad como "Brandschutz Modul 3" para los usuarios alemanes y mantener el inglés para la sede central. Hecho con descuido, los informes de cada región mostrarán nombres de actividad en inglés.
2. **Coherencia de los verbos**: traduzca los nombres de visualización de los verbos personalizados, nunca sus IRI. Dos cursos que usen IRI distintos para el mismo concepto ("completed" frente a "finished") fragmentarán sus informes entre idiomas.
3. **Legibilidad de los resultados**: si su LRS alimenta paneles que leen los directivos regionales, decida desde el principio en qué idioma se mostrarán las declaraciones, y manténgalo coherente en todas las versiones localizadas del curso.

## El flujo de trabajo que evita retrabajos

El orden de las operaciones importa más que las herramientas:

1. **Extraiga desde el archivo de proyecto fuente** (Storyline `.story`, Captivate `.cptx`), no desde el ZIP de SCORM publicado. Los archivos publicados están compilados; extraer texto de ellos pierde contexto y estructura de objetos.
2. **Traduzca con contexto**: los traductores necesitan ver dónde aparece cada cadena (botón, capa de retroalimentación, texto alternativo) para respetar los límites de espacio.
3. **Reimporte y reconstruya** en la herramienta de autoría, corrigiendo la expansión del texto objeto por objeto.
4. **Regrabe y resincronice audio y vídeo**, y luego sustituya las imágenes y capturas de pantalla localizadas.
5. **Publique y valide el paquete**: páselo por una prueba de conformidad SCORM (por ejemplo, SCORM Cloud) antes de acercarlo a su LMS.
6. **QA funcional en el idioma de destino**: un hablante nativo recorre cada interacción y verifica el reporte de finalización en el LMS real.

Saltarse el paso 1 es el error más costoso de todos: vemos con regularidad proyectos que hay que redelimitar después de que el proveedor descubre que no puede editar la salida compilada. Nuestra [visión general de la localización de e-learning](/es/news/elearning-localization-global-audiences/) cubre el proceso más amplio; este artículo es su mitad técnica.

## Preguntas que hacer antes de pedir un presupuesto

- ¿Puede entregar los **archivos de proyecto fuente**, o solo el paquete publicado?
- ¿Qué estándar y versión utiliza el curso (SCORM 1.2 / 2004, xAPI, cmi5)?
- ¿El curso contiene narración, vídeo o capturas de pantalla con texto?
- ¿Cuántas interacciones y tipos de cuestionario utiliza?
- ¿El proveedor ejecutará QA funcional en su LMS, o solo entregará archivos?

Un proveedor que presupuesta solo a partir del archivo ZIP está adivinando. Uno que hace estas preguntas ya lo ha hecho antes, y su presupuesto se mantendrá.

Si está planificando un despliegue de formación multilingüe y quiere que la ingeniería se delimite correctamente desde el principio, nuestro [equipo de localización de e-learning](/es/services/localization/elearning/) trabaja directamente en archivos de proyecto de Storyline, Captivate y Lectora: [envíenos un módulo de muestra](/es/contact/) y le diremos exactamente qué cambiará la localización en él.
