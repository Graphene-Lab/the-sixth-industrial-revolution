# Apéndice B --- Los proyectos tras la visión, y lectura adicional

## El laboratorio

Las tecnologías descritas a lo largo de este libro no son hipotéticas. Se están construyendo, publicando y refinando en un pequeño laboratorio de investigación, **AI Technology Graphene-Lab**, que prefiere dejar que las máquinas hablen por sí mismas. Su trabajo se publica abiertamente en GitHub, bajo licencias permisivas, precisamente para que los lectores de este libro puedan mirar, probar y --- si así lo deciden --- adoptar. Este apéndice señala al lector los repositorios reales que sustentan los capítulos anteriores, y luego algunas pocas libros y escritos para quienes quieran ir más allá, ya sea en la dirección de la máquina, de la nube, o del agente.

Todos los proyectos del laboratorio se recogen en: **https://github.com/orgs/Graphene-Lab/repositories**. A continuación se presentan los específicos que aparecen en este libro.

## Los proyectos de este libro

### AgentBridge --- el asistente agente que conoce tu negocio

**Repositorio:** https://github.com/Graphene-Lab/AgentBridge

AgentBridge es un asistente personal de IA autoalojado que automatiza el trabajo de oficina sin sacrificar la privacidad. Ejecuta sus propios agentes detrás de dos interfaces en un único proceso --- una terminal de chat a pantalla completa, y una API HTTP que habla el protocolo estándar de OpenAI, de modo que cualquier cliente compatible con OpenAI puede conducir los mismos agentes. Su idea definitoria es que las capacidades de un agente son ensamblajes compilados cargados como plugins, de modo que el agente llama al software directamente en lugar de hacerlo a través de un protocolo. Dispone de una memoria determinista y propietaria (nunca olvida los hechos, las personas y los documentos que ha manejado), se ejecuta dentro de un sandbox nativo de modo que sus acciones están acotadas y son reversibles, y puede abastecerse con la nube privada para que el conocimiento que lee nunca abandona la empresa. El laboratorio lo describe como la herramienta tras este libro --- la que hace real el "oficina a medianoche".

### CloudServer --- la nube privada, sin confianza y de conocimiento nulo

**Repositorio:** https://github.com/Graphene-Lab/CloudServer

CloudServer es la nube privada mantenida dentro de la empresa. Donde la nube pública centraliza los datos en enormes centros de datos que pueden ser leídos --- o compelidos a leer --- una nube privada y de conocimiento nulo como CloudServer mantiene los datos bajo el propio control de la empresa, de modo que la telemetría que fluye desde las máquinas nunca abandona la autoridad de la empresa y nunca es legible por un tercero. Esta es la respuesta, para la fábrica, a los fracasos de privacidad expuestos por el gran escándalo de datos de principios de la década de 2010.

### UISupportBlazor --- IA determinista para front-ends y APIs automáticos

**Repositorio:** https://github.com/Graphene-Lab/UISupportBlazor

UISupportBlazor es un proyecto pionero de IA agente para programar, pero su significado más profundo es conceptual: demuestra que un ensamblaje compilado --- la especificación exacta y completa de un backend --- puede usarse como el último prompt determinista, del que se derivan con certeza matemática las interfaces de usuario y las capas de API en lugar de adivinarse a partir de un prompt en lenguaje natural. Es el ejemplo insignia del argumento de las "dos clases de mente" (Capítulo 13) y del argumento del "ensamblaje como última verdad" (Capítulo 14): la mente determinista, donde la certeza es requerida.

### Las bibliotecas de apoyo de la IA determinista

Más allá de estos proyectos estelares, el laboratorio publica las bibliotecas de apoyo que hacen coherente todo el conjunto --- por ejemplo, las herramientas de análisis de ensamblajes (UISupportGeneric, GiraffeAI) que permiten a una máquina leer un ensamblaje compilado y derivar de él la interfaz o herramienta que necesita. Juntas, estas forman un ecosistema en lugar de un conjunto de herramientas aisladas, y ese ecosistema es lo que el libro describe en última instancia.

## La puerta de Telegram

El trabajo se muestra, no meramente se describe, en el canal de Telegram del laboratorio. El código QR en [Una nota sobre el libro](preface.md) --- y de nuevo en el [Epílogo](epilogue-the-factory-that-dreamed.md) --- lleva hasta allí. Si quieres ver la máquina que piensa, la nube que guarda su secreto, el agente que conoce tu negocio, y el humanoide que camina hacia el piso tal como son, en tiempo real, esa es la puerta.

## Lectura adicional

Para quienes deseen ampliar el horizonte más allá de este libro, algunas pocas direcciones ofrecen terreno particularmente rico. Son sugerencias, no una lista de lectura obligatoria; elige el camino que coincida con el lugar donde te encuentras.

**Sobre la historia de las revoluciones y la inteligencia.** El lector que quiera situar la sexta revolución en el largo arco encontrará mucho digno de leer en las historias de las olas anteriores --- la máquina de vapor, la línea de montaje, la computadora --- y en la historia más larga de la propia IA, con sus inviernos y sus primaveras. El patrón que esas historias revelan es la misma herramienta de decisión que ofrece este libro: conoce el patrón, y será más difícil que te engañen.

**Sobre las dos clases de mente.** La distinción entre la mente probabilística y la mente determinista es la idea más profunda de este libro, y vale la pena leerla en sus contextos originales: la teoría del cómputo y la naturaleza determinista de la compilación, por un lado; y el aprendizaje automático, por el otro. Los propios escritos del laboratorio sobre IA determinista (véase UISupportBlazor arriba) llevan esta idea más allá de lo que este libro puede, y son el siguiente paso natural para el lector que considere convincente el argumento de las dos mentes.

**Sobre la privacidad y la nube.** El lector interesado en la nube privada, sin confianza y de conocimiento nulo encontrará la discusión real en la documentación de CloudServer y en la literatura más amplia sobre criptografía, soberanía de datos, y los fracasos de la nube pública expuestos por el gran escándalo de datos. La lección --- que una nube que debes confiar no es un lugar para guardar tu futuro --- es una que vale la pena llevar mucho más allá de la fábrica.

**Sobre los agentes y su seguridad.** El lector atraído por el lado agente de la sexta revolución querrá estudiar AgentBridge y su memoria determinista y su sandbox, y la literatura más amplia sobre agentes acotados y autoalojados. El argumento de seguridad --- que un agente debe estar acotado por la estructura, no por la disciplina del prompt --- es uno que importará cada vez más a medida que los agentes asumen más trabajo real.

## La advertencia honesta

Este apéndice señala proyectos reales y publicados, y direcciones de lectura adicional; no promete que ninguno de ellos esté terminado, estable o sea fácil. Los proyectos del laboratorio están vivos y en evolución; los enlaces y los detalles pueden cambiar. El lector honesto trata este apéndice como una brújula en lugar de un mapa fijo --- una dirección para navegar según ella, verificada contra las propias fuentes. Eso, al final, es toda la lección de la sexta revolución: no te limites a confiar en el libro; ve y lee las fuentes, prueba las máquinas, y decide por ti mismo. La fábrica que piensa no es una promesa que creer; es una práctica que examinar.
