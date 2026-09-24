---
title: "El flujo de trabajo de localización de sitios web: de la auditoría al lanzamiento"
date: 2026-10-20T08:29:00+08:00
publishDate: 2026-10-20T08:29:00+08:00
category: "industry"
category_label: "Industria"
tags: ["localización de sitios web", "flujo de trabajo de localización", "sitio web multilingüe", "gestión de proyectos"]
keywords: ["proceso de localización de sitios web", "flujo de trabajo de localización web", "pasos de un proyecto de localización"]
cover: "/images/news/website-localization-workflow.jpg"
author: "MediaLocalize Team"
summary: "Qué ocurre realmente entre 'necesitamos un sitio web en alemán' y el día del lanzamiento: las ocho fases de un proyecto profesional de localización de sitios web, con plazos realistas."
---

"Necesitamos nuestro sitio web en alemán para el segundo trimestre" suena como una solicitud de traducción. En realidad es un pequeño proyecto de ingeniería: el contenido debe auditarse, extraerse, traducirse, revisarse, reintegrarse, probarse y lanzarse sin romper el sitio que ya está generando consultas. Las empresas que entienden el flujo de trabajo obtienen presupuestos realistas y lanzamientos sin sobresaltos; las que creen que es "solo traducción" se llevan sorpresas.

Este es el flujo de trabajo en ocho fases que ejecutamos para la localización de sitios web, qué ocurre en cada fase y dónde suelen torcerse los proyectos.

## Fase 1: Auditoría y delimitación (semana 1)

Antes de traducir nada, se audita el sitio de origen:

- **Inventario de contenido**: qué páginas existen, cuáles reciben tráfico, cuáles convierten. Un sitio de 200 páginas suele tener 40 que importan: localizarlo todo es el desperdicio de presupuesto más común.
- **Evaluación técnica**: CMS y estructura de URL, cómo se almacena el contenido (base de datos, plantillas, cadenas fijas en el código), si el tema admite la escritura y la dirección del idioma de destino.
- **Inventario de recursos**: imágenes con texto incrustado, PDF, vídeos, documentos descargables: todo lo que también necesita una versión localizada.

El resultado es un documento de alcance: lista de páginas, recuentos de palabras, lista de recursos y requisitos técnicos. Todo presupuesto honesto se construye sobre esto. Si un proveedor presupuesta sin auditar, la cifra es ficción: nuestra [plantilla de brief para proveedores](/es/news/localization-vendor-brief-template/) muestra qué preparar para que esta fase vaya rápido.

## Fase 2: Correcciones de internacionalización (semanas 1–2, en paralelo)

Los problemas encontrados en la auditoría se corrigen en el sitio de origen *antes* de que empiece la traducción, porque cada corrección es más barata en un idioma que en cinco:

- Cadenas fijas en el código trasladadas a recursos traducibles
- Formatos de fecha, moneda y unidades adaptados a la configuración regional
- Diseño ajustado para tolerar una expansión de texto del 30 % (alemán) y la representación de derecha a izquierda (árabe)
- Formularios corregidos para aceptar nombres, direcciones y números de teléfono internacionales

Saltarse esta fase es la razón por la que los sitios traducidos se entregan con botones cortados y mensajes de error en inglés.

## Fase 3: Glosario y guía de estilo (semana 2)

Dos documentos pequeños evitan la mayoría de las discusiones de calidad posteriores:

1. **Glosario terminológico**: sus nombres de producto, términos técnicos y vocabulario del sector con traducciones aprobadas, especialmente los términos que deben permanecer en inglés (nombres de marca, números de modelo) o seguir las convenciones del mercado.
2. **Guía de estilo**: tono (el Sie formal frente al du informal en alemán), formatos de números y fechas, cómo manejar frases de marketing intraducibles, requisitos de redacción legal.

Esta es la fase que los clientes más a menudo quieren saltarse y más a menudo desearían no haberse saltado. Quince términos acordados ahora ahorran tres rondas de revisión después.

## Fase 4: Traducción (semanas 2–5)

El contenido pasa a un sistema de gestión de traducción donde los lingüistas trabajan con memoria de traducción (TM): los segmentos traducidos anteriormente se reutilizan, manteniendo la coherencia terminológica y reduciendo el coste en contenido repetido como especificaciones de producto y textos legales.

El método depende del tipo de contenido:

- **Páginas de marketing (inicio, presentaciones de producto)**: traducción humana profesional, a menudo con un segundo lingüista revisando: este texto vende, y una redacción torpe aquí cuesta consultas.
- **Contenido de cola larga (archivos de noticias, preguntas frecuentes, documentación)**: la [traducción automática con postedición (MTPE)](/es/news/what-is-mtpe-post-editing/) suele ser el equilibrio correcto entre coste y calidad.
- **Nunca traducción automática en bruto** en páginas de cara al comprador; la diferencia de calidad es visible para cualquier hablante nativo.

## Fase 5: Revisión y QA lingüístico (semanas 4–6)

El contenido traducido se revisa en contexto: en un entorno de pruebas o en capturas de pantalla, no en una hoja de cálculo. Los revisores comprueban:

- Terminología contra el glosario
- Registro y tono según la guía de estilo
- Ajuste en contexto: ¿esa etiqueta de navegación sigue teniendo sentido con su longitud real, en su posición real?
- Números, unidades, enlaces y referencias cruzadas intactos

La revisión del lado del cliente, por su distribuidor regional o su equipo de ventas, encaja aquí. Dé a los revisores el glosario y una fecha límite; un "échale un vistazo" sin plazo es donde los proyectos se estancan durante meses.

## Fase 6: Integración y maquetación (semanas 5–6)

Las traducciones aprobadas vuelven al sitio. Esto es trabajo de ingeniería, no de copiar y pegar:

- Expansión del texto gestionada por componente: botones, navegación, tablas, formularios
- Fuentes verificadas para la escritura de destino (CJK, árabe, cirílico): vea nuestra [guía de tipografía multilingüe](/es/news/multilingual-dtp-typography-guide/)
- Imágenes, capturas de pantalla y documentos descargables localizados sustituidos
- Anotaciones hreflang, metatítulos y metadescripciones localizados, y selector de idioma conectados

## Fase 7: Pruebas funcionales y lingüísticas (semanas 6–7)

El sitio de pruebas recibe dos pasadas en paralelo:

- **Funcional**: cada formulario se envía, cada enlace resuelve, la búsqueda funciona con entrada no latina, el selector de idioma conserva la página actual, los flujos de compra o consulta se completan en cada idioma.
- **Lingüística**: hablantes nativos recorren recorridos de usuario reales buscando truncamientos, problemas de codificación (mojibake), fragmentos en idiomas mezclados y cadenas sin traducir.

Probar solo en el idioma de origen y asumir que el resto funciona es el fallo clásico: los diseños árabes y los campos de entrada CJK se rompen de formas que las pruebas en inglés nunca revelan.

## Fase 8: Lanzamiento y poslanzamiento (semanas 7–8)

El lanzamiento es aburrido a nivel de DNS si las fases anteriores se hicieron bien. El trabajo se traslada a la búsqueda:

- Enviar los sitemaps localizados a Google Search Console (y a Bing, Yandex o Naver donde corresponda)
- Verificar que los grupos de hreflang resuelven correctamente
- Supervisar la indexación de la nueva sección de idioma durante 2–4 semanas
- Configurar vistas de analítica por idioma para que el rendimiento de cada mercado sea visible desde el primer día

## Plazos realistas

| Tamaño del sitio | Idiomas | Duración típica |
|---|---|---|
| 20–40 páginas | 1 idioma | 4–6 semanas |
| 20–40 páginas | 3–4 idiomas | 6–8 semanas (las fases se paralelizan) |
| Más de 100 páginas con documentos y descargas | 1 idioma | 8–12 semanas |

Los plazos urgentes son posibles, reduciendo el alcance, no saltándose el QA. Localizar bien 15 páginas centrales supera a 60 páginas mal localizadas, y el resto puede seguir en una segunda oleada.

## Dónde se tuercen los proyectos

Los modos de fallo son consistentes entre empresas: presupuestar sin auditoría, traducir antes de las correcciones de internacionalización, ningún glosario, revisión sin plazos y pruebas solo en inglés. Cada uno de ellos es un problema de flujo de trabajo, no de traducción, y por eso el flujo de trabajo es lo que hay que evaluar al elegir un proveedor.

Si está planificando un sitio multilingüe, nuestro [equipo de localización](/es/services/localization/) ejecuta exactamente este flujo de trabajo y puede delimitar su proyecto a partir de una auditoría gratuita: [inicie la conversación](/es/contact/), respondemos en un día hábil.
