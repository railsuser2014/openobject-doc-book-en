******************************
Gestion de la relation clients
******************************

Configuration de la CRM
=======================

Dans le but de développer votre prototype pour NotSoTiny, vous allez devoir installer les modules de la CRM. Vous devez pouvoir gérer:

* Les leads (prospects)
* Les opportunités d'affaire
* Les appels téléphoniques
* Les calendriers partagés
* Les devis

..note:: Exercice 1 – Installez les modules CRM requis

Installez les modules nécessaires aux besoins ci-dessus.

..note:: Exercice 2 – Créez les Menus

???à supprimer???

..note:: Exercice 3 – Génération de devis

Installez le module qui permet de convertir une ou une liste d'opportunité(s) d'affaire en devis.

Flux CRM
========

Afin de préparer la démonstration de votre prototype, nous allons simuler un réel cas d'affaire, depuis la réunion avec le client jusqu'au devis pour un projet particulier.

Chaque année, la société NotSoTiny participe au salon « House & Design » à Paris. Pendant ce salon, la société va rencontrer environ 200 prospects en 3 jours.

..note:: Exercice 4 – Le salon

Encodez le salon en tant que campagne dans la CRM.

A la fin de chaque jour, les différents commerciaux présents au salon encodent dans le système toutes les cartes de visite qu'ils ont reçus des prospects. Sur le formulaire Lead (prospect) ils mettent un maximum d'informations relatifs au propect. Ensuite, quelques jours plus tard, ils contacteront chaque prospect un par un pour les qualifier et vérifier s'ils pourront déboucher sur une opportunité d'affaire avec lui.

..note:: Exercice 5 – Encodez les prospects suivants dans le système

	...à décrire...

Si le prospect semble intéressant, le commercial peut le convertir en opportunité et créer une fiche partenaire. Supposez que Luc s'occupe de quelques uns des prospects les plus intéressants du salon. Il remarque le prospect « ... ». 

Comme le prospect est très intéressant, le commercial va le convertir en opportunité d'affaire et en partenaire. Sur l'opportunité d'affaire, il peut fournir plus d'information, comme le revenu estimé (5.000 k€).

..note:: Exercice 6 – Convertissez le prospect en partenaire et opportunité d'affaire

Thomas, le commercial, se connecte au système et vérifie les prospects disponibles. Il sélectionne le prospect « ... » et le convertit en opportunité car il semble très intéressant et qu'il voudrait faire du suivi sur ce cas.

Afin de remplir la fiche partenaire, Thomas va contacter le prospect par téléphone.

..note:: Exercice 7 – Complétez les données de la fiche partenaire

Complétez l'adresse du partenaire concerné.

En discutant au téléphone avec le prospect, Thomas planifie une réunion pour Luc. Il demande aussi au client d'envoyer une description complètes de ses besoin par mail avant la réunion, de façon à ce que Luc puisse en prendre connaissance pour préparer efficacement cette réunion.

..note:: Exercice 8 – Plannifier une réunion

Depuis la fiche partenaire, plannifiez une réunion pour Luc. Cette réunion est organisée chez le client et est liée à l'opportunité d'affaire « ... ».

Quelques jours plus tard, le client appelle au bureau de NotSoTiny et c'est Eric qui répond au téléphone. Le client veut fournir plus d'informations sur les armoires qu'il désire. Il voudrait des armoires rouges et aimerait que Thomas lui apporte un catalogue d'armoires quand il viendra au bureau du client.

..note:: Exercice 9 – Encodez un appel téléphonique

Eric encode le résumé de la conversation téléphonique. Il lie cet appel à l'opportunité « ... ».

Le mercredi 12 février, Luc prépare cette réunion avant de se rendre chez le client. Il ouvre la fiche client et vérifie toutes les activités qu'il y a eu avec ce partenaire pendant les 15 derniers jours.

..note:: Exercice 10 – Vérifiez la fiche partenaire

Vérifiez tous les évènements enregistrés sur la fiche partenaire.

Luc rend visite au client et lui propose un devis. Etant donné qu'il n'y a pas d'autre besoin à ajouter, il peut proposer un devis lié à l'opportunité d'affaire, et va aussi devoir clôturer le cas du prospect.

..note:: Exercice 11 – Créez un devis à partir de l'opportunité d'affaire

Faites un devis avec les produits suivants:

	* Un projet de design de cuisine
	* Une armoire de 100cm

N'oubliez pas de clôturer l'opportunité puisque nous allons faire le suivi à partir du devis.

Gérer avec la CRM
=================

Luc, le directeur commercial, voudrait vérifier la qualité de son équipe commerciale.

..note:: Exercice 12 – Vérifiez le délai moyen pour clôturer une opportunité

Trouvez un moyen de savoir quel est le temps moyen (en heures) pour répondre à une requête d'un client (clôturer une opportunité d'affaire).

Luc remarque que le temps moyen pour clôturer une opportunité d'affaire est de 7 jours. Ce délai semble trop long pour lui. Etant donné qu'il veut améliorer la qualité de l'équipe commerciale, il aimerait recevoir une message d'alerte par email à chaque fois qu'une opportunité d'affaire n'est pas clôturée endéans les 5 jours après sa création.

..note:: Exercice 13 – Rappel par email

Envoyez un rappel au responsable si l'opportunité d'affaire n'est pas clôturé après 5 jours. Pour les prospects, il accepte seulement un délai de 3 jours avant de les clôturer. Mettre Luc en copie du mail quand le rappel est envoyé.

La société a différentes politiques pour gérer les prospects non-qualifiés et les réelles opportunité d'affaire. Les prospects sont gardés dans une réserve de prospects non assignés quand ils sont créés. Ensuite, les différents utilisateurs prennent les prospects et se les assignent périodiquement.

Pour les opportunités d'affaire, c'est différent. Toutes les opportunités d'affaire doivent être assignées à Luc. Ensuite, Luc décide s'il veut assigner le cas à quelqu'un autre ou de s'en occuper lui-même.

..note:: Exercice 14 – Assignation et réserve de cas disponibles

Trouvez un moyen d'obtenir une liste de tous les cas non assignés. Trouvez un moyen d'assigner automatiquement les opportunités d'affaire à Luc dès qu'ils sont créés.
