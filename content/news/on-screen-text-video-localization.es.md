---
title: "Localización de texto en pantalla y motion graphics"
date: 2026-11-11T08:15:00+08:00
publishDate: 2026-11-11T08:15:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["Localización de video", "motion graphics", "texto en pantalla", "DTP"]
keywords: ["localización de texto en pantalla", "traducción de motion graphics", "sustitución de texto en video"]
cover: "/images/news/on-screen-text-video-localization.jpg"
author: "MediaLocalize Team"
summary: "La locución es solo la mitad de la localización de video. Lo que implica traducir texto en pantalla, títulos y motion graphics, y por qué los archivos de proyecto importan más que el propio video."
---

Un video de producto vuelve de la "localización": la locución está en alemán, los subtítulos están en alemán... y cada título en pantalla, rótulo y etiqueta de gráfico sigue en inglés. Los espectadores lo notan de inmediato. El texto en pantalla es donde vive la densidad de información en el video corporativo moderno, y dejarlo sin traducir le dice a su público alemán que el video no se hizo para ellos.

Localizar el texto en pantalla (OST) y los motion graphics es una disciplina propia, entre la traducción y la edición de video. Esto es lo que implica, lo que cuesta y cómo definir su alcance correctamente.

## El inventario: qué cuenta como texto en pantalla

Antes de presupuestar nada, inventarie cada elemento de texto del video:

- **Títulos y rótulos de tercio inferior**: nombres de ponentes, tarjetas de capítulo, encabezados de sección
- **Rótulos y anotaciones**: etiquetas que señalan características del producto, indicaciones de dimensiones
- **Gráficos y diagramas**: etiquetas de ejes, leyendas, indicaciones de datos
- **Grabaciones de pantalla**: capturas de interfaces de software, recorridos por paneles
- **Subtítulos incrustados y superposiciones de texto estilo redes sociales**
- **Logotipos con eslogan, pantallas finales, CTA**: a menudo olvidados hasta la entrega

Cada categoría tiene un flujo de trabajo y un costo distintos. Un video de producto de 3 minutos suele contener entre 20 y 60 elementos de texto discretos.

## Flujo de trabajo A: con archivos de proyecto (la vía sensata)

Si dispone de los archivos de proyecto de After Effects / Premiere / motion graphics, la localización de OST es sistemática:

1. **Extraiga todas las capas de texto** a una hoja de cálculo con códigos de tiempo y capturas de contexto. Los traductores trabajan a partir de ella, no del video.
2. **Traduzca con restricciones de longitud.** El alemán es un 20–35% más largo; un texto que aparece animado durante dos segundos debe seguir cabiendo y ser legible: las mismas [reglas de expansión](/es/news/text-expansion-translation-layout/) que rigen la impresión se aplican aquí, con márgenes más ajustados.
3. **Sustituya el texto en el proyecto.** Aquí es donde se comprueba la cobertura de fuentes (glifos CJK, árabes, cirílicos), donde la expansión rompe diseños y donde los idiomas RTL exigen reconsiderar la dirección de las animaciones: un elemento que entra desde la izquierda puede leerse mal en árabe.
4. **Reajuste los tiempos de las animaciones.** El texto traducido más largo necesita más tiempo en pantalla; los fotogramas clave se desplazan y todo lo sincronizado con la locución se resincroniza con el nuevo audio.
5. **Vuelva a renderizar por idioma** y haga control de calidad fotograma a fotograma para detectar texto cortado, artefactos de codificación y elementos en inglés olvidados.

## Flujo de trabajo B: sin archivos de proyecto (la vía cara)

Sin archivos de proyecto hay que recrear los gráficos a partir del video renderizado:

- **Texto sencillo sobre fondos limpios**: se enmascara, se reconstruye el fondo y se compone el nuevo texto. Viable y asequible.
- **Texto sobre metraje en movimiento o animaciones complejas**: en la práctica, reanimación. A menudo de 3 a 5 veces el costo del flujo A; a veces se acerca al costo de volver a grabar.
- **Grabaciones de pantalla**: normalmente se vuelven a grabar con la interfaz del software localizada; no hay atajo que tenga aspecto profesional.

Por eso decimos lo mismo a cada cliente: **archive sus archivos de proyecto con el mismo cuidado que el video máster.** La petición "simplemente localice el video que nos hicieron hace dos años" pasa de ser un trabajo de dos días a uno de dos semanas justo cuando los archivos de proyecto se han perdido. Si una agencia hizo el video, consiga los archivos de proyecto en el contrato.

## Las trampas específicas de la traducción

- **La expansión rompe las revelaciones temporizadas.** Las viñetas que aparecen una a una están sincronizadas con la longitud del texto; las viñetas traducidas necesitan nueva coreografía, no solo reescribirse.
- **Las fuentes cambian el diseño.** Su fuente corporativa puede no cubrir chino o árabe; la fuente de reserva cambia el peso y el ancho, y de repente el diseño del título necesita rediseñarse. Decida por idioma: adaptar el diseño a la fuente o licenciar una alternativa corporativa adecuada al alfabeto.
- **Los números y las unidades también se localizan**: separadores decimales, formatos de fecha, unidades (kW frente a PS, pulgadas frente a mm), y están dentro de los gráficos, invisibles para la extracción de texto.
- **El árabe invierte el orden de lectura dentro de las animaciones**: las revelaciones de varios elementos deben secuenciarse de derecha a izquierda, y los indicadores de progreso llenarse de derecha a izquierda. Las medias tintas aquí se leen como defectos a ojos nativos.

## Lógica de alcance y precios

| Escenario | Esfuerzo típico por idioma |
|---|---|
| Solo títulos/rótulos, con archivos de proyecto | 0.5–1 día |
| Motion graphics completos, con archivos de proyecto | 1–3 días |
| Sin archivos de proyecto, complejidad moderada | 3–10 días (recreación) |
| Grabaciones de pantalla | Nuevas grabaciones con la interfaz localizada + edición |

Los costos por idioma caen rápido después del primero: las decisiones de adaptación (fuentes, reglas de diseño, ajustes de tiempo) se toman una vez, y los idiomas del segundo al octavo se benefician de esa plantilla. Combinada con la [locución localizada](/es/news/how-ai-dubbing-works/) y los [subtítulos](/es/news/subtitle-formatting-rules/), la localización de OST completa el paquete que hace que un video parezca producido *para* un mercado y no adaptado *a* él.

Si su biblioteca de videos se dirige a nuevos mercados, nuestro [equipo de localización de video](/es/services/localization/video/) se encarga de todo: locución, subtítulos y motion graphics, con archivos de proyecto o sin ellos. [Envíenos un video](/es/contact/) e inventariaremos sus elementos de texto y presupuestaremos toda la biblioteca a partir de él.
