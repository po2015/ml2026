---
title: "Localización de Articulate Storyline: paso a paso"
date: 2026-10-28T17:43:00+08:00
publishDate: 2026-10-28T17:43:00+08:00
category: "industry"
category_label: "Industria"
tags: ["E-Learning", "Articulate Storyline", "SCORM", "localización"]
keywords: ["traducción de articulate storyline", "flujo de localización de storyline", "exportación xlf de storyline"]
cover: "/images/news/articulate-storyline-translation-workflow.jpg"
author: "MediaLocalize Team"
summary: "La exportación para traducción de Storyline parece simple hasta que las capas de diapositivas, los disparadores y el texto con variables vuelven rotos. El flujo de trabajo completo que sobrevive a los cursos reales."
---

Articulate Storyline tiene una función de traducción integrada: exportar el texto, traducirlo, reimportarlo. Los proveedores que nunca lo han hecho cotizan basándose en la existencia de ese elemento de menú. Luego, el curso importado tiene etiquetas de botones truncadas en alemán, retroalimentación de cuestionarios que muestra marcadores de variables en lugar de los nombres de los alumnos, y una pista de texto a voz que sigue leyendo en inglés; y comienzan tres rondas de retrabajo.

La localización de Storyline funciona sin problemas cuando se sabe dónde están las trampas. Este es el flujo de trabajo que ejecutamos, paso a paso, con las verificaciones que detectan los problemas mientras todavía son baratos.

## Paso 1: preparar el archivo de origen (antes de cualquier exportación)

La mitad de la calidad de una localización de Storyline se decide antes de que comience la traducción:

- **Use el archivo .story de origen, nunca el contenido publicado.** Si el cliente solo tiene el paquete SCORM publicado, deténgase: la extracción de texto de archivos publicados pierde la estructura de diapositivas y el contexto.
- **Actualice a la última versión de Storyline** y guarde desde el principio una copia versionada del archivo por idioma de destino (`course_de.story`, `course_es.story`). Trabajar en un solo archivo e "ir importando los idiomas" es como se sobrescriben los archivos maestros.
- **Reemplace el texto incrustado en imágenes.** Las capturas de pantalla con llamadas, los diagramas con etiquetas y los gráficos de botones que contienen palabras deben reconstruirse como texto editable o marcarse para recrearse por idioma.
- **Estandarice las fuentes.** Elija fuentes que existan para cada escritura de destino: una fuente solo latina recurre silenciosamente a otra en las diapositivas en chino o árabe. Consulte nuestra [guía de tipografía](/es/news/multilingual-dtp-typography-guide/) para elegir fuentes seguras para cada escritura.
- **Anote cada fuente de texto dinámico**: las referencias a variables (`%UserName%`), los disparadores de número a texto y las cadenas generadas por JavaScript no aparecen en las exportaciones para traducción.

## Paso 2: exportar para traducción

Storyline ofrece dos formatos de exportación:

- **Word (.docx)**: una fila por segmento de texto con referencias de diapositiva/capa. Sirve para cursos pequeños y clientes que revisan en Word; es más débil para flujos de trabajo con memoria de traducción.
- **XLIFF (.xlf)**: la vía profesional. Se importa en cualquier herramienta CAT (memoQ, Trados), conserva los identificadores de segmento y hace el viaje de ida y vuelta sin problemas. Úselo siempre que haya un proveedor de traducción involucrado.

Configuraciones críticas: exporte **con el texto original como origen** y asegúrese de que quede cubierto "incluir texto de todas las diapositivas, capas, notas y bancos de preguntas": los bancos de preguntas y los maestros de retroalimentación son objetos separados en Storyline y son el contenido que más comúnmente se olvida.

## Paso 3: traducir con contexto

Storyline exporta el texto de los segmentos sin contexto visual. Los traductores que ven "Submit" no pueden saber si el botón admite 20 caracteres o 6. Dos prácticas evitan las conjeturas:

1. **Proporcione capturas de pantalla de las diapositivas o un enlace de revisión publicado** junto con el XLIFF, para que los traductores vean dónde vive cada segmento.
2. **Establezca restricciones de longitud** para los segmentos de interfaz: botones, pestañas y elementos de menú. En una herramienta CAT se convierten en límites de caracteres que señalan el desbordamiento durante la traducción, en lugar de después de la importación.

El alemán es entre un 20 y un 35 % más largo que el inglés; en cursos con muchos botones, acuerde desde el principio si el desbordamiento se resuelve con una redacción más corta o redimensionando. Nuestro [artículo sobre expansión del texto](/es/news/text-expansion-translation-layout/) explica por qué esta decisión corresponde a esta etapa, no al QA.

## Paso 4: reconstruir el audio, el video y los elementos dinámicos

La exportación para traducción solo cubre el texto. En paralelo con la traducción:

- **Vuelva a grabar la narración**: las [voces de IA](/es/news/how-ai-dubbing-works/) hacen esto drásticamente más barato para las bibliotecas de capacitación; documente la elección de voz en una guía de estilo para que los módulos futuros coincidan.
- **Localice videos y animaciones**: resincronice los subtítulos, vuelva a grabar la voz en off y reedite el texto incrustado. Los subtítulos opcionales de Storyline se adjuntan por diapositiva y deben volverse a subir por idioma.
- **Actualice el texto a voz integrado de Storyline**: no cambia de idioma automáticamente. Cada archivo de idioma necesita que el TTS se regenere con una voz del idioma correspondiente, o que se reemplace con audio grabado.
- **Gestione el texto con variables**: las cadenas ensambladas por disparadores (mensajes de puntuación, inserción de nombres) existen en parte en la exportación y en parte en la lógica de disparadores. Pruebe manualmente cada pantalla controlada por variables.

## Paso 5: importar y corregir la maqueta

Importe el XLIFF traducido en la copia de idioma del archivo .story. Luego reserve tiempo real para lo que la importación no corrige:

- **Desbordamiento de texto**: cajas redimensionadas, fuentes reducidas (dentro de los límites de legibilidad) o etiquetas reformuladas, diapositiva por diapositiva.
- **Idiomas de derecha a izquierda**: Storyline admite la entrada de texto en árabe, pero la alineación de viñetas, la sangría y la puntuación de dirección mixta necesitan revisión a nivel de diapositiva.
- **Etiquetas de texto del reproductor**: la interfaz del reproductor (botones Anterior/Siguiente, menú, glosario, pestaña de recursos) se traduce por separado en la configuración de etiquetas de texto del reproductor: un curso completamente en alemán con un botón "NEXT" en inglés es la firma de un trabajo amateur.

## Paso 6: publicar y validar

Publique cada idioma como su propio paquete SCORM/xAPI y valide antes de la entrega:

1. **SCORM Cloud o una prueba de conformidad equivalente**: detecta errores de manifiesto y empaquetado. Los problemas a nivel de empaquetado (títulos de manifiesto, cadenas de finalización) se cubren en nuestro [artículo sobre localización de SCORM y xAPI](/es/news/scorm-xapi-localization/).
2. **QA funcional en el LMS real**: un hablante nativo completa el curso: cada cuestionario enviado, cada ramificación recorrida, con la finalización y el reporte de puntuaciones verificados en el informe del LMS.
3. **QA lingüístico en contexto**: los traductores revisan el curso en funcionamiento, no el XLIFF; las cadenas truncadas y las traducciones fuera de contexto solo son visibles en pantalla.

## Esfuerzo y plazos realistas

Para un módulo corporativo típico de 30 minutos:

| Tarea | Esfuerzo |
|---|---|
| Preparación + exportación | 2–4 horas |
| Traducción (por idioma) | 1–2 días |
| Correcciones de maqueta tras la importación | 3–8 horas (más en cursos con mucha interacción) |
| Regrabación de audio + sincronización | 1–2 días (IA) / 3–5 días (estudio) |
| QA + validación en el LMS | 2–4 horas |

Multiplique por idiomas y paralelice: el trabajo de maqueta y audio en un idioma no bloquea a otro. Los proyectos por primera vez deben sumar un 30 % por la curva de aprendizaje; desaparece hacia el tercer módulo.

Si tiene cursos de Storyline que se dirigen a un despliegue multilingüe, nuestro [equipo de localización de e-learning](/es/services/localization/elearning/) trabaja directamente en archivos .story y entrega paquetes SCORM validados por idioma: [envíenos un módulo](/es/contact/) y cotizaremos toda la biblioteca a partir de él.
