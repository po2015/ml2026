---
title: "DTP en árabe: maquetación de derecha a izquierda en InDesign"
date: 2026-12-02T20:46:00+08:00
publishDate: 2026-12-02T20:46:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["DTP", "árabe", "RTL", "InDesign"]
keywords: ["dtp árabe indesign", "maquetación de derecha a izquierda", "composición tipográfica árabe"]
cover: "/images/news/arabic-dtp-indesign-rtl.jpg"
author: "MediaLocalize Team"
summary: "El DTP en árabe no es «reflejar el archivo en inglés». Las fuentes, los dígitos, la dirección de las tablas y la propia maquinaria RTL de InDesign tienen modos de fallo que solo aparecen en el PDF final: así se evitan."
---

Un fabricante europeo envía su catálogo de productos para DTP en árabe. Se refleja la maquetación en inglés, se pega el texto árabe, y el PDF vuelve con letras desconectadas, números latinos donde el cliente esperaba dígitos arábigos orientales, un índice que se lee de izquierda a derecha y un logotipo que ahora queda incómodo frente a un texto reflejado. Cada problema es pequeño; juntos anuncian que nadie de los implicados había compuesto en árabe antes.

El DTP en árabe es una especialización, no una casilla que marcar. Esto es lo que realmente cambia y cómo llevar un proyecto RTL en InDesign sin sobresaltos.

## El propio texto: conformación, ligaduras y dirección

**El árabe es cursivo por construcción.** Cada letra tiene hasta cuatro formas posicionales (aislada, inicial, media, final), y la reproducción correcta requiere que el motor de maquetación las conforme. Pegue árabe en un documento con una fuente sin glifos árabes, o con un compositor que no conforme, y obtendrá el síntoma clásico: letras renderizadas en sus formas aisladas, legibles pero evidentemente rotas para cualquier ojo nativo, como inglés impreso con espacios entre cada letra. En InDesign esto significa: use el **World-Ready Composer** (ajuste a nivel de párrafo) y una fuente con soporte árabe real; nunca lo dé por sentado.

**El texto bidireccional fluye en ambos sentidos en una misma línea.** Las frases árabes con términos latinos incrustados, números de modelo o URL contienen islas de izquierda a derecha dentro de un flujo de derecha a izquierda. El algoritmo bidi resuelve la mayoría de los casos, pero los casos límite (un número de modelo al inicio de una línea, puntuación entre dos escrituras, paréntesis alrededor de un término latino) necesitan inspección manual y, en ocasiones, marcas direccionales explícitas. Presupueste tiempo de revisión para cada línea mixta; no existe una automatización fiable.

**Los dígitos son una decisión, no un valor por defecto.** Los dígitos arábigos orientales (٠١٢٣٤٥٦٧٨٩) son el estándar en los materiales impresos del Golfo; los dígitos occidentales (0–9) dominan en la documentación técnica y en el norte de África. Su cliente debe elegir por tipo de documento, y "igual que el original" no es una política, es lanzar una moneda al aire. Inclúyalo en el brief del proyecto junto a las [decisiones de pronunciación y terminología](/es/news/ai-voice-pronunciation-lexicon/) que rigen su contenido de audio.

## La maquetación: reflejar es el principio, no el trabajo

Voltear una página a RTL es el 20 % del trabajo. El otro 80 %:

- **Elementos de orden de lectura**: índices, pasos numerados, migas de pan y texto en varias columnas deben fluir de derecha a izquierda; la columna uno está a la *derecha*. Una tabla de especificaciones de producto a dos columnas mantiene las etiquetas a la derecha y los valores a la izquierda... salvo que los valores sean números de modelo latinos, en cuyo caso la consistencia vence a la pureza.
- **Tablas**: refleje el orden de las columnas para que la columna de etiquetas quede a la derecha, pero mantenga el orden LTR en tablas de contenido latino (listas de referencias de piezas). Las tablas mixtas son normales; documente la regla por tipo de tabla.
- **Imágenes**: las fotos con composición direccional (el flujo de trabajo de una máquina mostrado de izquierda a derecha, una flecha en un diagrama) pueden necesitar versiones reflejadas. Nunca refleje imágenes que contengan texto legible, relojes, mapas o marcas registradas: la misma regla que en la [localización visual](/es/news/image-icon-color-localization/) en general.
- **Iconos y viñetas**: los iconos direccionales (flechas, chevrones, triángulos de reproducción) se voltean; los simétricos, no. Las viñetas migran al margen derecho junto con su texto.
- **Elementos de página**: números de página, encabezados corrientes y posición del lomo, todo se refleja; el lomo de un libro árabe en rústica está a la derecha, lo que afecta a las cubiertas y a la imposición de imprenta.

## La maquinaria de InDesign

Configuración de trabajo para un proyecto RTL:

1. **Parta de la versión con capacidad ME**: cualquier InDesign actual admite RTL, pero las funciones de Oriente Medio (controles de dirección de párrafo RTL, opciones tipográficas para árabe y hebreo) deben estar activadas; en las versiones actuales vienen con la instalación estándar.
2. **La dirección de párrafo es el interruptor maestro**: configúrela como RTL a nivel de *estilo*, nunca sobrescribiendo párrafos de forma puntual. La dirección de caracteres gestiona las islas LTR.
3. **World-Ready Composer en cada estilo árabe.** Este es el motor de conformación; el Adobe Paragraph Composer producirá el síntoma de las letras desconectadas.
4. **Fuentes con cobertura árabe genuina**: Noto Naskh Arabic / Noto Kufi Arabic, Adobe Arabic o tipografías de fundiciones con licencia (GE SS, Boutros, Sakkal Majalla para trabajo corporativo). Compruebe el comportamiento de la kashida si el diseño justifica el texto: la justificación árabe alarga las letras en lugar de espaciar las palabras, y una kashida mala es tan fea como un tracking malo. La misma [disciplina de combinación](/es/news/cjk-latin-font-pairing/) se aplica a los tramos latinos del documento: elija una tipografía latina acompañante, no herede la latina integrada de la fuente árabe.
5. **Los ajustes de dirección de artículo y de tabla** existen por separado de la dirección de párrafo: un párrafo RTL dentro de una tabla LTR es una fuente clásica de "¿por qué la primera columna está a la izquierda?".

## Números, fechas y unidades en documentos mixtos

Los catálogos técnicos son el caso común, y están llenos de números. Defina las reglas antes de empezar la maquetación: juego de dígitos (según lo anterior), formato de fecha (nombres de meses árabes frente a números; fechas del calendario hégira solo si el cliente lo pide), unidades (kW se queda en latín; traducciones de los *nombres* de las unidades en prosa) y separadores decimales (el árabe usa el separador decimal arábigo ٫ en documentos totalmente localizados, y convenciones occidentales en los técnicos). Estas decisiones interactúan con todo: una tabla de especificaciones que mezcla ٠.٥ y 0.5 en filas adyacentes parece un error porque lo es.

## Control de calidad: qué revisar antes de que salga el PDF

- Haga zoom al 100 % y lea cada línea que contenga un número, un término latino o un signo de puntuación: ahí viven los fallos de bidi.
- Revise la justificación en busca de kashidas estiradas o en colisión.
- Verifique que las referencias cruzadas, el índice y el índice analítico se regeneraron *después* de los cambios de dirección: los índices obsoletos conservan el orden de páginas LTR.
- Una lectura completa del PDF final por un hablante nativo, no del archivo de traducción. Los errores de conformación y dirección son invisibles fuera de la maquetación.
- Comprobación previa de incrustación de fuentes: las fuentes árabes con restricciones de licencia sobre incrustación morderán en la imprenta, no en su pantalla.

El DTP en árabe bien hecho es invisible: el catálogo simplemente parece diseñado en árabe. Hecho de forma descuidada, cada página dice lo contrario. Nuestro [equipo de DTP](/es/services/localization/dtp/) ejecuta proyectos RTL con revisión nativa integrada en la pasada de control de calidad. [Envíenos su original en inglés](/es/contact/) y le devolveremos una edición árabe lista para imprenta: conformación, dígitos y lomo, todo correcto.
