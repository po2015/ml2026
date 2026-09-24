---
title: "Expansión del texto: diseños que sobreviven a la traducción"
date: 2026-10-27T14:41:00+08:00
publishDate: 2026-10-27T14:41:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["DTP", "expansión del texto", "diseño multilingüe", "tipografía"]
keywords: ["expansión de texto en traducción", "diseño de maquetas multilingües", "crecimiento del texto al traducir"]
cover: "/images/news/text-expansion-translation-layout.jpg"
author: "MediaLocalize Team"
summary: "El alemán es un 30 % más largo que el inglés y el árabe se lee al revés. Cómo diseñar documentos e interfaces que sobrevivan a la traducción, antes de pagar por arreglar cada maqueta."
---

Todo documento traducido es una prueba de estrés para su maqueta. Un texto en inglés compuesto en un diseño ajustado y elegante se convierte en texto alemán que desborda sus cajas, en texto árabe que apunta en la dirección equivocada y en texto chino con huecos extraños. La maqueta no falló en la traducción: falló en el momento del diseño, cuando nadie presupuestó espacio para otros idiomas.

La expansión del texto es la fuente más predecible de costos de DTP multilingüe, y la más evitable. Este artículo la cuantifica y le da las reglas de diseño que hacen que las maquetas sobrevivan.

## ¿Cuánto crece realmente el texto?

Los factores de expansión con los que se planifica todo proyecto de localización (inglés como origen):

| Idioma de destino | Expansión típica | Notas |
|---|---|---|
| Alemán | +20–35 % | Las palabras compuestas crean cadenas muy largas e indivisibles |
| Ruso | +15–25 % | Palabras largas, glifos cirílicos más anchos |
| Árabe | +20–30 % | Más el cambio de dirección de derecha a izquierda |
| Español | +15–25 % | Palabras más largas, más artículos y preposiciones |
| Francés | +15–20 % | Más reglas tipográficas de espaciado (« comillas latinas », espacio antes de los dos puntos) |
| Chino | −10–30 % (se contrae) | Pero mayor altura de línea y reglas de corte distintas |
| Japonés | −10–20 % (se contrae) | Más la posibilidad de composición vertical |

Dos advertencias que importan más que los promedios. Primero, **las cadenas cortas son las que más se expanden**: una etiqueta de navegación como "Home" que se convierte en "Startseite" (+75 %) o "New" en "Neuigkeiten"; la interfaz, los botones y los encabezados de tabla sufren mucho más que los párrafos de cuerpo. Segundo, **la expansión es por cadena, no por documento**: un solo titular un 40 % más largo en un banner fijo rompe la maqueta aunque el promedio de la página sea del 20 %.

## Dónde rompe primero la expansión

1. **Navegación y botones**: menús de ancho fijo diseñados alrededor de etiquetas en inglés de 4 a 8 caracteres.
2. **Tablas**: los encabezados de columna son palabras cortas en inglés; los encabezados en alemán fuerzan saltos de línea o desplazamiento horizontal.
3. **Diagramas e infografías**: cajas de texto dimensionadas a la medida de la palabra, a menudo en imágenes aplanadas donde el texto ni siquiera es editable.
4. **Formularios**: etiquetas junto a campos de entrada, mensajes de error, texto de marcador de posición.
5. **Fichas técnicas en PDF**: el clásico: una ficha de una página en inglés se convierte en página y media de alemán, y alguien reduce las fuentes a mano para forzarla a caber.

## Reglas de diseño que previenen el daño

### Presupueste espacio en el momento del diseño

- Diseñe los contenedores de texto con **un 30–40 % de capacidad sobrante** en cualquier maqueta destinada a traducirse. Si el inglés llena la caja, el diseño ya está roto para otros cinco idiomas.
- Prefiera **maquetas flexibles**: marcos de texto que crecen automáticamente, columnas de tabla responsivas y una navegación que se ajuste con elegancia en lugar de anchos de píxel fijos.
- Pruebe las cadenas del peor caso, no los promedios: tome sus etiquetas más cortas y páselas por el alemán.

### Mantenga el texto editable

- Nunca incruste texto en imágenes. Los diagramas con capas de texto editables (InDesign, Illustrator, SVG) se localizan en minutos; los PNG aplanados se recrean desde cero por idioma, o se envían sin traducir, que es peor.
- En documentos impresos, use estilos de párrafo y de carácter con disciplina. Cuando el alemán necesita un ajuste de 0,5 pt en el cuerpo o un tracking distinto, los estilos lo aplican en todo el documento con una sola edición; el formato manual significa corregir cada instancia a mano.

### Planifique el cambio de dirección, no solo la longitud

Las maquetas en árabe y hebreo se reflejan: la lectura comienza arriba a la derecha, las barras de progreso se llenan de derecha a izquierda y las flechas de "anterior/siguiente" intercambian su significado. Reflejar no es voltear toda la página: los números, los nombres de marca en alfabeto latino y los gráficos permanecen de izquierda a derecha dentro de un flujo RTL. Pruebe con contenido árabe real desde el principio; el pseudo-reflejo detecta errores de maqueta, pero no los problemas de puntuación de dirección mixta.

### Respete la tipografía específica de cada escritura

- **El CJK necesita una altura de línea mayor** (1,5–1,7×) que el texto latino; un interlineado ajustado para el alfabeto latino hace que las páginas en chino se sientan apretadas.
- **Las reglas de corte de línea difieren**: el japonés prohíbe ciertos caracteres al inicio y al final de línea; el chino evita cortar dentro de los números; el árabe nunca usa guiones y en su lugar estira las palabras (kashida, el alargamiento caligráfico de los trazos).
- **Fuentes de reserva**: una pila de fuentes que cubra los glifos latinos, CJK, cirílicos y árabes; los glifos faltantes se renderizan como cuadrados, y a menudo aparecen solo en la larga cola de contenido de un solo idioma. Nuestra [guía de tipografía multilingüe](/es/news/multilingual-dtp-typography-guide/) cubre la selección de fuentes en profundidad.

## La economía: arreglar una vez o pagar por idioma

La matemática es simple y brutal. Una maqueta corregida para la traducción en el momento del diseño cuesta una ronda de ajustes. La misma maqueta parchada después de la traducción cuesta esa ronda **multiplicada por cada idioma y cada actualización futura**: vemos con frecuencia empresas que pagan más en reparaciones anuales de DTP que lo que costó el diseño original del documento. Las herramientas también importan: los documentos estructurados y basados en plantillas se recomponen de forma mucho más predecible que las maquetas ajustadas a mano, uno de los puntos de decisión en nuestra [comparación entre InDesign y FrameMaker](/es/news/indesign-vs-framemaker-multilingual/).

Una regla práctica que damos a los clientes: cuente **(páginas × idiomas × actualizaciones por año)**. Si el número supera unos pocos cientos, invierta en plantillas seguras frente a la expansión antes de traducir nada.

## Auditoría rápida para sus documentos existentes

1. ¿Tienen los marcos de texto más del 30 % de margen con la longitud del inglés?
2. ¿Está todo el texto de diagramas e infografías en capas editables?
3. ¿Se usan estilos de párrafo en todas partes (sin ajustes manuales)?
4. ¿Se ha probado alguna vez algo con texto de marcador de posición en alemán y árabe?
5. ¿Contienen sus fuentes glifos cirílicos, CJK y árabes?

Cuatro o cinco respuestas "no" significan que su próximo proyecto de traducción financiará un proyecto de reparación de DTP en paralelo.

Si está preparando documentos para publicación multilingüe, nuestro [equipo de DTP](/es/services/localization/dtp/) puede auditar sus plantillas para verificar su resistencia a la expansión y reconstruir las frágiles: [envíenos un archivo de muestra](/es/contact/) y le mostraremos exactamente dónde se romperá.
