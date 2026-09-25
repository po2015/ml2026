---
title: "Gestión de terminología: cómo construir una base de términos que rinde"
date: 2027-04-06T12:51:00+08:00
publishDate: 2027-04-06T12:51:00+08:00
category: "industry"
category_label: "Industria"
tags: ["Localización", "terminología", "base de términos", "calidad de traducción"]
keywords: ["gestión de terminología", "base de términos glosario traducción", "terminología multilingüe"]
cover: "/images/news/terminology-management-termbase.jpg"
author: "MediaLocalize Team"
summary: "Su ficha técnica en alemán dice Kugelhahn, su manual en alemán dice Kugelventil y su sitio web en alemán usa ambos en la misma página. Los compradores lo notan; los buscadores lo notan; sus propios ingenieros se estremecen. La terminología inconsistente es el defecto de calidad más común del contenido multilingüe — y el único que se corrige casi gratis: una base de términos, construida una vez, mantenida para siempre."
---

Un comprador lee los materiales en alemán de un fabricante: el sitio web ofrece *Kugelhähne*, la ficha técnica descargada especifica un *Kugelventil*, el manual menciona un *Absperrventil* — tres términos distintos para la misma válvula de bola. Envía un correo con una pregunta simple: "¿Son el mismo producto?" El ingeniero de ventas pasa veinte minutos desenredando terminología en lugar de vender. Multiplique esa confusión por cada documento, cada idioma, cada comprador que *no* escribió — y eso es lo que cuesta la terminología sin gestionar. Es el defecto más extendido del contenido multilingüe porque la traducción está distribuida: distintos traductores, distintos años, distintos proveedores toman decisiones localmente razonables que divergen globalmente. La solución es una base de términos (termbase) — un glosario multilingüe gestionado de sus términos — y es una de las pocas inversiones de localización que se amortiza ya en el siguiente proyecto.

## Qué es una base de términos (y qué no es)

Una base de términos no es un diccionario ni una memoria de traducción. Es una tabla curada de *sus* conceptos, con reglas:

| Campo | Ejemplo | Propósito |
|---|---|---|
| Término fuente | ball valve | El concepto canónico en inglés |
| Traducciones aprobadas | DE: *Kugelhahn*; ES: *válvula de bola*; JA: ボールバルブ | Una versión aprobada por idioma |
| Términos prohibidos | DE: ✗ *Kugelventil* (para nombres de producto) | Variantes explícitamente bloqueadas — tan valiosas como las aprobaciones |
| Definición | "Válvula de cuarto de giro que usa una bola perforada pivotante" | Desambigüa el concepto de sus parecidos (válvula de compuerta, válvula de globo) |
| Contexto/categoría gramatical | sustantivo, nombre de producto; nunca como verbo | Los traductores aplican el término correctamente, no solo literalmente |
| Estado | aprobado / en revisión / obsoleto | Gobernanza — quién decidió, y si sigue vigente |

Tres de estos campos hacen el trabajo pesado: **aprobado**, **prohibido** y **definición**. Un glosario de términos aprobados sin la lista de prohibidos les dice a los traductores lo que le gusta, pero no lo que deben dejar de hacer; sin definiciones, la misma palabra inglesa ("head", "charge", "race") recibe la traducción correcta para el concepto equivocado.

## Por qué rinde: los cuatro retornos

1. **Consistencia en todo.** Sitio web, fichas técnicas, manuales, cadenas de interfaz, videos, empaques — todos los canales toman de los mismos términos aprobados. El comprador nunca más se pregunta si su ficha técnica y su sitio web venden el mismo producto. Esta es la [señal de confianza](/es/news/b2b-website-trust-signals/) que es invisible cuando está presente y flagrante cuando falta.
2. **Traducción más barata y rápida.** Los traductores dejan de investigar los mismos 200 términos en cada proyecto y dejan de hacer las mismas preguntas. Las consultas de términos ocurren automáticamente en la herramienta CAT; los ciclos de revisión se acortan porque las disputas terminológicas desaparecen. Combinada con la [memoria de traducción](/es/news/translation-memory-dtp-efficiency/), la terminología es la otra mitad de la economía de la traducción: la TM reutiliza oraciones; la base de términos estandariza las palabras dentro de las nuevas.
3. **Alineación con el SEO.** Su sitio en alemán se posiciona por el término que los compradores alemanes realmente buscan — la base de términos es donde la investigación de palabras clave y la traducción se encuentran. Alimente su [investigación de palabras clave multilingüe](/es/news/multilingual-keyword-research-guide/) en la base de términos para que los traductores usen la variante que gana en las búsquedas, no solo una correcta.
4. **Resiliencia en la incorporación.** Nuevo traductor, nuevo proveedor, nuevo mercado — la base de términos transfiere sus decisiones acumuladas en lugar de redescubrirlas. También sobrevive a la rotación de personal *interna*: el ingeniero que conocía el vocabulario del producto se jubila, pero la base de términos no.

## Cómo construirla: la secuencia pragmática

**1. Recolecte lo que ya tiene.** Extraiga términos candidatos de los materiales existentes: nombres de producto, familias de modelos, nombres de componentes, términos de procesos, referencias a certificaciones y normas, etiquetas de interfaz. Las traducciones existentes (especialmente los [manuales bilingües](/es/news/technical-manual-translation-dtp-checklist/) y las memorias de traducción anteriores) ya contienen decisiones de facto — recójalas, conflictos incluidos.

**2. Priorice sin piedad.** Una base de 300 términos que se usa le gana a una de 5.000 que no se usa. Empiece con: nombres de producto y modelo (consistencia innegociable), los 100–200 términos técnicos centrales de su catálogo, términos con peso legal o de seguridad (advertencias, valores nominales — aplican las [exigencias de cumplimiento](/es/news/compliance-training-translation-accuracy/)) y el lenguaje de marca (eslóganes, convenciones de nombres de familias de productos).

**3. Decida con las personas correctas, una sola vez.** Cada término aprobado necesita el visto bueno de quien es dueño del concepto (ingeniería de producto) y de quien es dueño del idioma (revisor local o distribuidor). El ingeniero de ventas del distribuidor vale oro aquí — sabe lo que dicen los compradores, exactamente como en la [revisión en contexto](/es/news/in-context-translation-review/). Registre la decisión, prohíba las variantes rechazadas, siga adelante.

**4. Póngala donde trabajan los traductores.** Una base de términos en una hoja de cálculo en el disco de alguien es un museo. Pertenece al entorno de traducción (cualquier herramienta CAT consume bases TBX/CSV), reforzada por controles de QA que *marcan* los términos prohibidos automáticamente — más una versión legible para marketing, ventas y sus [briefs para proveedores](/es/news/localization-vendor-brief-template/), que deberían referenciarla explícitamente.

**5. Gobierne con ligereza, pero para siempre.** Un responsable, un proceso de cambio simple (proponer → revisar → aprobar → distribuir), una revisión trimestral de las incorporaciones. Los nuevos productos se lanzan con términos nuevos — la base de términos es la forma de que sus nombres lleguen a seis idiomas *decididos*, no improvisados por canal.

## Las notas multilingües

- **Algunos términos no deberían traducirse en absoluto** — números de modelo, muchos nombres de producto y a menudo las invenciones de marca. La base de términos registra "mantener tal cual" como decisión explícita, para que un traductor servicial no localice su numeración de piezas.
- **Los sistemas de escritura necesitan variantes explícitas**: decisiones entre chino simplificado y tradicional, transcripciones en katakana en japonés (ボールバルブ frente a un compuesto en kanji), política de transliteración para ruso y árabe.
- **La lista de prohibidos crece a partir de los tickets de soporte.** Cada pregunta de "¿son el mismo producto?" es un informe de error terminológico — recoléctelo.

La gestión de terminología es la disciplina de localización más pequeña con el mayor retorno compuesto: una tarde de decisiones por línea de producto, que rinde en cada traducción, cada documento, cada mercado, para siempre. Nuestro [equipo de localización](/es/services/localization/) construye y mantiene bases de términos de clientes como parte permanente de los programas de traducción — extracción, flujos de aprobación, integración con herramientas CAT y la gobernanza que la mantiene viva. [Cuéntenos sus idiomas y líneas de producto](/es/contact/) y empezaremos con sus 200 términos de mayor impacto.
