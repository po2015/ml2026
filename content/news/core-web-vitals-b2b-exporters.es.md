---
title: "Core Web Vitals para exportadores B2B: una guía no técnica"
date: 2027-03-15T10:50:00+08:00
publishDate: 2027-03-15T10:50:00+08:00
category: "industry"
category_label: "Industria"
tags: ["Exportación B2B", "velocidad del sitio web", "SEO", "Core Web Vitals"]
keywords: ["core web vitals", "velocidad del sitio web seo", "rendimiento de sitios web b2b"]
cover: "/images/news/core-web-vitals-b2b-exporters.jpg"
author: "MediaLocalize Team"
summary: "Tu sitio carga en 1.2 segundos en la oficina de Shenzhen — y en 9 segundos para un comprador en Lagos con Wi-Fi de hotel. Las Core Web Vitals de Google miden la segunda experiencia, no la primera, y deciden silenciosamente si tus páginas posicionan y si los compradores móviles se quedan. Las tres métricas, traducidas a términos de negocio."
---

El nuevo sitio web de un exportador se lanza. En la oficina, vuela. La demo de la agencia fue impecable. Seis meses después, el tráfico orgánico del Sudeste Asiático y África es un tercio de lo proyectado, y la tasa de rebote en móvil es del 70%. El diagnóstico, cuando alguien por fin lo hace: el sitio tarda entre 8 y 11 segundos en volverse usable en un teléfono de gama media con una conexión 4G en Yakarta o Nairobi — exactamente los mercados para los que se construyó. Google lo había notado mucho antes que el equipo de ventas. Las Core Web Vitals son la forma en que Google mide lo que experimentan tus *compradores*, y para los exportadores, la brecha entre "rápido en la sede" y "rápido en el mercado objetivo" es donde se pierden posicionamientos y consultas.

## Las tres métricas en lenguaje sencillo

Las Core Web Vitals son tres números que Google mide desde los navegadores de usuarios reales (usuarios de Chrome que visitan tu sitio), no desde pruebas de laboratorio:

| Métrica | Qué mide | Traducción de negocio | Umbral "bueno" |
|---|---|---|---|
| **LCP** (Largest Contentful Paint) | Cuándo aparece el contenido principal | Cuánto tiempo mira el comprador una página en blanco o parcial | ≤ 2.5 s |
| **INP** (Interaction to Next Paint) | Qué tan rápido reacciona la página a toques/clics | Si el sitio se siente receptivo o roto al tocarlo | ≤ 200 ms |
| **CLS** (Cumulative Layout Shift) | Cuánto salta el diseño mientras carga | Si los botones se mueven justo cuando el comprador intenta tocarlos | ≤ 0.1 |

Las páginas que pasan las tres obtienen una ventaja (modesta) de posicionamiento y, lo más importante, *se sienten* profesionales. Las que fallan sufren dos veces: una pequeña penalización directa de posicionamiento y una grande indirecta — los compradores que se van antes de que la página termine de cargar no pueden convertir, y sus rebotes le dicen a Google que la página no satisfizo.

## Por qué los exportadores fallan estas pruebas por defecto

Tres razones estructurales, todas corregibles:

**1. Distancia.** Tu servidor está en China (o con un hosting local); tus compradores están en São Paulo, Riad, Lagos, Varsovia. Cada solicitud cruza océanos: 200–400 ms de latencia por ida y vuelta, y una página necesita docenas de idas y vueltas. La solución es la [disciplina de CDN y caché en el borde](/es/news/export-website-speed-cdn-performance/): servir el sitio desde nodos físicamente cercanos a tus compradores. Solo esto suele reducir el LCP a la mitad en mercados distantes.

**2. Páginas pesadas.** El video del recorrido por la fábrica reproduciéndose automáticamente a 40 MB, las fotos de producto de 5 MB sin comprimir, el plugin de slider que carga seis bibliotecas de JavaScript. Los compradores con teléfonos Android de gama media — el dispositivo dominante en la mayoría de los mercados de exportación emergentes — experimentan esto como una pantalla congelada. Las soluciones no son glamurosas: comprimir y redimensionar imágenes (servir WebP, dimensionadas para el dispositivo), carga diferida de los medios bajo el pliegue, aplazar los scripts no críticos, eliminar el video con reproducción automática o convertirlo en una imagen de portada con botón de reproducción.

**3. Inestabilidad del diseño por elementos que cargan tarde.** Los banners de cookies, los widgets de chat, las fuentes web y los espacios de imagen sin dimensiones empujan el contenido hacia abajo a medida que cargan — eso es CLS, y en una conexión lenta significa que el botón "Contáctanos" literalmente esquiva el dedo del comprador. Reservar espacio para cada elemento dinámico (dimensiones fijas, ajustes de font-display, marcadores de posición para banners) lo elimina.

## Dónde ver tus números reales

No necesitas confiar en la experiencia de tu oficina ni en la demo de la agencia:

- **Google Search Console → informe Core Web Vitals**: tus datos de campo reales, por grupo de páginas, móvil y escritorio — los números que usa Google. Esto pertenece a la [rutina mensual de Search Console](/es/news/google-search-console-exporters/).
- **PageSpeed Insights** (pagespeed.web.dev): ejecuta cualquier URL; la sección superior muestra datos de usuarios reales ("esto es lo que experimentan tus visitantes"), la inferior una simulación de laboratorio útil para diagnosticar causas.
- **La prueba manual honesta**: abre tu sitio en un teléfono de gama media, con datos móviles y la caché vacía — idealmente a través de una VPN con salida en un mercado objetivo. Si tú no esperarías, un comprador tampoco.

Observa el patrón que suelen encontrar los exportadores: **la página de inicio en inglés pasa (el marketing se llevó el presupuesto de optimización) mientras las versiones en otros idiomas y las páginas de producto profundas fallan** (heredaron todas las decisiones pesadas de la plantilla y no recibieron atención). Google evalúa por tipo de página; una página de inicio que pasa no protege a las páginas de producto que fallan de [posicionar mal para tus palabras clave de cola larga](/es/news/industrial-long-tail-keywords/).

## El orden de corrección que se recupera más rápido

1. **CDN delante de todo** — la mayor ganancia individual para mercados distantes; normalmente es un cambio de configuración, no una reconstrucción.
2. **Disciplina de imágenes** — comprimir, redimensionar, formatos modernos; en la mayoría de los sitios B2B las imágenes son el 60–80% del peso de la página.
3. **Elimina o aplaza los scripts que bloquean el renderizado** — widgets de chat, etiquetas de analítica y bibliotecas de sliders cargadas en el encabezado de la página; la mayoría puede cargar después del contenido.
4. **Reserva espacio en el diseño** — dimensiones en cada imagen e incrustación; marcadores de posición para banners y widgets.
5. **Luego vuelve a medir en un mes** — los datos de campo son una ventana móvil de 28 días, así que las mejoras aparecen gradualmente, y los [números de rebote e interacción de GA4](/es/news/ga4-export-website-metrics/) confirman el efecto de negocio antes que Search Console.

Las Core Web Vitals no son una métrica de vanidad de TI; son la expresión técnica de "¿respeta tu sitio el tiempo de un comprador ocupado?" — medida donde el comprador realmente está. Nuestro [equipo de construcción de sitios web](/es/services/website-building/) construye sitios de exportadores que pasan las tres vitales desde los mercados objetivo por defecto: entrega en el borde, medios disciplinados, diseños estables. [Envíanos tu URL](/es/contact/) y te diremos qué experimentan hoy los compradores en tus tres principales mercados.
