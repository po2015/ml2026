---
title: "Combinación de fuentes CJK y latinas: cómo armonizar la tipografía china y latina"
date: 2026-11-16T15:40:00+08:00
publishDate: 2026-11-16T15:40:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["DTP", "CJK", "tipografía", "combinación de fuentes"]
keywords: ["combinación de fuentes cjk", "armonizar fuentes chinas y latinas", "source han sans"]
cover: "/images/news/cjk-latin-font-pairing.jpg"
author: "MediaLocalize Team"
summary: "Los documentos mixtos en chino y latino fracasan cuando las dos escrituras parecen provenir de empresas distintas. Cómo combinar tipografías CJK y latinas para que folletos, manuales y sitios web se lean como un solo diseño."
---

Abra un folleto de producto bilingüe y fíjese solo en la tipografía. En la versión deficiente, el chino está compuesto en una delicada fuente de estilo Ming mientras el texto latino usa una sans geométrica pesada: misma página, dos personalidades. En la versión buena, el cambio de escritura apenas se percibe. Esa invisibilidad es el objetivo de la combinación de fuentes CJK y latinas, y lograrla exige decisiones deliberadas, no valores predeterminados.

Esto importa en cualquier lugar donde el texto chino y el latino compartan página: fichas técnicas con números de modelo, manuales con etiquetas de interfaz en inglés, sitios web bilingües, empaques con texto normativo en inglés. Así es como los profesionales combinan ambas escrituras, en pantalla y en imprenta.

## Por qué el resultado predeterminado es malo

Toda fuente CJK incluye glifos latinos integrados, y por lo general son un añadido secundario, dibujados para llenar páginas de códigos y no para armonizar con nada. Componga un párrafo en una fuente china y deje que las palabras en inglés recurran a su latino integrado, y aparecerán las señales delatoras: letras latinas ligeramente demasiado pequeñas, demasiado ligeras o con un espaciado incómodo junto a los hanzi. A la inversa, componer el texto chino con lo que el sistema elija (SimSun en Windows antiguos, una fuente de reserva aleatoria en macOS) hace que el chino parezca prestado.

La solución es siempre la misma: **elija la fuente latina y la fuente CJK de forma independiente, y luego verifique que funcionen juntas.**

## Los cuatro criterios de armonización

**1. Peso.** El grosor del trazo debe percibirse equivalente al mismo tamaño nominal. Un peso Medium CJK suele combinar mejor con un peso Regular latino que con Medium: los glifos CJK son más densos, de modo que trazos de igual grosor se leen más pesados. Compare siempre visualmente; nunca confíe en los nombres de los pesos.

**2. Proporción.** El texto latino se apoya en una línea de base con altura x y descendientes; los hanzi ocupan cuadrados de em completos. Las buenas parejas equilibran la altura x latina con el cuerpo CJK para que las líneas mixtas no formen dientes de sierra. Las fuentes latinas humanistas (con alturas x más altas) suelen integrarse con más facilidad que las geométricas.

**3. Textura.** El "color" en sentido tipográfico: la densidad de gris general de un párrafo. Las fuentes CJK de estilo Song/Ming (con contraste de trazos, como las serif latinas) combinan con serif latinas; las de estilo Hei/góticas (trazos uniformes) combinan con sans latinas. Cruzar las corrientes —chino Ming con Helvetica— es el error de aficionado más común.

**4. Personalidad.** Redondeada, técnica, caligráfica, corporativa. Una fuente latina amable y redondeada junto a una gótica china severa y cuadrada desvirtúa a ambas.

## Combinaciones que funcionan

| Caso de uso | Fuente CJK | Acompañante latina | Notas |
|---|---|---|---|
| Sans corporativa (web + imprenta) | Source Han Sans / Noto Sans CJK SC | Source Sans, o su latino integrado sustituido por Inter | Diseñadas como familia; la opción predeterminada más segura |
| Imprenta editorial/serif | Source Han Serif / Noto Serif CJK SC | Source Serif, Charter | Para informes, libros blancos, libros |
| Documentación técnica | Noto Sans CJK SC | IBM Plex Sans, Roboto | Tolera tamaños pequeños y tablas |
| Imprenta de marca premium | Fuente de fundición con licencia (p. ej. FounderType, Hanyi) | Latina a juego del mismo programa de la fundición | Prevea presupuesto para licenciar ambas escrituras |

Las familias Noto/Source Han (mismo diseño, distinto empaquetado de Google y Adobe) dominan el trabajo profesional por una razón: gamas completas de pesos, enorme cobertura de glifos y licencias que permiten incrustarlas en PDF, aplicaciones y proyectos web sin costo.

## Problemas específicos de la web

**Tamaño de archivo.** Una fuente CJK completa pesa 5–20 MB por peso: inaceptable como fuente web monolítica. Soluciones: subdivisión por rangos Unicode (el navegador descarga solo los bloques de glifos que la página usa, algo que las fuentes web Noto CJK hacen automáticamente), pilas de fuentes del sistema para el texto de cuerpo, o limitar las fuentes CJK web a tamaños de titulares.

**Las pilas del sistema varían según la plataforma.** `PingFang SC` (macOS/iOS), `Microsoft YaHei` (Windows), `Noto Sans CJK SC` (Android/Linux) son los valores predeterminados sensatos: declare los tres. Omitir la pila significa que los usuarios de Android reciben una serif de reserva mientras los de iPhone reciben una sans.

**Negrita simulada.** Muchas fuentes CJK del sistema tienen solo uno o dos pesos. Si el CSS pide `font-weight: 700` y la fuente no tiene negrita, el navegador la sintetiza ensanchando los trazos: reconocible al instante y de aspecto barato. Cargue un peso de negrita real o rediseñe para no necesitarlo nunca.

## Especificidades de imprenta y DTP

En InDesign y herramientas similares, defina las fuentes CJK y latinas explícitamente en los estilos de párrafo mediante fuentes compuestas; nunca confíe en un "aplicar a todo" con una sola tipografía. Vigile la puntuación: la puntuación china de ancho completo （，。：）corresponde al texto chino, la de medio ancho al latino, y las frases mixtas requieren revisión manual. Las reglas de kinsoku (corte de línea) difieren según el idioma; un párrafo chino compuesto con reglas de justificación inglesas produce ríos tipográficos y cortes desagradables. Son la misma clase de problemas de maquetación que la [expansión del texto](/es/news/text-expansion-translation-layout/): invisibles hasta que se miran páginas reales.

## Una lista de verificación práctica

1. Elija primero la fuente latina de la marca (normalmente ya existe) y luego pruebe candidatas CJK frente a ella, a tamaños reales en maquetas reales.
2. Pruebe los casos más difíciles: texto mixto en línea ("支持 PDF/A-2b 格式"), titulares en negrita, pies de foto pequeños, numerales en tablas.
3. Verifique la incrustación y las licencias para cada canal de salida: PDF, web, aplicación, tirada de empaques.
4. Documente la combinación en la guía de estilo con las correspondencias exactas de pesos, para que el próximo diseñador no tenga que replantearla.

La combinación de fuentes se decide una vez y la hereda cada documento que se produzca: vale la pena resolverla a nivel de sistema en lugar de corregir folleto por folleto. Nuestro [equipo de DTP](/es/services/localization/dtp/) integra sistemas tipográficos bilingües en cada proyecto de maquetación, desde fichas técnicas hasta catálogos completos. [Envíenos una página de muestra](/es/contact/) y le mostraremos lo que su tipografía actual está diciendo de su marca.
