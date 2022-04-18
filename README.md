## Cours 1

Les slides du premier cours : https://docs.google.com/presentation/d/1vMnQlz5kkXJXnZPPXM6KZL2T3_yM2zYY/edit#slide=id.g6b138fac16_0_0


Ressources complémentaires : 

- (6 Reasons Why APIs Are Reshaping Your Business) de FABERNOVEL : https://fr.slideshare.net/faberNovel/6-reasons-why-apis-are-reshaping-your-business


- https://www.youtube.com/watch?v=s7wmiS2mSXY What is an API (MuleSoft)
- https://a16z.com/2018/03/13/api-economy-why-what-how/ (L'économie de l'API - Le pourquoi, le quoi et le comment) 
- https://a16z.com/2018/03/09/api-world-summit/ (Le monde à travers une API)
- https://www.programmableweb.com/ : site de référence qui catalogue les APIs 

 - https://gigaom.com/2013/12/07/why-cognition-as-a-service-is-the-next-operating-system-battlefield/
 
 À retenir : 
 
 "Bringing computer science smarts to the masses
Home appliances, connected home, internet of things

The original goal of the Semantic Web was to provide an open framework for apps to integrate and reason across any data in any repository, anywhere. But the open standards that were introduced by the WC3, such as RDF and OWL have proved to be unwieldy and difficult for non-computer scientists to grasp.

Where CaaS comes in is that much of the reasoning capabilities that Semantic Web hoped to enable could now become simple APIs in the cloud that any developer can use, without needing a PhD. As we head toward 2020, CaaS will make the world more helpful. The cognitive operating system will reach out and connect our bodies and even REACH into them via augmented reality devices like Google Glass, and the quantified self movement.

Everything is going to get smarter. Your phone, your calendar, your watch, your radio, your TV, your car, your refrigerator, your house, your glasses, your briefcase and clothing. The vast cognitive capabilities of the global CaaS providers will be cheap and available via APIs to every device from the nano scale up to the giant global applications and services."

 - Exemple d'un objet connecté - un peu particulier - basé sur l'API ALEXA : https://www.01net.com/actualites/il-pirate-l-assistant-alexa-pour-en-faire-un-poisson-qui-parle-1056346.html 
 
 - Le chiffre d'affaires de AWS : https://www.capital.fr/entreprises-marches/decouvrez-aws-lactivite-qui-rapporte-plus-a-amazon-que-le-e-commerce-1336734 
 
  - Développement de nouveaux services à partir de l'OpenAPI Radio france : https://hyperradio.radiofrance.fr/actualite/vous-aussi-participez-a-la-creation-de-la-radio-de-demain-avec-lopen-api-de-radio-france/ 
  
  - https://www.journaldunet.com/solutions/cloud-computing/1181302-twilio-la-start-up-qui-motorise-les-services-de-communication-de-facebook-ou-uber/


## cours 2

Découverte des servives https://zapier.com/ , https://ifttt.com/home ou encore https://www.make.com/en

Exemples de recettes IFTT, ZAPIER dans différents domaines :

https://www.stevecummins.com/blog/journalists-can-benefit-using

https://www.makeuseof.com/tag/best-ifttt-recipes-smart-home-automation/

1/ URL afin de connecter la lampe connectée : https://googlecodelabs-candle-bluetooth.glitch.me/

et les URls (API) afin de changer la couleur de la lampe

- https://changecolor-candle.glitch.me/vert
- https://changecolor-candle.glitch.me/bleu
- https://changecolor-candle.glitch.me/orange
- https://changecolor-candle.glitch.me/rouge
- https://changecolor-candle.glitch.me/jaune
- https://changecolor-candle.glitch.me/flash
- https://changecolor-candle.glitch.me/rainbow

2/ l'URL de l'API Effeil Tower https://litght-lego-led.glitch.me/home

URL (pour l'illuminer) https://litght-lego-led.glitch.me/api/light_on

API (pour l'éteindre) https://litght-lego-led.glitch.me/api/light_off

 ### Exercices demandés 
 
- Création de 5 zaps de A à Z (me fournir les copies d'écrans par email) ! 
- Ecrire 5 phrases en français sur le principe d'une recette IFTTT à partir de services non proposés par cet outil en ligne ! 

Exemples : 

- Illuminer la tour Eiffel au survol de Thomas Pesquet au dessus de la France.
- Si la qualité de l'air réglementaire n'est pas respectée à Toulouse, toutes les voitures en train de rouler au centre de Toulouse s'arrêtent.
- Faire remuer la queue de mon chat (connecté avec un arduino) 5 min avant que le bus arrive en bas de chez moi.

## cours 3, cours 4 , cours 5 

Développement d'une application de A à A faisant appel à plusieurs API : googleSheet pour la base de données (contenu exposé via une API en utilisant le service https://sheety.co/, l'API Deepl pour la traduction d'un texte , https://apidocs.geoapify.com pour le reverse geocoding d'une longitude, latitude, etc 

A/ créer une feuille excel dans googleSpreadSheet : https://docs.google.com/spreadsheets/d/1PpfKm4uMSEb2TP6I5fKgo7vOnZUq8r5Pk46r7PmULFU/edit?usp=sharing

B/ Exposer cette base de données par l'intermédiaire d'une API via cet outil https://sheety.co/ (besoin de se connecter avec le compte google associé à la feuille excel)

B/ Créer un projet en python3.9 avec le service en ligne : https://replit.com/~

https://replit.com/@AurlienFache/ExposeSheetAPI

Exercices demandés : 

1/ Créer une autre feuille excel et modifier le code python existant afin de récupérer la nouvelle feuille excel

2/ Récupération d'autres données du fichier JSON à part la longitude, latitude

3/ jouer avec les URLs du service https://sheety.co/ et récupération d'une des entrées du fichier excel et les filtres ! 

regarder dans la documentation du service : https://sheety.co/docs/requests

récupération de la deuxième ligne de la feuille Excel : https://api.sheety.co/917a493d299bb9a04c196c7cf0393353/apiSciencesPo/responses/3

ou encore récupération de l'ensemble de réponses dont la valeur sendSms est égal à 1 : 

"https://api.sheety.co/917a493d299bb9a04c196c7cf0393353/apiSciencesPo/responses/?filter[sendSms]=1

4/ création d'une donnée dans le fichier Excel via appel de l'API en post et mise à jour d'une entrée existante : 

éléments de réponses dans cet article en ligne : https://funkytwig.com/2021/11/18/beginer-guide-sheety-python-api-update-goodle-sheets/


C/ Utilisation de l'API reverse-geocoding : https://apidocs.geoapify.com

- Création d'un compte, obtention d'un API key, regarder les statistiques, en savoir plus sur le billing de cette API.

- Exploration la notion de bac à sable proposé par le service https://apidocs.geoapify.com/playground/geocoding et mettre l'API key dans le playground.

Exercices demandés : 

1/ Modifier avec les paramètres dans le GET http (clef API, lang, format, etc ): 

https://api.geoapify.com/v1/geocode/reverse?lat=48.8734703&lon=2.3580603&format=json&apiKey=d90b1a594bb84aebab6bfac77b29ccf0&lang=fr

2/ Dans le code source du programme en python, pour chaque association lon, lat, récupération de l'adresse postale exacte ou encore le code pays ou de la ville, et mise à jour des deux colonnes correspondantes dans le fichier excel.

E/ utilisation de l'API du service en ligne Deepl pour la traduction du champ commentaire dans la base de données : 

https://api-free.deepl.com/v2/translate

Exercice demandé : changer la langue de traduction 

F/ envoie d'un SMS via Twillio

Exercice demandés : fouiller la documentation de Twillio afin de dénicher le bon code en python à utiliser !

G/ utilisation de cette API pour la detection du sentiment du commentaire : https://beta.openai.com/examples/default-tweet-classifier

Prendre le temps de regarder le 'pricing' de ce service : https://openai.com/api/pricing/ ainsi que le https://beta.openai.com/playground/

H/ Cartographie des réponses contenues dans le fichier Excel en utilisant https://apidocs.geoapify.com/samples/maps/js-mapbox/ 

Thématiques abordées lors du cours 3.4,5 : 

Obtention d'une API KEY, notion de Token, dashboard de consommation d'une API, consommation d'une une API data (feuille excel), playground d'une API (tester une API en ligne le plus rapidement possible sans avoir à télécharger quoi que ce soit) , consommation d'une API logicielle (reverse geo coding, sms, cartographie), d'une API cognitive, approfondissement du format JSON, notion d'API en écrtiure, etc 

## cours 6
