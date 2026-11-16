# Annexe A --- Un glossaire de la nouvelle langue

## Pourquoi un glossaire

La sixième révolution industrielle a, comme toute révolution, apporté son propre vocabulaire --- des mots qui étaient autrefois la propriété privée des ingénieurs et des programmeurs et qui sont maintenant, discrètement, devenus partie intégrante de la langue de l'usine et, dans bien des cas, de celle du bureau. Cette annexe est un guide doux vers ces mots, définis dans une langue simple dès qu'ils deviennent utiles, mais réunis ici afin que le lecteur puisse s'y replonger avec aisance. Rien ici n'exige un diplôme pour être lu; chaque définition est écrite comme si l'on s'adressait à un néophyte réflchi.

## Les termes

**IA agentique.** Une IA qui ne se contente pas de répondre à une question mais poursuit un objectif: elle planifie, agit, observe le résultat et s'ajuste, à l'aide des outils qu'on lui a confiés. Contrairement à un chatbot qui attend d'être interrogé, un agent se voit confier un objectif et trouve le moyen de l'atteindre. AgentBridge en est un exemple.

**Assemblage (logiciel).** L'artifact compilé qu'un programme produit lorsqu'il est construit --- la spécification la plus détaillée, exacte et non ambiguë de ce que le programme fait. Dans l'IA déterministe (voir ci-dessous), l'assemblage sert de source de vérité, plutôt qu'un prompt en langue naturelle qui doit être interprété.

**Cloud (public et privé).** Un cloud public est un ensemble de gigantesques centres de données détenus par quelques entreprises, où vous stockez et calculez des données qui vivent sur les machines de quelqu'un d'autre. Un cloud privé est maintenant sous le contrôle d'une seule entreprise. La sixième révolution favorise le cloud privé, sans confiance et à connaissance nulle (voir ces termes).

**IA déterministe.** Une IA --- ou, plus précisément, un calcul automatisé --- qui produit le même résultat, garanti, à chaque fois, sans aucun pari. C'est l'esprit du compilateur: exact, traçable, prouvable. Elle est idéale là où une décision doit être certaine (sécurité, finance, conformité) plutôt que simplement plausible.

**IA au bord / IA sur machine.** Une intelligence qui s'exécute localement, sur ou près de la machine qui produit les données, plutôt que d'envoyer les données vers un cloud lointain pour y être traitées. Elle est plus rapide, moins chère et plus privée, car les données ne quittent jamais le bâtiment.

**NPU (Unité de traitement neuronal).** Une petite puce à l'intérieur d'un processeur plus grand, construite spécifiquement pour exécuter rapidement et efficacement des modèles de réseaux de neurones (apprentissage automatique), surtout localement. C'est ce qui permet à une petite carte sur une machine d'usine de «voir» et de «prédire» sans aller et revenir vers le cloud.

**SBC (Ordinateur à carte unique).** Un ordinateur complet sur une seule carte de circuit. Les SBC intelligents modernes sont basés sur des processeurs ARM avec une NPU intégrée, sont souvent sans ventilateur, et peuvent être très bon marché --- ce qui rend l'intelligence sur machine abordable pour tous.

**Télémétrie.** Des données mesurées à un endroit et rapportées, automatiquement et en continu, vers un autre. Sur une usine, c'est le stream en direct --- vibration, température, courant, son, images --- qui rend compte en temps réel de l'état de la machine. C'est le sang de la nouvelle usine.

**Cloud sans confiance.** Un cloud que vous n'avez pas à *faire confiance* pour se comporter, car son architecture --- et non les bonnes intentions de l'opérateur --- maintient vos données en sécurité. Vos données sont chiffrées avec une clé que vous seul détenez, de sorte que le cloud peut les traiter et les synchroniser sans jamais pouvoir les lire.

**Cloud à connaissance nulle.** Un cloud qui peut vérifier et traiter vos données sans jamais connaître les données elles-mêmes. Il agit sur le coffre-fort verrouillé, jamais sur son contenu. Tiré son nom des «preuves à connaissance nulle» en cryptographie, qui prouvent qu'une affirmation est vraie sans rien révéler au-delà de cette vérité.

**Jumeau numérique.** Un modèle numérique et vivant d'une chose physique --- une machine, une ligne, une usine entière --- qui en reflète l'état réel. Sur la sixième révolution, un jumeau numérique peut vivre localement sur la carte même de la machine, toujours disponible et privé.

**Humñoïde.** Un robot qui se déplace sur deux jambes à la façon d'un être humain, et peut donc utiliser un monde conçu pour les humains --- portes, escaliers, leviers à hauteur de main. Sur la sixième révolution, l'humnoïde est précieux là où le travail est dangereux, inaccessible, ou use le corps humain, plutôt que comme remplacement général pour tout travailleur.

**Robotique / robotique collaborative (cobotique).** La science des machines qui bougent et agissent. Les robots collaboratifs sont conçus pour travailler *à côté* des humains en toute sécurité, percevant constamment leur environnement et s'ajustant, plutôt que d'être enfermés à distance des personnes.

**LLM (Modèle de langue large).** Un modèle de aprendizaje automático entraîné sur d'énormes quantités de texte pour comprendre et générer la langue humaine. Il est flexible et impressionnant, et il peut inventer des choses --- ce qui fait que, là où la certitude compte, il est combiné à un calcul déterministe plutôt que seul et de confiance.

**PLC (Contrôleur logique programmable).** L'ancien contrôleur, extraordinairement fiable, sur presque tous les sols d'usine, qui lit les interrupteurs et les capteurs et allume et éteint les sorties selon des règles explicites écrites par les humains. La sixième révolution ne casse pas nécessairement le PLC; elle l'augmente d'une petite carte intelligente qui perçoit et prédit ce que le PLC n'a jamais pu faire.

**Vision / inspection visuelle.** L'utilisation d'une caméra plus un modèle appris pour juger automatiquement les produits --- repérer les rayures, les mauvais alignements, les défauts --- à la vitesse de la lumière et sans la fatigue de l'œil humain.

**Maintenance prédictive.** Prédire, à partir des propres signaux d'une machine (vibration, température, son, courant), quand une pièce est sur le point de tomber en panne, de sorte que la réparation puisse être planifiée avant la panne plutôt qu'après elle.

**Pilote automatique / le bureau à minuit.** La vision, explorée dans ce livre, dans laquelle un agent --- connaissant l'entreprise et travaillant dans un cloud privé --- termine le travail de bureau (comptabilité, entrepôt, ventes, support, conformité) automatiquement, en continu et en privé, de sorte que le bureau continue de travailler après l'extinction des lumières.

**Autopoïèse.** Littéralement «se faire soi-même» (du grec *auto*, «soi-même», et *poiesis*, «production»). Un terme inventé en 1972 par Humberto Maturana et Francisco Varela pour les systèmes vivants, qui construisent et réparent leurs propres composants sans que personne ne les assemble depuis l'extérieur. Le livre l'utilise dans un sens étendu: un système industriel qui conçoit ses propres outils, écrit ses propres agents et maint ses propres clouds a fait de lui-même son indépendance vis-à-vis de l'être humain, qui reste à l'extérieur du cycle de reproduction.

**Industrie 7.0.** Le cadre que ce livre utilise pour la sixième révolution: la septième génération d'industrie, dans laquelle les machines deviennent des périphériques d'une IA interne, et que cette IA --- agentique, connectée à un cloud privé, connaissant l'entreprise --- automatise l'entreprise entière en une seule boucle auto-coordonnée.

## La note honnête

Un glossaire peut donner la fausse impression que ces termes sont fixés une fois pour toutes. Ils ne le sont pas --- la langue de la sixième révolution s'écrit pendant que nous parlons, et certains de ces mots changeront. Lisez cette annexe comme un point de départ amical, non comme un verdict. Le livre qui suivra définira chaque terme au fur et à mesure de ses besoins, dans le contexte, car c'est dans le contexte que les mots vivent véritablement.
