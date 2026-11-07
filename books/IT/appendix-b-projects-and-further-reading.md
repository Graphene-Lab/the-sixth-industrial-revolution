# Appendice B --- I progetti dietro la visione, e letture ulteriori

## Il laboratorio

Le tecnologie descritte in questo libro non sono ipotetiche. Sono costruite, pubblicate e affinate da un piccolo laboratorio di ricerca, **AI Technology Graphene-Lab**, che preferisce lasciar parlare le macchine per sé. Il suo lavoro è pubblicato apertamente su GitHub, con licenze permissive, precisamente perché i lettori di questo libro possano guardare, provare e, se lo desiderano, adottare. Questa appendice indica al lettore i repository reali che sostengono i capitoli precedenti e, poi, qualche libro e scritto per chi vuole andare oltre, che sia nella direzione della macchina, della nuvola o dell'agente.

I progetti dell'intero laboratorio sono raccolti qui: **https://github.com/orgs/Graphene-Lab/repositories**. Qui sotto quelli specifici che compaiono in questo libro.

## I progetti di questo libro

### AgentBridge --- l'assistente agentico che conosce la vostra azienda

**Repository:** https://github.com/Graphene-Lab/AgentBridge

AgentBridge è un assistente personale di intelligenza artificiale self-hosted che automatizza il lavoro d'ufficio senza sacrificare la riservatezza. Fa girare i propri agenti dietro due interfacce in un unico processo: un terminale di chat a tutto schermo e un'API HTTP che parla il protocollo standard OpenAI, così che qualsiasi client compatibile con OpenAI possa guidare gli stessi agenti. La sua idea decisiva è che le capacità di un agente sono assembly compilati caricati come plugin, così l'agente chiama il software direttamente invece che attraverso un protocollo. Porta con sé una memoria deterministica proprietaria (non dimentica mai i fatti, le persone e i documenti che ha trattato), gira dentro una sandbox nativa così che le sue azioni siano circoscritte e reversibili, e può essere alimentato con la nuvola privata, così che la conoscenza che legge non lasci mai l'azienda. Il laboratorio lo descrive come lo strumento dietro questo libro: quello che rende reale l'«ufficio a mezzanotte».

### CloudServer --- la nuvola privata, trustless e a conoscenza zero

**Repository:** https://github.com/Graphene-Lab/CloudServer

CloudServer è la nuvola privata tenuta dentro l'azienda. Dove la nuvola pubblica centralizza i dati in centri dati giganteschi che si possono leggere, o obbligare a leggere, una nuvola privata a conoscenza zero come CloudServer tiene i dati sotto il controllo dell'azienda stessa, così che la telemetria che scorre dalle macchine non lasci mai l'autorità dell'azienda e non sia mai leggibile da una terza parte. È la risposta, per la fabbrica, ai fallimenti della riservatezza esposti dal grande scandalo dei dati dei primi anni Dieci.

### UISupportBlazor --- intelligenza artificiale deterministica per front-end e API automatici

**Repository:** https://github.com/Graphene-Lab/UISupportBlazor

UISupportBlazor è un progetto pioniere di intelligenza artificiale agentica per la programmazione, ma il suo significato più profondo è concettuale: dimostra che un assembly compilato --- la specifica esatta e completa di un back-end --- può essere usato come prompt deterministico definitivo, da cui interfacce utente e livelli API sono derivati con certezza matematica invece che indovinati da un prompt in linguaggio naturale. È l'esempio di punta dell'argomento dei «due tipi di mente» (capitolo 13) e dell'argomento dell'«assembly come ultima verità» (capitolo 14): la mente deterministica, dove la certezza è richiesta.

### Le librerie di supporto dell'intelligenza artificiale deterministica

Oltre a questi progetti principali, il laboratorio pubblica le librerie di supporto che rendono coerente l'intero stack: per esempio gli strumenti di analisi degli assembly (UISupportGeneric, GiraffeAI) che permettono a una macchina di leggere un assembly compilato e di ricavarne l'interfaccia o lo strumento di cui ha bisogno. Insieme, questi formano un ecosistema più che un insieme di strumenti isolati, e quell'ecosistema è ciò che il libro descrive in ultima analisi.

## La porta Telegram

Il lavoro viene mostrato, non soltanto raccontato, sul canale Telegram del laboratorio. Il codice QR in [Una nota sul libro](preface.md) --- e di nuovo nell'[Epilogo](epilogue-the-factory-that-dreamed.md) --- conduce lì. Se volete vedere la macchina che pensa, la nuvola che custodisce il proprio segreto, l'agente che conosce la vostra azienda e l'umanoide che entra in reparto come sono, in tempo reale, quella è la porta.

## Letture ulteriori

Per chi desidera allargare l'orizzonte oltre questo libro, alcune direzioni offrono un terreno particolarmente ricco. Sono suggerimenti, non una bibliografia obbligatoria: scegliete il percorso che corrisponde a dove vi trovate.

**Sulla storia delle rivoluzioni e dell'intelligenza.** Il lettore che vuole collocare la sesta rivoluzione nell'arco lungo troverà molto da leggere nelle storie delle ondate precedenti --- la macchina a vapore, la catena di montaggio, il computer --- e nella storia più lunga dell'intelligenza artificiale stessa, con i suoi inverni e le sue primavere. Lo schema che quelle storie rivelano è lo stesso strumento decisionale che questo libro offre: conoscere lo schema rende più difficile essere ingannati.

**Sui due tipi di mente.** La distinzione tra la mente probabilistica e la mente deterministica è l'idea più profonda di questo libro, e vale la pena leggerne nei contesti originali: la teoria della computazione e la natura deterministica della compilazione da un lato, e l'apprendimento automatico dall'altro. Gli scritti del laboratorio sull'intelligenza artificiale deterministica (si veda UISupportBlazor sopra) spingono questa idea più avanti di quanto questo libro possa fare, e sono il passo naturale successivo per il lettore che trova convincente l'argomento delle due menti.

**Sulla riservatezza e la nuvola.** Il lettore interessato alla nuvola privata, trustless e a conoscenza zero troverà la discussione vera nella documentazione di CloudServer e nella letteratura più ampia sulla crittografia, sulla sovranità dei dati e sui fallimenti della nuvola pubblica esposti dal grande scandalo dei dati. La lezione --- che una nuvola di cui dovete fidarvi non è un posto dove tenere il vostro futuro --- vale la pena di essere portata ben oltre la fabbrica.

**Sugli agenti e la loro sicurezza.** Il lettore attratto dal lato agentico della sesta rivoluzione vorrà studiare AgentBridge, la sua memoria deterministica e la sua sandbox, e la letteratura più ampia sugli agenti vincolati e self-hosted. L'argomento di sicurezza --- che un agente vada circoscritto per struttura, non per disciplina di prompt --- è un argomento che conterà sempre di più man mano che gli agenti si assumono lavoro reale.

## L'avvertenza onesta

Questa appendice indica progetti reali e pubblicati e direzioni di lettura ulteriore; non promette che nessuno di essi sarà finito, stabile o facile. I progetti del laboratorio sono vivi e in evoluzione; i link e i dettagli possono cambiare. Il lettore onesto tratta questa appendice come una bussola più che come una mappa fissa: una direzione in cui orientarsi, verificata contro le fonti stesse. È, alla fine, l'intera lezione della sesta rivoluzione: non credere soltanto al libro; andate a leggere le fonti, provate le macchine e decidete da soli. La fabbrica che pensa non è una promessa da credere: è una pratica da esaminare.
