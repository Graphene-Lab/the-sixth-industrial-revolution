# Appendice A --- Glossario della nuova lingua

## Perché un glossario

La sesta rivoluzione industriale ha portato, come ogni rivoluzione, un proprio vocabolario: parole che un tempo erano proprietà privata di ingegneri e programmatori e che oggi, in silenzio, sono diventate parte del linguaggio della fabbrica e, in molti casi, dell'ufficio. Questa appendice è una guida gentile a quelle parole, definite in parole semplici nel momento in cui servono, ma raccolte qui perché il lettore possa tornarvi con calma. Nulla di ciò che segue richiede una laurea per essere letto; ogni definizione è scritta come se si spiegasse a una persona intelligente che arriva da fuori.

## I termini

**Intelligenza artificiale agentica.** Un'intelligenza artificiale che non si limita a rispondere a una domanda ma persegue un obiettivo: pianifica, agisce, osserva il risultato e si corregge, usando gli strumenti che le sono stati dati. A differenza di un chatbot che aspetta di essere interrogato, a un agente viene consegnato un obiettivo e lui capisce come raggiungerlo. AgentBridge ne è un esempio.

**Assembly (software).** L'artefatto compilato che un programma produce quando viene costruito: la specifica più dettagliata, esatta e inequivocabile di ciò che il programma fa. Nell'intelligenza artificiale deterministica (vedi sotto) l'assembly è usato come fonte di verità, invece di un prompt in linguaggio naturale che va interpretato.

**Nuvola (pubblica e privata).** Una nuvola pubblica è un insieme di centri dati giganteschi posseduti da poche aziende, dove conservate ed elaborate dati che vivono su macchine di altri. Una nuvola privata è tenuta sotto il controllo di una singola azienda. La sesta rivoluzione preferisce la nuvola privata, trustless e a conoscenza zero (vedi quelle voci).

**Intelligenza artificiale deterministica.** Intelligenza artificiale --- o, più precisamente, calcolo automatizzato --- che produce ogni volta lo stesso risultato garantito, senza alcuna ipotesi. È la mente del compilatore: esatta, tracciabile, dimostrabile. È ideale dove una decisione deve essere certa (sicurezza, finanza, conformità) e non soltanto plausibile.

**Intelligenza artificiale al margine / a bordo macchina.** Intelligenza che gira localmente, sulla macchina o vicino alla macchina che produce i dati, invece di mandarli a una nuvola lontana per essere elaborati. È più veloce, più economica e più riservata, perché i dati non lasciano l'edificio.

**NPU (Neural Processing Unit, unità di elaborazione neurale).** Un piccolo chip dentro un processore più grande, costruito apposta per eseguire reti neurali (modelli di apprendimento automatico) in fretta e con efficienza, soprattutto localmente. È ciò che permette a una piccola scheda su una macchina di fabbrica di «vedere» e «prevedere» senza un viaggio di andata e ritorno verso la nuvola.

**SBC (Single-Board Computer, computer a scheda singola).** Un computer completo su un solo circuito stampato. I moderni SBC intelligenti sono basati su processori ARM con NPU integrata, spesso senza ventola, e possono costare pochissimo: è ciò che rende l'intelligenza a bordo macchina accessibile a tutti.

**Telemetria.** Dato misurato in un luogo e riferito, automaticamente e di continuo, a un altro. In fabbrica è il flusso vivo --- vibrazione, temperatura, corrente, suono, immagini --- che riferisce in tempo reale la condizione della macchina. È il sangue della nuova fabbrica.

**Nuvola trustless.** Una nuvola di cui non dovete *fidarvi* perché si comporti bene, perché è la sua architettura, non le buone intenzioni del gestore, a tenere al sicuro i vostri dati. I dati sono cifrati con una chiave che solo voi possedete, così la nuvola può elaborarli e sincronizzarli senza mai poterli leggere.

**Nuvola a conoscenza zero.** Una nuvola che sa verificare ed elaborare i vostri dati senza mai apprendere i dati stessi. Opera sulla cassaforte chiusa, mai sul contenuto. Il nome viene dalle «prove a conoscenza zero» della crittografia, che dimostrano che un'affermazione è vera senza rivelare nulla oltre quella verità.

**Gemello digitale.** Un modello digitale vivo di una cosa fisica --- una macchina, una linea, un intero stabilimento --- che ne rispecchia lo stato reale. Nella sesta rivoluzione un gemello digitale può vivere localmente sulla scheda della macchina, sempre disponibile e privato.

**Umanoide.** Un robot che si muove su due gambe come un essere umano, e che quindi può usare un mondo costruito per gli esseri umani: porte, scale, leve all'altezza della mano. Nella sesta rivoluzione l'umanoide è prezioso dove il lavoro è pericoloso, inaccessibile o logora il corpo umano, più che come sostituto generale di ogni lavoratore.

**Robotica / robotica collaborativa (cobotica).** La scienza delle macchine che si muovono e agiscono. I robot collaborativi sono progettati per lavorare *accanto* agli esseri umani in sicurezza, percependo di continuo l'ambiente e correggendosi, invece di essere chiusi in gabbia lontano dalle persone.

**LLM (Large Language Model, grande modello linguistico).** Un modello di apprendimento automatico addestrato su enormi quantità di testo per capire e generare linguaggio umano. È flessibile e impressionante, e sa inventare: è per questo che, dove conta la certezza, viene combinato con il calcolo deterministico invece che creduto da solo.

**PLC (Programmable Logic Controller, controllore logico programmabile).** Il vecchio controllore straordinariamente affidabile presente in quasi ogni reparto del mondo, che legge interruttori e sensori e accende o spegne uscite secondo regole esplicite scritte da esseri umani. La sesta rivoluzione non rompe necessariamente il PLC: lo affianca a una piccola scheda intelligente che percepisce e prevede ciò che il PLC non ha mai saputo fare.

**Visione / ispezione visiva.** L'uso di una telecamera più un modello addestrato per giudicare automaticamente i prodotti --- individuando graffi, disallineamenti, difetti --- alla velocità della luce e senza la stanchezza di un occhio umano.

**Manutenzione predittiva.** Prevedere, dai segnali della macchina stessa (vibrazione, temperatura, suono, corrente), quando un componente sta per cedere, così che la riparazione si possa programmare prima del guasto invece che dopo.

**Pilota automatico / l'ufficio a mezzanotte.** La visione esplorata in questo libro, in cui un agente --- che conosce l'azienda e lavora dentro una nuvola privata --- porta a termine il lavoro d'ufficio (contabilità, magazzino, vendite, assistenza, conformità) in modo automatico, continuo e riservato, così che l'ufficio continui a lavorare dopo che le luci si sono spente.

**Autopoiesi.** Letteralmente «farsi da sé» (dal greco *auto*, «da sé», e *poiesis*, «produzione»). Termine coniato nel 1972 da Humberto Maturana e Francisco Varela per i sistemi viventi, che costruiscono e riparano da sé i propri componenti senza che nessuno li assembli dall'esterno. Nel libro è usato in senso esteso: un sistema industriale che progetta i propri strumenti, scrive i propri agenti e mantiene le proprie nuvole si è reso indipendente dall'essere umano, che resta fuori dal ciclo di riproduzione.

**Industria 7.0.** La cornice che questo libro usa per la sesta rivoluzione: la settima generazione dell'industria, in cui le macchine diventano periferiche di un'intelligenza artificiale interna, e quell'intelligenza --- agentica, connessa a una nuvola privata, conoscitrice dell'azienda --- automatizza l'intera impresa in un unico ciclo autocoordinato.

## La nota onesta

Un glossario può dare la falsa impressione che questi termini siano fissati una volta per tutte. Non lo sono: la lingua della sesta rivoluzione si sta scrivendo mentre parliamo, e alcune di queste parole cambieranno. Leggete questa appendice come un punto di partenza amichevole, non come un verdetto. Il libro che segue definirà ogni termine quando serve, nel contesto, perché è nel contesto che le parole vivono davvero.
