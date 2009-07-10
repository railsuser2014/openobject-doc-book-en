***************************
Installation et paramétrage
***************************

Création d'une base de données
==============================

[Expliquer comment faire avec Odoo]

* Inscription sur Odoo
* Se connecter à la base de données

Ou installation manuelle

* Installer manuellement
* Créer une base de données

..note:: Exercice 1 – Installer Open ERP

Afin de configurer le système, vous devez commencer par préparer une nouvelle base de données pour NotSoTiny. Durant le processus, vous devez configurer l'en-tête et pied de page des documents de NotSoTiny. Donnez-leur un logo et une adresse:

	NotSoTiny SARL
	Rue du Nid 1
	75000 Paris
	France

NotSoTiny prévoit d'utiliser Open ERP pour gérer toutes leurs activités. Les besoins de base de la société NotSoTiny ont été définies ci-dessus, donc vous avez maintenant la responsabilité d'installer et configurer la base de données en sélectionnant les modules qui seront nécessaires à NotSoTiny.

Vous devez tenir compte des départements, mais dans le but de ne pas compliquer le système, vous ne devez pas installer les modules qui ne seront pas utilisés par NotSoTiny. Il est préférable d'installer trop peu que trop de modules.

..note:: Exercice 2 – Installer les modules requis

Afin de configurer le système, vous devez installer et configurer les modules nécessaires à la société NotSoTiny. Relisez les informations sur leurs activités et départements pour pouvoir sélectionner les modules qui correspondront le mieux à leurs besoins.

Paramétrage du système
======================

Ensuite, nous chargeons une personnes de la société de nous fournir une inventaire des différents utilisateurs. NotSoTiny nous fournit alors le tableau simplifié suivant:

----------------------------------------------
|Employé|Rôle|Login|Mot de passe|Activités|
----------------------------------------------
|Fabien Dupont|CEO|fabien|fabien|Accès à toutes les fonctionnalités, sauf à l'administration de l'ERP|
|Luc Lecoq|CSO&CFO|luc|luc|Accès à tous les documents financiers et commerciaux|
|Eric Dubois|ouvrier|eric|eric|accès aux ordres de production, menu le plus simple possible|

..note:: Exercice 3 – Créez les différents users

Definissez les différents utilisateurs et assignez les aux bons groupes. Etant donné que ceci n'est qu'un prototype pour une démonstration, assignez les groupes existants, sans créer des règles spécifiques.

Luc Lecoq, le co-fondateur et directeur finacier/commercial insiste pour avoir un tableau de bord qui apparaîtra automatiquement lors de sa connection au système. En effet, chaque matin quand il arrive au bureau, la première chose qu'il a besoin de voir ce sont ses statistiques de ventes.

..note:: Exercice 4 – Assignez un tableau de bord des ventes à la connection de Luc

Mettez en place un tableau de bord 'Responsable des ventes' à Luc. Ce tableau de bord doit apparaître quand il se connecte.

Fabien pense que leur base de données clients est la plus grande valeur de leur société. Depuis le début de la création de la société, ils ont définis des règles très strictes sur comment garder et maintenir leur base de données clients. Une des exigences de Fabien pour son ERP est que personnes n'a le droit de supprimer un partenaire de la base de données. Fabien doit être le seul utilisateur a avoir le droit de supprimer un partenaire de la base de données.

..note:: Erxercice 5 – Modifiez les règles de sécurité

Créez une nouveau groupe d'utilisateurs qui a le droit de supprimer un partenaire. Vérifiez que les autres groupes n'ont pas ce droit. Assignez ce nouveau groupe à Fabien.

Mise en place de la base de données
===================================

Afin de préparer votre prototype, vous demandez à NotSoTiny de vous fournir les fichiers qui contiennent leur données principales. Le but est d'importer tous leur partenaires dans la base de données.

Ils ont exporté 3 tables de leur ancien logiciel Sage:

* Catégories de clients et fournisseurs
* Liste des clients
* Liste des fournisseurs

NotSoTiny vous a envoyé 3 fichiers .CSV (Comma Separated Values) contenant ces données. Voici une copie de quelques enregistrements de ces fichiers:

* categories.csv
Clients
Détaillants
Fournisseurs bois
Fournisseurs divers

* clients.csv
Nom, Nom contact, Ville, Pays, Catégorie
The Shelve House, Henry Chard, Paris, France, Détaillants
ZeroOne Inc, Geoff, Bruxelles, Belgique, Clients

* fournisseurs.csv
Nom, Nom contact, Ville, Pays, Catégorie
Wood y Wood Pecker, Roger Pecker, Kainuu, Finland, Fournisseurs bois
Vicking Direct, , Bruxelles, Belgique, Fournisseurs divers

..note:: Exercice 6 – Définissez les catégories de partenaires

Etant donné qu'il n'y a que quelques catégories, nous vous suggérons de les encoder manuellement. Dans un but de clareté, vous pouvez structurer leurs catégories en arbre hiérarchique.

..note:: Exercice 7 – Importez les partenaires

NotSoTiny vous a fourni des fichiers d'environ 1200 clients et 200 fournisseurs. Pour votre prototype, créez des fichiers .csv avec les données ci-dessus et importez ces partenaires en utilisant l'outil d'importation .csv d'Open ERP.

..note:: Question – Comment retrouver facilement la liste des fournisseurs de bois?

Mise en place des produits
==========================

Après une analyse rapide de leurs produits, Luc, le directeur des ventes vous fournit une liste des catégories de leurs produits:

* Produits vendable
	* Services
	* Armoires
* Autres produits

..note:: Exercice 8 – Catégories de produits

Avant de mettre en place les produits, vous devez d'abord définir les catégories de produits disponibles. Créez la structure des catégories de produits en utilisant les données fournies par Luc, le directeur des ventes.

NotSoTiny n'a pas encore fourni le fichier d'exportation de leur produits. Afin de ne pas prendre de retard dans le projet, vous décidez d'encoder manuellement quelques produits. Vous allez encoder seulement 4 produits pour le moment, mais vous en encoderez d'autres quand vous recevrez la liste complète des produits.

Voici une liste de quelques produits à encoder, avec leur caractéristiques principales:

|Code|Description|Type|Unité de mesure|Px clients|Coût|Supply method|Procure method|Fournisseur|Delai livraison|Catégorie|Taxe
------------------------------------------------------------------
|ARM100|Armoire 100cm|Produit|PCE|130€|50€|Sur stock|Produire|/|/|Armoires|21% vente|
|ARM200|Armoire 200cm|Produit|PCE|210€|80€|Sur commande|Produire|/|/|Armoires|21% vente|
|BOIS002|Bois 2mm|Produit|Mètre|10€|5€|Sur stock|Acheter|Wood y Wood Pecker|2 semaines|Autres produits|21% achat|
|PROJ|Projet Design cuisine|Service|Heure|90€|20€|Sur commande|Produire|/|/|Services|

..note:: Exercice 9 – Produits

Créez ces produits dans la base de données de NotSoTiny.

Afin de pouvoir vendre quelques produits, vous allez encoder un inventaire de départ. Actuellement, voici le niveau de stock des produits décrits ci-dessus:

|Code|Stock|
------------
|ARM100|50 pièces|
|ARM200|20 pièces|
|BOIS002|20 mètres|

..note:: Exercice 10 – Créez l'inventaire du stock initial

Créez l'inventaire du stock initial. Une fois l'inventaire confirmé, vous devriez voir le stock réel de chaque produit sur la fiche produit.

..note:: Exercice 11 – Testez le système

Vous devriez maintenant être capable de tester le système. Effectuez les opérations suivantes:

* Créez un devis:

	* Client: ZeroOne Inc
	* Produits: 1 projet design cuisine, 3 armoires 100cm

* Convertissez le devis en commande confirmée
* Livrez les armoires au client
* Générez la facture brouillon
* Confirmez la facture et imprimez-la

..note:: Exercice 12 – Vérifiez le niveau de stock

Vous pouvez maintenant tester le niveau de stock du produit ARM100. Il devrait y avoir 47 pièces en stock.


