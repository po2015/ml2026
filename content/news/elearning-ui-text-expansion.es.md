---
title: "Expansión de texto en la interfaz del curso: botones y menús"
date: 2027-01-12T19:36:00+08:00
publishDate: 2027-01-12T19:36:00+08:00
category: "industry"
category_label: "Industria"
tags: ["E-Learning", "localización de UI", "expansión de texto", "diseño de cursos"]
keywords: ["localización ui elearning", "expansión de texto botones", "traducción interfaz de curso"]
cover: "/images/news/elearning-ui-text-expansion.jpg"
author: "MediaLocalize Team"
summary: "«Submit» cabe en su botón. «Absenden» casi cabe. «Envoyer la réponse» no cabe. La expansión de texto rompe las interfaces de los cursos antes de que los alumnos lleguen al contenido: cómo diseñar una interfaz de curso que sobreviva a la traducción."
---

Una academia corporativa se lanza en ocho idiomas. El contenido está traducido de forma impecable; el curso es inutilizable. El botón Submit desborda su forma de píldora en alemán, el menú de navegación se parte en dos líneas en francés, la flecha de «Siguiente» en la versión árabe apunta en la dirección equivocada, y una etiqueta de progreso que dice «Pregunta 3 de 10» choca con el marcador de puntuación en ruso. Nada de esto es un error de traducción: es una suposición de diseño, la de que el texto de la interfaz tiene un tamaño fijo. Nunca lo tiene. El inglés es uno de los idiomas más compactos del planeta, y toda interfaz de curso diseñada alrededor de las longitudes de las cadenas en inglés es un incidente de maquetación esperando a su segundo idioma.

## Los números detrás de la ruptura

Los factores de expansión son lo bastante consistentes como para diseñar en función de ellos:

| Idioma | Expansión típica frente al inglés | Víctima clásica |
|---|---|---|
| Alemán | +25–35 % | Sustantivos compuestos que no se pueden dividir con guion de forma elegante |
| Francés | +15–25 % | Artículos y preposiciones por todas partes |
| Ruso | +15–25 % | Palabras largas, sin sinónimos cortos para los términos de UI |
| Español | +15–25 % | «Next» → «Siguiente» es el caso benigno |
| Árabe | +25 % *y* RTL | La maquetación se espeja; las cadenas también crecen |
| CJK | −20–40 % (más corto) | El problema contrario: la UI se ve vacía, las zonas táctiles se encogen |

Las zonas de la UI que se rompen primero, en orden: **botones** (verbos cortos en inglés se convierten en frases largas), **menús y pestañas de ancho fijo**, **etiquetas emparejadas con valores** («Puntuación: 85»: la etiqueta crece, la pareja colisiona), **mensajes emergentes/toast** dimensionados para una línea, y **encabezados de tabla**. Nuestra [guía general de expansión de texto](/es/news/text-expansion-translation-layout/) cubre el lado de los documentos; la UI de los cursos es más implacable porque no hay un flujo de página fluido que absorba el crecimiento: cada elemento vive en un reproductor de píxeles fijos.

## Reglas de diseño que lo previenen

- **Presupueste un 40 % de ancho adicional para cada contenedor de texto.** Si «Submit» define el ancho de su botón, la versión alemana ya está rota. Dimensione los botones para la traducción más larga prevista, o hágalos de ancho automático con max-width razonables.
- **Nunca use texto-como-imagen en la UI del reproductor.** Un botón incrustado en un PNG significa retrabajo gráfico por idioma, el mismo impuesto que el [texto incrustado en gráficos](/es/news/infographic-chart-localization/). Texto vivo o no se publica.
- **Separe las etiquetas de los valores.** «Pregunta 3 de 10» como tres componentes alimentados por datos («Pregunta», 3, «de 10») se reensambla según la gramática de cada idioma; como una sola cadena fija se destroza en idiomas con orden de palabras distinto, y algunos idiomas necesitan una formulación completamente diferente (「10 题中的第 3 题」).
- **Prefiera iconos con tooltips para controles repetitivos**, pero nunca solo iconos para acciones críticas: la ambigüedad de los iconos entre culturas es su propio [problema de localización](/es/news/image-icon-color-localization/).
- **Diseñe la versión árabe al principio, no al final.** El RTL espeja todo el reproductor: dirección de navegación, relleno de la barra de progreso, dirección de la flecha «siguiente», como se detalla en [diseño web RTL](/es/news/rtl-website-design-arabic/). Adaptar RTL a un curso terminado cuesta más que la construcción original de la UI.

## El ángulo de la herramienta de autoría

Las herramientas modernas ayudan si se usan correctamente:

- **Storyline/Rise**: el texto de la UI del reproductor (botones, mensajes, etiquetas de menú) vive en el conjunto de *player text labels*, que se exporta y traduce como una unidad, según el [flujo de trabajo de Storyline](/es/news/articulate-storyline-translation-workflow/). Traducir el contenido de las diapositivas pero olvidar las etiquetas del reproductor produce un Frankenstein bilingüe: diapositivas en alemán, botones en inglés.
- **Reproductores HTML5 personalizados**: las cadenas pertenecen a un archivo de recursos (JSON/properties), nunca en línea dentro del código ni —peor aún— dentro del propio contenido del curso.
- **La interfaz del LMS también es UI**: mensajes de finalización, correos de inscripción, plantillas de certificado. También se expanden.

Sea cual sea la herramienta, el paso de verificación es el mismo: **pseudolocalización**. Ejecute el curso con una pseudoconfiguración regional que infle cada cadena un 40 % e invierta la dirección, según la [guía de pruebas de pseudolocalización](/es/news/pseudolocalization-testing-guide/): cada desbordamiento, truncamiento y cadena fija se revela en una sola pasada, antes de traducir una sola palabra. Es el paso de control de calidad más barato de todo el presupuesto de localización.

## Las mitigaciones del lado del contenido

Algunos problemas de expansión se resuelven mejor en la redacción que en la maquetación:

- **Escriba textos de UI más cortos en el origen.** «Enviar» y no «Envíe su respuesta»; «Reintentar» y no «Intente esta pregunta de nuevo». La brevedad en el origen es la palanca más grande: cada palabra que recorta ahorra espacio en los ocho idiomas.
- **Mantenga un glosario de UI.** Las interfaces de los cursos reutilizan unas pocas docenas de cadenas; traducirlas de forma consistente (y elegir equivalentes naturalmente cortos, trabajo de un traductor nativo, no de un diccionario) previene tanto el desbordamiento como el problema de «tres traducciones de Submit en un mismo curso».
- **Los números y los formatos se mantienen correctos según la configuración regional** en puntuaciones, fechas y duraciones: la [disciplina de formatos](/es/news/date-currency-format-localization/) se aplica dentro de los cursos exactamente igual que en los sitios web.

## Una lista de verificación previa al lanzamiento

1. Todas las cadenas del reproductor externalizadas e incluidas en el paquete de traducción
2. Cada contenedor de texto probado a +40 % de ancho (pasada con pseudolocalización)
3. Etiquetas y valores separados; ninguna gramática fijada en el código
4. Variante RTL del reproductor verificada, no supuesta
5. Botones, menús, ventanas emergentes y encabezados de tabla revisados visualmente en el idioma *más largo* (normalmente el alemán)
6. Certificados y mensajes del LMS comprobados: los alumnos también los ven

La UI del curso es el marco alrededor de su contenido formativo; los alumnos perdonan una frase torpe, pero un botón que no pueden leer ni tocar le cuesta la tasa de finalización para la que existe todo el proyecto. Nuestro [equipo de localización de e-learning](/es/services/localization/elearning/) audita la UI de los cursos en busca de problemas de expansión y RTL como paso estándar del proyecto, antes de que empiece la traducción, no después de que se rompa. [Envíenos un curso](/es/contact/) y le haremos la auditoría con pseudolocalización.
