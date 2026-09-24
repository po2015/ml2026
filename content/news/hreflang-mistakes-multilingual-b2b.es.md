---
title: "Errores de hreflang en sitios B2B multilingües (y cómo corregirlos)"
date: 2026-10-19T16:52:00+08:00
publishDate: 2026-10-19T16:52:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["SEO", "hreflang", "sitio web multilingüe", "SEO técnico"]
keywords: ["implementación hreflang", "errores hreflang", "seo multilingüe"]
cover: "/images/news/hreflang-mistakes-multilingual-b2b.jpg"
author: "MediaLocalize Team"
summary: "Hreflang es la etiqueta más mal implementada del SEO internacional. Los seis errores que encontramos con más frecuencia en sitios B2B, cómo detectarlos y cómo corregir cada uno."
---

Hreflang es una idea simple: decirle a Google qué versión lingüística de una página mostrar a cada usuario. En la práctica, es el elemento más consistentemente mal implementado del SEO internacional: las auditorías de sitios multilingües encuentran habitualmente errores de hreflang en la mayoría de las páginas, y la propia documentación de Google lo califica como uno de los aspectos más complejos de la segmentación internacional.

El coste de equivocarse es específico del B2B: su cliente potencial alemán busca, recibe la página en inglés (o peor, su página en español) y abandona antes de leer una palabra. Este artículo cubre los seis errores que encontramos con más frecuencia en sitios B2B multilingües, cómo comprobar cada uno y su corrección.

## Qué se supone que hace hreflang

Cada página declara su propio idioma y las URL de sus alternativas:

```html
<link rel="alternate" hreflang="en" href="https://example.com/products/valve/">
<link rel="alternate" hreflang="de" href="https://example.com/de/products/valve/">
<link rel="alternate" hreflang="zh" href="https://example.com/zh/products/valve/">
<link rel="alternate" hreflang="x-default" href="https://example.com/products/valve/">
```

Google usa estas anotaciones como una pista para intercambiar las URL en los resultados de búsqueda, de modo que los usuarios lleguen a la versión en su idioma. Dos propiedades lo hacen frágil: **las anotaciones deben ser recíprocas** (si la página A apunta a la página B, la página B debe apuntar de vuelta a A), y **un solo enlace roto en el grupo puede invalidar todo el conjunto**.

## Los seis errores que encontramos con más frecuencia

### 1. Enlaces de retorno ausentes

El error más común con diferencia. La página en inglés lista todas las alternativas, pero las páginas traducidas no listan ninguna, o apuntan a una URL distinta de la que apuntaba a ellas. Sin confirmación de ambos lados, Google ignora la anotación.

**Síntoma**: Google Search Console reporta "Página alternativa con etiqueta canónica adecuada" o simplemente nunca intercambia las URL; las páginas traducidas rara vez aparecen en sus resultados de búsqueda locales.
**Corrección**: genere las anotaciones hreflang de forma centralizada —desde su CMS, su generador de sitemaps o su sistema de compilación— en lugar de editar plantillas por idioma. Cualquier página de un grupo debe listar a todos los miembros, incluida ella misma.

### 2. Códigos de idioma o región incorrectos

`en-UK` en lugar de `en-GB`, `zh-CH` en lugar de `zh-CN`, `jp` en lugar de `ja` (el código es el idioma, no el país). También es común usar un código de región solo (`de` es válido; `DE` solo como idioma no es un valor hreflang: hreflang acepta idioma o idioma+región, nunca región sola).

**Síntoma**: errores en el antiguo informe de segmentación internacional de Search Console; los rastreadores de terceros marcan valores no válidos.
**Corrección**: valide cada código contra ISO 639-1 (idioma) e ISO 3166-1 Alpha 2 (región). En caso de duda, use solo el código de idioma (`de`): se dirige a los hablantes de alemán de todo el mundo, que suele ser lo que un sitio B2B quiere de todos modos.

### 3. Hreflang en páginas no canónicas o desindexadas

La anotación apunta a una URL que redirige, que está canonicalizada a otra URL o que lleva una etiqueta `noindex`. Google sigue la canónica, encuentra una página distinta de la anotada y descarta la señal. Esto ocurre constantemente tras las migraciones de sitios, cuando las plantillas de hreflang siguen apuntando a URL antiguas.

**Síntoma**: problemas de cobertura "Duplicada, Google eligió una canónica diferente"; anotaciones descartadas silenciosamente.
**Corrección**: las URL de hreflang deben ser las URL finales, canónicas, indexables y con estado 200. Tras cualquier cambio de URL, regenere todo el conjunto de hreflang: las actualizaciones parciales son la forma en que estos errores persisten durante años.

### 4. x-default roto o ausente

`x-default` le dice a Google a dónde enviar a los usuarios cuyo idioma usted no cubre. Los sitios o bien lo omiten o bien lo apuntan a una página de selección de idioma que a su vez tiene contenido escaso. Sin él, Google adivina, y a menudo adivina mal para compradores que buscan en, digamos, francés cuando usted solo tiene inglés, alemán y chino.

**Síntoma**: la versión lingüística "equivocada" aparece para los mercados no cubiertos.
**Corrección**: apunte `x-default` a su versión global principal (normalmente el inglés). Una página de selección de idioma también es aceptable, pero solo si es una página real e indexable.

### 5. Grupos de hreflang que no coinciden con el contenido

Cada grupo debería conectar **páginas equivalentes**: la misma página de producto en cinco idiomas. Violaciones comunes: la página de "producto" alemana anotada como alternativa de la página de *categoría* inglesa, o páginas traducidas que nunca se crearon y aún así figuran en las anotaciones, devolviendo errores 404.

**Síntoma**: Google intercambia a los usuarios a una página que no coincide con la intención de su consulta: las tasas de rebote aumentan en las páginas localizadas.
**Corrección**: anote solo equivalentes verdaderos. Si una página existe solo en inglés, forma un grupo de una: liste solo a ella misma (más x-default), en lugar de apuntar a una página casi equivalente.

### 6. Señales en conflicto: hreflang frente a canónicas frente a redirecciones

La página en inglés canonicaliza a la página alemana ("básicamente son el mismo contenido"), mientras hreflang dice que son alternativas distintas. O las redirecciones por geolocalización fuerzan a los visitantes de EE. UU. a `/en/` sin importar en qué hicieron clic, lo que también redirige a Googlebot y le impide rastrear sus otras versiones lingüísticas por completo.

**Síntoma**: secciones enteras de idiomas desaparecen del índice.
**Corrección**: las canónicas deben ser autorreferenciales dentro de cada versión lingüística; deje que hreflang haga el trabajo entre idiomas. Nunca redirija de forma forzosa por IP: muestre en su lugar un banner de sugerencia de idioma descartable, para que Googlebot (que rastrea desde IP de EE. UU.) pueda seguir llegando a cada versión.

## Tabla rápida de diagnóstico

| Error | Forma más rápida de detectarlo |
|---|---|
| Enlaces de retorno ausentes | Rastree con Screaming Frog; compare las anotaciones salientes de cada página con las entrantes |
| Códigos incorrectos | Cualquier validador de hreflang, o el informe de valores no válidos del rastreo |
| Destinos no canónicos | Compruebe que cada URL anotada devuelve 200 y canonicaliza a sí misma |
| x-default ausente | Vea el código fuente de la página de inicio |
| Equivalentes que no coinciden | Revise manualmente diez grupos en distintos idiomas |
| Conflictos de redirección | Rastree desde una IP de EE. UU. y confirme que todas las versiones lingüísticas son accesibles |

## Cómo probar después de corregir

1. **Rastree todo el sitio** y exporte todas las anotaciones hreflang; los errores de reciprocidad y validez aparecen inmediatamente en el informe de la herramienta.
2. **Compruebe la cobertura de Search Console** para las secciones de idioma afectadas durante las semanas siguientes: "Rastreada, actualmente no indexada" en las páginas traducidas suele resolverse una vez que las anotaciones son coherentes.
3. **Busque como sus compradores**: use `site:example.com/de/` más un término de producto alemán desde una IP alemana (o una VPN) y verifique que aparece la URL alemana.

## Cuándo podría no necesitar hreflang

Si su sitio tiene exactamente un idioma por mercado y cada idioma vive en su propio ccTLD (`example.de` para el alemán), las señales geográficas de Google ya son fuertes: hreflang sigue siendo recomendable, pero los errores ahí son menos dañinos. Hreflang importa más en la configuración que la mayoría de los exportadores realmente usa: **un `.com` con subdirectorios de idioma**, donde Google no tiene otra forma de saber qué versión sirve a qué usuario. Si esa es su arquitectura, un hreflang correcto no es decoración opcional: es el mecanismo que pone la página correcta frente al comprador correcto.

Hacer bien las anotaciones es una tarea de ingeniería única con beneficios permanentes. Nuestro [equipo de creación de sitios web](/es/services/website-building/) implementa la arquitectura de SEO multilingüe —hreflang, estructura de URL y configuración de Search Console— como parte de cada sitio de exportación que construimos. [Envíenos su dominio](/es/contact/) y le haremos una revisión de hreflang gratuita.
