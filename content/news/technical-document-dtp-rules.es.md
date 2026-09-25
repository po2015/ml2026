---
title: "Manuales, fichas técnicas, catálogos: reglas de DTP por tipo de documento"
date: 2027-02-16T16:13:00+08:00
publishDate: 2027-02-16T16:13:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["DTP", "documentación técnica", "manuales", "fichas técnicas"]
keywords: ["dtp documentos técnicos", "maquetación de manuales fichas catálogos", "documentos técnicos multilingües"]
cover: "/images/news/technical-document-dtp-rules.jpg"
author: "MediaLocalize Team"
summary: "Una ficha técnica se lee durante 40 segundos en una feria; un manual se maldice durante tres horas en una planta de fábrica. Documentos distintos fallan de formas distintas al traducirlos: las reglas de DTP que importan, por tipo de documento."
---

Pida a un operador de DTP que maquete «la versión en alemán» y la primera pregunta de vuelta debería ser: ¿versión en alemán de *qué*? Una ficha técnica de una página, un manual de instalación de 200 páginas y un catálogo de 400 SKU son tres disciplinas distintas disfrazadas con el mismo traje de «documento técnico». Difieren en cómo los lectores los usan, dónde el texto traducido los rompe y qué debe detectar el QA. Tratarlos de forma idéntica es como se obtienen fichas con filas de especificaciones huérfanas, manuales con advertencias desplazadas a la página equivocada y catálogos cuyas descripciones de piezas en alemán empujan los precios fuera de la cuadrícula. Estas son las reglas de trabajo, por tipo.

## Fichas técnicas: la densidad es el diseño

Las fichas técnicas son documentos de vistazo: un comprador escanea las especificaciones en menos de un minuto, a menudo impresas en un stand de feria. Todo está al servicio de la tabla:

- **La tabla de especificaciones es sagrada.** El orden de las filas, las unidades y la alineación de columnas deben sobrevivir intactos a la traducción. Traduzca las etiquetas de fila, nunca los valores, y mantenga números y unidades con el formato de la convención del mercado destino (comas decimales para la mayor parte de Europa, según la [disciplina de formatos](/es/news/date-currency-format-localization/)).
- **Diseñe para el idioma más largo.** Las etiquetas de fila en alemán son un 25–35 % más largas que en inglés ([reglas de expansión](/es/news/text-expansion-translation-layout/)); si la maqueta en inglés ya va a sangre, el alemán *va a* envolver una etiqueta sobre la línea de su valor. Incorpore un 30 % de holgura en las columnas de etiquetas o use una tipografía condensada desde el inicio.
- **Una página significa una página.** Una ficha que se desborda a dos páginas en francés ha fallado: los compradores engrapan, escanean y reenvían páginas sueltas. Fije presupuestos estrictos de caracteres por bloque durante la traducción en lugar de reducir el cuerpo tipográfico después; el [brief para el proveedor](/es/news/localization-vendor-brief-template/) tiene un campo exactamente para esto.
- **Las notas al pie y las líneas legales** (certificaciones, descargos de responsabilidad) son texto regulatorio: tradúzcalas con el mismo cuidado que el cuerpo del texto; una nota de certificación mal traducida es un problema de cumplimiento, no una errata.

## Manuales: la estructura porta el significado

Los manuales se recorren secuencialmente, a menudo con mala luz, bajo presión de tiempo, por alguien con una llave inglesa en la mano. Las reglas de DTP se derivan de eso:

- **Las advertencias nunca se recolocan.** Los avisos de seguridad (DANGER/WARNING/CAUTION) deben conservar su icono, su recuadro y *su posición en la página respecto al paso que rigen*. Una expansión de texto que aleja una advertencia de su paso de procedimiento es un defecto de responsabilidad legal: establezca restricciones de «mantener con el siguiente» y verifique los saltos de página en cada idioma.
- **Los procedimientos numerados deben renumerarse limpiamente.** Las listas de pasos, las referencias a figuras («véase la Fig. 4b») y las referencias cruzadas («como se describe en la sección 7.2») se rompen silenciosamente cuando la traducción cambia la paginación. Use campos de referencia cruzada, nunca números tecleados a mano, y ejecute una comprobación de enlaces/referencias como puerta de QA. Aquí es donde las [herramientas de autoría estructurada](/es/news/indesign-vs-framemaker-multilingual/) justifican su costo.
- **Los llamados de ilustración** (las burbujas 1, 2, 3 en los diagramas en despiece) se mantienen numéricos, pero el texto de su leyenda se expande. Deje espacio de leyenda para un +40 %, o traslade las leyendas debajo de la figura en forma de tabla.
- **Mantenga la arquitectura de información del original idéntica entre idiomas.** Un técnico francés y uno inglés deben poder discutir «el paso 14 de la página 38»: la paridad de paginación es una función, así que elija fuentes y espaciados que la preserven. El flujo completo está en nuestra [lista de verificación de traducción de manuales](/es/news/technical-manual-translation-dtp-checklist/).

## Catálogos: la cuadrícula es la marca

Los catálogos son documentos de venta disfrazados de documentos de referencia. Cientos de productos, cuadrículas rígidas y fotografía que hace la persuasión:

- **La longitud del nombre de producto es la restricción.** Los nombres compuestos alemanes son el clásico rompedor de cuadrículas; los nombres en CJK son más cortos pero necesitan las [decisiones de combinación de fuentes](/es/news/cjk-latin-font-pairing/) para verse intencionales. Fije presupuestos de caracteres en los campos de nombre por nivel de producto antes de traducir.
- **Las columnas de precios/especificaciones usan cifras tabulares** y alineación de ancho fijo en todos los idiomas; una columna de precios desalineados se lee como poco profesional en cualquier mercado.
- **El orden de índices y números de parte cambia por idioma.** Los índices alfabéticos se reordenan por nombres traducidos (y por las reglas de ordenación de cada configuración regional: ä se ordena de forma distinta en alemán y en sueco); reconstruya los índices por idioma, no se limite a traducir las entradas.
- **Una plantilla, muchos idiomas**: los catálogos justifican la inversión en una plantilla maestra con capas por idioma, porque se reeditan trimestralmente. La [economía de la memoria de traducción](/es/news/translation-memory-dtp-efficiency/) aquí es la mejor: una reedición con un 15 % de contenido modificado debería costar el 15 % del DTP original, no el 100 %.

## La comparación de un vistazo

| Regla | Ficha técnica | Manual | Catálogo |
|---|---|---|---|
| Restricción principal | Ajuste a una sola página | Paridad de paginación | Integridad de la cuadrícula |
| Estrategia de expansión | Presupuestos de caracteres | Reflujo con reglas de conservación | Presupuestos en campos de nombre |
| Elementos no traducibles | Valores, unidades | Posición de advertencias, números de paso | Números de parte, precios |
| Enfoque de QA | Alineación de tablas | Referencias cruzadas, advertencias, saltos | Orden del índice, desbordamiento de cuadrícula |
| Cadencia de reedición | Por actualización de producto | Rara, versionada | Trimestral: la TM rinde |

## Las reglas compartidas

Sea cual sea el tipo: traduzca en la herramienta de maquetación o con vistas previas conscientes del diseño (nunca a ciegas en hojas de cálculo para archivos finales); mantenga fuentes con la cobertura de idiomas que exige el [flujo de publicación](/es/news/multilingual-dtp-typography-guide/); y corrija *en el PDF final*: los saltos de línea cambian el significado, y solo una página renderizada los muestra. Para originales escaneados o no editables, reconstruya primero según el [flujo de trabajo con PDF](/es/news/pdf-translation-workflow-editable/) en lugar de maquetar sobre parches.

Documentos distintos fallan de formas distintas, y todos los fallos se pueden prevenir en el momento de crear la plantilla. Nuestro [equipo de DTP](/es/services/localization/dtp/) mantiene plantillas listas para cada idioma para los tres tipos de documento, con presupuestos de caracteres, reglas de conservación e índices por idioma integrados. [Envíenos uno de cada](/es/contact/) y le diremos dónde se romperán sus plantillas actuales en alemán, francés y árabe.
