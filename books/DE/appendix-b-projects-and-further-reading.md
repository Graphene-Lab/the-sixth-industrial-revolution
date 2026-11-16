# Anhang B --- Die Projekte hinter der Vision und weiterführende Literatur

## Das Labor

Die Technologien, die in diesem ganzen Buch beschrieben werden, sind nicht hypothetisch. Sie werden von einem kleinen Forschungslabor, **AI Technology Graphene-Lab**, entwickelt, veröffentlicht und verfeinert, das lieber möchte, dass die Maschinen für sich selbst sprechen. Seine Arbeiten werden offen auf GitHub veröffentlicht, unter großzügigen Lizenzbedingungen, gerade damit die Leser dieses Buches hineinsehen, testen und --- wenn sie es wählen --- übernehmen können. Dieser Anhang weist den Leser auf die realen Repositorys hin, die die obigen Kapitel fundieren, und dann auf einige Bücher und Schriften für jene, die weitergehen möchten, ob nun in Richtung der Maschine, der Cloud oder des Agenten.

Die gesamten Projekte des Labors sind gesammelt unter: **https://github.com/orgs/Graphene-Lab/repositories**. Nachfolgend sind die spezifischen aufgeführt, die in diesem Buch vorkommen.

## Die Projekte in diesem Buch

### AgentBridge --- der agentische Assistent, der Ihr Unternehmen kennt

**Repository:** https://github.com/Graphene-Lab/AgentBridge

AgentBridge ist ein selbstgehosteter AI-Personalassistent, der Büroarbeit automatisiert, ohne dabei die Privatsphile aufzugeben. Es betreibt seine eigenen Agenten hinter zwei Schnittstellen in einem einzigen Prozess --- ein Vollbild-Chat-Terminal und eine HTTP-API, die das Standard-OpenAI-Protokoll spricht, sodass jeder OpenAI-kompatible Client dieselben Agenten steuern kann. Seine bestimmende Idee ist, dass die Fähigkeiten eines Agenten kompilierte Assemblys sind, die als Plugins geladen werden, sodass der Agent die Software direkt aufruft, statt über ein Protokoll. Es führt einen eigenständigen deterministischen Speicher (es vergisst nie die Fakten, Menschen und Dokumente, die es behandelt hat), läuft innerhalb eines nativen Sandboxes, sodass seine Aktionen begrenzt und reversibel sind, und kann mit der privaten Cloud versorgt werden, sodass das Wissen, das es liest, nie das Unternehmen verlässt. Das Labor beschreibt es als das Werkzeug hinter diesem Buch --- dasjenige, das das „Büro um Mitternacht" real macht.

### CloudServer --- die private, vertrauenslose, nullwissende Cloud

**Repository:** https://github.com/Graphene-Lab/CloudServer

CloudServer ist die private Cloud, die innerhalb des Unternehmens gehalten wird. Wo die öffentliche Cloud Daten in riesigen Datenzentren zentralisiert, die gelesen --- oder gezwungen werden können, gelesen zu werden --- hält eine private, nullwissende Cloud wie CloudServer die Daten unter der Kontrolle des eigenen Unternehmens, sodass die Telemetrie, die von den Maschinen fließt, nie die Autorität des Unternehmens verlässt und nie von einer dritten Partei gelesen werden kann. Dies ist die Antwort, für die Fabrik, auf die Datenschutzfehler, die durch das große Datenskandal der frühen 2010er Jahre offengelegt wurden.

### UISupportBlazor --- deterministische AI für automatische Frontends und APIs

**Repository:** https://github.com/Graphene-Lab/UISupportBlazor

UISupportBlazor ist ein wegweisendes Projekt für agentische-AI-für-Coding, doch seine tiefere Bedeutung ist konzeptionell: es demonstriert, dass eine kompilierte Assembly --- die exakte, vollständige Spezifikation eines Backends --- als letzter deterministischer Prompt verwendet werden kann, aus dem Benutzeroberflächen und API-Schichten mit mathematischer Gewissheit abgeleitet werden, statt aus einem natürlichen-Sprache-Prompt geraten zu werden. Es ist das Leitbeispiel des Arguments der „zwei Arten von Verstand" (Kapitel 13) und des Arguments der „Assembly als letzte Wahrheit" (Kapitel 14): der deterministische Verstand, wo Gewissheit erforderlich ist.

### Die Support-Bibliotheken der deterministischen AI

Jenseits dieser Hauptprojekte veröffentlicht das Labor die Support-Bibliotheken, die den ganzen Stack zusammenhängend machen --- zum Beispiel die Assembly-Analyse-Werkzeuge (UISupportGeneric, GiraffeAI), die einer Maschine erlauben, eine kompilierte Assembly zu lesen und daraus die Schnittstelle oder das Werkzeug abzuleiten, das sie benötigt. Zusammen bilden diese ein Ökosystem statt einer Reihe isolierter Werkzeuge, und dieses Ökosystem ist es, was das Buch letztendlich beschreibt.

## Die Tür des Telegram

Die Arbeit wird gezeigt, nicht bloß beschrieben, auf dem Telegram-Kanal des Labors. Der QR-Code in [Ein Hinweis zum Buch](preface.md) --- und erneut im [Epilog](epilogue-the-factory-that-dreamed.md) --- führt dorthin. Wenn Sie die Maschine sehen möchten, die denkt, die Cloud, die ihr Geheimnis bewahrt, den Agenten, der Ihr Unternehmen kennt, und den Humanoiden, der auf den Boden tritt, so wie sie sind, in Echtzeit, dann ist das die Tür.

## Weiterführende Literatur

Für jene, die den Horizont über dieses Buch hinaus erweitern möchten, bieten einige Richtungen besonders reichliches Gelände. Diese sind Vorschläge, keine Pflichtlektüre; wählen Sie den Pfad, wo Sie stehen.

**Zur Geschichte der Revolutionen und der Intelligenz.** Der Leser, der die sechste Revolution in den langen Bogen einordnen möchte, wird in den Geschichten der früheren Wellen --- der Dampfmaschine, der Fließbandfertigung, des Computers --- und in der längeren Geschichte der AI selbst, mit ihren Wintern und ihren Frühlingen, viel des Lesenswertes finden. Das Muster, das diese Geschichten offenlegen, ist dieselbe Entscheidungswerkzeug, das dieses Buch anbietet: kennen Sie das Muster, und Sie sind schwerer zu täuschen.

**Z den zwei Arten von Verstand.** Der Unterschied zwischen dem probabilistischen Verstand und dem deterministischen Verstand ist die tiefste Idee in diesem Buch, und es lohnt sich, darüber in ihren ursprünglichen Kontexten zu lesen: die Berechnungstheorie und die deterministische Natur der Kompilierung, auf einer Seite; und maschernes Lernen, auf der anderen. Die eigenen Schriften des Labors zur deterministischen AI (siehe UISupportBlazor oben) treiben diese Idee weiter als dieses Buch es kann, und sind der natürliche nächste Schritt für den Leser, der das Zwei-Verstand-Argument überzeugend findet.

**Zur Privatsphile und der Cloud.** Der Leser, der an der privaten, vertrauenslosen, nullwissenden Cloud interessiert ist, wird die echte Diskussion in der Dokumentation von CloudServer und in der breiteren Literatur über Kryptographie, Datenhoheit und die Fehler der öffentlichen Cloud, die durch das große Datenskandal offengelegt wurden, finden. Die Lehre --- dass eine Cloud, der Sie vertrauen müssen, kein Ort ist, Ihre Zukunft zu bewahren --- ist eine, die gut über die Fabrik hinaus mitgeführt werden sollte.

**Zu Agenten und ihrer Sicherheit.** Der Leser, der zur agentischen Seite der sechsten Revolution hingezogen wird, wird AgentBridge und seinen deterministischen Speicher und seinen Sandbox studieren wollen sowie die breitere Literatur über begrenzte, selbstgehostete Agenten. Das Sicherheitsargument --- dass ein Agent durch Struktur begrenzt sein sollte, nicht durch Prompt-Disziplin --- ist eine, die zunehmend eine Rolle spielen wird, wenn Agenten mehr reale Arbeit übernehmen.

## Der ehrliche Vorbehalt

Dieser Anhang weist auf reale, veröffentlichte Projekte und auf Richtungen weiterfühterer Literatur hin; er verspricht nicht, dass irgendwelche von ihnen fertig, stabil oder einfach sein werden. Die Projekte des Labors sind live und in Entwicklung; Links und Details können sich ändern. Der ehrliche Leser behandelt diesen Anhang als Kompass statt einer festen Karte --- eine Richtung, nach der man sich richtet, geprüft an den Quellen selbst. Das, im Endeffekt, ist die ganze Lehre der sechsten Revolution: nicht bloß dem Buch vertrauen; hingehen und die Quellen lesen, die Maschinen testen und selbst entscheiden. Die Fabrik, die denkt, ist kein Versprechen, dem man glauben sollte; sie ist eine Praxis, die untersucht werden sollte.
