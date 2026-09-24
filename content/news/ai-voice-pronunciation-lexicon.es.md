---
title: "Pronunciación de voces IA: cómo acertar con los nombres de marca"
date: 2026-11-10T12:35:00+08:00
publishDate: 2026-11-10T12:35:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["Doblaje con IA", "TTS", "pronunciación", "SSML"]
keywords: ["control de pronunciación tts", "nombres de marca con voz ia", "léxico de pronunciación"]
cover: "/images/news/ai-voice-pronunciation-lexicon.jpg"
author: "MediaLocalize Team"
summary: "Su voz TTS pronunciará mal el nombre de su empresa, los de sus productos y las siglas de su industria. Cómo lo corrigen los léxicos de pronunciación, y cómo construir uno que escale."
---

Todo motor de texto a voz lee el texto mediante conjeturas estadísticas. Aliméntelo con "Xinwei's XW-4500 meets IP67 per ISO 20653" y escuchará su nombre de marca destrozado, su número de modelo leído como una palabra, e "ISO" deletreado o no según el humor del motor. En un video de producto de 30 segundos es vergonzoso; en una biblioteca de formación de 200 módulos es daño a la marca a escala.

La solución es un léxico de pronunciación: una correspondencia documentada y reutilizable entre sus términos escritos y cómo deben sonar. Este artículo explica cómo funciona el control de pronunciación en TTS y cómo construir un léxico que sobreviva al crecimiento.

## Por qué la pronunciación predeterminada falla con contenido empresarial

Los motores TTS aprenden la pronunciación a partir de texto general. Su contenido no es texto general:

- **Los nombres de marca inventados** no tienen entrada en el diccionario. "Zontec", "Huayu", "Wilo": el motor adivina a partir de la grafía, y adivina mal de formas distintas según el idioma.
- **Números de modelo y códigos**: "XW-4500" puede salir como "X W minus four thousand five hundred" o "exwuh forty-five hundred". Ninguna es lo que dice su equipo de ventas.
- **Siglas con convenciones**: "SQL" es "sequel" en algunos equipos y "S-Q-L" en otros; "ISO" suele deletrearse; "API" siempre. El motor no puede conocer su convención.
- **Homógrafos**: "lead" (metal frente a verbo), "read" (presente frente a pasado), "live" (adjetivo frente a verbo). El contexto suele resolverlos, hasta que no lo hace, a mitad de frase en su formación de cumplimiento.
- **Palabras extranjeras dentro de una narración en otro idioma**: una voz alemana leyendo su nombre de producto en inglés, o una voz inglesa leyendo "Porsche" o "Hannover Messe". La pronunciación entre idiomas es donde los motores son más débiles.

## Los tres mecanismos de control

### 1. Marcado SSML en línea

Speech Synthesis Markup Language incrusta instrucciones de pronunciación en el texto:

```xml
<phoneme alphabet="ipa" ph="ˈzɒn.tɛk">Zontec</phoneme>
<say-as interpret-as="characters">XW</say-as>-<say-as interpret-as="number">4500</say-as>
```

Preciso y compatible con todos los motores importantes (Amazon Polly, Google Cloud TTS, Azure, ElevenLabs, con dialectos variables). El problema: el SSML en línea vive dentro de cada guion, así que la misma corrección se pega en cientos de archivos y se actualiza cientos de veces cuando cambia.

### 2. Léxicos personalizados (la vía escalable)

La mayoría de las plataformas permite subir un diccionario de pronunciación que se aplica a cada solicitud: término → grafía fonética o IPA. Un solo archivo, mantenido de forma centralizada, se aplica a todos los guiones actuales y futuros. Es el único enfoque que escala más allá de un puñado de videos.

### 3. Reescrituras fonéticas en el texto fuente

Escribir "Zon-tek" o "eye-ess-oh" directamente en los guiones. Funciona en un apuro, pero contamina los guiones, confunde a los traductores y se rompe al cambiar de motor. Úselo solo para emergencias puntuales.

## Construir su léxico: el proceso práctico

**Paso 1: Reúna los términos.** Extraiga candidatos de sus guiones existentes, catálogos de producto y manual de estilo: nombre de la empresa, nombres de producto, números de modelo, siglas, términos técnicos, nombres de personal, topónimos. Un fabricante típico termina con 50–300 entradas.

**Paso 2: Registre la verdad.** Haga que los responsables de cada término lo digan: el director general dice el nombre de la empresa, los gerentes de producto dicen los nombres de producto, los ingenieros dicen los términos técnicos. Los desacuerdos aquí son reales (dos divisiones que pronuncian el mismo producto de forma distinta) y el léxico obliga a decidir; eso es una ventaja.

**Paso 3: Codifique por motor e idioma.** El mismo término necesita entradas separadas por motor TTS (sus conjuntos de fonemas difieren) y por idioma (su voz alemana ya pronuncia "Bosch" correctamente; su voz inglesa no). IPA donde se admita; alfabetos fonéticos específicos de la plataforma donde no.

**Paso 4: Pruebe con pares mínimos.** Renderice cada entrada en una frase corta, escuche, ajuste. Reserve dos o tres iteraciones para el 10% difícil: normalmente nombres con secuencias vocálicas inusuales.

**Paso 5: Versione como código.** El léxico vive en control de versiones, se revisa cuando se lanzan productos y se entrega con cada brief de proyecto. Nuestra [plantilla de brief para proveedores](/es/news/localization-vendor-brief-template/) lo incluye exactamente por esta razón.

## Reglas de mantenimiento del léxico

- **Un solo responsable.** Las decisiones de pronunciación por comité producen deriva; asigne el léxico a quien sea dueño de la marca o del marketing de producto.
- **Producto nuevo = entrada en el léxico antes del lanzamiento**, no después del primer video mal pronunciado.
- **Revalide al cambiar de motor o de voz.** Los léxicos no son portátiles; una actualización de voz puede cambiar cómo se renderizan sus entradas.
- **Registre cada excepción.** Las excepciones de SSML en línea deben ser raras, estar documentadas y migrarse al léxico cuando se repiten.

## Qué cuesta y qué ahorra

Un primer léxico para una empresa B2B típica toma de dos a cuatro días, incluidas las grabaciones con las partes interesadas y las pruebas. A partir de ahí elimina la fuente más común de solicitudes de revisión en contenido doblado con IA, y es la diferencia entre una narración IA que suena producida en masa y una que suena a *su* empresa. Para ver cómo encaja esto en la selección de voz en general, consulte nuestra guía sobre [cómo elegir una voz IA](/es/news/choosing-ai-voice-brand/).

Nuestro [equipo de doblaje](/es/services/localization/dubbing/) construye y mantiene léxicos de pronunciación como parte de cada proyecto de voz IA, en todas las principales plataformas TTS. [Envíenos su lista de productos](/es/contact/) y le devolveremos un léxico inicial probado con renderizaciones de muestra.
