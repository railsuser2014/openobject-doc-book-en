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

..note:: Exercice 1 – Installer les modules CRM requis

    Le module standard nécessaire aux besoins listés ci-dessus est 'CRM_configuration'. Vérifiez si ce module est déjà installé et si non, installez-le. Lors de la configuration de ce module, vous devrez choisir les options qui vous seront utiles pour gérer les points ci-dessus, les autres critères ne vous seront pas nécessaire dans le cas NotSoTiny. Pour la gestion des devis, cela sera traité dans un exercice plus loin.

Flux CRM
========

Afin de préparer la démonstration de votre prototype, nous allons simuler un réel cas d'affaire, depuis l'encodage du client en tant que prospect jusqu'au devis pour un projet particulier.

Chaque année, la société NotSoTiny participe au salon « House & Design » à Paris. Pendant ce salon, la société va rencontrer environ 200 prospects en 3 jours. Pour chaque évènement de ce type, NotSoTiny envoie ses commerciaux qui auront la charge d'établir une nouvelle campagne marketing. Ils devront encoder les prospects rencontrés, ensuite, de retour chez NotSoTiny, ils les contacteront un par un afin d'essayer de conclure le plus d'affaire possible.

..note:: Exercice 2 – Le salon

    La première étape est donc de créer une nouvelle campagne, c'est à dire de créer une nouvelle catégorie de cas qui portera le nom de "House&Design 2009". Cela permettra d'encoder tous les prospects sous cette catégorie afin de les différencier des autres évèvements auxquels participe NotSoTiny.

A la fin de chaque jour, les différents commerciaux présents au salon encodent dans le système toutes les cartes de visite qu'ils ont reçus des prospects. Sur le formulaire Lead (prospect) ils mettent un maximum d'informations relatifs au propect. Ensuite, quelques jours plus tard, ils contacteront chaque prospect un par un pour les qualifier et vérifier s'ils pourront déboucher sur une opportunité d'affaire.

..note:: Exercice 3 – Encoder les prospects dans le système

    Thomas, un des commerciaux de NotSoTiny, se charge de regouper les cartes de visites et les différentes notes et encode dans le système les informations suivantes en tant que nouveaux leads (prospects).

+--------------+--------+-----------------+-------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
|Description   |Section |Source           |Nom prospect |E-mail                 |Détail de l'affaire                                                                                                                       |
+==============+========+=================+=============+=======================+==========================================================================================================================================+
|Prospect Brico|Affaires|House&Design 2009|Pierre Durand|p.durand@brico.be      |Brico est intéressé par nos armoires pour les revendre dans leurs magasin, mais quantité exigée trop importante (environ 100 armoires/moi)|
+--------------+--------+-----------------+-------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
|Dubois sprl   |Affaires|House&Design 2009|Marc Dubois  |m.dubois@dubois.be     |Sprl Dubois, soc. indépendante, voudrait vendre nos armoires, mais sans devoir les stocker chez eux car manque de place => sur commande   |
+--------------+--------+-----------------+-------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
|Particulier   |Affaires|House&Design 2009|Lucie Vonck  |lucie.vonck@hotmail.com|Mme Vonck serait intéressée par un projet de rénovation de sa cuisine. Lui envoyer un devis.                                              |
+--------------+--------+-----------------+-------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+

Si un des prospect semble intéressant, le commercial (Thomas) peut le convertir en opportunité et créer une fiche partenaire. Cela permettra de suivre cette opportunité de plus près et d'essayer de conclure l'affaire par une vente ou la signature d'un contrat, par exemple.

Supposons que Thomas trouve que le prospect "Dubois sprl" est très intéressant, il aimerait le convertir en opportunité et le transférer à Luc, le directeur commercial, qui s'occupe des cas les plus intéressants.
Sur l'opportunité d'affaire, il pourra fournir plus d'informations, comme le revenu estimé (5.000 k€). En premier lieu, Thomas va convertir le prospect en partenaire afin de faciliter la gestion future du cas, s'il y a aboutissement. Pour remplir la fiche partenaire, Thomas va donc contacter le prospect par téléphone.

..note:: Exercice 4 – Convertir et compléter les données de la fiche partenaire

    Convertissez le prospect en partenaire, puis complétez l'adresse du partenaire concerné:
    Dubois sprl
    Avenue de la liberté 56
    1000 Bruxelles
    Belgique


..note:: Exercice 5 – Convertir le prospect en opportunité d'affaire

    Thomas convertit le prospect en opportunité car il semble très intéressant et indique que le revenu estimé serait de 5.000 k€.

En discutant au téléphone avec le prospect, Thomas planifie une réunion pour Luc. Il demande aussi au client d'envoyer une description complètes de ses besoin par mail avant la réunion, de façon à ce que Luc puisse en prendre connaissance pour préparer efficacement cette réunion.

..note:: Exercice 6 – Plannifier une réunion

    Depuis la fiche partenaire, plannifiez une réunion pour Luc. Cette réunion est organisée dans une semaine chez le client et est liée à l'opportunité d'affaire "Dubois sprl".

Quelques jours plus tard, le client appelle au bureau de NotSoTiny et c'est Eric qui répond au téléphone. Le client veut fournir plus d'informations sur les armoires qu'il désire. Il voudrait des armoires rouges et aimerait que Thomas lui apporte un catalogue d'armoires quand il viendra au bureau du client.

..note:: Exercice 7 – Encoder un appel téléphonique

    Eric encode le résumé de la conversation téléphonique. Il lie cet appel à l'opportunité "Dubois sprl".

La semaine passe, et Luc voit parmi ses RDV planifiés qu'il a une réunion le lendemain avec un client. Il va donc préparer cette réunion avant de se rendre chez le client. Il ouvre la fiche client et vérifie toutes les activités qu'il y a eu avec ce partenaire pendant les 15 derniers jours.

..note:: Exercice 8 – Vérifier la fiche partenaire

    Luc se connecte, voit ses RDV dont celui avec Dubois sprl et va consulter la fiche du partenaire "Dubois sprl" avec en historique tous les évènements enregistrés dessus.

Luc rend visite au client, discute, négocie et finalement lui propose un devis. Le directeur de Dubois sprl désire obtenir un devis pour un projet de design de cuisine et une armoire pour évaluer la qualité du produit. Etant donné qu'il n'y a pas d'autre besoin à ajouter, il peut proposer un devis lié à l'opportunité d'affaire, et va aussi devoir clôturer le cas du prospect.

..note:: Exercice 9 – Installer le module de génération de devis

    En tant qu'utilisateur Admin, installez le module 'sale_crm' qui permet de convertir une ou une liste d'opportunité(s) d'affaire en devis.

..note:: Exercice 10 – Créez un devis à partir de l'opportunité d'affaire

    Reconnectez-vous en tant que Luc et faites un devis à partir de l'opportunité d'affaire "Dubois sprl" avec les produits suivants:

	* Un projet de design de cuisine
	* Une armoire de 100cm

    N'oubliez pas de clôturer l'opportunité puisque nous allons faire le suivi à partir du devis.

Gérer avec la CRM
=================

Luc, le directeur commercial, voudrait vérifier la qualité de son équipe commerciale.

..note:: Exercice 11 – Délai moyen pour clôturer une opportunité

    Parmi les différents rapports de reporting fournis par le module CRM,  trouvez celui qui permet de connaître le temps moyen pour répondre à une requête d'un client (c'est à dire pour clôturer une opportunité d'affaire).

[Problème bug?]Luc remarque que le temps moyen pour clôturer une opportunité d'affaire est de 7 jours. Ce délai semble trop long pour lui. Etant donné qu'il veut améliorer la qualité de l'équipe commerciale, il aimerait recevoir une message d'alerte par email à chaque fois qu'une opportunité d'affaire n'est pas clôturée endéans les 5 jours après sa création.

..note:: Exercice 12 – Rappel par email [Problème bug?]

    Créez une règle pour la CRM spécifiant qu'il faut envoyer un rappel au responsable si l'opportunité d'affaire n'est pas clôturé après 5 jours. Pour les prospects, il accepte seulement un délai de 3 jours avant de les clôturer. Mettre Luc en copie du mail quand le rappel est envoyé.

[Problème bug?]La société a différentes politiques pour gérer les prospects non-qualifiés et les réelles opportunité d'affaire. Les prospects sont gardés dans une réserve de prospects non assignés quand ils sont créés. Ensuite, les différents utilisateurs prennent les prospects et se les assignent périodiquement.

Pour les opportunités d'affaire, c'est différent. Toutes les opportunités d'affaire doivent être assignées à Luc. Ensuite, Luc décide s'il veut assigner le cas à quelqu'un autre ou de s'en occuper lui-même.

..note:: Exercice 13 – Assignation et réserve de cas disponibles [Problème bug?]

Trouvez un moyen d'obtenir une liste de tous les cas non assignés. Trouvez un moyen d'assigner automatiquement les opportunités d'affaire à Luc dès qu'ils sont créés.
