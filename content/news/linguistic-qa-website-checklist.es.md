---
title: "QA lingüístico para sitios web traducidos: la lista de verificación"
date: 2027-02-09T13:43:00+08:00
publishDate: 2027-02-09T13:43:00+08:00
category: "industry"
category_label: "Industria"
tags: ["localización", "QA lingüístico", "traducción de sitios web", "calidad"]
keywords: ["qa lingüístico sitio web", "lista de verificación lqa traducción", "control de calidad traducción web"]
cover: "/images/news/linguistic-qa-website-checklist.jpg"
author: "MediaLocalize Team"
summary: "La traducción era perfecta —en la hoja de cálculo. En el sitio en vivo, la navegación alemana se parte en dos líneas, la mitad de los textos alt sigue en inglés y el checkout dice 'Vielen Dank' en una página en árabe. El LQA de sitios web es una pasada distinta con su propia lista de verificación. Aquí está la que nosotros ejecutamos."
---

Un proyecto de localización termina con una entrega: archivos traducidos, revisados, aprobados. Luego el sitio sale en vivo y llega la realidad: cadenas que tenían sentido en una hoja de cálculo quedan en el contexto equivocado, un botón se trunca, la versión francesa de una página enlaza a la versión inglesa de la siguiente. Esta brecha existe porque la revisión de traducción comprueba *texto*, mientras que los usuarios experimentan *páginas*. El QA lingüístico (LQA) es la pasada en contexto que cierra la brecha: un revisor nativo recorre el sitio en vivo (o de staging) con una lista de verificación, cazando los defectos que solo existen en contexto. Aquí está la lista, en el orden en que la ejecutamos, y las decisiones de proceso que determinan si atrapa cosas o no.

## Por qué el QA de hoja de cálculo no basta

Tres clases de defectos son invisibles fuera del sitio en funcionamiento:

- **Errores de contexto**: «Home» traducido como 主页 (correcto para una página de inicio) donde en realidad es una miga de pan que significa otra cosa; «Return» como tecla del teclado vs. devolución de un producto. El traductor vio una cadena; el usuario ve una oración.
- **Errores de ensamblaje**: fragmentos traducidos unidos gramaticalmente por código — "Showing 1–10 of 247 results" («mostrando 1–10 de 247 resultados») reconstruido según el orden de palabras de cada idioma, o no reconstruido y destrozado. La [disciplina de cadenas de UI](/es/news/elearning-ui-text-expansion/) de los reproductores de cursos aplica a los sitios web exactamente igual.
- **Brechas de cobertura**: las cadenas que nadie exportó: textos alt, meta descripciones, mensajes de validación de formularios, páginas de error, plantillas de correo, PDF descargables. Cada una fue traducida *en algún lugar* o no lo fue; el LQA es donde se descubre cuál de las dos.

## La lista de verificación, pasada por pasada

Ejecútela como tres pasadas enfocadas en lugar de una difusa. Cada pasada toma aproximadamente una hora por cada 50 páginas.

**Pasada 1 — Cobertura de idioma (cualquier revisor, sin lingüística).**
Cace el contenido sin traducir: navegación, pie de página, botones, etiquetas de formularios *y* sus mensajes de error, textos alt (inspección o lector de pantalla), meta títulos/descripciones (ver código fuente o un rastreador), páginas 404/de mantenimiento, correos transaccionales disparados por un envío de formulario de prueba y activos descargables. Regla: toda cadena que un usuario pueda ver o un buscador pueda indexar está dentro del alcance. Solo esta pasada suele revelar el 60 % de los hallazgos en un primer LQA.

**Pasada 2 — Maquetación y renderizado (revisor + herramientas del navegador).**
- Truncamiento y desbordamiento: botones, elementos de menú, tarjetas, encabezados de tabla, especialmente compuestos en alemán/finés, según las [reglas de expansión](/es/news/text-expansion-translation-layout/).
- Desastres de salto de línea: titulares que se parten a mitad de palabra, palabras huérfanas en secciones hero.
- Fuentes: glifos faltantes (cuadros «tofu»), fuentes de respaldo que cambian el tono del diseño: los [problemas de combinación de fuentes](/es/news/cjk-latin-font-pairing/) hechos visibles.
- RTL donde aplique: maquetación espejada, direcciones de flechas correctas, según la [lista de verificación RTL](/es/news/rtl-website-design-arabic/).
- Números, fechas, monedas: la ambigüedad de 01/02/2027, comas decimales, separadores de miles: toda la [disciplina de formatos](/es/news/date-currency-format-localization/) verificada *renderizada*, no supuesta.

**Pasada 3 — Revisión lingüística en contexto (revisor nativo).**
- Corrección de contexto: ¿cada cadena significa lo correcto *aquí*? Botones, CTA, mensajes de error, texto legal.
- Consistencia terminológica: el mismo término de producto en todas las páginas, coincidiendo con el glosario y la [memoria de traducción](/es/news/translation-memory-dtp-efficiency/): el LQA es donde se nota la deriva de la TM.
- Registro y voz: consistencia formal/informal (Sie alemán, usted español), tono acorde a la marca.
- Enlaces: ¿los enlaces internos permanecen dentro del idioma o se fugan al inglés? ¿El selector de idioma aterriza en la página *equivalente*, no en la raíz de la sección?
- Elementos SEO: títulos/descripciones traducidos, [comportamiento hreflang](/es/news/hreflang-mistakes-multilingual-b2b/) correcto, slugs localizados donde la arquitectura los tiene.

## La escala de severidad (para que las correcciones realmente se hagan)

| Severidad | Definición | Ejemplo | Acción |
|---|---|---|---|
| **S1 bloqueante** | Significado erróneo, riesgo legal/de marca, transacción rota | El mensaje de error dice lo contrario; el precio está formateado 10× | Corregir antes del lanzamiento, sin excepciones |
| **S2 mayor** | Daño de calidad visible en páginas clave | CTA truncado en la página de inicio; texto alt en inglés en imágenes de producto | Corregir antes del lanzamiento |
| **S3 menor** | Problemas de pulido en páginas secundarias | Sinónimo inconsistente en una página de archivo del blog | Corregir en el próximo ciclo de contenido |
| **S4 sugerencia** | Preferencia del revisor, no un error | «Yo redactaría este titular de otra forma» | Registrar; decidir una vez, actualizar el glosario |

Sin severidades, los informes de LQA se convierten en listas de 300 ítems que nadie atiende. Con ellas, la decisión de lanzamiento es mecánica: cero S1/S2 abiertos = publicar.

## Reglas de proceso que hacen que funcione

1. **LQA en staging, en el CMS real**, no en capturas de pantalla. Los revisores deben hacer clic, enviar formularios y provocar estados de error. El QA por capturas pierde la mitad interactiva del sitio.
2. **Los hallazgos vuelven a los activos, no solo a las páginas.** Cada corrección terminológica actualiza el glosario y la TM; cada truncamiento recurrente actualiza los presupuestos de cadenas del sistema de diseño; cada nota de contexto omitida mejora el [brief al proveedor](/es/news/localization-vendor-brief-template/) para la próxima vez. De lo contrario, paga por los mismos hallazgos en cada lanzamiento.
3. **Un revisor por idioma con autoridad.** El LQA por comité se estanca; un revisor nativo con poder para marcar S1–S4 lo mantiene en días, no semanas.
4. **Reejecute las pasadas baratas en cada despliegue.** La pasada 1 (cobertura) y la mitad de maquetación de la pasada 2 pueden automatizarse en gran parte con un rastreador y comparación de capturas: ejecútelas en cada lanzamiento; reserve a los lingüistas humanos para la pasada 3.
5. **Presupuéstelo.** El LQA cuesta entre el 10 y el 15 % de la traducción y atrapa los defectos que de otro modo encontrarían sus *clientes*, en público. Es la misma lógica de seguro que la [pseudolocalización](/es/news/pseudolocalization-testing-guide/) río arriba: certeza barata contra vergüenza cara.

La traducción hace su sitio multilingüe; el LQA lo hace *creíble*. Nuestro [equipo de localización](/es/services/localization/) integra el LQA en contexto en cada proyecto web: revisores nativos, hallazgos triados por severidad y correcciones que fluyen de vuelta a su glosario y su TM. [Envíenos la URL de su staging](/es/contact/) y le ejecutaremos la pasada 1 como auditoría gratuita.
