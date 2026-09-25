---
title: "Revisión de traducciones en contexto: más allá de las capturas de pantalla"
date: 2027-03-17T09:10:00+08:00
publishDate: 2027-03-17T09:10:00+08:00
category: "industry"
category_label: "Industria"
tags: ["Localización", "revisión de traducciones", "QA", "calidad de sitios web"]
keywords: ["revisión de traducciones en contexto", "revisión de traducciones de sitios web", "qa de contenido localizado"]
cover: "/images/news/in-context-translation-review.jpg"
author: "MediaLocalize Team"
summary: "La traductora de alemán revisó su trabajo en una hoja de cálculo. Se leía de maravilla. Luego se lanzó el sitio: el elegante botón de tres palabras se partió en dos líneas, la etiqueta del formulario apuntaba al campo equivocado, y 'Anmelden' (iniciar sesión) quedó en el botón de pago donde debía decir 'Registrarse'. Una traducción revisada fuera de contexto es una traducción revisada a medias: el flujo de trabajo que cierra esa brecha."
---

Un gerente de marketing recopila comentarios sobre la traducción como lo hacen la mayoría de las empresas: exporta los textos del sitio a una hoja de cálculo, se la envía al traductor o a un colega nativo, recibe correcciones cuidadosas y las implementa. Semanas después se lanza el sitio localizado, y los problemas aparecen de inmediato: botones truncados, etiquetas asociadas a los campos equivocados, un elemento de navegación que tenía sentido en una lista y ninguno en un encabezado, una frase perfecta que simplemente es demasiado larga para su tarjeta. Cada revisor hizo su trabajo. El proceso garantizó estos fallos de todos modos, porque revisaron *cadenas de texto* mientras los usuarios experimentan *pantallas*. La revisión en contexto — revisar la traducción donde realmente aparece — es la diferencia entre un texto correcto y un sitio web correcto.

## Por qué la revisión a nivel de cadena no puede funcionar

Las hojas de cálculo y los segmentos de las herramientas CAT eliminan todo lo que determina si una traducción funciona:

- **Espacio.** Un botón en inglés de 12 caracteres se convierte en 22 en alemán. En una celda, ambos se ven bien; en un botón de ancho fijo, uno se parte. El [problema de la expansión del texto](/es/news/text-expansion-translation-layout/) es invisible fuera del diseño.
- **Función.** La palabra inglesa "Register" es un sustantivo en el título de un formulario ("Warranty Register", registro de garantía) y un verbo en un botón ("Register now", regístrese ahora): palabras alemanas distintas (*Register* vs. *registrieren*). Sin ver la pantalla, el traductor adivina, y se equivoca un porcentaje de las veces. Multiplícalo por cada cadena ambigua: "Home", "Back", "Charge", "Application".
- **Composición.** Titular, subtítulo, imagen y CTA se traducen como cadenas separadas, pero se *leen* como un solo mensaje. Los desajustes de tono y las repeticiones ("Soluciones… nuestras soluciones… orientados a soluciones") solo aparecen en la página compuesta.
- **Interacción.** Las opciones de menús desplegables, los mensajes de error, las pistas de validación y los estados vacíos solo tienen sentido en el flujo donde se activan. Nadie puede revisar un mensaje de error sin saber qué lo provocó.

## Los tres niveles de contexto, y su costo

| Nivel | Qué ve el revisor | Detecta | Costo |
|---|---|---|---|
| Capturas de pantalla | Capturas estáticas por pantalla, con cadenas vinculadas a regiones de la imagen | Expansión, truncamiento, composición, la mayoría de las ambigüedades | Bajo — pero queda desactualizado y no capta interacciones |
| Revisión en sitio de pruebas | El sitio real en un entorno de pruebas; el revisor navega con una lista de verificación | Todo lo anterior + flujos, errores, comportamiento responsive | Medio — requiere una URL de pruebas y rondas de revisión |
| Edición en contexto en vivo | El revisor hace clic en el texto de la página renderizada y lo edita en el lugar, con el cambio escrito de vuelta en la TM/CMS | Todo, con el ciclo de retroalimentación más rápido | Depende de la herramienta (algunos CMS/configuraciones proxy lo soportan de forma nativa) |

El estándar práctico para la mayoría de los exportadores: **revisión en sitio de pruebas con un mapa de rutas definido**. Los revisores reciben la URL de pruebas más una lista de rutas que recorrer — página de inicio, las 5 principales páginas de producto, el formulario RFQ incluyendo un error provocado a propósito, el flujo de pago/consulta, un artículo de noticias, las páginas legales del pie — en escritorio *y* en un teléfono. De treinta a sesenta minutos por idioma, y detecta toda la clase de fallos descrita arriba.

## El flujo de trabajo que lo hace perdurar

1. **Traduce con contexto desde el principio.** Da a los traductores capturas de pantalla o acceso al sitio de pruebas *durante* la traducción, no después: las preguntas sobre ambigüedades se hacen en lugar de adivinarse. El [brief para el proveedor](/es/news/localization-vendor-brief-template/) debe especificar las fuentes de contexto por tipo de contenido.
2. **Revisa en el entorno de pruebas, no en el sitio en vivo.** Los revisores necesitan hacer clic libremente, provocar errores y redimensionar ventanas sin tocar producción — y sus hallazgos no deberían ser correcciones urgentes en un sitio en vivo.
3. **Reporta los problemas como "pantalla + cadena + sugerencia".** "Página de contacto, botón de envío, el alemán se parte — sugiero *Senden* ('enviar') en lugar de *Anfrage senden* ('enviar consulta')" es accionable en un paso; "algunos botones se ven mal" inicia una cadena de correos de una semana.
4. **Devuelve las correcciones a la memoria de traducción.** Una corrección hecha solo en la página se vuelve a romper en el siguiente ciclo de actualización; escrita de vuelta en la [TM](/es/news/translation-memory-dtp-efficiency/), queda corregida para siempre, en todas partes. Así es también como el [mantenimiento de la sincronización](/es/news/multilingual-content-sync-maintenance/) se mantiene barato.
5. **Vuelve a ejecutarla después de cada lanzamiento importante.** La revisión en contexto no es un evento de lanzamiento: incorpora una pasada abreviada al ciclo mensual de actualización, y una pasada completa a los rediseños y cambios de plantilla (que vuelven a romper los supuestos de expansión).

## Quién revisa — y la trampa que hay que evitar

La fluidez nativa es necesaria pero no suficiente. El revisor ideal combina el idioma nativo con conocimiento del *dominio*: el ingeniero de ventas de tu distribuidor alemán supera a un corrector alemán genérico en un sitio de hidráulica, porque sabe que los compradores dicen *Kugelhahn* (válvula de bola). La revisión por distribuidores y equipos locales es valiosa — con una regla de gobernanza: sus cambios pasan por tu responsable de terminología antes de publicarse, o cada mercado deriva hacia su propio vocabulario (el [problema de las ediciones en la sombra](/es/news/multilingual-content-sync-maintenance/) en forma de revisión). Y formaliza el alcance: los revisores verifican el mapa de rutas definido, no "el sitio", o la revisión nunca termina.

La calidad de la traducción se decide donde los usuarios la leen: en la pantalla, en el flujo, en el teléfono. Nuestro [equipo de localización](/es/services/localization/) integra la revisión en contexto en cada proyecto de sitio web: entornos de pruebas, listas de verificación por rutas, revisores nativos del dominio y correcciones escritas de vuelta en tu memoria de traducción. [Cuéntanos tus idiomas](/es/contact/) y te mostraremos cómo se ven tus traducciones actuales en contexto: solo los botones partidos suelen justificar la conversación.
