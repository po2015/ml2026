---
title: "Pseudolocalización: pruebe antes de traducir"
date: 2026-11-09T11:59:00+08:00
publishDate: 2026-11-09T11:59:00+08:00
category: "industry"
category_label: "Industria"
tags: ["localización", "pseudolocalización", "pruebas", "internacionalización"]
keywords: ["pruebas de pseudolocalización", "pseudolocalización", "pruebas i18n"]
cover: "/images/news/pseudolocalization-testing-guide.jpg"
author: "MediaLocalize Team"
summary: "Simule la traducción de su interfaz antes de pagar por la traducción real. La pseudolocalización detecta roturas de diseño, cadenas fijas en el código y errores de codificación mientras corregirlos no cuesta nada."
---

Una verdad incómoda sobre los proyectos multilingües: la mayoría de los errores no está en la traducción. Está en su código y en sus diseños: cadenas en inglés fijas en el código, botones que cortan el texto alemán, formularios que rechazan nombres con acentos, plantillas que destrozan el árabe. Descubrir estos problemas después de pagar la traducción a cinco idiomas significa corregirlos cinco veces.

La pseudolocalización existe para encontrar estos errores primero, gratis. Es una traducción simulada: su texto en inglés se transforma mecánicamente para imitar lo que hará la traducción real (se alarga, se acentúa, se envuelve entre corchetes) y se ejecuta en su interfaz real. Lo que se rompe ahora se habría roto en producción.

## Qué hace realmente la pseudolocalización

Una transformación típica de pseudolocalización convierte:

`Save changes` → `[Šàṽé çħàñğéš~~~ ąć]`

Tres cosas ocurren en esa única cadena:

1. **Sustitución de caracteres**: las vocales reciben versiones acentuadas (à, ṽ, é). Esto expone al instante los problemas de codificación: si su sistema maneja mal UTF-8, estos caracteres se muestran como `Ã©` o `?`.
2. **Expansión**: la cadena crece un 30–40%, simulando la longitud del texto en alemán, ruso o español. Los botones, menús, tablas y cuadros de diálogo muestran de inmediato si tienen espacio.
3. **Marcadores de límite**: los corchetes (aquí `[` y `ąć]`) envuelven cada cadena. El texto truncado pierde su marcador de cierre, de modo que las cadenas cortadas se ven a simple vista. Las cadenas concatenadas (dos fragmentos traducidos por separado y unidos) muestran dos marcadores en una misma etiqueta, lo que expone cadenas que serán imposibles de traducir correctamente.

Algunas configuraciones añaden también un **modo de espejo** que invierte la dirección del diseño para hacer una prueba rápida de la renderización de derecha a izquierda para árabe y hebreo antes de tener texto árabe real.

## Qué detecta (con ejemplos reales)

- **Cadenas fijas en el código**: cualquier texto que permanezca en inglés durante una ejecución pseudolocalizada nunca fue externalizado; los traductores nunca lo verán y se publicará en inglés en su producto alemán. Es el hallazgo más común con diferencia.
- **Texto cortado o superpuesto**: elementos de lista de altura fija, navegación de ancho fijo, tablas dimensionadas para encabezados en inglés.
- **Concatenación**: `"Your order" + status + "was received"` produce un orden de palabras que solo funciona en inglés; los marcadores de pseudolocalización revelan cada caso.
- **Fallos de codificación**: caracteres acentuados que se convierten en mojibake en correos, PDF, exportaciones o idas y vueltas a la base de datos.
- **Lagunas de fuentes**: los glifos faltantes aparecen como cuadros (tofu) mucho antes de que una cadena CJK o cirílica real llegue a la pantalla.
- **Formato ciego a la configuración regional**: fechas, monedas y números fijados a un solo formato.
- **Confusión de identificadores de cadenas**: claves duplicadas o reutilizadas donde una misma cadena fuente en inglés sirve para dos contextos; aceptable en inglés, incorrecto en idiomas que necesitan dos traducciones distintas.

## Cómo ejecutarla

1. **Genere la pseudoconfiguración regional.** La mayoría de los entornos tiene herramientas: opciones de pseudolocale en bibliotecas i18n (i18next, FormatJS), pseudolocalización integrada en Crowdin/Phrase/Lokalise, o scripts de transformación sencillos para sitios estáticos. Para un [sitio estático tipo Hugo](/es/news/website-localization-workflow/), un script que transforme sus archivos de contenido es suficiente.
2. **Añádala como una configuración regional real** (`en-XA` es el código convencional de pseudolocale) para que todo su flujo de idiomas (enrutamiento, respaldos, formato) se ejercite, no solo las cadenas.
3. **Recorra los flujos de usuario reales.** Registro, pago, formularios, estados de error, correos, exportaciones a PDF, búsqueda con entradas pseudolocalizadas. Las capturas de pantalla por página superan a las comprobaciones puntuales.
4. **Registre cada defecto en dos grupos**: problemas de código (cadenas fijas, concatenación, codificación) y problemas de diseño (recortes, desbordamiento, dirección). Los corrigen personas distintas.
5. **Corrija y repita.** La pseudolocalización es lo bastante barata como para ejecutarla en CI; algunos equipos la usan como condición para publicar.

## Cuándo ejecutarla

Cuanto antes mejor, pero hay tres momentos que importan más:

- **Antes del primer proyecto de traducción**: las correcciones aquí son de un solo idioma. Una vez iniciada la traducción, cada corrección de código corre el riesgo de invalidar cadenas traducidas.
- **Después de grandes cambios de interfaz**: las pantallas y componentes nuevos reintroducen cadenas fijas constantemente.
- **Antes de añadir un nuevo alfabeto o dirección**: primer idioma CJK, primer idioma RTL; ejecute la pseudolocalización primero, siempre.

Los equipos que omiten la pseudolocalización no omiten los errores; los descubren durante el control de calidad lingüístico, cuando las correcciones cuestan retraducción, o en producción, cuando cuestan clientes. Una pasada de pseudolocalización en un sitio web B2B típico toma a un ingeniero uno o dos días y suele sacar a la luz decenas de problemas, cada uno de los cuales habría sido más caro después.

Si está planificando un despliegue multilingüe y quiere saber qué se romperá antes de gastar en traducción, nuestro [equipo de localización](/es/services/localization/) incluye la revisión de internacionalización en cada proyecto web: [empiece con una auditoría](/es/contact/) y ejecutaremos la pseudolocalización en su sitio como parte de la evaluación.
