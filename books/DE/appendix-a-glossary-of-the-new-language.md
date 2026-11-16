# Anhang A --- Ein Glossar der neuen Sprache

## Warum ein Glossar

Die sechste industrielle Revolution hat, wie jede Revolution, ihre eigene Sprache mitgebracht --- Wörter, die einst das Privateigentum von Ingenieuren und Programmierern waren und nun stillsam Teil der Sprache der Fabrik und in vielen Fällen der Sprache des Büros geworden sind. Dieser Anhang ist ein einfühlsamer Leitfaden zu diesen Wörtern, die im Moment, in dem sie nützlich werden, in verständlicher Sprache definiert werden, aber hier zusammengetragen sind, damit der Leser jederzeit und in Ruhe in sie einkehren kann. Hier ist nichts zu lesen, für das ein akademischer Grad erforderlich wäre; jede Definition ist so geschrieben, als würde man einem nachdenklichen Neuling erklärt.

## Die Begriffe

**Agentic AI.** Eine KI, die nicht nur eine Frage beantwortet, sondern ein Ziel verfolgt: sie plant, handelt, beobachtet das Ergebnis und passt sich an, wobei sie die Werkzeuge nutzt, die ihr übergeben wurden. Im Gegensatz zu einem Chatbot, der darauf wartet, angesprochen zu werden, wird ein Agent ein Ziel übergeben und findet heraus, wie es zu erreichen ist. AgentBridge ist ein Beispiel hierfür.

**Assembly (Software).** Das kompilierte Produkt, das ein Programm bei seinem Erzeugen hervorbringt --- die detaillierteste, exakte und mehrdeutige Spezifikation dessen, was das Programm tut. In der deterministischen KI (siehe unten) wird die Assembly als Wahrheitsquelle verwendet, statt eines natürlichen Sprachprompt, das interpretiert werden muss.

**Cloud (öffentlich und privat).** Eine öffentliche Cloud ist eine Ansammlung riesiger Rechenzentren, die wenigen Unternehmen gehören, wo Sie Daten speichern und verarbeiten, die auf den Maschinen anderer laufen. Eine private Cloud bleibt innerhalb der Kontrolle eines einzigen Unternehmens. Die sechste Revolution bevorzugt die private, vertrauenslose, nulldatenschutzende Cloud (siehe diese Begriffe).

**Deterministische KI.** KI --- oder genauer gesprochen, automatisierte Berechnung --- die jedes Mal dasselbe, garantierte Ergebnis hervorbringt, ohne jedes Raten. Sie ist der Geist des Compilers: exakt, nachvollziehbar, beweisbar. Sie ist dort ideal, wo eine Entscheidung sicher sein muss (Sicherheit, Finanzen, Compliance) statt bloß plausibel.

**Edge AI / On-Machine AI.** Intelligenz, die lokal läuft, auf oder nahe der Maschine, die die Daten erzeugt, statt die Daten an eine ferngelegene Cloud zu senden, um dort verarbeitet zu werden. Sie ist schneller, billiger und privater, weil die Daten das Gebäude nicht verlassen.

**NPU (Neural Processing Unit).** Ein kleiner Chip innerhalb eines größeren Prozessors, der eigens gebaut wurde, um neuronale Netze (Machine-Learning-)Modelle schnell und effizient zu laufen zu lassen, besonders lokal. Es ist dasjenige, was einer kleinen Karte an einer Fabrikmaschine ermöglicht, zu "sehen" und zu "vorhersagen", ohne eine Rückreise zur Cloud.

**SBC (Single-Board Computer).** Ein vollständiger Computer auf einer einzigen Leiterplatte. Die modernen intelligenten SBCs basieren auf ARM-Prozessoren mit einem eingebauten NPU, sind oft lüfterlos und können sehr billig sein --- was es on-machine-Intelligenz für alle erschwinglich macht.

**Telemetrie.** Daten, die am einen Ort gemessen und automatisch und fortlaufend an einen anderen übermittelt werden. Auf einer Fabrik ist sie der Live-Stream --- Vibration, Temperatur, Strom, Klang, Bilder --- der den Zustand der Maschine in Echtzeit berichtet. Sie ist das Blut der neuen Fabrik.

**Vertrauenslose Cloud.** Eine Cloud, die man nicht *vertrauen* muss, um sich verhaltensgemäß zu äußern, weil ihre Architektur --- nicht die guten Absichten des Betreibers --- Ihre Daten schützt. Ihre Daten sind mit einem Schlüssel verschlüsselt, den nur Sie halten, sodass die Cloud sie verarbeiten und synchronisieren kann, ohne je in der Lage zu sein, sie zu lesen.

**Nulldatenschutzende Cloud.** Eine Cloud, die Ihre Daten verifizieren und verarbeiten kann, ohne je die Daten selbst zu erfahren. Sie arbeitet am verschlossenen Safe, nie am Inhalt. Benannt nach den "Nulldatenschutz-Beweisen" (zero-knowledge proofs) der Kryptographie, die eine Aussage wahr beweisen, ohne jenseits dieser Wahrheit irgendetwas preiszugeben.

**Digitaler Zwilling.** Ein lebendiges, digitales Modell einer physischen Sache --- einer Maschine, einer Linie, einer ganzen Anlage --- das ihren echten Zustand spiegelt. Auf der sechsten Revolution kann ein digitaler Zwilling lokal auf der eigenen Karte der Maschine leben, stets verfügbar und privat.

**Humanoid.** Ein Roboter, der sich auf zwei Beinen so bewegt wie ein Mensch und daher eine Welt nutzen kann, die für Menschen gebaut wurde --- Türen, Treppen, Hebel in Handhöhe. Auf der sechsten Revolution ist der Humanoid dort wertvoll, wo die Arbeit gefährlich, unzugänglich ist oder den menschlichen Körper abnutzt, statt als allgemeiner Ersatz für jeden Arbeiter.

**Robotik / kollaborative Robotik (Cobotik).** Die Wissenschaft der Maschinen, die sich bewegen und handeln. Kollaborative Roboter sind darauf ausgelegt, sicher *neben* Menschen zu arbeiten, fortlaufend ihre Umgebung wahrnehmend und sich anpassend, statt von Menschen abgekoppelt zu werden.

**LLM (Large Language Model).** Ein Machine-Learning-Modell, das auf enormen Textmengen trainiert wurde, um menschliche Sprache zu verstehen und zu erzeugen. Sie ist flexibel und beeindruckend, und sie kann Dinge erfinden --- weshalb sie dort, wo Sicherheit zählt, mit deterministischer Berechnung kombiniert wird statt allein vertraut zu werden.

**PLC (Programmable Logic Controller).** Der alte, außergewöhnlich zuverlässige Controller auf fast jedem Fabrikboden, der Schalter und Sensoren liest und Ausgänge nach ausdrücklichen, menschlich geschriebenen Regeln ein- und ausschaltet. Die sechste Revolution zerbricht die PLC nicht unbedingt; sie ergänzt sie durch eine kleine intelligente Karte, die wahrnimmt und vorherzusagen weiß, was die PLC nie konnte.

**Vision / visuelle Prüfung.** Die Nutzung einer Kamera plus eines gelernten Modells, um Produkte automatisch zu beurteilen --- Kratzer, Fehlausrichtungen, Mängel aufspürend --- auf der Geschwindigkeit des Lichts und ohne die Müdigkeit eines menschlichen Auges.

**Prädiktive Instandhaltung.** Das Vorhersagen, aus den eigenen Signalen einer Maschine (Vibration, Temperatur, Klang, Strom), wann sich ein Teil dem Ausfall nähert, sodass die Reparatur geplant werden kann, bevor der Ausfall stattfindet, statt danach.

**Autopilot / das Büro um Mitternacht.** Die Vision, die in diesem Buch erkundet wird, in der ein Agent --- der das Geschäft kennt und innerhalb einer privaten Cloud arbeitet --- die Büroarbeit (Buchhaltung, Lager, Vertrieb, Support, Compliance) automatisch, fortlaufend und privat erledigt, sodass das Büro weiterarbeitet, nachdem die Lichter ausgegangen sind.

**Autopoiesis.** Wörtlich "Selbsterzeugung" (aus dem Griechischen *auto*, "selbst," und *poiesis*, "Erzeugung"). Ein Begriff, der 1972 von Humberto Maturana und Francisco Varela für lebende Systeme geprägt wurde, die ihre eigenen Komponenten aufbauen und reparieren, ohne dass jemand sie von außen zusammenfügt. Das Buch verwendet ihn in erweitertem Sinne: Ein industrielles System, das seine eigenen Werkzeuge entwirft, seine eigenen Agenten schreibt und seine eigenen Clouds wartet, hat sich unabhängig vom Menschen gemacht, der außerhalb des Reproduktionszyklus zurückbleibt.

**Industry 7.0.** Das Gerüst, das dieses Buch für die sechste Revolution verwendet: die siebte Generation der Industrie, in der Maschinen Peripheriegeräte einer internen KI werden, und diese KI --- agentic, mit einer privaten Cloud verbunden, das kennend das Geschäft --- das ganze Unternehmen zu einem einzigen selbstkoordinierenden Kreislauf automatisiert.

## Die ehrliche Anmerkung

Ein Glossar kann den falschen Eindruck erwecken, dass diese Begriffe einmal für immer feststehen. Das ist nicht so --- die Sprache der sechsten Revolution wird geschrieben, während wir sprechen, und einige dieser Wörter werden sich verschieben. Lesen Sie diesen Anhang als freundlichen Ausgangspunkt, nicht als Urteil. Das folgende Buch wird jeden Begriff definieren, wenn er benötigt wird, im Kontext, weil der Kontext der Ort ist, an dem Wörter wirklich leben.
