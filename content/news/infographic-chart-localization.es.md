---
title: "Localización de gráficos, diagramas e infografías"
date: 2026-12-22T16:37:00+08:00
publishDate: 2026-12-22T16:37:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["DTP", "infografías", "gráficos", "localización visual"]
keywords: ["localización de infografías", "traducción de gráficos", "localización de diagramas"]
cover: "/images/news/infographic-chart-localization.jpg"
author: "MediaLocalize Team"
summary: "Un gráfico no es una imagen con palabras encima: es texto, números, ejes, colores y orden de lectura fusionados en un solo argumento. Cómo localizar gráficos de datos sin romper el argumento ni el diseño."
---

La ficha técnica está perfectamente traducida. Entonces el comprador llega a la página tres: una curva de rendimiento con las etiquetas de los ejes en inglés, una tabla comparativa incrustada en un PNG y una infografía cuyos rótulos ahora apuntan a lo que no deben porque alguien tradujo la capa de texto y nada más. Los gráficos de datos son donde los proyectos de traducción se rompen silenciosamente, porque un gráfico no es una imagen con palabras encima. Es un argumento hecho de texto, números, posición y color, y localizarlo significa reconstruir ese argumento para cada mercado.

## Primera decisión: qué gráficos realmente necesitan trabajo

Haga triaje antes de tocar nada:

- **Sin texto, imágenes universales** (fotos de producto, diagramas solo con iconos): publíquelos tal cual.
- **Con texto pero regenerables** (gráficos de Excel/Tableau/bibliotecas web de gráficos): regenérelos desde la fuente con las etiquetas traducidas; es lo más barato y limpio.
- **Texto incrustado en píxeles** (PNG exportados, capturas de pantalla, diagramas escaneados): hay que reconstruirlos o retocarlos en DTP. Aquí es donde mueren los presupuestos, y por eso recomendamos a los clientes [mantener el texto fuera de las imágenes](/es/news/image-icon-color-localization/) desde la fase de creación.
- **Capturas de pantalla de software**: decida por mercado; capturas de la interfaz localizada si el producto existe en ese idioma, originales anotados si no.

## La mecánica: texto, números, ejes

**La expansión del texto afecta a los gráficos más que a la prosa.** El alemán es aproximadamente un 30 % más largo que el inglés; un cuadro de rótulo ajustado que albergaba «Torque» ahora debe albergar «Drehmoment» (bien), pero «Max. operating pressure» convertido en «Maximaler Betriebsdruck» rompe el diseño. Se aplica el [manual estándar sobre expansión de texto](/es/news/text-expansion-translation-layout/) con una amplificación: los gráficos no tienen un diseño fluido que absorba el crecimiento. Presupueste tiempo de redibujado, acorte las etiquetas con decisión (abreviaturas, leyendas en lugar de etiquetas en línea) y nunca reduzca la fuente por debajo de la legibilidad para que quepa.

**Los números y los ejes siguen al mercado.** Comas decimales (3,14 frente a 3.14), separadores de miles, formatos de fecha en ejes temporales, unidades en los títulos de los ejes: todo se localiza, según las convenciones de nuestra [guía de formatos de fecha y número](/es/news/date-currency-format-localization/). Un gráfico regenerado con etiquetas traducidas pero con formatos numéricos estadounidenses está localizado a medias y se percibe como tal.

**El orden de lectura se invierte en RTL.** Un diagrama de proceso que fluye de izquierda a derecha en inglés debe fluir de derecha a izquierda en árabe: flechas, números de secuencia y todo lo demás. Simplemente reflejar la imagen rompe los gráficos (los valores de los ejes reflejados son incorrectos); la solución correcta es reconstruir el diseño en RTL con los datos intactos. La misma disciplina bidireccional que en el [DTP árabe](/es/news/arabic-dtp-indesign-rtl/), aplicada a los gráficos.

**El soporte tipográfico decide la legibilidad.** Las etiquetas en CJK, árabe y tailandés necesitan fuentes que las representen correctamente en tamaños pequeños: véase la [guía de combinación de fuentes](/es/news/cjk-latin-font-pairing/). Una infografía en inglés preciosa, compuesta con una fuente de sustitución en su versión china, parece rota exactamente para los lectores a los que iba destinada.

## El color y el simbolismo también son datos

El color codifica significado en los gráficos: rojo para pérdidas, verde para crecimiento en la convención occidental; el rojo es positivo en las bolsas de China y Japón. Un gráfico de rendimiento en rojo/verde puede invertir su mensaje para algunas audiencias. Consulte las [convenciones de color](/es/news/image-icon-color-localization/) por mercado y, en caso de duda, use codificación redundante (color *más* iconos o etiquetas), que además es mejor para la accesibilidad en todas partes.

## Un flujo de trabajo que escala

1. **Cree por capas.** Conserve la fuente de cada gráfico (hoja de cálculo, archivo vectorial) con el texto en su propia capa. Los gráficos creados en plano cuestan entre 5 y 10 veces más de localizar.
2. **Extraiga el texto como cualquier otro contenido.** Las etiquetas de los gráficos entran en el mismo flujo de traducción y en la misma [memoria de traducción](/es/news/translation-memory-dtp-efficiency/) que el cuerpo del texto: los títulos de ejes y los rótulos se repiten entre documentos más de lo que cree.
3. **Regenere, no retoque, donde exista la fuente.** Una biblioteca de gráficos programable (incluso una simple plantilla matplotlib/D3) convierte las reconstrucciones por idioma en un paso de compilación.
4. **Retoque solo lo que quedó varado.** Para gráficos que existen solo en píxeles, un especialista en DTP reconstruye las capas de texto en Photoshop o Illustrator: prográmelo, no lo descubra en la entrega.
5. **Revise en contexto con revisores nativos.** Los números se malinterpretan al moverlos: un separador decimal intercambiado es un error factual, no una errata. El control de calidad de los gráficos pertenece a la [lista de verificación de DTP](/es/news/technical-manual-translation-dtp-checklist/), con los números contrastados contra los datos de origen, no solo las etiquetas contra el glosario.

## El panorama de costes

Localizar un gráfico correctamente cuesta desde casi cero (regenerado desde una fuente por capas) hasta más que la traducción de la página que lo rodea (infografía incrustada en píxeles, diez idiomas, variantes RTL). La palanca está totalmente aguas arriba: los equipos que crean gráficos localizables una vez localizan cada documento posterior a bajo coste. Los que no lo hacen pagan el impuesto del redibujado para siempre.

Los gráficos persuaden donde los párrafos no pueden: un comprador que compara curvas de par está más cerca de una solicitud de presupuesto que uno que lee texto de marketing. Nuestro [equipo de DTP](/es/services/localization/dtp/) localiza gráficos de datos como parte de cada proyecto documental: extracción, regeneración, reconstrucciones RTL y control numérico de calidad incluidos. [Envíenos un documento de muestra](/es/contact/) y le mostraremos cuáles de sus gráficos son localizables tal cual y cuáles son bombas de relojería.
