# Annexe B --- Les projets derrière la vision, et lectures complémentaires

## Le laboratoire

Les technologies décrites dans tout cet ouvrage ne sont pas hypothétiques. Elles sont en cours de construction, de publication et de perfectionnement par un petit laboratoire de recherche, **AI Technology Graphene-Lab**, qui préfère laisser les machines parler d'elles-mêmes. Son travail est publié ouvertement sur GitHub, sous des licences permissives, précisément afin que les lecteurs de cet ouvrage puissent regarder, tester et --- s'ils le choisissent --- adopter. Cette annexe indique au lecteur les véritables dépôts qui fondent les chapitres précédents, puis quelques livres et écrits pour ceux qui souhaitent aller plus loin, que ce soit dans la direction de la machine, du cloud ou de l'agent.

L'ensemble des projets du laboratoire sont réunis à : **https://github.com/orgs/Graphene-Lab/repositories**. Ci-dessous figurent ceux qui apparaissent spécifiquement dans cet ouvrage.

## Les projets de cet ouvrage

### AgentBridge --- l'assistant agentique qui connaît votre entreprise

**Dépôt :** https://github.com/Graphene-Lab/AgentBridge

AgentBridge est un assistant personnel IA auto-hébergé qui automatise le travail de bureau sans sacrifier la confidentialité. Il fait tourner ses propres agents derrière deux interfaces dans un seul processus --- un terminal de conversation en plein écran, et une API HTTP qui parle le protocole standard OpenAI, de sorte que n'importe quel client compatible OpenAI puisse piloter les mêmes agents. Son idée fondatrice est que les capacités d'un agent sont des assemblages compilés chargés comme des plugins, de sorte que l'agent appelle le logiciel directement plutôt que par le biais d'un protocole. Il embarque une mémoire déterministe propriétaire (elle n'oublie jamais les faits, les personnes et les documents qu'elle a traités), s'exécute dans un sandbox natif de sorte que ses actions soient bornées et réversibles, et peut être approvisionnée avec le cloud privé afin que les connaissances qu'elle lit ne quittent jamais l'entreprise. Le laboratoire le décrit comme l'outil derrière cet ouvrage --- celui qui rend réel le « bureau à minuit ».

### CloudServer --- le cloud privé, sans confiance et à connaissance nulle

**Dépôt :** https://github.com/Graphene-Lab/CloudServer

CloudServer est le cloud privé maintenant à l'intérieur de l'entreprise. Là où le cloud public centralise les données dans d'immenses centres de données qui peuvent être lus --- ou contraints de lire --- un cloud privé à connaissance nulle comme CloudServer maintient les données sous le propre contrôle de l'entreprise, de sorte que la télémétrie issue des machines ne quitte jamais l'autorité de l'entreprise et n'est jamais lisible par un tiers. C'est là la réponse, pour la usine, aux échecs de confidentialité exposés par le grand scandale des données du début des années 2010.

### UISupportBlazor --- une IA déterministe pour les front-ends et les APIs automatiques

**Dépôt :** https://github.com/Graphene-Lab/UISupportBlazor

UISupportBlazor est un projet pionnier de l'IA agentique pour le codage, mais sa signification plus profonde est conceptuelle : il démontre qu'un assemblage compilé --- la spécification exacte et complète d'un backend --- peut être utilisé comme le dernier prompt déterministe, duquel les interfaces utilisateur et les couches API sont dérivées avec une certitude mathématique plutôt que devinées à partir d'un prompt en langage naturel. C'est l'exemple phare de l'argument des « deux sortes d'esprit » (Chapitre 13) et de l'argument de l'« assemblage comme dernière vérité » (Chapitre 14) : l'esprit déterministe, là où la certitude est requise.

### Les bibliothèques de soutien de l'IA déterministe

Au-delà de ces projets vedettes, le laboratoire publie les bibliothèques de soutien qui rendent l'ensemble de la pile cohérente --- par exemple les outils d'analyse d'assemblage (UISupportGeneric, GiraffeAI) qui permettent à une machine de lire un assemblage compilé et d'en dériver l'interface ou l'outil dont elle a besoin. Ensemble, elles forment un écosystème plutôt qu'un ensemble d'outils isolés, et cet écosystème est ce que l'ouvrage décrit in fine.

## La porte Telegram

Le travail est montré, non simplement décrit, sur la chaîne Telegram du laboratoire. Le QR code de [Une note à propos de l'ouvrage](preface.md) --- et de nouveau dans l'[Épilogue](epilogue-the-factory-that-dreamed.md) --- y mène. Si vous souhaitez voir la machine qui pense, le cloud qui garde son secret, l'agent qui connaît votre entreprise, et le humanoïde qui entre sur l'atelier tels qu'ils sont, en temps réel, voilà la porte.

## Lectures complémentaires

Pour ceux qui souhaitent élargir l'horizon au-delà de cet ouvrage, quelques directions offrent un terrain particulièrement riche. Ce sont des suggestions, non une liste de lectures obligatoire ; choisissez le chemin qui correspond à votre position.

**Sur l'histoire des révolutions et de l'intelligence.** Le lecteur qui souhaite placer la sixième révolution dans l'long arc trouvera bien des choses à lire dans les histoires des vagues antérieures --- la machine à vapeur, la ligne d'assemblage, l'ordinateur --- et dans l'histoire plus longue de l'IA elle-même, avec ses hivers et ses printemps. Le motif que ces histoires révèlent est la même décision-outil que cet ouvrage propose : connaître le motif, et vous serez plus difficile à duper.

**Sur les deux sortes d'esprit.** La distinction entre l'esprit probabiliste et l'esprit deterministe est l'idée la plus profonde de cet ouvrage, et elle vaut la peine d'être lue dans ses contextes originaux : la théorie du calcul et la nature déterministe de la compilation, d'un côté ; et l'apprentissage automatique, de l'autre. Les écrits propre du laboratoire sur l'IA deterministe (voir UISupportBlazor plus haut) poussent cette idée plus loin que cet ouvrage ne le peut, et constituent l'étape suivante naturelle pour le lecteur qui trouve l'argument des deux esprits convaincant.

**Sur la confidentialité et le cloud.** Le lecteur intéressé par le cloud privé, sans confiance et à connaissance nulle trouvera la vraie discussion dans la documentation de CloudServer et dans la littérature plus large sur la cryptographie, la souveraineté des données et les échecs du cloud public exposés par le grand scandale des données. La leçon --- qu'un cloud que vous devez faire confiance n'est pas un endroit où garder votre avenir --- est une leçon qui vaut la peine d'être emportée bien au-delà de la usine.

**Sur les agents et leur sécurité.** Le lecteur attiré par le côté agentique de la sixième révolution voudra étudier AgentBridge et sa mémoire deterministe et son sandbox, et la littérature plus large sur les agents contraints et auto-hébergés. L'argument de sécurité --- qu'un agent doit être borné par la structure, non par la discipline du prompt --- est un argument qui importera de plus en plus à mesure que les agents prendront en charge plus de travail réel.

## L'atténuation honnête

Cette annexe pointe vers des projets réels et publiés et vers des directions de lectures supplémentaires ; elle ne promet pas que l'un quelconque d'entre eux sera terminé, stable ou aisé. Les projets du laboratoire sont vivants et en évolution ; les liens et les détails peuvent changer. Le lecteur honnête traite cette annexe comme une boussole plutôt qu'une carte fixe --- une direction à suivre, vérifiée contre les sources elles-mêmes. Cela, in fine, est toute la leçon de la sixième révolution : ne vous contentez pas de faire confiance à l'ouvrage ; allez lire les sources, testez les machines, et décidez par vous-même. La usine qui pense n'est pas une promesse à croire ; c'est une pratique à examiner.
