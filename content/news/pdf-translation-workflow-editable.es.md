---
title: "Flujos de trabajo de traducción de PDF: editables frente a aplanados"
date: 2027-01-11T19:45:00+08:00
publishDate: 2027-01-11T19:45:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["DTP", "PDF", "traducción de documentos", "flujo de trabajo"]
keywords: ["flujo traducción pdf", "traducir documento pdf", "localización pdf editable"]
cover: "/images/news/pdf-translation-workflow-editable.jpg"
author: "MediaLocalize Team"
summary: "«¿Pueden traducir este PDF?» es la frase más cara de la localización de documentos. Por qué la respuesta depende de lo que hay dentro del archivo, y el flujo de trabajo que deja de pagar el impuesto del PDF."
---

Un distribuidor pide su catálogo en portugués. Marketing exporta el PDF y lo envía a un proveedor de traducción. Dos semanas después, el presupuesto vuelve al triple del precio esperado, con una nota sobre «reconstrucción DTP». ¿Qué pasó? El PDF era la *única* fuente, y un PDF no es un documento. Es una impresión. Que traducirlo cueste 500 o 5 000 dólares depende por completo de qué clase de impresión sea. Aquí está cómo distinguirlo y el flujo de trabajo que hace desaparecer el problema.

## Los tres tipos de PDF

**1. PDF con fuente editable.** Exportados directamente desde InDesign, Word, FrameMaker o una página web. El texto es texto de verdad: seleccionable, extraíble, en orden de lectura. Estos se traducen limpiamente: extraer, traducir, reimportar, ajustar la maquetación. El matiz: rara vez querrá traducir el PDF en sí; querrá traducir el *archivo fuente* del que procede, lo que lleva a la regla de oro de más abajo.

**2. PDF aplanados.** Texto convertido en contornos, o páginas exportadas como imágenes envueltas en un contenedor PDF. Es común cuando un diseñador «finaliza» un archivo para imprenta o cuando el PDF pasó por un taller de impresión. Nada es extraíble; cada página debe reconstruirse: reescrita u OCR, maquetada de nuevo, revisada de nuevo. De aquí salen las partidas de «reconstrucción DTP».

**3. PDF escaneados.** Fotografías de papel. La calidad del OCR varía de decente (escaneo limpio, fuentes estándar) a desesperante (inclinaciones, sellos, escritura a mano, baja resolución). Las tablas y los diseños a varias columnas son lo peor para el OCR, exactamente el contenido del que están hechas las fichas técnicas.

El diagnóstico de 30 segundos: abra el PDF e intente seleccionar una frase del texto. Se selecciona limpiamente → tipo 1. Se selecciona como imagen o no se selecciona → tipo 2 o 3. Luego compare el tamaño del archivo con el número de páginas: un «catálogo» de 20 páginas que pesa 80 MB probablemente son imágenes disfrazadas.

## La regla de oro: nunca traduzca el PDF

Un PDF es una salida, como un folleto impreso. Traducirlo directamente significa pagar por aplicar ingeniería inversa a una maquetación que ya existe en algún punto aguas arriba. La regla:

> **Traduzca el archivo fuente; regenere el PDF.**

Si su catálogo vive en InDesign, traduzca el .indd (o su IDML exportado): la traducción cae en la maquetación existente, con los estilos intactos, y solo quedan los ajustes por expansión, según la [lista de verificación de DTP](/es/news/technical-manual-translation-dtp-checklist/) estándar. El PDF que envía al distribuidor es entonces simplemente una exportación nueva. Las empresas que interiorizan esta regla dejan de pagar el impuesto del PDF para siempre; las que no, lo pagan en cada documento, cada idioma, cada revisión.

## Cuando el archivo fuente se perdió de verdad

Sucede: la agencia cerró, el empleado se fue, el archivo es de 2009. El flujo de trabajo de recuperación, en orden de preferencia:

1. **OCR + reconstrucción en una herramienta adecuada.** Extraiga el texto mediante OCR, reconstruya el documento en Word o InDesign y traduzca *eso*, pagando el coste de reconstrucción **una sola vez**. A partir de ahí el documento tiene una fuente real y cada idioma y revisión futura sale barato. Esta es casi siempre la decisión correcta para documentos vivos (catálogos, manuales, listas de precios).
2. **Traducir como texto, entregar bilingüe o con maquetación simplificada.** Para documentos puntuales de poca importancia (un certificado antiguo, un informe heredado), sáltense por completo la reconstrucción de la maquetación: entregue el texto traducido en un documento limpio y sencillo. No es bonito, es adecuado.
3. **Parches superpuestos** para el caso raro en que la maquetación original deba conservarse exactamente pero la fuente ya no exista: vacíe las zonas de texto de origen y componga las traducciones encima. Lento, frágil, y el problema de la expansión del texto ([+30 % en alemán](/es/news/text-expansion-translation-layout/)) destroza las maquetaciones ajustadas. Último recurso.

Elija el camino que elija: los gráficos con texto incrustado necesitan su propio tratamiento, según el [flujo de trabajo de gráficos e infografías](/es/news/infographic-chart-localization/): son la otra mitad de la factura de reconstrucción.

## Construir la canalización aguas arriba

La solución permanente es procedural y no cuesta más que una decisión:

- **Archive los archivos fuente como entregables.** Todo proyecto de documento —interno o de agencia— termina con los archivos fuente en su repositorio, no solo con el PDF. Conviértalo en una cláusula contractual con las agencias de diseño.
- **Elija herramientas pensando en la traducción.** InDesign exporta IDML; FrameMaker está construido para documentación multilingüe estructurada (los pros y contras en [InDesign frente a FrameMaker](/es/news/indesign-vs-framemaker-multilingual/)); incluso los documentos de Word se traducen limpiamente cuando se construyen con estilos reales en lugar de formato manual. La documentación basada en Markdown con PDF generados es el caso soñado: traduzca el texto, reconstruya el PDF en el paso de compilación.
- **Mantenga el texto fuera de las imágenes** y las fuentes incrustadas con licencias que permitan la edición, de modo que la extracción y la recomposición sigan siendo legales y posibles.
- **Alimente la memoria de traducción.** Cada documento traducido añade pares de segmentos a su [TM](/es/news/translation-memory-dtp-efficiency/): la revisión 3 del catálogo en el idioma 5 cuesta entonces una fracción de la revisión 1, porque solo se traducen los segmentos modificados. Aquí es donde ocurre el verdadero efecto compuesto.

## La decisión en una tabla

| Situación | Camino | Coste relativo |
|---|---|---|
| Existe el archivo fuente | Traducir la fuente, reexportar el PDF | 1× |
| PDF editable, sin fuente | Extraer → traducir → reconstruir una vez → ahora ya tiene fuente | 1,5–3× una vez, luego 1× |
| Aplanado/escaneado, documento vivo | OCR + reconstruir → traducir | 2–4× una vez, luego 1× |
| Aplanado/escaneado, caso puntual | Traducir como texto, maquetación sencilla | ~1×, sin fidelidad de maquetación |

El patrón: las opciones caras son todas caras *una sola vez* si reconstruye correctamente, y caras *para siempre* si sigue traduciendo el PDF.

Sus documentos deberían ser activos que se abaratan de localizar con el tiempo, no artefactos que rescata de un programa de maquetación cada trimestre. Nuestro [equipo de DTP](/es/services/localization/dtp/) gestiona la cadena completa —extracción, traducción, reconstrucción y el control tipográfico en [cada escritura](/es/news/multilingual-dtp-typography-guide/)— y siempre le devuelve los archivos fuente. [Envíenos su PDF más doloroso](/es/contact/) y le diremos exactamente en qué fila de la tabla está.
