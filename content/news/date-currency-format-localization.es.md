---
title: "Fechas, monedas, unidades: pequeños detalles que rompen la confianza"
date: 2026-12-15T20:59:00+08:00
publishDate: 2026-12-15T20:59:00+08:00
category: "industry"
category_label: "Industria"
tags: ["localización", "formatos", "i18n", "experiencia de usuario"]
keywords: ["localización de formatos de fecha", "localización de moneda", "conversión de unidades sitios web"]
cover: "/images/news/date-currency-format-localization.jpg"
author: "MediaLocalize Team"
summary: "03/04/2026 significa 3 de abril para un alemán y 4 de marzo para un estadounidense. Los errores de formato son pequeños, constantes y corrosivos: una guía de campo para acertar con fechas, monedas, números y unidades en cada mercado."
---

Un comprador alemán lee su promesa de entrega «03/04/2026» como el 3 de abril; usted quiso decir el 4 de marzo. Un comprador argentino ve «$1.500» y no sabe si son mil quinientos dólares o uno y medio. Un ingeniero japonés encuentra especificaciones de par en libras-pie y cierra la ficha técnica. Ninguno de estos es un error de traducción: cada palabra era correcta. Son errores de *formato*, y causan un daño silencioso y acumulativo: cada uno le dice al lector que este documento no fue hecho para él.

Los formatos son la capa más descuidada de la localización porque parecen detalles. Esta es la guía de campo.

## Fechas: la trampa de la ambigüedad

El problema central: las fechas numéricas son ambiguas entre mercados. `03/04/2026` es el 4 de marzo en EE. UU., el 3 de abril en la mayor parte de Europa y Latinoamérica, y de nuevo el 3 de abril en un orden distinto (2026/04/03) en Japón y China. No existe un formato solo numérico seguro salvo ISO 8601 (`2026-04-03`), que es inequívoco pero se lee como técnico.

Reglas prácticas:

- **En prosa, escriba el mes con letra**: «3 de abril de 2026» o «April 3, 2026» según la convención del locale. Inequívoco en todas partes y se lee con naturalidad.
- **En tablas e interfaces compactas, use ISO 8601** o un formateador consciente del locale; nunca codifique a mano `MM/DD/YYYY`.
- **Los nombres de días y meses deben venir del locale**, no de un reemplazo de cadenas («Mon» → en alemán es «Mo»; mayo es «May» en inglés, «mai» en francés, «Mai» en alemán, «mayo» en español: el truncamiento ingenuo falla).
- **Calendarios**: los documentos del Golfo a veces combinan fechas gregorianas con hijri; Japón tiene años de era (Reiwa 8 = 2026) en contextos oficiales. El contenido web B2B puede permanecer gregoriano, pero conozca los contextos en que la documentación de sus compradores no lo hará.

## Números: los separadores no son decoración

| Mercado | 1,500,000.50 se escribe |
|---|---|
| EE. UU. / Reino Unido / China / Japón | 1,500,000.50 |
| Alemania / España / Brasil | 1.500.000,50 |
| Francia | 1 500 000,50 (espacios estrechos) |
| Suiza | 1'500'000.50 |
| India | 15,00,000.50 (agrupación por lakh) |

Los modos de fallo: su sitio en inglés muestra «1.500 kg» (un alemán lee kilo y medio, usted quiso decir 1,500), o un formulario valida `1,5` como inválido porque espera un punto. Dos reglas arreglan casi todo: **renderice los números con un formateador consciente del locale** (todo framework moderno tiene uno; los sitios Hugo pueden formatear en tiempo de compilación) y **acepte ambos separadores en los campos de entrada**, normalizando en el servidor. Para las medidas, añada siempre la unidad: un número desnudo obliga al lector a adivinar el sistema.

## Moneda: símbolo, posición y qué dólar

- **«$» son cinco monedas** (dólares de EE. UU., Canadá, Australia, Singapur, Hong Kong; y el «peso» comparte el símbolo en México y Argentina). En contextos internacionales escriba `USD 1,500` o `US$1,500`, nunca `$` a secas.
- **La posición del símbolo varía**: `$1,500` pero `1 500 €` en francés, `1.500 €` en alemán, `¥150,000`. El formateador lo sabe; las plantillas codificadas a mano no.
- **Qué moneda mostrar**: para el B2B transfronterizo, USD o EUR con una nota es estándar y honesto. Mostrar la moneda local convertida a un tipo de cambio no declarado crea otro problema: cotizaciones que no coinciden. Elija lo que elija, declárelo: «Precios en USD, EXW Shenzhen».
- **Números grandes**: los compradores indios piensan en lakhs y crores (1 crore = 10 millones); los chinos en 万 (10,000) y 亿 (100 millones). Una afirmación de «capacidad de un millón de unidades» puede funcionar mejor reformulada en la magnitud local para esos mercados.

## Unidades: elija un sistema por audiencia, muestre ambos cuando sea crítico

El mundo industrial es métrico, con una excepción gigante: las unidades habituales de EE. UU., y su persistencia en aeroespacial, petróleo y gas (especificaciones API) y algunas normas de fijaciones y roscas. Reglas que evitan los peores errores:

- **Use el sistema métrico por defecto para audiencias internacionales**; añada el imperial entre paréntesis para contenido orientado a EE. UU., no al revés.
- **Nunca convierta silenciosamente en especificaciones técnicas.** Una dimensión de 25.4 mm que nació como 1 pulgada debe decir `1″ (25.4 mm)`: el valor convertido solo pierde la información de que es un tamaño estándar, y el redondeo (25 mm ≠ 25.4 mm) ha causado disputas reales de fabricación.
- **Presión, par y energía tienen favoritos por mercado**: bar frente a psi frente a MPa, Nm frente a ft-lb, kW frente a hp (y PS en Alemania, donde 1 PS ≠ 1 hp). Siga la convención del mercado y mantenga el original entre paréntesis.
- **Temperatura**: °C en todas partes excepto EE. UU. En «recetas para la industria» (especificaciones de curado, recocido), dé ambas.

## Teléfonos, direcciones, nombres

- **Teléfono**: E.164 (`+86 755 1234 5678`) en la visualización y en los enlaces `tel:`; los campos de entrada deben aceptar `+`, espacios y ceros iniciales. Un formulario que rechaza formatos no estadounidenses es un filtro de consultas: la misma clase de fricción que señalamos en [señales de confianza](/es/news/b2b-website-trust-signals/).
- **Direcciones**: el orden de los campos varía (Japón: de mayor a menor, código postal primero; Alemania: calle y luego número). Un formulario rígido de «Dirección 1 / Ciudad / Estado / Código postal» no encaja en la mayor parte del mundo: solo «Estado» excluye la mitad de sus mercados.
- **Nombres**: un único campo «Nombre completo» supera a «Nombre/Apellido» (orden chino y japonés, dobles apellidos españoles, monónimos indonesios). Y deje pasar UTF-8: un formulario que rechaza «José» o «Müller» está fallando la misma prueba de codificación que la [pseudolocalización](/es/news/pseudolocalization-testing-guide/) existe para detectar.

## Convertirlo en sistema

Los formatos fallan en el código y las plantillas, así que arréglelos ahí:

1. **Un formateador por stack**, usado en todas partes: nada de cadenas de fecha construidas a mano.
2. **El locale gobierna el formato, el idioma gobierna las palabras**: una página en inglés para lectores alemanes (pensamiento en-de) formatea al estilo alemán; no acople ciegamente el formato al idioma de traducción.
3. **Pruebe con pseudolocales y con locales reales**: configure su navegador en de-DE y ar-EG y recorra cada tipo de página una vez.
4. **Añada los formatos a la guía de estilo de localización**, junto a las fuentes y la terminología, para que cada mercado nuevo herede las decisiones.

Nada de esto es caro; todo es visible. Los compradores perdonan una frase imperfecta; no perdonan una fecha de entrega que no pueden interpretar. Nuestro [equipo de localización](/es/services/localization/) audita los formatos como parte de cada proyecto web: [envíenos su URL](/es/contact/) y le listaremos lo que sus fechas y números están diciendo realmente.
