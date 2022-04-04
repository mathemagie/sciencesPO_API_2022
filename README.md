## cours 1

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

exemples de recette dans diff domaines :

https://www.stevecummins.com/blog/journalists-can-benefit-using

https://www.makeuseof.com/tag/best-ifttt-recipes-smart-home-automation/

1/ URL afin de connecter la lampe connectée : https://googlecodelabs-candle-bluetooth.glitch.me/

- https://changecolor-candle.glitch.me/vert
- https://changecolor-candle.glitch.me/bleu
- https://changecolor-candle.glitch.me/orange
- https://changecolor-candle.glitch.me/rouge
- https://changecolor-candle.glitch.me/jaune
- https://changecolor-candle.glitch.me/flash
- https://changecolor-candle.glitch.me/rainbow

2/ l'URL de l'API Effeil Tower https://litght-lego-led.glitch.me/home

https://litght-lego-led.glitch.me/api/light_on

https://litght-lego-led.glitch.me/api/light_off

 ### Exercices demandés 
 
- création de 5 zaps de A à Z ! 
- écrire 5 phrases en français sur le principe d'une recette IFTTT à partir de services non proposés par ces différents services.


# cours 3 

développement d'une application de A à A faisant appel à plusieurs API : googleSheet, Deepl pour la traduction, https://apidocs.geoapify.com pour lre reverse geocoding


A/ depuis une base de donnée hebergée sur googleSheet 

https://sheety.co/

B/ créer un projet avec repl.it

https://replit.com/@mathemagie/sheet#main.py


C/ https://apidocs.geoapify.com

- création d'un compte, obtention d'un API key, les statistiques,le billing
- les faire explorer la notion de bac à jeux proposé par le service https://apidocs.geoapify.com/playground/geocoding et mettre l'API key dans le playground

- examiner le résultat de la réponse JSON avec un outil en ligne 

exercices : jouer avec les paramètres dans le GET http : 

https://api.geoapify.com/v1/geocode/reverse?lat=48.8734703&lon=2.3580603&format=json&apiKey=d90b1a594bb84aebab6bfac77b29ccf0&lang=fr


avec le JSON : récupérer que le code pays à partir d'une liste de ligne lng, lat de

https://api.geoapify.com/v1/geocode/reverse?lat=48.8734703&lon=2.3580603&format=json&apiKey=d90b1a594bb84aebab6bfac77b29ccf0&lang=fr

ou encore récuprérer l'adresse exacte et non le code pays

D/ envoie d'un sms vi Twillio

E/ Deepl

https://api-free.deepl.com/v2/translate


F/ carto en utilisant https://apidocs.geoapify.com/samples/maps/js-mapbox/ 

thématique abordée lor du cours 3.4 : 

Obtention d'une API KEY, notion de Token, dashboard de consommation d'une API;, consommation d'une une API data, playground , consommation d'une API logicielle (reverse geo coding, sms, maps), approfondissement du format JSON,

https://replit.com/@mathemagie/sheet#main.py

https://replit.com/@mathemagie/tempcolor#main.py
  
 
 


 
 
  
