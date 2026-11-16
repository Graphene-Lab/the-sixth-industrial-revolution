# Apéndice A --- Un glosario del nuevo lenguaje

## Por qué un glosario

El sexto revolución industrial ha traído, como toda revolución, su propio vocabulario --- palabras que una vez fueron propiedad privada de ingenieros y programadores y que ahora, en silencio, se han convertido en parte del lenguaje de la fábrica y, en muchos casos, del de la oficina. Este apéndice es una guía amable para esas palabras, definidas con lenguaje sencillo en el momento en que resultan útiles, pero recogidas aquí para que el lector pueda volver a ellas con tranquilidad. Nada de esto exige un título académico para leerlo; cada definición está escrita como si se explicara a un recién llegado reflexivo.

## Los términos

**AI agéntica.** Una IA que no se limita a responder una pregunta, sino que persigue un objetivo: planifica, actúa, observa el resultado y se ajusta, usando las herramientas que se le han dado. A diferencia de un chatbot que espera a que se le hable, un agente recibe un objetivo y descubre cómo alcanzarlo. AgentBridge es un ejemplo.

**Ensamblaje (software).** El artefacto compilado que produce un programa cuando se construye --- la especificación más detallada, exacta y sin ambigüedades de lo que hace el programa. En la IA determinista (ver más abajo), el ensamblaje se usa como fuente de verdad, en lugar de un prompt en lenguaje natural que deba interpretarse.

**Nube (pública y privada).** Una nube pública es un conjunto de grandes centros de datos propiedad de unas pocas empresas, donde almacenas y procesas datos que viven en máquinas de terceros. Una nube privada se mantiene dentro del control de una sola empresa. El sexto revolución favorece la nube privada, sin confianza y de conocimiento nulo (ver esos términos).

**IA determinista.** La IA --- o, más precisamente, el cálculo automatizado --- que produce el mismo resultado, garantizado, en cada ocasión, sin hacer conjeturas. Es la mente del compilador: exacta, trazable, demostrable. Es ideal donde una decisión debe ser cierta (seguridad, finanzas, cumplimiento) más que meramente plausible.

**IA en el borde / IA en la máquina.** Inteligencia que se ejecuta localmente, en la máquina que produce los datos o cerca de ella, en lugar de enviar los datos a una nube lejana para ser procesados. Es más rápida, más barata y más privada, porque los datos no salen del edificio.

**NPU (Unidad de Procesamiento Neural).** Un pequeño chip dentro de un procesador más grande, construido específicamente para ejecutar modelos de redes neuronales (aprendizaje automático) de forma rápida y eficiente, especialmente de manera local. Es lo que permite que una pequeña tarjeta en una máquina de la fábrica "vea" y "prediga" sin un viaje de ida y vuelta a la nube.

**SBC (Computadora de Tablero Único).** Una computadora completa en un único tablero de circuito. Los SBC inteligentes modernos se basan en procesadores ARM con una NPU integrada, a menudo son sin ventilador y pueden ser muy baratos --- lo que hace que la inteligencia en la máquina sea asequible para todos.

**Telemetría.** Datos medidos en un lugar y reportados, automática y continuamente, a otro. En una fábrica es el flujo en vivo --- vibración, temperatura, corriente, sonido, imágenes --- que reporta la condición de la máquina en tiempo real. Es la sangre de la nueva fábrica.

**Nube sin confianza.** Una nube que no tienes que *confiar* en que se comporte bien, porque su arquitectura --- no las buenas intenciones del operador --- mantiene tus datos a salvo. Tus datos se cifran con una clave que solo tú posees, de modo que la nube puede procesarlos y sincronizarlos sin poder jamás leerlos.

**Nube de conocimiento nulo.** Una nube que puede verificar y procesar tus datos sin aprender nunca los datos mismos. Opera sobre la caja fuerte cerrada, nunca sobre su contenido. Recibe su nombre de las "pruebas de conocimiento nulo" en criptografía, que demuestran que una afirmación es verdadera sin revelar nada más allá de esa verdad.

**Gemelo digital.** Un modelo digital y vivo de una cosa física --- una máquina, una línea, toda una planta --- que refleja su estado real. En el sexto revolución, un gemelo digital puede vivir localmente en el propio tablero de la máquina, siempre disponible y privado.

**Humanoide.** Un robot que se mueve sobre dos piernas como un ser humano, y por tanto puede usar un mundo construido para humanos --- puertas, escaleras, palancas a altura de mano. En el sexto revolución, el humanoide es valioso donde el trabajo es peligroso, inaccesible o desgasta el cuerpo humano, más que como reemplazo general de todo trabajador.

**Robótica / robótica colaborativa (cobotica).** La ciencia de las máquinas que se mueven y actúan. Los robots colaborativos están diseñados para trabajar *al lado* de los humanos de forma segura, percibiendo constantemente su entorno y ajustándose, en lugar de estar aislados en jaulas.

**LLM (Modelo de Lenguage Grande).** Un modelo de aprendizaje automático entrenado con cantidades enormes de texto para entender y generar lenguaje humano. Es flexible e impresionante, y puede inventar cosas --- por eso, donde importa la certeza, se combina con cálculo determinista en lugar de confiarse a sí solo.

**PLC (Controlador de Lógica Programmable).** El controlador antiguo, extraordinariamente fiable, en prácticamente todo piso de fábrica, que lee interruptores y sensores y encende y apuye salidas mediante reglas explícitas escritas por humanos. El sexto revolución no necesariamente rompe al PLC; lo complementa con una pequeña tarjeta inteligente que percibe y predice lo que el PLC nunca pudo.

**Visión / inspección visual.** Uso de una cámara más un modelo aprendido para juzgar productos automáticamente --- detectando rayones, desalineaciones, defectos --- a la velocidad de la luz y sin la fatiga de un ojo humano.

**Mantenimiento predictivo.** Predecir, a partir de las propias señales de una máquina (vibración, temperatura, sonido, corriente), cuándo una pieza está a punto de fallar, de modo que la reparación pueda programarse antes de la falla en lugar de después de ella.

**Piloto automático / la oficina a medianoche.** La visión, explorada en este libro, en la que un agente --- que conoce el negocio y trabaja dentro de una nube privada --- concluye el trabajo de oficina (contabilidad, almacén, ventas, soporte, cumplimiento) automáticamente, continuamente y de forma privada, de modo que la oficina sigue trabajando tras apagarse las luces.

**Autopoiesis.** Literalmente "self-making" (from the Greek *auto*, "self," and *poiesis*, "production"). A term coined in 1972 by Humberto Maturana and Francisco Varela for living systems, which build and repair their own components without anyone assembling them from outside. The book uses it in an extended sense: an industrial system that designs its own tools, writes its own agents, and maintains its own clouds has made itself independent of the human being, who is left outside the cycle of reproduction.

**Industry 7.0.** The framing this book uses for the sixth revolution: the seventh generation of industry, in which machines become peripherals of an internal AI, and that AI --- agentic, connected to a private cloud, knowing the business --- automates the whole enterprise into one self-coordinating loop.

## La nota honesta

Un glosario puede dar la falsa impresión de que estos términos están fijos de una vez por todas. No lo están --- el lenguaje del sexto revolución se está escribiendo mientras hablamos, y algunas de estas palabras se moverán. Lea este apéndice como un punto de partida amable, no como un veredicto. El libro que sigue definirá cada término según se necesite, en contexto, porque es en el contexto donde las palabras viven verdaderamente.
