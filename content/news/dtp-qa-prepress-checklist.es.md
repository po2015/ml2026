---
title: "QA de DTP: la lista de verificación de preprensa para archivos traducidos"
date: 2027-03-24T10:36:00+08:00
publishDate: 2027-03-24T10:36:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["DTP", "aseguramiento de calidad", "preprensa", "producción impresa"]
keywords: ["aseguramiento de calidad dtp", "lista de verificación preprensa traducción", "qa de impresión de archivos traducidos"]
cover: "/images/news/dtp-qa-prepress-checklist.jpg"
author: "MediaLocalize Team"
summary: "El catálogo en árabe volvió de la imprenta con los números de teléfono invertidos. El índice del manual en alemán apuntaba a páginas que ya no existían. Ambos archivos habían sido 'revisados' — por alguien que miró la pantalla, no el PDF listo para imprenta. El QA de preprensa para documentos traducidos es una disciplina propia: la lista de verificación que detecta lo que la revisión de traducción nunca ve."
---

Un distribuidor envía una foto por correo: 5 000 catálogos impresos, y en las páginas en árabe cada número de teléfono se lee al revés — el operador de DTP pegó números LTR en párrafos RTL y la dirección de párrafo de InDesign invirtió el orden de los dígitos. El archivo había pasado dos revisiones: el traductor verificó el texto (correcto), el ejecutivo de cuenta verificó el aspecto (plausible, si no se lee árabe). Lo que nadie ejecutó fue una ronda de QA de preprensa — la verificación sistemática de un documento traducido como *archivo de producción impresa*, donde vive toda una categoría de defectos que ni la revisión lingüística ni una hojeada casual pueden ver. Los archivos traducidos fallan en preprensa de maneras específicas de los archivos traducidos. Aquí está la lista de verificación, en el orden en que la ejecuta un profesional.

## Por qué los archivos traducidos necesitan su propia ronda de QA

Las verificaciones estándar de preprensa (fuentes incrustadas, imágenes en resolución, sangrado, espacio de color) aplican a todo documento. La traducción añade una segunda capa de fallas:

- **El texto cambió después de finalizado el diseño** — la expansión, la contracción y los cambios de escritura tensionan cada supuesto del layout ([reglas de expansión](/es/news/text-expansion-translation-layout/)).
- **Varios idiomas multiplican el número de archivos** — un catálogo en 6 idiomas son 6 oportunidades de que se imprima la versión equivocada de una imagen, una lista de precios o una línea legal.
- **Escrituras que el equipo de producción no sabe leer** — nadie en su equipo puede distinguir a simple vista el árabe invertido del árabe correcto, y esa es exactamente la razón por la que la lista de verificación debe ser *mecánica* (comparar valores, verificar ajustes) y no un juicio visual.

## La lista de verificación

**1. Paridad de versión e integridad.** Abra el original y el destino lado a lado: mismo número de páginas (o una razón documentada para la diferencia), cada sección presente, sin texto sin traducir olvidado en marcos — incluidos los escondites clásicos: páginas maestras, pies de página, marcos bloqueados por capa, texto en tablas y texto convertido a contornos en gráficos. Busque en el PDF palabras comunes del idioma de origen ("the", "and") para detectar rezagados de forma mecánica.

**2. Tipografía y fuentes.** Fuentes correctas para la escritura, incrustadas y con licencia (el [mapa de licencias de fuentes](/es/news/font-licensing-multilingual-publishing/) aplica exactamente en este momento); sin cuadros de glifo faltante (□) ni sustituciones por fuentes de reserva — en InDesign, los informes de verificación preliminar los señalan — y las [convenciones tipográficas](/es/news/multilingual-dtp-typography-guide/) por idioma (comillas, guiones, reglas de espaciado) verificadas contra el manual de estilo.

**3. Números, unidades e intraducibles.** Compare mecánicamente cada número entre el original y el destino: números de parte, dimensiones, tolerancias, números de teléfono, precios. Deben coincidir dígito por dígito, salvo donde el [formato local](/es/news/date-currency-format-localization/) los cambia deliberadamente (comas decimales, separadores de miles, formatos de fecha). Números de teléfono en documentos RTL: orden de dígitos verificado *marcando mentalmente el número impreso* — la historia del catálogo de arriba es esta verificación omitida.

**4. Integridad del layout.** Desbordamiento de texto (el signo más rojo en InDesign, texto truncado en el PDF), líneas viudas y huérfanas, títulos separados de su cuerpo, filas de tabla partidas entre páginas, saltos de línea que cambian el significado en tablas y fichas de especificaciones. Advertencias y avisos de seguridad verificados contra sus pasos de procedimiento, según las [reglas de DTP de manuales](/es/news/technical-document-dtp-rules/) — las restricciones de "mantener con el siguiente" no siempre sobreviven al reajuste de la traducción.

**5. Referencias cruzadas, tabla de contenido e índice.** "Ver página 38" — ¿la página 38 sigue conteniendo ese contenido en el idioma de destino? Haga clic en cada referencia cruzada del PDF; regenere y verifique la tabla de contenido; confirme que el índice se *reconstruyó* para el orden alfabético del idioma traducido, no traducido entrada por entrada (la ordenación local difiere: ä se ordena de forma distinta en alemán y en sueco).

**6. Gráficos e imágenes.** Versiones localizadas correctas de las imágenes colocadas (capturas de pantalla, diagramas con leyendas traducidas — y *no* las capturas en inglés en el manual alemán); [imágenes culturalmente apropiadas](/es/news/image-icon-color-localization/); resolución de imagen y espacio de color según la especificación de imprenta, sin cambios por el viaje de ida y vuelta de la localización.

**7. Verificaciones mecánicas específicas del idioma.** Documentos RTL: dirección de párrafo, dirección de dígitos, geometría de página espejada donde se requiera (el [DTP en árabe](/es/news/arabic-dtp-indesign-rtl/) tiene su propia lista de verificación completa). CJK: sin estilos sintetizados de negrita o cursiva falsas, reglas de ruptura de línea correctas (kinsoku), [combinación de fuentes CJK-Latin](/es/news/cjk-latin-font-pairing/) adecuada. Separación silábica activada y correcta por idioma — las palabras compuestas alemanas separadas con reglas inglesas producen errores espectaculares.

**8. Verificación de salida.** Ejecute la verificación preliminar del PDF final contra la especificación de la imprenta (fuentes incrustadas, imágenes a 300 dpi, CMYK, sangrado, ajustes de sobreimpresión) — y haga la *prueba desde el PDF final*, nunca desde el archivo de layout. El PDF es lo que se imprime; solo el PDF muestra lo que hará el rip.

## Las notas de proceso que hacen que el QA se mantenga

- **QA por idioma, no por proyecto.** La lista de verificación se ejecuta en cada archivo de idioma individualmente; "revisamos el alemán" no dice nada del árabe, que falla en lugares distintos.
- **Un lector por idioma para las verificaciones de significado.** Las verificaciones mecánicas (números, versiones, verificación preliminar) no requieren conocimiento del idioma; las de integridad del layout y de saltos de línea necesitan un lector nativo — presupueste una hora por idioma para una hojeada del PDF de prueba por un hablante nativo.
- **Registro de aprobaciones.** Quién ejecutó la lista, sobre qué versión del archivo, cuándo. Con 6 idiomas × 3 tipos de documento, lo necesitará para el segundo proyecto — y las industrias reguladas lo exigen directamente, igual que los [registros de capacitación de cumplimiento](/es/news/compliance-training-translation-accuracy/).
- **Retroalimente los defectos a las plantillas.** Cada desbordamiento, cada referencia cruzada rota es una lección de plantilla: los presupuestos de caracteres, las reglas de conservación y el dimensionado de marcos se ajustan una vez, y el siguiente idioma hereda la corrección, según la [economía de las plantillas](/es/news/translation-memory-dtp-efficiency/).

El QA de preprensa es una o dos horas por idioma frente a reimpresiones de cinco cifras y daños a la confianza del distribuidor — el seguro más barato de todo el presupuesto de localización. Nuestro [equipo de DTP](/es/services/localization/dtp/) ejecuta esta lista de verificación como estándar en cada archivo traducido, con lectores nativos por idioma y un informe de QA firmado por entregable. [Envíenos su próximo proyecto de impresión](/es/contact/) y le mostraremos lo que el informe detecta antes que la imprenta.
