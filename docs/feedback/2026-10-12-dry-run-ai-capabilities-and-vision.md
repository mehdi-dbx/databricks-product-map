# **📝 notes**

oct. 12, 2026

## **\[Dry Run\] AI Capabilities and vision**

Invité [Eric Latour](mailto:eric.latour@databricks.com) [Mehdi Lamrani](mailto:mehdi.lamrani@databricks.com) [David Dokhan](mailto:david.dokhan@databricks.com)

Pièces jointes [\[Dry Run\] AI Capabilities and vision](https://calendar.google.com/calendar/event?eid=NWcxcWxpajMzMWNwdmlxNjhiNHEwZzM0dnEgbWVoZGkubGFtcmFuaUBkYXRhYnJpY2tzLmNvbQ)

Enregistrements de réunions [Transcription](https://docs.google.com/document/d/1vCO7YabbRKv1tvkzvuq1mVa6zU3H5CFZzpi1MnPtxV4/edit?usp=drive_web&tab=t.ewxczuocycax) 

### **Résumé**

Revue des offres Databricks avec stratégie de pitch et structuration visuelle.

**Positionnement et architecture globale**  
Discussion sur les arguments Databricks et la structuration visuelle de la pyramide architecturale pour les présentations.

**Fonctionnalités IA et agents**  
Examen des Foundation Model APIs, de la recherche documentaire et des protocoles MCP pour les agents.

**Restructuration du support**  
Validation des modifications de la présentation et planification de la soumission du document.

### **Décisions**

## En accord

* **Approche prudente pour le déploiement de la Gateway** L'équipe s'accorde pour recommander l'utilisation de la Gateway sur des environnements non critiques et exclure un déploiement massif immédiat.

* **Restructuration de la présentation avec les opérations de production** Les participants ont validé de placer la section sur les opérations de production avant les applications de domaine.

* **Adoption d'une introduction globale inspirée d'Amadeus** Mehdi s'est engagé à débuter sa présentation par une vue globale inspirée de l'approche Amadeus.

* **Organisation de l'introduction et du cadrage de réunion** Eric assurera une introduction de deux minutes pour poser le contexte, suivie d'un temps final pour planifier les sessions d'approfondissement.

### **Étapes suivantes**

- [ ] \[Mehdi Lamrani\] Partager lien présentation: Transmettre le lien de la présentation via Slack à Eric Latour.

- [ ] \[Eric Latour\] Envoyer document architecture: Rechercher et envoyer le lien vers le slide de présentation architecture à Mehdi Lamrani.

- [ ] \[Mehdi Lamrani\] Mettre à jour présentation: Reformater le support de présentation en mettant en évidence les points importants. Condenser le contenu pour le rendre plus percutant.

- [ ] \[Mehdi Lamrani\] Produire document synthèse: Rédiger le document récapitulatif de architecture globale pour le client.

- [ ] \[Mehdi Lamrani\] Exporter présentation PDF: Créer une version PDF du support de présentation destiné aux clients.

- [ ] \[Mehdi Lamrani\] Réviser présentation: Réviser la présentation en tenant compte des retours reçus et intégrer une vue d'ensemble globale au début pour structurer le récit.

- [ ] \[Mehdi Lamrani\] Soumettre présentation: Soumettre la version mise à jour de la présentation à Eric Latour pour examen avant la réunion.

- [ ] \[Mehdi Lamrani\] Ajouter battle cards: Ajouter les battle cards aux documents de préparation.

### **Détails**

* **Stratégie de pitch et positionnement sur les offres Databricks**: Eric Latour et David Dokhan discutent des arguments à présenter à Pierre pour positionner les offres Databricks, identifiant trois thématiques principales : le machine learning traditionnel sur Azure Machine Learning, l'hébergement d'agents (Agent Bricks), et la GenAI orientée données d'entreprise ("talk to my data"), tout en évitant les constructeurs d'applications de Microsoft ([00:00:00](#00:00:00)). Mehdi Lamrani souligne que les clients comme Ubisoft ont essuyé les plâtres avec la Gateway et recommande d'attendre que la technologie mûrisse, une approche prudente que David Dokhan approuve pour maintenir un rôle de conseiller de confiance ("Trusty Advisor") ([00:02:36](#00:02:36)). Mehdi Lamrani note que l'inertie s'estompe et que 60 à 70 % des aspects techniques se stabilisent d'ici fin septembre ([00:04:20](#00:04:20)).

* **Présentation interactive et structure du storytelling**: David Dokhan et Mehdi Lamrani examinent la présentation mise à jour et la stratégie de storytelling pour convaincre le client ([00:04:20](#00:04:20)). Mehdi Lamrani partage l'expérience d'Emirates où des sessions prolongées ont permis de lever les doutes, et présente l'application interactive conçue pour naviguer dynamiquement entre les différents chapitres selon les questions posées ([00:06:46](#00:06:46)). Eric Latour et Mehdi Lamrani conviennent que l'application doit couvrir l'ensemble des sujets tout en permettant d'adapter le parcours en direct ([00:07:37](#00:07:37)).

* **Défis globaux de l'intelligence artificielle et architecture de fondation**: Mehdi Lamrani expose les défis généraux rencontrés par les entreprises, incluant les données fragmentées en anglais, le besoin de reproductibilité, de sécurité, de gouvernance et la mise en production des pilotes d'intelligence artificielle ([00:09:44](#00:09:44)). Mehdi Lamrani détaille l'architecture unifiée combinant une fondation de données, MLflow, Unity Catalog et Unity Gateway, ce qui évite l'hétérogénéité constatée chez des concurrents comme Foundry ou Bedrock ([00:11:13](#00:11:13)). Eric Latour demande à consulter les documents d'architecture globale pour aligner la présentation ([00:13:42](#00:13:42)).

* **Structure macroscopique et visuelle de la pyramide architecturale**: Eric Latour suggère d'ajouter une représentation visuelle sous forme de pyramide ou d'étapes dans l'application pour situer chaque chapitre dans l'architecture macroscopique (fondation de données, ML et model serving, orchestrateurs et frameworks) ([00:15:36](#00:15:36)). Mehdi Lamrani accepte d'intégrer des surcatégories colorées pour clarifier la progression ([00:16:29](#00:16:29)).

* **Fondations de données et stockage open table**: Mehdi Lamrani présente les capacités de stockage de tables ouvertes prenant en charge le traitement par lots (batch) et le streaming, ainsi que la maintenance transactionnelle sur la même plateforme ([00:17:28](#00:17:28)). Mehdi Lamrani et Eric Latour conviennent d'ignorer les détails superflus sur l'OLAP pour se concentrer sur la vision intelligence artificielle, tout en soulignant l'importance du catalogue de données et de la qualité des données gérés par Unity Catalog ([00:18:46](#00:18:46)).

* **Cycle de vie de la science des données et MLflow**: Mehdi Lamrani détaille le support des notebooks, l'utilisation concurrente, le Feature Store (où chaque caractéristique est construite une fois et réutilisée), l'accompagnement du cycle MLOps via MLflow pour le suivi des expérimentations, l'AutoML pour la recherche d'algorithmes, ainsi que l'entraînement distribué sur GPU ([00:19:41](#00:19:41)).

* **Couche de service des modèles et Foundation Model APIs**: Mehdi Lamrani explique la couche unique de service pour les modèles personnalisés et les Foundation Model APIs, incluant la mise à l'échelle automatique jusqu'à zéro et la facturation par jeton. Eric Latour ajoute un commentaire sur la transition historique du model serving vers Unity Catalog pour la gestion des agents, permettant une scalabilité supérieure ([00:22:57](#00:22:57)). Mehdi Lamrani précise que les Foundation Model APIs permettent d'accéder aux modèles de tiers (Anthropic, OpenAI, Google) via une API unique pour s'affranchir de la dépendance envers un unique fournisseur ([00:23:48](#00:23:48)).

* **Gestion des modèles externes et gouvernance centralisée**: David Dokhan quitte temporairement la réunion pour un point sur l'observabilité. Mehdi Lamrani expose la gestion des modèles externes permettant de suivre, auditer et centraliser les clés API et les secrets, évitant ainsi le contournement des politiques de sécurité et le manque de visibilité sur les coûts ([00:25:43](#00:25:43)).

* **Fonctions d'intelligence artificielle et recherche documentaire RAG**: Mehdi Lamrani présente les fonctions d'intelligence artificielle permettant d'extraire, classifier, résumer, traduire, masquer et analyser des documents directement depuis SQL ou des pipelines sans déplacer les données ([00:26:55](#00:26:55)). Mehdi Lamrani et Eric Latour abordent le RAG et la distinction entre les solutions gérées comme AI Search et les approches personnalisées basées sur Lakebase search pour configurer les embeddings et le classement ([00:31:35](#00:31:35)).

* **Protocoles MCP et connecteurs d'agents**: Mehdi Lamrani détaille les connecteurs MCP (Model Context Protocol) offrant un dépôt centralisé pour les connexions sécurisées (Google Workspace, Microsoft, Slack, GitHub) et la possibilité d'héberger des serveurs MCP personnalisés ou gérés ([00:35:08](#00:35:08)). Mehdi Lamrani mentionne le développement d'agents personnalisés avec choix de la mémoire et des frameworks (LangChain, OpenAI) exécutés dans des environnements isolés ([00:36:23](#00:36:23)).

* **Environnements isolés pour l'exécution de code**: Eric Latour explique le fonctionnement des sandboxes Databricks, qui permettent à un agent d'exécuter du code généré dans un environnement isolé afin de réduire la surface d'attaque. Mehdi Lamrani s'enquiert de la facturation et du monitoring, et Eric Latour confirme que la facturation s'effectue à la seconde d'utilisation de l'environnement sandbox ([00:40:22](#00:40:22)).

* **Évaluation, traçabilité et standardisation avec MLflow 3.0**: Mehdi Lamrani et Eric Latour insistent sur l'importance du suivi des agents et de l'évaluation via MLflow 3.0 ([00:47:59](#00:47:59)). Eric Latour souligne que MLflow 3.0, basé sur OpenTelemetry, constitue une norme open source pour l'instrumentation des agents, et recommande de positionner cette technologie comme un standard de l'industrie, qu'il s'agisse de cibler Databricks ou non ([00:49:52](#00:49:52)). Mehdi Lamrani note ces éléments pour structurer les diapositives d'évaluation et de traçabilité des exécutions et des versions ([00:51:31](#00:51:31)).

* **Restructuration de la présentation et priorisation des sujets MLOps**: Mehdi Lamrani et Eric Latour examinent la structure de la présentation et décident d'écarter des éléments jugés trop techniques tels que Customer Lake, product registry, model serving scale et CI monitoring. Iels conviennent d'isoler les sujets MLOps et CD dans une section spécifique intégrant la description de MLOps et les automation bundles ([00:56:37](#00:56:37)). Eric Latour soulève la question de la vision stratégique concernant les agents, et Mehdi Lamrani précise qu'un versionnage via le model registry sera privilégié par rapport à un serveur de suivi Mflow ([00:59:44](#00:59:44)).

* **Ajustement de la section opérations de production et outils de développement**: Eric Latour met en avant l'importance accordée par les interlocuteurs au support du day two, incitant Mehdi Lamrani à replacer la section sur les opérations de production en amont du parcours ([01:00:48](#01:00:48)). Concernant les outils de développement, Mehdi Lamrani liste l'utilisation de Databricks Apps, Jny Nicod, kit et Ominent, tandis qu'Eric Latour mentionne l'intégration d'un modèle Claude spécialisé. Mehdi Lamrani valide la prise en compte de ces retours et décide d'adopter une approche globale inspirée du modèle Amadeus ([01:01:29](#01:01:29)).

* **Intégration d'éléments visuels et ergonomie du support de présentation**: Eric Latour suggère d'incorporer des images en plus des insertions de diapositives pour illustrer la navigation, ce qu'approuve Mehdi Lamrani. Mehdi Lamrani signale un dysfonctionnement technique mineur lié au mode hors-ligne du code de stratégie avant de présenter le système de repères visuels par cases ([01:02:41](#01:02:41)). Eric Latour se félicite de la profondeur technique et de la cartographie proposées, tout en insistant sur la nécessité d'une mise en contexte globale initiale et d'un support visuel constant pour capter l'attention sur la durée d'une heure ([01:03:56](#01:03:56)).

* **Organisation de l'introduction et gestion du temps de la réunion**: Eric Latour propose d'animer une introduction de 2 minutes pour poser le cadre, rappeler les attentes sur l'état des produits, leur maturité et la vision globale, tout en posant la limite d'un format d'une heure qui ne permet pas d'approfondir techniquement chaque sujet. Mehdi Lamrani marque son accord sur cette démarche. Eric Latour indique qu'iel formalisera en clôture ou de manière asynchrone les sujets nécessitant des sessions de travail approfondies (deep dive) ([01:04:41](#01:04:41)).

* **Planification des prochaines étapes et validation finale du support**: Mehdi Lamrani confirme l'application de l'ensemble des modifications discutées et propose de soumettre le support mis à jour à Eric Latour aux alentours de 14h30. Eric Latour valide cette proposition et confirme sa disponibilité pour examiner le document ([01:05:31](#01:05:31)).

*Nous vous conseillons d'examiner les notes de Gemini pour vérifier qu'elles ne contiennent pas d'erreur. [Profitez de nos astuces et découvrez comment Gemini prend des notes](https://support.google.com/meet/answer/14754931)*

*Que pensez-vous de la qualité de **ces notes spécifiques ?** [Participez à une courte enquête](https://google.qualtrics.com/jfe/form/SV_5bXzKQfylMIhSXc?confid=wwWvD18g38p89IRlrxRODxIVOBEQAjIGCIoCIAAYAwg&detailLevel=standard&hasImages=False&entryPoint=footerMain&isGoogler=False&lang=fr-FR) pour nous faire part de vos commentaires et nous dire si ces notes vous ont été utiles.*

# **📖 Transcription**

oct. 12, 2026

## **\[Dry Run\] AI Capabilities and vision \- Transcription**

### **00:00:00** {#00:00:00}

**Eric Latour:** de ce qui est au cours d'un toujours en cours de de développement ou de release et ainsi de suite. être très clair pour tester des choses qui sont en release en qui sont pas encore PR ready mais on veut le savoir quand on les teste.

**David Dokhan:** Ouais, c'est faire. OK.

**Mehdi Lamrani:** Ouais. Bah ça ça fait partie des choses que j'ai mis en valeur dans mon dans mon doc.

**David Dokhan:** Et et nous, on a une intuition sur là où on veut les emmener. C'est quoi nos où est-ce qu'on veut les emmener complètement ? Où est-ce qu'on veut emmener Pierre ? Est-ce qu'on veut l'emmener sur le sur les Gateway ? qu'on veut l'emmener plutôt sur la partie sur la partie bricks anciennement à John Bricks. Peut-être un sujet chaud à gérer d'ailleurs. Euh si s'ils avaient eu s'ils avaient déjà été sollicités sur ces sujetsl c'est quoi notre intuition là-dessus de ce qui va ce qu'on pourrait leur vendre ?

**Eric Latour:** indusion, il y en a deux euh il y en a trois même en fait.

### **00:00:50**

**Eric Latour:** les trois thématiques sur lesquelles on peut essayer de le revendre, c'est une qui est ML traditionnel parce qu'en fait actuellement ils sont

**David Dokhan:** Ok.

**Eric Latour:** sur Azure machine learning qui est de la merde et que bah globalement il y a quand même un peu de pépette à les récupérer de les basculer. Toute la data est déjà sur data brick ça aurait quand même du sens qu'il fasse le trading directement sur data brick plutôt que sur plutôt que sur sur Azure Machine Learning sachant que c'est un

**David Dokhan:** Même ils font du training.

**Eric Latour:** produit pardon.

**David Dokhan:** Ils font du training chez eux.

**Eric Latour:** Ouais ouais. Ils ont des équipes de de data scien sist, ils font du training. Après, c'est pas des centaines de millions par an, hein, mais ils en font quand même.

**David Dokhan:** OK.

**Eric Latour:** Euh et actuellement, ils le font sur Azure Machine Learning qui est un produit qui est pas sunset mais qui est presque tout comme côté côté Microsoft. Voilà. Euh, ça c'est le premier point. Le deuxième c'est de les embarquer sur l'hébergement d'agent d'agent sur sur un sur bricks.

### **00:01:42**

**Eric Latour:** Donc là la partie agent brick custom agent et ainsi de suite. Et le troisème ce serait du coup il a presque quatre mais le troisème ce serait quand même Jenny ça intéresse. Mais plutôt le Jenny dans le sens talk to my data. Tu vois les Jenny, les Jenny Agent, Jenny One, ça l'intéresse. Jenny ontologie, ça va l'intéresser. Le Jenny code et Jenny apps builder, il en a rien à carré,

**David Dokhan:** et Genny tour data,

**Eric Latour:** tu vois le

**David Dokhan:** on se fracasse pas à à Microsoft qui a MB dans tous ces outils des choses similaires.

**Eric Latour:** Non, parce que c'est parce que toute la data est déjà sur Databrix.

**David Dokhan:** Ouais.

**Eric Latour:** C'est ça en fait la grosse différence et notamment tous les trucs de de Microsoft en tout cas à

**Mehdi Lamrani:** Hop.

**Eric Latour:** dat ils indexent très très mal le parquet et donc c'est pas du tout prévu pour ça en fait.

**David Dokhan:** OK.

**Eric Latour:** Euh

**David Dokhan:** Et je vois pas je vois pas Gateway. Du coup, tu l'as on on a envie

### **00:02:36** {#00:02:36}

**Eric Latour:** c'était le 3è 4e c'était ça aurait été justement la partie gateway observabilité

**David Dokhan:** ou pas qu'ils aillent sur Gateway ?

**Eric Latour:** transverse de machin.

**David Dokhan:** On a envie qu'ils aillent sur Gateway ou pas ?

**Eric Latour:** Ah bah on aurait envie. Oui, à terme.

**Mehdi Lamrani:** On

**David Dokhan:** Les mecs Ubisoft on dit surtout surtout surtout les emmène pas sur Gateway. C'est c'est Ils l'ont dit ça en rigolant. Mais euh je je vo l'équipe de compte

**Mehdi Lamrani:** Ah non non, qui t'a dit ça ? Clément ou non ?

**Eric Latour:** Je reviens,

**David Dokhan:** globalement

**Eric Latour:** je me chercher un

**Mehdi Lamrani:** Non, c'est pas ce que j'ai C'est pas ce qu'ils m'ont dit. Ouais, c'était disons Non,

**David Dokhan:** dis tu veux pas d'emmerde.

**Mehdi Lamrani:** non, mais disons disons disons que Ubisoft a essuyé les plâtres.

**David Dokhan:** Ouais.

**Mehdi Lamrani:** Ubisoft a fait, j'aurais été Moi, j'aurais été sur Ubisoft, je l'aurais dit. Euh c'est simple. Enfin, moi je joue plus à la roulette avec Data Brix, j'attends que ça sèche.

### **00:03:23**

**Mehdi Lamrani:** Euh un exemple, ENT Bricks, j'ai pas tu trouveras pas un seul de mes clients sur à qui j'ai dit va sur BCKS.

**David Dokhan:** OK.

**Mehdi Lamrani:** J'ai toujours j'ai pas bâché mais j'ai les ai toujours gentiment orienté vers du custom parce que j'attendais de voir comment ça prenait. mon intuition a été bonne.

**David Dokhan:** Ouais.

**Mehdi Lamrani:** Donc

**David Dokhan:** Soyons customer obsess et gardons notre casquette de Trusty Advisor. Ne ne nous cramons pas effectivement.

**Mehdi Lamrani:** voilà,

**David Dokhan:** Je suis d'accord avec

**Mehdi Lamrani:** donc c'est très gentil. Je suis d'accord avec Alie, je suis d'accord avec Arsalon dans l'ensemble. Allez, allons-y, fonçons. Mais euh toujours un petit peu avec circonscription. On attend de voir ce que ça donne. Moi, j'ai j'ai un œil dessus sur le channel API Unity Gateway, ça pop toutes les 10 minutes, hein. Donc euh on va positionner, moi c'est ce que j'ai fait avec, j'ai positionné mes pions, il joue avec, il regarde mais sur des workspace qui sont pas critiques. Le bouton euh big bang pas tout de suite.

### **00:04:20** {#00:04:20}

**David Dokhan:** OK,

**Mehdi Lamrani:** Voilà,

**David Dokhan:** C'est

**Mehdi Lamrani:** maintenant il y a toute une inertie euh qui va se mettre en place le temps que ça remonte au cerveau, qu'il l'utilise, qu'il comprennent un peu le truc, que d'ici là, ça sera sec. et ça commence déjà à être sec. Le seul la seule erreur tactique pas stratégique en fait que qu'à euh qu'a commis le compte Ubisoft, c'est de d'être trop en avance de phase. Ils ont commencé à le vendre dès le mois d'avril mai. Voilà. Maintenant, de tout ce que j'ai vu, j'ai refait un point avec Clément. Fin septembre,

**Eric Latour:** Ja.

**Mehdi Lamrani:** il y a eu 80 60 70 % des choses qui ont été qui qui commencent à sécher. Voilà.

**David Dokhan:** OK. OK. Et donc pour tout ça, on a une donc j'ai vu ton appli, c'est top. Et donc on a on a une presse aussi. Du coup euh

**Mehdi Lamrani:** Oui. Alors du coup, j'ai mis à jour la presse. Hop.

### **00:05:12**

**Mehdi Lamrani:** Screen. Ils ont changé.

**David Dokhan:** que je je je sais pas du tout pour mettre la pression,

**Mehdi Lamrani:** Ils ont changé.

**David Dokhan:** mais je suis pas sûr qu'on ait beaucoup de on a beaucoup de cartouches avec avec

**Mehdi Lamrani:** Euh déroule ton idée. C'està dire qu'on a qu'une qu'une faut qu'on soit bon.

**David Dokhan:** il faut qu'on soit bon. Je suis sûr que vous allez Non,

**Mehdi Lamrani:** Ouais. Ouais. Ouais.

**David Dokhan:** mais je suis sûr que vous allez être bon.

**Mehdi Lamrani:** Ouais.

**David Dokhan:** Mais faut que faut les emmener quoi.

**Mehdi Lamrani:** Aprèsement,

**David Dokhan:** Faut les

**Mehdi Lamrani:** moi je vais pas te je vais pas te vendre du rêve. Euh dans ce genre de de situation, c'est du 60 70 30 euh ça dépend vraiment de comment on est challengé.

**David Dokhan:** Ouais.

**Mehdi Lamrani:** qui on a en face la pétence ou la le pouvoir de rejection, tu vois le pouvoir la la perméabilité de de l'audicre. Si on se fait challenger, nous on va tenir notre notre position. Mais voilà, on va on va on va vraiment essayer d'être impactant.

### **00:06:04**

**Mehdi Lamrani:** Maintenant euh il y a des choses qui ce que je veux dire, c'est que ce qui revient euh ce qui nous revient, notre part, on va la faire au maximum quoi. Maintenant, il y a des intrans qui sur lequel on a pas total.

**David Dokhan:** sûr.

**Eric Latour:** Oui, mais tout à fait. Après, moi je pense qu'ils seront euh moi je enfin tu vois Pierre et de ça, ils sont curieux en fait, ils vont avoir envie de d'écouter ce qui est important et tu vois moi c'est quand je vois le les 11 points en 1 heure et ainsi de suite et je suis du coup je suis curieux parce que il y a toujours le tu sais il y a le slide, il y a le story, il y a le storyting on top qui la différence.

**Mehdi Lamrani:** Exactement.

**Eric Latour:** Donc je suis curieux de voir un peu comment tu comment tu structures ça parce que je pense faut réussir à les emmener. Tu vois, j'ai bien aimé ce qu'il a dit tout à l'heure David, c'est les emmener c'est il y a un peu un côté storytelling, c'est quoi l'histoire qu'on leur raconte de ce qu'on avait discuté ?

### **00:06:46** {#00:06:46}

**Eric Latour:** Bah en fait sur le machine learning, on est très bon. On est on a été quand même des top leaders sur la partie ML. Bah c'est quand même pas déconnant qu'on soit aussi très bon sur la partie Jenny et qu'on construise des bons outils parce que ce qu'on fait c'est de construire des outils. Voilà, pardon, je te laisse dérouler,

**Mehdi Lamrani:** Ouais. Ouais.

**Eric Latour:** je suis curieux du coup.

**Mehdi Lamrani:** Euh alors c'est moi moi je vais dire je vais juste avant euh je vais dire comment ça s'est passé chez Emirates. On avait exactement le même challenge sauf qu'on avait une semaine. Euh ils nous ont dit "On n pas temps, vous avez 3h euh 2h30 et euh on va arrêter. Enfin faut faut que vous délivriez tous vos messages." On est venu sur place, on a délivré ils ont eu tellement de questions qu'on a refait des sessions de 2h tous les jours jusqu'à la fin de la semaine et tout d'un coup ils se sont libérés. Donc faut créer de la pétence, euh être là, répondre à toutes les questions.

### **00:07:37** {#00:07:37}

**Mehdi Lamrani:** Euh mais par rapport à euh au temps qui est imparti, je n'ai moi dans ma tête, j'ai un déroulé euh qui va prendre 1 heure, mais il va falloir piocher. Je peux pas tout dérouler en une heure. Donc c'est là où j'ai besoin. C'est pour ça qu'on fait ce dry run.

**Eric Latour:** Et ben super trop bien.

**Mehdi Lamrani:** Quel que soit moi en fait c'est fait.

**Eric Latour:** OK. Ça me rassure en fait.

**Mehdi Lamrani:** Voilà,

**Eric Latour:** Ça me rassure, c'est que tu me dis c'est que tu vas pick and shoot parce que je genre je sais pas à quelle vitesse il va parler,

**Mehdi Lamrani:** moi c'est Ah non non mais je suis obligé en fait le

**Eric Latour:** ça va aller drôlement vite.

**Mehdi Lamrani:** c'est ce que je pour tout le dire. On a on a un peu des des des challenges similaires avec ma femme. On en a discuté, je lui dit de toute façon moi parce que j'ai passé j'ai passé une partie du weekend dessus, je couvre tout et derrière en fait je suis obligé d'avoir une surface complète mais je vais pas tout couvrir.

### **00:08:27**

**Mehdi Lamrani:** C'està dire que au moment où il m'attaque sur ça ou il me dirige vers ça, regarde je donner juste un exemple ici je vais taper flow. Voilà. Tac. Ouais. Voilà. Experiment tracking de ML ML Flow. Tac. Et je vais dessus. Voilà. J'ai mon interface est vraiment faite de façon à ce que euh si on m'interromp dans mon storytelling, je je peux cliquer exactement là où il faut et être. Voilà. Bon, maintenant euh c'est encore working progress, mais l'idée je vais euh sûrement revoir un petit peu ressortir en gras les points importants, mais voici l'histoire. Je parle des challenges, donc les le fait que la data c'est en anglais, on est d'accord.

**Eric Latour:** Oui oui oui oui oui. M.

**Mehdi Lamrani:** OK. Spread across systems. Je t'explique pourquoi j'ai rajouté ça parce que tu m'avais dit que tu vois ça ça manquait un petit peu de de visuel. Euh on a besoin de productivité et de reproductivité de regrouper les modèles provider.

### **00:09:44** {#00:09:44}

**Mehdi Lamrani:** Euh, on a besoin de sécurité, de safety aussi et de gouvernance pour les agents. Euh,

**David Dokhan:** C'est c'est des choses qui ont été partagées par Amadeous ou c'est plutôt les génériques challenges de

**Mehdi Lamrani:** ça c'est les Ah,

**David Dokhan:** ailleurs.

**Mehdi Lamrani:** ça c'est les générique challenges.

**David Dokhan:** OK.

**Mehdi Lamrani:** Voilà,

**Eric Latour:** Ouais ouais maison qui ring belle qui

**Mehdi Lamrani:** ça j'ai gardé après c'est ça m'étonnerait enfin

**David Dokhan:** Non non, je veux que je

**Eric Latour:** ring belle chez eux.

**Mehdi Lamrani:** moi moi j'ai croisé avec ce que bah tout ce que j'ai vu euh du bout de malette à moi. Amadeous Amadeus a les mêmes problèmes que tout le monde.

**David Dokhan:** Ouais. Oui ou

**Mehdi Lamrani:** Voilà donc après voilà euh customer and security data. Donc voilà, ça c'est pour dire qu'il faut que le business domaine soit aligné avec les les philos en terme de localisation de data residency et de sécurité et les AI Pilot n'arrivent pas à les en production. Ça c'est la situation globale. Maintenant euh pour pouvoir résoudre ça, il faut une fondation data euh des fonctionnalités data science, donc avec le data science Life Cycle, euh avoir une gouvernance et accès aux modèles qui sont mis à disposition, gouvernance commune, que ce soit pour euh la partie datacience ou la partie AI.

### **00:11:13** {#00:11:13}

**Mehdi Lamrani:** Euh mon fil conducteur est de dire que on a d'abord créé ML Flow, on a d'abord créé les features store et toutes les features data séance et ensuite on a passé à l'a moderne avec les LLM euh tout ce qu'il y a autour et la Gen mais ça procède

**Eric Latour:** Ok.

**Mehdi Lamrani:** de la même vision. Donc on c'est on a pour la partie data, on a Unity Gateway et aujourd'hui on a Unity pardon, on a Unity Catalog. Aujourd'hui, on a Unity Gateway avec toute la partie ops et ça procède d'un même environnement. Donc il y a pas de rupture contrairement à ce qui peut être vu dans des produits comme Fundry ou Bedrock où vous avez un côté le monde, un côté le monde data, un côté le monde GNI. Et tout ça est un petit peu euh hétérogène. Nous, on a une fondation commune. Ensuite, on a des fonctionnalités pour construire les agents, pour les évaluer, pour les gouverner et une couche pour permettre aux business users d'accéder à l'AI facilement. Enfin, on a des outils de Developer Tools qui permettent de faciliter le développement et faciliter l'accès au déiliter via des API, faciliter via des AIS et en il y a les domain applications et le production operations avec les CD et tout le reste.

### **00:12:42**

**Mehdi Lamrani:** Voilà, ça c'est un petit peu le arche. Je compte d'ici peut-être 1 heure faire un premier slide. qui résume tout ça global. Si tu as d'ailleurs Éric, si tu as si tu as des si tu as des slides, moi ici j'ai mes dex si tu veux. J'ai vraiment j'ai listé tous les dex. D'ailleurs, si on revient euh si on revient ici par exemple, tu vois par exemple Agent Brix use case guide, j'ai ça et derrière si je clique dessus, il me renvoie au deck qui va bien.

**Eric Latour:** M.

**Mehdi Lamrani:** Tu vois, ça me permet de d'éviter de de jongler entre mes

**Eric Latour:** Ouais ouais ouais. Ça permet de de ça fait le ça fait le graphe presque de de de la du des sources.

**Mehdi Lamrani:** des documentations. Exactement.

**Eric Latour:** Ouais exactement.

**Mehdi Lamrani:** Et ça c'est un projet à part dont je te parlerai plus tard mais je suis en train de généraliser ça et parce que finalement on fait on refait la même chose avec touses les équipes de toutes les équipes de voilà.

### **00:13:42** {#00:13:42}

**Mehdi Lamrani:** Euh donc toi si tu as euh des documents euh qui reprennent un peu l'architecture globale de l'ensemble de datab ou des choses comme ça qui qui sont le lient global, n'hésite pas à partager. C'est c'est ce que je vais produire là dans leur tissu. Donc

**Eric Latour:** OK bah envoie-moi le lien dès que tu l'as parce qu'il y en a un qui est pas mal et qui qu'on avait pour le di mais sais qui est le nouveau là qui te Adica, gouvernance machin. Je trouve que pour cette tu as la comme introduction pour dire bah voilà comment c'est actuellement et maintenant on va les suivre. Je pense que ça il est vraiment bien ce slide là du dernier.

**Mehdi Lamrani:** partage. Je sais pas si je l'ai ou pas, il y en a tellement.

**Eric Latour:** Ouais bah mets-moi ton mets-moi le lien de ta présentation,

**Mehdi Lamrani:** Mais dans dans le do dans le do

**Eric Latour:** je te le copiercollerai dedans.

**Mehdi Lamrani:** euh Non, envoie-moi envoie-moi Slack parce que ma présentation c'est une app.

**Eric Latour:** Non, je te le trouve tout de suite.

### **00:14:40**

**Eric Latour:** Je te le trouve après là.

**Mehdi Lamrani:** Ouais. OK. Donc allez, je déroule je je je déroule en super accéléré. Donc je vais très rapidement passer sur ça. Je vais pas le dérouler en détail parce que c'est pas le sujet mais je l'ai expliqué qu'on a toujours cette cette organisation cette construction. La fondation c'est la data. Au-dessus, on a une catalogue. Au-dessus, on a les capacités data science avec les notebook et le comput et ensuite on généralise avec l'Id et la gouvernance. A et une c'est un petit peu le triangle qui qui la pyramide qui se construit par la base. Donc euh la première des choses, c'est euh Oui.

**Eric Latour:** Je peux je peux me permet un truc du coup c'est l'aventure pour ton app. J'adore l'idée de ça des steps et en fait si tu l'avais en visuel quelque part quand tu déroules,

**Mehdi Lamrani:** Oui.

**Eric Latour:** tu vois sur le côté là,

**Mehdi Lamrani:** Euh ce que tu veux,

**Eric Latour:** il te reste de la place avec les chapter si tu voyais

### **00:15:36** {#00:15:36}

**Mehdi Lamrani:** je sais ce que tu veux. Je sais ce que tu veux. Je sais ce que tu veux. Je vais te montrer. Je l'ai déjà fait euh pour euh

**David Dokhan:** H

**Mehdi Lamrani:** Emirates euh 2 secondes. Strategy Je pense que ce que tu veux c'est ça. Regarde. Ce que tu veux c'est un truc comme ça ici là en dessus. Regarde ce que ça va faire. Tac tac tac. Ici là.

**Eric Latour:** Attends, je t'ai perdu. Je t'ai perdu, je t'ai perdu. Ouais, voilà, un truc comme ça. Moi, je l'aurais même été genre moi je un truc plus simple. Moi, je t'aurais vraiment fait le sais, tu me parlais de la pyramide à genre quatre niveaux et tu sais d'avoir en gros un logo. Moi je fais mais c'est un peu c'est dire la progression. Où est-ce que tu es dans cette pyram ?

**Mehdi Lamrani:** En fait ici le chapter mais le chapter en plus en

**Eric Latour:** Ouais. En fait, tu as les chapter mais tu vois bah ouais,

### **00:16:29** {#00:16:29}

**Mehdi Lamrani:** visuel enfin le chapter parce que il y a il y a déjà le chapitrage.

**Eric Latour:** ça peut être en visuel, tu vois, dans cette pyramide, c'est genre Ah, je suis là, je monte.

**Mehdi Lamrani:** Regarde si je vais question si je vais ici à Data Science Life Cycle ça ça déroule mais toi ce que tu propose là c'est quelque chose de de visuel parce que en gros c'est ça on a un de les étapes de 1 de 1 à 10 et on on déroule

**Eric Latour:** Ben, je trouve que je trouve que tuas trouve que tu ce que tu j'avais l'impression que ta pyramide dont tu me parlais en fait, elle était plus macro que toutes ces choses-là. En fait, tu as le data foundation. Je suis d'accord sur le premier, mais tu vois, en fait, tu vas pas faire apparaître domaine application production operation dans ta pyramide.

**Mehdi Lamrani:** Non.

**Eric Latour:** Ça va être le dernier. Tu vois, c'est pour ça que je te disais en fait je pour y a deux choses. Il y a la la structure de des chapters et à côté il y a la vision de où est-ce que chaque chapter se range dans un truc macro qui est data foundation ML and and model serving orchestrator and framework.

### **00:17:28** {#00:17:28}

**Mehdi Lamrani:** Ouais, je vais je vais je vais je vais créer des surcatégories, pas des sous-catégories mais des surcatégories colorées si tu veux ou savoir un petit

**Eric Latour:** Non, trop bien.

**Mehdi Lamrani:** peu.

**Eric Latour:** Juste été une idée. Excuse-moi,

**Mehdi Lamrani:** Non non non mais ok.

**Eric Latour:** je t' loupé dans le con.

**Mehdi Lamrani:** Anyways, c'est Non non, tu m'as pas coupé du tout de toute façon c'est c'est l'exercice. OK, donc on passe la partie de challenge, on passe à la fondation directement. OK. Donc historiquement, on a un stockage de table open table et j'ai toujours en fait j'ai toujours orchestré de cette façon enfin organisé de cette façon. D'abord, il y a en résumé comp c'est

**David Dokhan:** H

**Mehdi Lamrani:** un peu les ça c'est la solution single format now serves batch and streaming like et c'est pour ça qu'on a data lake et un petit peu les détails techniques pour chacun l'inestion transformation et table maintenance transactional data on the same platform là c'est le base. Donc on explique pourquoi on a ramené le l base.

### **00:18:46** {#00:18:46}

**Mehdi Lamrani:** Euh real time analytics on operation data dashboard application read of ste copy. Là j'ai introduit le lentement euh c'est qu'il y avait de monde. Vous avez le OLAP ou LTE.

**Eric Latour:** Ouais, mais moi tu as ça par exemple, je suis pas sûr de voir le lien avec la partie I vision.

**Mehdi Lamrani:** Ça je peux il y en a aucun. C'est pour ça que je propose de skipper cette partie complètement.

**Eric Latour:** Moi on skip. Ouais,

**Mehdi Lamrani:** OK.

**Eric Latour:** on skipe ça.

**Mehdi Lamrani:** Euh en fait ça je vais je vais pas en parler. En fait, ce que je vais dire, ce que je propose de dire, c'est tout ça le regrouper en un seul slide en lui disant on a ses capacités, on peut ingérer, transformer la la data,

**Eric Latour:** Voilà.

**Mehdi Lamrani:** on peut avoir la partie transactionnelle.

**Eric Latour:** Et et pour Amadeus, votre data est déjà là. C'est l'endroit où votre data.

**Mehdi Lamrani:** Oui. N'hésite pas à m'interrompre,

**Eric Latour:** Ouais ouais t'inquiète je je vais quand même faire attention.

### **00:19:41** {#00:19:41}

**Mehdi Lamrani:** n'hésite pas à combler en fait ce genre de choses et de me dire voilà euh real time, voilà, data catalogue and data quality, ça c'est important par contre. J'explique que tout ce qui va découler de l'AI va interagir. Que fait l'AI au final ? Ai read and interact through tools with data and resources. So data catalog and data quality already by unity catalog. Ok so we have two branches data science and more recently Gen AI and LLM AI for data data science life cycle uh we provide notebooks and data exploration where data scientists work in notebooks uh they can run whatever language they want uh there is concurrency usage several people editing the same notebooks and um it's universal frameworks. Ça là s' me pose des questions, je peux repasser sur la sur cette partie et faire un Tu vois, si jamais il me pose la question et pour revenir, je me reviens dans ma story directement. Donc je peux faire des apartés, je pourrais pas parler de tout. Ça je propose de leur dire au fur et à mesure enfin au début je vais tout dérouler.

### **00:21:14**

**Mehdi Lamrani:** S'il y a des points de détails sur lesquels vous voulez deep dive ou juste faire un un zoom, pas deep dive mais zoomer, manifestez-vous et autrement je partirai du principe que le niveau de profondeur que que j'aborde vous est suffisant. Le feature store each feature is built once and reused by every team every model. Uh we also provide experiment tracking through MLO and auto so ML flow records every training run with its parameters metrics versioning and it uh also uh covers the whole uh MLOPS life cycle and auto provides an algorithm um search grid that tries every algorithm and uh writes the trials and results to uh the registry in order to keep the best model available. Distributed training and GPUs are offered. Training is no longer limited by hardware or by access to GPUs. So we offer distributed training uh across GPUs and also AI run types model access and governance. Um so putting the model into production no longer takes dedicated infrastructure. We offer one single infrastructure and we serve all the models. And here it's important to state that we have uh one single um serving layer for both uh foundation model APIs um or any custom model and data science.

### **00:22:57** {#00:22:57}

**Mehdi Lamrani:** So we need minified the same model uh serving layer.

**David Dokhan:** Tu pouras juste redemander sur le modèle serving er Sí,

**Eric Latour:** Ouais, je pense que là ce serait intéressant que tu fasses un petit commentaire. J'allais ce que j'allais dire sur le fait que initialement notre il y a au début on pensait que les agents allaient être servis comme des modèles, donc à travers modèle serving parce que c'est comme ça qu'on faisait les agents historiquement et que finalement ça basculé sur

**Mehdi Lamrani:** Oui. Oui,

**Eric Latour:** la tab.

**Mehdi Lamrani:** c'est vrai.

**Eric Latour:** faire un petit commentaire là-dessus parce que c'est un sujet de bref, c'est un truc avec Garvea et ainsi de suite.

**Mehdi Lamrani:** Super important. Super important. OK, de toute façon, c'est noté.

**Eric Latour:** Ouais, au pire si tu le zap,

**Mehdi Lamrani:** Euh non,

**Eric Latour:** c'est moi qui le dirai à l'oral. Enfin, tu vois,

**Mehdi Lamrani:** je

**Eric Latour:** c'est juste sois pas surpris si je le dis à un moment et dire qu'en fait on s'est rendu compte et notamment parce qu'en fait ça permet d'avoir une scalabilité euh qu'on a pas avec modèle serving parce que la façon le modèle serving était construit, c'était que ça répondait façon et ça bref.

### **00:23:48** {#00:23:48}

**Mehdi Lamrani:** ag ça c'est mes notes, ça sera pas oublié. Ok. Um, end point scale with demand. down to zero. Donc on a le zero scale et le scale scale zerale per token provision. Voilà. foundation models. for language models depending on one provider creates login token spent grows unpredictably models from different providers artisted unit uh in a uh model by model fashion and this creates a scattered division and the scatter governance the dependency on any single vendor goes away through foundation model uh api it gives access through one API models from providers that include Antropic Open AI Google and others uh build per token. Uh new versions arrive on olders are retired as they come and we publish the supported models and the retirement dates as they go. All i uh calls are uh centered around the same architecture and the same gateway and moving to a newer model stays a small change. So you can switch whatever model you use for your applications through that same AP. Um we offer model finding capabilities if you need to adapt a model to your inhouse data.

### **00:25:43** {#00:25:43}

**Mehdi Lamrani:** G effent. Ça je vais pas trop en parler parce que personne ne fait ils sont pas concernés.

**David Dokhan:** Je fais je fais juste une petite petite aparté. On a le meeting observability. J'y vais. Je sais pas si tu veux venir Eric ou pas.

**Eric Latour:** Non non, moi je reste là-dessus, c'est plus important.

**David Dokhan:** Je je leur fais l'update. OK,

**Eric Latour:** Ouais,

**David Dokhan:** je pas de souci.

**Eric Latour:** tu me pinges si jamais il y a un truc.

**Mehdi Lamrani:** Salut.

**David Dokhan:** Co?

**Eric Latour:** À plus.

**Mehdi Lamrani:** Alors,

**Eric Latour:** External modè,

**Mehdi Lamrani:** external models.

**Eric Latour:** ça va ça peut intéresser.

**Mehdi Lamrani:** OK.

**Eric Latour:** Je pense

**Mehdi Lamrani:** Donc outside models are tracked on audited like the others. Uh so you might need to call models that areed directly at a provider but the problem is you have two problems. API keys end up scattered across cold and people and these calls bypass security with no view of what uh no view of the cost. So um with external models serving through FMEPI they can come under the same control as the rest and they registered as external models with key stored centrally and secrets.

### **00:26:55** {#00:26:55}

**Mehdi Lamrani:** Il faut que je plug aussi ici. Euh plug et mais je suis encore en train de parler de j'ai pas encore parlé d'agents mais bon. OK. building ag ça c'est ça va changer c'est function docum large volumes of documents without moving data ai functions model or any model you like from sequel or pipeline to classify extract summarize data and documents scal je vais pas faire de dém mot j'ai pas le temps une honnêtement après sil veulent

**Eric Latour:** Non non non mais là par contre tu par exemple je te couperai la parole enfin je rajouterai un truc qui est bah par exemple l'article que je vous ai fait suivre en le mail que je vous avais préparé sur AI AI descide c'est c c'est c'est une function disponible M.

**Mehdi Lamrani:** exactement exactement euh du coup je pense j'ai attends c'est pas du tout ça attends là je suis sur function ça c'est intéressant faudrait qu'il rajoute ça c'est pas grave Voici donc we have functions directly um functions like part document extract content classify prep search search or enrich you can transcribe translate summarize mask and uh also you can analyze sentiment similarity and decide structur decision choices and probabilities.

### **00:28:53**

**Mehdi Lamrani:** OK, donc je passe à la suite. Je parle un peu du rag. Euh tout ça, je bon, j'ai j'ai je suis en train de renommer les titres. J'ai fait un travail propre.

**Eric Latour:** Ouais, c'est impressionnant quand même vraiment ça se

**Mehdi Lamrani:** Non non, j'ai bossé hein.

**Eric Latour:** voit.

**Mehdi Lamrani:** J'ai j'ai C'est parce que c'est franchement si tu demandes à un agent de te faire ça, il va il va il va te faire de la merde.

**Eric Latour:** Ah

**Mehdi Lamrani:** Il va te faire de la merde. Euh donc non, j'ai du coup du coup bref ça, j'aime pas trop ce type de truc, c'est trop verbeux. J'ai la deuxième passe va être plus plus condensé, plus straight to the point. Donc je vais parler un peu du rag. Je vais expliquer que ça c'estour ça c'est les problem ça ce ça sera dans une autre couleur. OK,

**Eric Latour:** Et ça du coup tu tu le mettrais Yeah.

**Mehdi Lamrani:** ça c'est

**Eric Latour:** pas j'ai question he mais je me demande sur le building agent est-ce que tu le mettrais pas sur le truc contexte d'accord

### **00:30:05**

**Mehdi Lamrani:** Euh non euh ça c'est pas du contexte, ça c'est le rag.

**Eric Latour:** tu mets pas dans le contexte la capacité à ton agent à aller chercher de l'information qui est propre à ton entreprise à ton use case.

**Mehdi Lamrani:** Je sais plus c'est la question

**Eric Latour:** Moi je le mettrai donc pas moi pour moi c'est du contexte en fait c'est justement c'est la capacité à donner de la connaissance et du contexte supplémentaire au LLM par différentes méthodes. Le rag étant une des méthodes.

**Mehdi Lamrani:** m'emmène sur le terrain de des autres façons de créer du du contexte qui sont l'ontologie, les choses comme ça. Et alors jeis pas sûr d'avoir tout appel business users, je l'ai pas mis dans le même endroit. Bon, du coup ce que je peux faire c'est pas con. J'aime bien le reframing. Je vais noter ça. Euh faut que je fasse un rappel. Donc euh rappeler enfin faire un un callback une sorte euh sorte de call back euh vers le company. Company business contex ou domain contex compagnie business.

### **00:31:35** {#00:31:35}

**Eric Latour:** Contex. Ouais. domaine contexte ou compagnie contexte. Ouais.

**Mehdi Lamrani:** texte euh à savoir notamment et logique. Ok.

**Eric Latour:** Et ma question c'est que là sur le rag pur, tu mets pas leg base leg base search s'appelle pas se s'appelle B je sais plus quoi mais celui qui est P Vector custom sur

**Mehdi Lamrani:** Ouais, No.

**Eric Latour:** parce que je pense que ça c'est un truc ça c'est une question qui vont poser qui en fait vous avez deux solutions enfin c'est quoi le truc qu'on voit utiliser bah en fait il y en a un qui est euh alors pourtant ils ont bien dit qu'il fallait pas dire que c'était l'un managé l'autre pas managé mais c'est en fait c'est l'un qui est parce que les deux sont les solutions fully managé ton la base derrière en PG et les bagés mais en la question c'est c'est le niveau d'autonomie que tu as dans la configuration que tu veux faire c'est est-ce que tu veux gérer toiême même tes t des algorithmes d'bending, tu veux faire tes rankings toi-même et ainsi de suite.

### **00:32:49**

**Eric Latour:** Et dans ces cas-là, tu passes sur leg base avec euh leg base search où en fait tu veux que toutes ces choses-là soient automatisées et tu veux quelque chose de standard. Yeah. Euh et dans ce cas-là, tu peux t'appuyer directement sur AI search. Et pour le coup, il y avait une presse qui était top là-dessus que j'ai lu la semaine, ce weekend. Ah, c'était pas un slide, c'était p\*\*\*\*\*, je vais le retrouver. Je te le retrouve, je te le copicole.

**Mehdi Lamrani:** OK donc AI search indexes documents and tables for vector and keyword searches keep the index in sy with the delta tables and retranslitations um and knowledge assistance package into a Et ça malheureusement c'est bien marqué comme legacy. Tu vois regarde ça c'est le petit détail important où là j'ai quand c'est public preview c'est PP et quand c'est Legacy, c'est legacy.

**Eric Latour:** Ouais. Et alors moi j'ai une question euh pratique parce que il vont te la poser. Mais du coup euh tu vous nous donnez accès après à cette app parce que c'est sûr qu'ils vont vouloir y avoir accès.

### **00:34:12**

**Mehdi Lamrani:** Euh non euh j'ai un export PDF, je peux pas leur donner accès à Tu sais pourquoi ?

**Eric Latour:** Mais du coup

**Mehdi Lamrani:** Parce que euh je vais te montrer, j'ai un truc qui est ici, j'ai un truc qui est internal. Et quand internal est actif, euh il y a tous les toutes les réserves et les vérifications et des notes internes qui sont qui sont activées.

**Eric Latour:** du coup est-ce que le data story euh

**Mehdi Lamrani:** Déter les story, je leur ferai un PDF, hein. Ça c'est pas compliqué.

**Eric Latour:** Ouais et tu gardes les liens tous les liens dans ton PDF, il va être joli. Je veux dire, il va pas être

**Mehdi Lamrani:** Non non, j'ai déjà fait ça super proprement. Euh j'ai un agent qui prend qui qui refait les choses.

**Eric Latour:** OK.

**Mehdi Lamrani:** Par contre, il y aura pas euh il y aura pas les liens vers les présentes.

**Eric Latour:** Oui, mais ça c'est des présent internes, c'est pas grave.

**Mehdi Lamrani:** Ouais. OK.

**Eric Latour:** Ça te donne les trucs, tu vois, il savent ça le rur permet Euh

### **00:35:08** {#00:35:08}

**Mehdi Lamrani:** Ouais. Ouis. Ouais. S'ils veulent s'ils veulent, il y a pas de souci. Ça je vais garder ça tel quel. Bon. OK. Euh, j'en étais où ? J'en étais là. OK. Donc du coup, MCP euh agents reach the company tools. Tout ça c'est réécrit one governad of connections. Docum data. Ça c'est pas bon. Tac tac. Ça c'est à réécrire. Moi je vais recommencer par là. Each connection can instead bevered in one place. So we have one central repository for all the connections. If you need uh your own model context protocol server to be tied or access to server through datab You can if you need to host an MCP server inside datab you can as well so both can be connected. Uh we have manage MCP server for its own services uh for for network own services like gen search and sequel these are managed MCP that can be uh registered uh to agents.

### **00:36:23** {#00:36:23}

**Mehdi Lamrani:** We also uh give connectors provide connectors to uh provide uh governed access to Google Workspace, Microsoft, Slack, Detub and more and teams can register their own NCP servers as data bricks apps if they choose to host. S'ils veulent une petite démo, je leur dis pour la partie gateway, je leur ferai euh je leur propose de la faire une une autre fois. Voilà.

**Eric Latour:** Ouais ouais gateway ils en ont déjà eu un peu donc il vont plutôt poser des tuis je pense qu'ils vont poser des questions et en fait de là faut qu'il fasse du pick and shoes en mode de

**Mehdi Lamrani:** You can develop your own custom agents and attribute them uh memory, manage memory or uh manage your memory yourself through uh through Lake base and you can run them in isolated sandboxes. You can choose whatever framework to write the code in. Lapha chain, open um these are just containers where you can uh host your custom code. So there is absolutely no limitation with that. Euh qu'est-ce que je peux dire de plus ?

### **00:38:00**

**Mehdi Lamrani:** Euh non, ça je vais passer. Ça sert à rien, je pense. Enfin, c'est un peu trop tôt. Quoi que qu'est-ce que tu en penses ?

**Eric Latour:** Attends, je t'ai perdu. Bah moi, je trouve que celui-là, il est très parlant.

**Mehdi Lamrani:** Hm.

**Eric Latour:** Euh,

**Mehdi Lamrani:** Et ça me dérange qu'il commence par le Omnium quoi. C'est pas grave. Mais il est bien, il est bien ce slide.

**Eric Latour:** il est vraiment bien, moi je trouve.

**Mehdi Lamrani:** Euh, est-ce que je parle ? Ouais, bah oui, oui, oui, oui, oui. Ça c'est bien. C'est bien cet endroitlà. Je viens de parler des DMCP, j'ai parlé de RAG.

**Eric Latour:** Moi je le ferai même Attends,

**Mehdi Lamrani:** Je parlais des fonctions au début.

**Eric Latour:** tu sais quoi ? Mais moi en fait, je démarrerai presque par celui-là. En fait, tu building agents, premier truc, c'est OK, ben tu veux créer des custom agents, c'est ça et ensuite voilà et ensuite tu vois, tu as le cœur, c'est que tu crées le custom agent et ensuite tu as tout plein de trucs que tu viens pluger autour.

### **00:39:14**

**Eric Latour:** Et les trucs que tu viens pluguer, c'est finalement mettre du contexte avec du rag, mettre du MCP pour aller trigger des solutions, faire l'observabilité. Mais tu vois, tu commences. Moi, je trouve que la thématique de building agent, c'est OK, tu peux créer ton agent d'ailleurs by the way, regarde tout ce qu'on a et maintenant je vais te parler de tout ce qu'on a. Et je trouve que dans le road dans le 360, dans le L300 là de Ouais.

**Mehdi Lamrani:** Je suis là

**Eric Latour:** dans le L300, il y avait un moment le truc était pas mal trouvait. Il y avait un slide avec une image qui était assez bien. C'était le slide 14 a peut-être à peaufin celui-là là.

**Mehdi Lamrani:** ça

**Eric Latour:** Ouais, je trouve que en tout cas je trouve l'image était bien en fait. OK, je te parle du cœur et puis en je te raconte.

**Mehdi Lamrani:** il est là, il Il est là, il est là.

**Eric Latour:** Ouais, voilà.

**Mehdi Lamrani:** Regarde.

**Eric Latour:** Ben celui-là, je trouve qu'il est pas mal dans l'explication.

### **00:40:22** {#00:40:22}

**Mehdi Lamrani:** C'est quoi d'avrix 5 box ? C'est une app, c'est juste une petite app.

**Eric Latour:** Datab sbox.

**Mehdi Lamrani:** Une micro app.

**Eric Latour:** Non, c'est que tu vas faire exécuter. Si ton si ton agent a du code à exécuter, il veut générer du code, il va l'exécuter. En fait, il va déployer une soundbox, exécuter le code dans la soundbox, récupérer le résultat et créer la soundbox. Et ça, c'est pas mal.

**Mehdi Lamrani:** Et c'est facturé comment ce truc ?

**Eric Latour:** Ça évite que tu puisses tu en fait c'est c'est c'est notamment pour limiter les surface d'attaque sur ton agent parce que tu peux ton agent va pas être corrompu par du code qu'il aura lui-même exécuté de tu vois.

**Mehdi Lamrani:** Ouais. Et euh c'est facturé comment ce truc ?

**Eric Latour:** à la conso des buu en c'est une réponse de sens mais en gros autant autant non mais autant de la soundbox

**Mehdi Lamrani:** C'est c'est ta réponse c'est t'inquiète on va te facturer. T'inquiète t'inquiète c'est pas gratuit.

**Eric Latour:** voilà non comment c'est fait c'est facturé autant à la seconde non mais c'est facturé à la seconde de l'environnement sbox donc effectivement ton agent vrille

### **00:41:18**

**Mehdi Lamrani:** Mais c'est c'est monitoré ou est-ce que tu le vois ça dans l'interface ? J'ai jamais vu.

**Eric Latour:** mais je sais Bah, j'en sais rien. Eh, tu je pose des questions. Moi,

**Mehdi Lamrani:** Je suis pas c'est ça.

**Eric Latour:** je suis là pour je suis pas ça.

**Mehdi Lamrani:** OK.

**Eric Latour:** Moi je suis je suis là pour vendre.

**Mehdi Lamrani:** Chacun son taf.

**Eric Latour:** Non, si euh où est-ce que c'est ? Je ne sais pas.

**Mehdi Lamrani:** D'accord.

**Eric Latour:** Mais parce que le point c'est que je suis pas sûr que Sandbox soit J déjà.

**Mehdi Lamrani:** Non mais moi je j'anticipe les questions à la con.

**Eric Latour:** Non, non, mais tu as raison, tu as raison,

**Mehdi Lamrani:** C'est tout de suite les tout de suite c'est dans des questions qu'on va me poser.

**Eric Latour:** tu as raison.

**Mehdi Lamrani:** Ah ok. Non c'est pas mal hein. C'est c'est pas mal. C'est pas celui-là dont tu parlais slide du dice.

**Eric Latour:** Si si, c'était celui-là.

**Mehdi Lamrani:** Non.

**Eric Latour:** C'était exactement celui-là.

### **00:41:52**

**Mehdi Lamrani:** Ouais.

**Eric Latour:** Moi je trouvais qu' était non le slide du das dont moi je te parlais qui était une vue plus allup de de

**Mehdi Lamrani:** Ouais.

**Eric Latour:** ça et je peux te le donner euh p\*\*\*\*\* j'ai tellement de trucs. Faut que je ferme mes fenêtres moi en fait c'est c'est un peu comple pas.

**Mehdi Lamrani:** Oh p\*\*\*\*\*, je commence mon lundi, je suis déjà cassé. Incroyable.

**Eric Latour:** J'ai pas dormi de la nuit là. J'ai eu des quintes de tout d'enculé.

**Mehdi Lamrani:** Ah merde \! Ah p\*\*\*\*\* \!

**Eric Latour:** J'ai ça fait ça fait bah c'est pas toi qui m'a rendu malade hein.

**Mehdi Lamrani:** Ouais mais bon en je veux dire allez je compatis

**Eric Latour:** Euh c'est celui-là. Je te le mets dans le je te le mets dans le slack tous les deux. Euh marque tac. Ce slide là, moi je trouve qu'il est pas mal. tu vois et qui a le contexte contrôle cost choice et confiance tu vois mais qui marche pas en anglais

**Mehdi Lamrani:** Ah p\*\*\*\*\*, faut que je fasse les battle cart aussi.

### **00:43:03**

**Mehdi Lamrani:** Euh c'est quoi ? Ah ah mais tu l'as renommé en Amadeus.

**Eric Latour:** Oui oui mais je peux te l'envoyer il existe en standard que là je j'enit un pour eux mais tu vois je trouve que le slide 3 là le slide 3 audessus Celui-là, je trouve qu'il a quand même, tu vois,

**Mehdi Lamrani:** H Ah,

**Eric Latour:** il est je trouve qu'il

**Mehdi Lamrani:** c'est beau ça. Ah, c'est très beau ça.

**Eric Latour:** permet de fixer un peu les étages où est-ce que tu es dans ton truc.

**Mehdi Lamrani:** Ouais.

**Eric Latour:** tu dis "OK, j'ai ça et moi je trouve que juste ce qui manque, ce que je trouve pas top, c'est que dans Adantic Work, je trouve qu'ils ont mis trop de trucs sur la partie Jenny où on fait Jenny one Jenny agent, Jenny Cod,

**Mehdi Lamrani:** Ouais ouais ouais ouais.

**Eric Latour:** il y a Jenny et en fait dans la Jun Brick là maintenant tu dis bah OK, j'ai le runtime, j'ai exécuté et puis j'ai tout le reste. Donc j'ai les MCPN point, j'ai les modèles serving, j'ai les j'ai les memory, j'ai les search, j'ai les tools, tu vois ?

### **00:44:05**

**Eric Latour:** Et c'est là où

**Mehdi Lamrani:** Hm. Ouais. Euh mais attends, mais ce que tu dis là, ça y est pas ici.

**Eric Latour:** non, je trouve que ce slide devrait être comme ça,

**Mehdi Lamrani:** H Et où est-ce qu'on Attends,

**Eric Latour:** tu vois, pour donner la clarté.

**Mehdi Lamrani:** ouais, je suis d'accord. Ben après, ils ont fait un choix de non, il est dans aucune architecture.

**Eric Latour:** Non non. Ouais, ils l'ont pas mis. Ils le mettent juste dans MGP MZP registr sur la gatewayant

**Mehdi Lamrani:** OK.

**Eric Latour:** pour le coup. Ouais. Et alors par contre, j'ai appris un truc,

**Mehdi Lamrani:** Ouais, mais bon, c'est très marketing,

**Eric Latour:** c'est que Ouais.

**Mehdi Lamrani:** c'est ce qu'ils veulent pousser, quoi.

**Eric Latour:** Bah celui-là, il est il est 100 quoi. Moi je trouve qu'il faudrait juste mettre adentic work, tu as Jenny.

**Mehdi Lamrani:** Š.

**Eric Latour:** En fait, presque Jenny pour moi c'est presque une tool de J'exagère mais tu vois Jenny Agent c'est presque un tool de des agents que tu vas construire sur John Brick parce qu'en fait techniquement parlant si tu veux query de la data qui est dans des tables diverses et variées

### **00:45:19**

**Mehdi Lamrani:** Bri, je comprends pas ce qu'on peut dire. Bah Agent BCK si c'est build ton propre truc c'est ça s'appelle plus Agent BCK je comprends plus ce produitement

**Eric Latour:** Bah moi je pense qu'en fait si moi à Jen Bricks et mais par contre je pense que c'est effectivement c'est un changement de de mindset complet par rapport au à ce qui a été initialement à J Bricks qui était soit-disant tu fais du low code c'est plus

**Mehdi Lamrani:** ratical oui

**Eric Latour:** ça c'est en fait c'est tu veux construire des agents, je te mets à disposition tous les outils dont tu toutes les petites les écrous les machins, les bidules, tu les déjà dispo maintenant c'est à toi de de le de construire avec les briques d' et tu mets tu

**Mehdi Lamrani:** J'aime beaucoup cette vision.

**Eric Latour:** vois

**Mehdi Lamrani:** C'est c'est des des Legos mais c'est euh c'est des écrous.

**Eric Latour:** non mais c'est des écrous des vis des machin qu'est-ce que tu veux faire et des fois tu as des trucs déjà tout voilà mais et

**Mehdi Lamrani:** C'est exact Agent Bolt.

**Eric Latour:** dedans tu as le choix c'est que des fois tu veux prendre le truc qui est déjà tout prêt ready to use tu as pas de posé de question euh bah en fait tu prends ai search en fait je voudrais parce

### **00:46:16**

**Mehdi Lamrani:** Ouais.

**Eric Latour:** que bah en fait je me rends compte que c'est des trucs business un peu particuliers. Je voudrais un edding bien particulier que j'ai pu entraîner.

**Mehdi Lamrani:** Mais c'est quoi ? Il y a plus d' sech.

**Eric Latour:** Si ça s'appelle AI search maintenant c'est des vecteur search ça s'appelle AI search maintenant.

**Mehdi Lamrani:** Ouais mais oui d'accord. OK. OK, mais c'est pas ridituose, hein. C'est faut enfin tu tu invoques.

**Eric Latour:** Non mais ce que je veux dire c'est que tu as tu as pas la main tuasas tu as peu de levier de configuration et de

**Mehdi Lamrani:** Oui. Oui.

**Eric Latour:** customisation. Ça vient avec une configuration relativement rigide qui te permet de pas te poser un million de questions et de pas te faire toi tout tout seul. Là aussi,

**Mehdi Lamrani:** Oh mais si tu veux un orchestrateur,

**Eric Latour:** tu peux search.

**Mehdi Lamrani:** tu te débrouilles par exemple.

**Eric Latour:** Pardon Mehdi?

**Mehdi Lamrani:** Si tu veux un orchestrateur, tu te débrouilles. Il y a plus de supervisor agent.

### **00:46:59**

**Eric Latour:** Oui mais le supervisor c'était pour faire bosser plusieurs agents en temps.

**Mehdi Lamrani:** Il y a plus Non non non non.

**Eric Latour:** C'était pas tellement sur la partie AI search en tant que tel.

**Mehdi Lamrani:** Si tu veux un orchestrateur supervisor,

**Eric Latour:** Ok.

**Mehdi Lamrani:** c'était pas juste pour bosser plusieurs agents, c'estas besoin d'un orchestrateur pour appeler tes tools et cetera. Maintenant tu te débrouilles, tuas ton propre agent. Maintenant tuas G agent, je sais pas ce qu'il veut. N'allons pas trop sur ça cré plus de confusion. Je reviens sur ma sur mon truc. Donc OK. Bon, je vais je vais prendre en compte ce que tu m'as dit euh pour que je refasse une passe dessus correct. Euh Multient Orchestration, justement, bah le multi supervisor agent, il est en Legacy. Ça, je peux plus euh je peux plus en parler quoi. Ça, je vais en créer une note.

**Eric Latour:** Ouais, même qu'il No.

**Mehdi Lamrani:** Non, je suis obligé d'en parler. euh enfin ouais non mais il faut que je le dise.

### **00:47:59** {#00:47:59}

**Eric Latour:** Ben non mais je un truc ilutilise pas

**Mehdi Lamrani:** Non, je suis obligé de parler de l'orchestration. Euh to be deated. Becated pour leurestration, il faut pointer custom. Si elle existe sinon tourner ça.

**Eric Latour:** Moi honnêtement dans une heure de présentation s'il y a un truc on n pas ils utilise pas on est en train de dire qu'on a pas de produit gagne du temps.

**Mehdi Lamrani:** Hm hm.

**Eric Latour:** En tout cas, dans la présentation, ce qui pleut,

**Mehdi Lamrani:** OK.

**Eric Latour:** tu peux te laisser dans ton truc mais ce qui pleut en parle pas de temps pour dire on avait un truc mais on a plus, on dépend, on av un. OK. Message pas clair, on a rien, on a rien.

**Mehdi Lamrani:** OK. OK.

**Eric Latour:** On en parle pas.

**Mehdi Lamrani:** OK. Euh OK. Tu sais quoi ? Je vais rajouter un truc euh rajouter dans la story euh marqué notamment Alors l'évaluation, j'ai parlé du tracing euh operator inside every request step by step including the cost.

### **00:49:52** {#00:49:52}

**Mehdi Lamrani:** Le pain c'est que agent chas opn 2 secondes.

**Eric Latour:** Ça moi pour moi c'est un truc sur lequel il faut appuyer à mort.

**Mehdi Lamrani:** Ah si c'est Ouais.

**Eric Latour:** À mort mec les gars. En fait ML Flow c'est juste la norme euh pour le data scientist. Euh bah en fait vous savez quoi ? On a on l'a juste mis à jour pour la partie de Jenny et pas partie pardon adjonic ML Flow 3 et en gros ben c'est open source c'est pas que pour nous.

**Mehdi Lamrani:** Ah.

**Eric Latour:** Nous on peut on lesber chez nous, ça marche partout et on est convaincu que ça va comme pour comme ML Flow 2, ça va devenir la norme pour pour tout ça. C'est open télé mais derrière ça envoie les trucs en hôtel, les tracing sont en hôtel, tu peux les mettre dans n'importe quel agrégator. En gros mec, demain si tu fais ton instrumentation d'agent en fait un MF 3.0 frérot héberger chez nous ou pas après. Euh

**Mehdi Lamrani:** Alors euh Euh euh on va prendre les notes de source.

### **00:51:31** {#00:51:31}

**Mehdi Lamrani:** Qu'est-ce que tu as dit aussi sur lequel ? Je devais insister.

**Eric Latour:** Euh bah le fait que c'était open open source que ça ça s'appuyait sur hôtel. Ça ça c'est des petits mots clés qui vont les faire vibrer. Tu vois, c'est du hôtel donc tu peux l'envoyer n'importe où. Et donc même si vous ne décidez pas, notre recommandation c'est que même si vous ne décidez pas d'utiliser euh après de target databx pour ça, juste votre instrumentation fait le mfow 3.0 zé ça va juste devenir nous consideration c'est que ça va devenir la norme our

**Mehdi Lamrani:** Lock.

**Eric Latour:** conviction new standard agent instrumentation ml flow for for data scientist

**Mehdi Lamrani:** single

**Eric Latour:** Common ? Ouais, j'aime bien common.

**Mehdi Lamrani:** D'accord. Ça, je vais renommer en évaluation. Donc euh ce qui me va pas là-dedans, c'est que euh Ouais. Là, il va vraiment falloir est-ce que Non, non, non. Je vais me poser la question de savoir si je se prépare entre l'évaluation Gen ou euh et et l'évaluation.

### **00:53:17**

**Mehdi Lamrani:** On va juste falloir outliner quoi. Il va falloir juste une slide pour que ça gère les deux et valpre un bullet point. with no record and staging and production drift apart with agentation measures anwers andion proms scores je vais présenter quelques éventuellement production each agents gets runs and also have register 32 version. Et là, je parle un peu enfin tu vois je parle un peu de des itérations dimension relevature and increase decrease regarding knobs and bols were um tweaked between each run. So as you can see uh with each we can have an increasing in in the values of each matric and th being able to evaluate the overall improvement of your agent.

**Eric Latour:** Excuse-moi, j'ai basculé parce que je me suis fait pinguer par Dragan. Il faut que je réponde ultra rapidement.

**Mehdi Lamrani:** Vas-y. Bon, c'est bon.

**Eric Latour:** Je pour une je met je shoot

**Mehdi Lamrani:** Vas-y, vas-y, hein.

**Eric Latour:** Euh Non, j'ai pas pas besoin de la side d'info. Ça va créer de la confusion pour lui.

### **00:56:37** {#00:56:37}

**Mehdi Lamrani:** Moi je mais plus que

**Eric Latour:** M.

**Mehdi Lamrani:** Hab

**Eric Latour:** Voilà. Super, déso, je suis revenu.

**Mehdi Lamrani:** Pas de souci. Euh du coup euh je crois que je vais zapper je vais zapper ça.

**Eric Latour:** Ouais,

**Mehdi Lamrani:** On s'en fout ça.

**Eric Latour:** domaine application, ils sont ils sont fout.

**Mehdi Lamrani:** Customer Lake et L on s'en un peu product registry. Bon ça c'est un peu technique, on peut en parler un petit peu. Ça ça n'a rien à faire là. Model serving scale pareil, ça n'a rien à faire là. C'est vraiment des jou techniques. Les C monitoring pareil, on s'en fout. Ça par contre si ça c'est important. Donc ça peut-être le mettre dans sa propre dans sa propre

**Eric Latour:** C'est quoi que tu veux là ?

**Mehdi Lamrani:** section MLOPS et CD.

**Eric Latour:** C'est c'est quoi l'idée ? te dire que tu dois tout.

**Mehdi Lamrani:** En fait c'est très simple. MLOs describe attends ça. Automation bundle. Attends il mélange deux choses différentes en fait.

### **00:59:44** {#00:59:44}

**Mehdi Lamrani:** Leops c'est important de de C'est ça en fait. Ah oui, c'est là un truc de tu vois en fait Yeah. development workspace, le saging workspace, le production workspace. En fait, tu peux faire des promotes.

**Eric Latour:** Ouais.

**Mehdi Lamrani:** Euh ouais.

**Eric Latour:** OK. Donc c'est vraiment la truc de t modèle de comment tu gères et mais alors en fait

**Mehdi Lamrani:** Non non, je pense que c'est peut-être un peu trop technique ça.

**Eric Latour:** je suis pas sûr moi ça intéresse. Le point c'est que c'est surtout euh la question qui va se poser c'est surtout quelle est notre vision de ça sur la partie parce que finalement demain tu peux avoir le même problème sur un agent en fait tu le releases quelque part tu le fais. Donc en fait c'est l'agent HBS.

**Mehdi Lamrani:** Bah la vision elle est la même sauf que tu vas pas avoir un tracking server via Mflow mais tu vas avoir un version un version de ton modèle dans le model registry, c'est tout. Donc euh

**Eric Latour:** Bah ça moi je pense ça ça mérite d'être dit hein.

### **01:00:48** {#01:00:48}

**Eric Latour:** Encore une fois, ils sont très intéressés par le day to.

**Mehdi Lamrani:** Ouais,

**Eric Latour:** Donc ça peut être dans operation. Je sais pas si tu as un truc operation.

**Mehdi Lamrani:** bah c'est bah c'est là, regarde. Production operations.

**Eric Latour:** Ah ben voilà. Bah moi je trouve que c'est ça vaut le coup de finir là-dessus.

**Mehdi Lamrani:** OK, donc peut-être commencer. Je vais peut-être commencer par ça.

**Eric Latour:** C'est pas le plus sexy mais genre tu sais tu closes en disant bah en fait globalement si on est

**Mehdi Lamrani:** Je peut-être je pense

**Eric Latour:** bon c'est pas

**Mehdi Lamrani:** que domaine en fait domain application je vais le pousser en bas et je vais mettre tout production operation avant

**Eric Latour:** Ouais.

**Mehdi Lamrani:** quoi.

**Eric Latour:** Et développer tool c'est quoi ? parce que je suis pas sûr que Developer Tool, c'est un grand intérêt pour eux là,

**Mehdi Lamrani:** Alors, développeur tools.

**Eric Latour:** je veux dire.

**Mehdi Lamrani:** Ouais. Euh, je vais contrairement ça va pas être databaps. Dat brickaps, il faut que j'en parle.

### **01:01:29** {#01:01:29}

**Mehdi Lamrani:** Euh, je mett dans une autre section. Par contre, c'est Jny Nicod quoi et kit et Omnit.

**Eric Latour:** Ouais, il y a Omnent, c'est un gar Omn.

**Mehdi Lamrani:** Jod, il s'en fout.

**Eric Latour:** Non, non, mais il faut passer rapidement quoi. En gros, le principe que tu as un code,

**Mehdi Lamrani:** Oui, oui, bien sûr,

**Eric Latour:** que tu as un que tu as un Claude un peu spécialisé qui te fait tes trucs trop bien.

**Mehdi Lamrani:** bien sûr.

**Eric Latour:** Bon, OK. des bomb euh

**Mehdi Lamrani:** Voilà, voilà. Globalement, je vais prendre en compte toutes les toutes les remarques.

**Eric Latour:** et du coup

**Mehdi Lamrani:** Je vais essayer vraiment de m'inspirer de quelque chose d'un peu plus global comme le back from dice là. Euh tac,

**Eric Latour:** Amadeus back from c'est ton dernier onglet

**Mehdi Lamrani:** je vais mettre là. Je vais essayer de commencer par un truc global de ce genre et ensuite Euh

**Eric Latour:** Et tu voudrais pas en fait, moi je me disais, je me demandais alors j'ai deux points. Du coup, toi ta présentation, l'idée c'est d'utiliser cette en fait le le ton support de présentation, ça va être ce flow là dans l'application.

### **01:02:41** {#01:02:41}

**Eric Latour:** Est-ce que tu mettrais pas des images et pas uniquement des inserts de slide ? Mon point est, tu vois par exemple ton premier quoi que tu peux cliquer, tuouvres, tu le sais que tu Ouais,

**Mehdi Lamrani:** bien sûr.

**Eric Latour:** c'est pas mal. Oui, tu as raisonuse en fait.

**Mehdi Lamrani:** Oui, voilà.

**Eric Latour:** Tu vois, j'ai

**Mehdi Lamrani:** Par contre, en fait ici, regarde, tu vois, je euh j'ai j'ai j'ai Alors, attends, ça c'est relou. Code faut juste un petit bug parce que j'ai fait offline. 2 secondes, de petites secondes. Euh je suis dans code ensuite de CL stratégie. Non non, c'est pas une porte. On a dû accélérer.

**Eric Latour:** Ok.

**Mehdi Lamrani:** Voilà. Donc en fait là, j'ai j'ai les petites les petites coches pour savoir si je le garde ou pas quoi. Tac. Donc là par exemple quand bah quand je vais dérouler euh même si je fais je fais un refresh au fur et à mesure que je déroule, je vais avoir ceux que j'ai choisi qui vont être en rouge quoi.

### **01:03:56** {#01:03:56}

**Mehdi Lamrani:** Voilà.

**Eric Latour:** truc merde.

**Mehdi Lamrani:** OK. Bon ben écoute, je pense qu'on est bon dans l'ensemble.

**Eric Latour:** Ouais, moi je pense qu'ils vont être ravis.

**Mehdi Lamrani:** Je te je te

**Eric Latour:** Moi vraiment mon feedback c'est je pense qu'ils vont être ravis d'un point de vue profondeur technique, cartographie, discussion, les bonnes questions. Je pense que les deux le point où ils vont c'est un peu faut c'est pour ça me remettre un peu au début, j'ai un peu une vision globale qu'il se comprennent que tu set the scene parce que si tu jumpes directement dedans,

**Mehdi Lamrani:** Hm hm

**Eric Latour:** tu es un peu perdu et qu'il y a un peu un truc visuel à côté pour les rappeler où est-ce qu'ils sont dans l'histoire pour bien les

**Mehdi Lamrani:** hm.

**Eric Latour:** garder qu'ils partent pas.

**Mehdi Lamrani:** Ouais ouais.

**Eric Latour:** Et après, mais ça c'était normal sur 1 heure, c'est que moi j'ai j'ai peur qu'on arrive pas, enfin tu vois 1 heure ça va passer très très vite, surtout s'il se mettent à poser des questions. Euh mais du coup euh

### **01:04:41** {#01:04:41}

**Mehdi Lamrani:** Je te franchement je te je t'invite à faire ta part en leur disant écoutez voilà si quoi que ce soit on fait des

**Eric Latour:** Ouais ouais ouais. T'inquiète, je le fais et puis je dirais bah je vois qu'il y a des questions.

**Mehdi Lamrani:** followup moi je le ferai hein. C'est juste que voilà,

**Eric Latour:** Oui. Oui.

**Mehdi Lamrani:** toujours

**Eric Latour:** Non mais euh et encore une fois euh moi je leur dirai en fait je pense qu'en en ouverture de meeting, c'est moi qui fait l'intro 2 minutes et qui dit justement voilà je resette the scene en disant voilà les expectation ça a été de vous présenter une vision all up de où est-ce qu'on en est, quels sont les produits qu'est-ce qui est dispo ? Qu'est-ce qui est pas dispo ? Qu'est-ce qui est mature pas mature et qu'on vous partage notre vision. En 1 heure, on peut pas faire du deep dive, on veut quand même faire du technique, on peut pas faire du deep dive. Donc l'objectif c'est qu'à la suite de ça euh même en clôture, on se prend 3 minutes ou en asynchrone pour dire quels sont les sujets sur lesquels on déclenche des sessions de deep time.

### **01:05:31** {#01:05:31}

**Mehdi Lamrani:** Ça me va, ça me va.

**Eric Latour:** C'est vraiment le but quoi.

**Mehdi Lamrani:** Euh,

**Eric Latour:** C'est une introduction en fait en

**Mehdi Lamrani:** est-ce que tu vas voir euh c'est quoi c'est à quoi ressemble ta journée ? Genre parce que l'idée c'est que je puisse te soumettre. C'est quoi ça ? 4h genre 14h30, je te enfin dans dans OK.

**Eric Latour:** c'est mec ce sera c'est pour moi c'est ma topo. Donc tout le reste, je le nettoierai pour ça.

**Mehdi Lamrani:** Bon ben je te OK super. Bah,

**Eric Latour:** Et je suis full.

**Mehdi Lamrani:** je vais te refiler.

**Eric Latour:** Je suis full. Mais ça tout passe après ça.

**Mehdi Lamrani:** Pas de souci, pas de souci. Du coup, je vais reprendre je prendre en tout ce qu'on s'est dit là et le mettre en application et je te remets ressoumets à tes yeux tout à l'heure.

**Eric Latour:** Magnifique. Je te remercie.

**Mehdi Lamrani:** OK. Allez, à plus. Ciao. Merci.

**Eric Latour:** Ciao bon courage.

**Mehdi Lamrani:** Merci pour tout. Très utile les feedback.

**Eric Latour:** C'est moi qui te remercie.

**Mehdi Lamrani:** Merci.

**Eric Latour:** Yeah.

**Mehdi Lamrani:** Sure.

### **Transcription terminée après 01:06:18**

*Cette transcription modifiable a été générée par ordinateur et peut contenir des erreurs. Les utilisateurs peuvent également modifier le texte après sa création.*
