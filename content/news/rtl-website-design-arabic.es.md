---
title: "Diseño web RTL: espejo del diseño para el árabe"
date: 2027-01-04T11:56:00+08:00
publishDate: 2027-01-04T11:56:00+08:00
category: "industry"
category_label: "Industria"
tags: ["Creación de sitios web", "árabe", "RTL", "diseño web"]
keywords: ["diseño web rtl", "diseño web árabe", "diseño web de derecha a izquierda"]
cover: "/images/news/rtl-website-design-arabic.jpg"
author: "MediaLocalize Team"
summary: "Un sitio web en árabe no es su sitio LTR con texto traducido: toda la lógica visual se refleja. Qué se invierte de verdad, qué no debe invertirse y las prácticas de CSS que permiten a una sola base de código servir ambas direcciones."
---

En algún lugar del mundo, ahora mismo, un comprador en Riad está mirando un sitio web «en árabe» donde el texto es árabe pero todo lo demás está mal: el menú se abre desde la izquierda, las migas de pan se leen al revés, una barra de progreso se llena de izquierda a derecha y un número de teléfono se muestra con los dígitos desordenados por errores de texto bidireccional. La empresa pagó por la traducción y se saltó la dirección. El diseño RTL no es una tarea de traducción ni puramente una tarea de desarrollo: es una disciplina de diseño de maquetación, y hacerlo bien es la diferencia entre un sitio localizado y un reflejo improvisado.

## Qué se refleja y qué no

La regla general: **todo lo que implica dirección de lectura o progreso se invierte; todo lo que representa el mundo físico o una norma, no.**

Se refleja en RTL:

- La retícula de la página: navegación, barras laterales, columnas de contenido
- La alineación del texto (derecha por defecto), las sangrías, la posición de las viñetas
- Migas de pan, indicadores de progreso, asistentes paso a paso, líneas de tiempo
- Flechas que implican secuencia (→ se convierte en ←), direcciones de carruseles
- Iconos que implican movimiento u orden de lectura: chevrones de atrás/adelante, el avión de papel de «enviar», barras de progreso de lectura
- Diseño de formularios: etiquetas y campos fluyen de derecha a izquierda

**No** se refleja:

- Logotipos (nunca invierta una marca verbal)
- Iconos que representan objetos: teléfono, sobre, impresora, reloj (aunque las *esferas* del reloj se quedan: el tiempo no corre hacia atrás)
- Controles multimedia: reproducción (▶), avance rápido, volumen; la convención universal los mantiene LTR
- Gráficos y diagramas: el eje x sigue aumentando de izquierda a derecha por convención científica, pero las *etiquetas y el diseño de la leyenda* siguen el RTL, como explicamos para la [localización de gráficos](/es/news/infographic-chart-localization/)
- Números, números de teléfono, fechas en dígitos latinos: se mantienen LTR *dentro* del flujo RTL (aquí es donde viven los errores de bidi; más abajo)

## El problema del texto bidireccional

Los errores más difíciles no son de maquetación, son **cadenas de dirección mixta**. El texto árabe fluye en RTL, pero los números, los nombres de marca latinos, las URL y los términos técnicos se mantienen LTR. Cuando ambos aparecen en una misma cadena, el algoritmo bidireccional de Unicode decide el orden visual, y con regularidad decide mal:

- Una frase que termina en un número de modelo puede mostrar el número en el extremo equivocado
- Los números de teléfono con prefijo `+` pueden desordenarse (`+966 11 234 5678` apareciendo como `5678 234 11 966+`)
- La puntuación adyacente al texto latino salta al lado equivocado

Las soluciones viven en el marcado: envuelva los fragmentos latinos incrustados en `<bdi>` o aplique `unicode-bidi: isolate`, use marcas direccionales (`&lrm;`) alrededor de la puntuación cuando sea necesario y *pruebe con contenido real*; la misma disciplina que el [DTP en árabe](/es/news/arabic-dtp-indesign-rtl/), donde se aplican las mismas reglas de bidi en impresión. Como señalamos en [SEO en árabe](/es/news/arabic-seo-gulf-markets/), Google posiciona bien las páginas árabes con LTR roto, pero los compradores no convierten en ellas.

## Construir una sola base de código para ambas direcciones

El CSS moderno hace que los sitios bidireccionales sean mantenibles, siempre que se construya con propiedades lógicas desde el principio:

| Física (se rompe en RTL) | Lógica (se adapta automáticamente) |
|---|---|
| `margin-left` / `margin-right` | `margin-inline-start` / `margin-inline-end` |
| `padding-left: 20px` | `padding-inline-start: 20px` |
| `left: 0` / `right: 0` | `inset-inline-start: 0` / `inset-inline-end: 0` |
| `text-align: left` | `text-align: start` |
| `border-right` | `border-inline-end` |

Establezca `dir="rtl"` en el elemento `<html>` de las páginas en árabe (nuestras plantillas lo hacen desde la configuración del idioma), escriba los estilos con propiedades lógicas y la maquetación se reflejará sola. Lo que sigue siendo manual: invertir los iconos direccionales (sirva una variante RTL o use `transform: scaleX(-1)` en los iconos específicos que implican dirección; nunca en componentes completos) y auditar la lista de excepciones anterior.

## Tipografía y detalles de diseño

- **Fuentes**: el árabe necesita fuentes web árabes creadas expresamente (no una fuente latina con reserva en árabe). La altura de línea debe aumentar entre un 20 y un 30 % sobre los ajustes latinos: los diacríticos y las formas de las letras árabes colisionan con alturas de línea latinas. La disciplina paralela al [emparejamiento de fuentes CJK-latinas](/es/news/cjk-latin-font-pairing/), con especificidades distintas.
- **Numerales**: los contextos empresariales del Golfo usan abrumadoramente dígitos occidentales (0-9), no arábigo-índicos (٠-٩), pero *conozca su mercado*; cierto contenido cercano a la administración pública espera dígitos arábigo-índicos. Elija por mercado y mantenga la coherencia, exactamente igual que con los [formatos de fecha y número](/es/news/date-currency-format-localization/).
- **Negrita y cursiva**: el árabe no tiene cursiva verdadera; la inclinación sintética se ve rota. Use peso y color para el énfasis, no inclinación.
- **Letter-spacing**: nunca lo aplique al árabe, rompe la unión cursiva entre letras. Cualquier `letter-spacing` global en su CSS debe restablecerse para el árabe.

## La lista de verificación de la auditoría

Antes de publicar una sección en árabe:

1. Maquetación totalmente reflejada: navegación, pie de página, migas de pan, formularios, deslizadores
2. Iconos direccionales invertidos; iconos de objetos y logotipos intactos
3. Auditoría bidi: números de teléfono, correos electrónicos, números de modelo, precios en contenido real
4. Fuente árabe cargada y primera en la pila de fuentes; altura de línea aumentada
5. Sin letter-spacing ni cursiva sintética en el texto árabe
6. Formularios: maquetación RTL pero comportamiento de entrada LTR para correos, teléfonos y URL
7. Navegación completa de prueba en un Android de gama media: la clase de dispositivo dominante en el mercado

Una sección en árabe construida así no se siente «localizada», se siente nativa, que es todo el punto, como sostiene la [guía de marketing para Oriente Medio](/es/news/middle-east-arabic-b2b-marketing/) desde el lado comercial. Nuestro [equipo de localización](/es/services/localization/) construye secciones web en árabe con texto nativo, renderizado bidi correcto y diseño en espejo desde el primer commit. [Envíenos su URL](/es/contact/) y ejecutaremos la auditoría RTL de siete puntos en su sitio actual.
