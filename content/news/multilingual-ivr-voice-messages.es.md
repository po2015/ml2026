---
title: "IVR multilingüe: un proyecto pequeño con gran impacto"
date: 2027-03-02T17:51:00+08:00
publishDate: 2027-03-02T17:51:00+08:00
category: "tech"
category_label: "Tecnología"
tags: ["Doblaje", "IVR", "grabación de voz", "experiencia del cliente"]
keywords: ["locución IVR multilingüe", "mensajes de voz para sistemas telefónicos", "grabación IVR en varios idiomas"]
cover: "/images/news/multilingual-ivr-voice-messages.jpg"
author: "MediaLocalize Team"
summary: "Un comprador alemán llama a su línea de exportación y escucha: un saludo en inglés vacilante, luego una larga pausa, luego un menú en alemán de calidad Google Translate grabado por el colega de alguien. Cuelga y le escribe a su competidor. El IVR son diez minutos de audio, y a menudo el primer punto de contacto con voz humana que recibe un comprador. Cómo hacer bien este pequeño proyecto."
---

El gerente de exportación dedicó seis meses al sitio web multilingüe y luego grabó él mismo el saludo en alemán del sistema telefónico, "porque son solo unas frases". Un distribuidor en Frankfurt ahora escucha: acento inglés, acentuación incorrecta en el nombre de la empresa, una opción de menú que dice *Taste drei* ("tecla tres") cuando el mensaje quiere decir "presione 3 para ventas". El sitio web decía *socio proveedor alemán profesional*; el teléfono decía *no pensamos que llamaría*. El IVR —los saludos, menús, mensajes de espera y de buzón de voz de su sistema telefónico— es el proyecto de localización más pequeño que jamás va a definir, y uno de los más escuchados. De diez a veinte mensajes, unos minutos de audio y una línea directa a sus [señales de confianza](/es/news/b2b-website-trust-signals/). Así se hace bien una sola vez.

## Por qué el IVR pega por encima de su tamaño

Tres propiedades hacen que el IVR sea desproporcionadamente importante:

- **Es secuencial e inevitable.** Los visitantes del sitio web hojean; quienes llaman *escuchan cada segundo*. En un menú telefónico no hay forma de saltarse nada: cada defecto recibe atención total.
- **A menudo es la primera "voz" de su empresa.** Los compradores que ya exploraron el sitio llaman cuando hablan en serio. El IVR es la transición del marketing a la conversación: exactamente donde la confianza debería subir, no tambalearse.
- **Los errores son inconfundibles.** Un párrafo rígido en una página web puede pasar; un hablante no nativo que pronuncia mal el idioma de quien llama, no. Los juicios sobre la calidad del audio son instantáneos y severos.

## El inventario de mensajes

Un árbol de IVR típico de una empresa exportadora tiene entre 10 y 25 mensajes. Antes de grabar nada, invéntielos:

| Tipo de mensaje | Ejemplo | Sensibilidad |
|---|---|---|
| Saludo de bienvenida | "Gracias por llamar a [Empresa]" | Máxima: primera impresión, pronunciación del nombre de marca |
| Selección de idioma | "Para español, presione 1" | Alta: debe ser en sí multilingüe o independiente del idioma |
| Opciones de menú | "Para ventas, presione 2" | Alta: la claridad determina el enrutamiento |
| Mensajes de espera/cola | "Su llamada es importante para nosotros…" | Media: se escucha repetidamente, amplificador de irritación |
| Mensaje fuera de horario | "Nuestras oficinas están cerradas en este momento…" | Alta: a menudo es el único mensaje que escuchan quienes llaman desde otras zonas horarias |
| Mensaje de buzón de voz | "Por favor, deje su mensaje…" | Media |
| Nombres y extensiones | Lectura del directorio | Media: pero los nombres deben pronunciarse correctamente |

Del inventario surgen dos reglas estructurales. Primero, **el mensaje fuera de horario importa más a los exportadores que a nadie**: con una diferencia horaria de 6 a 12 horas, una gran parte de quienes llaman del extranjero llega a él, y debe indicar su horario *en la lógica de la zona horaria de quien llama* ("9:00–18:00 hora de China, GMT+8") y ofrecer el canal asíncrono (correo electrónico, [WhatsApp/WeChat](/es/news/export-website-contact-channels/)) que realmente usarán. Segundo, ponga la **selección de idioma primero y manténgala superficial**: quien llama debe llegar a una persona o a un mensaje útil en un máximo de dos niveles de menú.

## Adaptación del guion, no traducción

Los guiones de IVR son hablados, cronometrados y de navegación: tres razones por las que la traducción literal falla:

- **Registro hablado.** "Por favor, seleccione entre las siguientes opciones" es lenguaje escrito. El alemán hablado pide *Wählen Sie* ("elija usted"); el japonés hablado pide un marco más cortés del que sugiere la fuente en inglés. Los guiones se reescriben para el oído, idioma por idioma.
- **La numeración del menú cambia el orden.** El inglés "press 1 for sales, 2 for support" se traduce palabra por palabra, pero la *ubicación de la instrucción de la tecla* varía según el idioma. Algunos idiomas ponen el dígito primero ("1 wählen für Vertrieb", "marque 1 para ventas"), otros al final. La coherencia dentro de su propio árbol importa más que igualar la formulación de la fuente.
- **Tiempos.** Los menús deben poder completarse antes de que se acabe la paciencia de quien llama: aproximadamente de 5 a 8 segundos por opción. Si el menú traducido dura un 40 % más (el alemán lo hará), reestructure el árbol en lugar de dejar que el locutor corra.

Y el detalle que todos olvidan: **el nombre de marca y los nombres de producto requieren una decisión de pronunciación por idioma**: ¿se leen en la fonología local o deliberadamente en inglés? Decídalo una vez, escríbalo en la disciplina del [léxico de pronunciación](/es/news/ai-voice-pronunciation-lexicon/) y exija que todos los mensajes lo respeten.

## Grabación: humana, IA o híbrida

La [decisión entre voz humana e IA](/es/news/ai-dubbing-vs-human-voice/) tiene una forma específica para el IVR:

- **La voz humana profesional** es la opción por defecto para los mensajes de cara al cliente: de 10 a 25 mensajes cortos es una sesión de estudio pequeña, el costo es realmente menor y el saludo carga con su marca. Use talento nativo, del país, y la *misma* voz en todo el árbol de cada idioma.
- **El [TTS neuronal](/es/news/neural-tts-ai-voice-localization/)** encaja en la cola dinámica: nombres, lectura de extensiones, consultas de estado de pedidos, todo lo que se genera a partir de datos. El TTS moderno con [dirección SSML](/es/news/ssml-ai-voice-direction/) maneja bien estos casos, y regenerar un mensaje no cuesta nada cuando el menú cambia.
- **La trampa híbrida que debe evitar**: no mezcle un saludo humano cálido con opciones de menú evidentemente sintéticas en la misma ruta de llamada: el desnivel de calidad resulta más chocante que un TTS consistente. Mantenga cada ruta de llamada en una sola calidad.

Elija lo que elija, pase los mensajes grabados por la misma [disciplina de control de calidad de audio](/es/news/dubbing-audio-qa-checklist/) que cualquier entrega de voz: sonoridad normalizada, piso de ruido limpio y —el específico del IVR— **probados en una línea telefónica real**, no en monitores de estudio. El ancho de banda telefónico se come las sibilantes y los graves; un mensaje nítido en altavoces puede sonar turbio por un auricular.

## El ángulo del mantenimiento

Los mensajes de IVR cambian: nuevas opciones de menú, horarios festivos, un departamento renombrado. Dos hábitos evitan que el audio derive: mantenga los **guiones maestros bajo control de versiones con la redacción exacta grabada** (para que las actualizaciones sean comparables y regrabables), y mantenga **la relación con la voz activa**: el mismo talento o el mismo [perfil de voz](/es/news/choosing-ai-voice-brand/) disponible para grabaciones de parche, de modo que la opción 4 del año próximo no suene como de otra empresa.

La localización de IVR es unos días de trabajo, un presupuesto modesto y una parte desproporcionada de cómo los compradores internacionales *escuchan* su empresa. Nuestro [equipo de doblaje y locución](/es/services/localization/dubbing/) cubre todo el arco: adaptación del guion por idioma, talento nativo o producción TTS, control de calidad en línea telefónica y los archivos maestros para actualizaciones sin dolor. [Envíenos su lista actual de mensajes](/es/contact/) y le devolveremos un plan de grabación por idioma en días, no en semanas.
