
.. i18n: ***************************
.. i18n: Installation et paramétrage
.. i18n: ***************************

***************************
Installation et paramétrage
***************************

.. i18n: Création d'une base de données
.. i18n: ==============================

Création d'une base de données
==============================

.. i18n: Expliquer comment faire avec Odoo

Expliquer comment faire avec Odoo

.. i18n: * Inscription sur Odoo
.. i18n: * Se connecter à la base de données

* Inscription sur Odoo
* Se connecter à la base de données

.. i18n: Ou installation manuelle

Ou installation manuelle

.. i18n: * Installer manuellement
.. i18n: * Créer une base de données

* Installer manuellement
* Créer une base de données

.. i18n: .. note:: Exercice 1 – Installer Open ERP et créer une nouvelle base de données
.. i18n: 
.. i18n:     Afin de configurer le système, vous devez commencer par préparer une nouvelle base de données pour NotSoTiny. Votre prototype sera construit à partir d'une base vide, donc il ne faut pas charger les données démo. Choisissez la langue du système (FR) et prenez le profil minimal car les différents modules seront chargés au fur et à mesure des besoins. Durant le processus, vous devrez configurer l'en-tête et pied de page des documents de NotSoTiny. Donnez-leur un logo et l'adresse suivante:
.. i18n: 
.. i18n: 	NotSoTiny SARL
.. i18n: 	Rue du Nid 1
.. i18n: 	5000 Namur
.. i18n: 	Bruxelles

.. note:: Exercice 1 – Installer Open ERP et créer une nouvelle base de données

    Afin de configurer le système, vous devez commencer par préparer une nouvelle base de données pour NotSoTiny. Votre prototype sera construit à partir d'une base vide, donc il ne faut pas charger les données démo. Choisissez la langue du système (FR) et prenez le profil minimal car les différents modules seront chargés au fur et à mesure des besoins. Durant le processus, vous devrez configurer l'en-tête et pied de page des documents de NotSoTiny. Donnez-leur un logo et l'adresse suivante:

	NotSoTiny SARL
	Rue du Nid 1
	5000 Namur
	Bruxelles

.. i18n: NotSoTiny prévoit d'utiliser Open ERP pour gérer toutes leurs activités. Les besoins de base de la société NotSoTiny ont été définies ci-dessus, donc vous avez maintenant la responsabilité d'installer et de configurer la base de données en sélectionnant les modules qui seront nécessaires à NotSoTiny.

NotSoTiny prévoit d'utiliser Open ERP pour gérer toutes leurs activités. Les besoins de base de la société NotSoTiny ont été définies ci-dessus, donc vous avez maintenant la responsabilité d'installer et de configurer la base de données en sélectionnant les modules qui seront nécessaires à NotSoTiny.

.. i18n: Vous devez tenir compte des départements, mais dans le but de ne pas compliquer le système, vous ne devez pas installer les modules qui ne seront pas utilisés par NotSoTiny. Il est préférable d'installer trop peu que trop de modules.

Vous devez tenir compte des départements, mais dans le but de ne pas compliquer le système, vous ne devez pas installer les modules qui ne seront pas utilisés par NotSoTiny. Il est préférable d'installer trop peu que trop de modules.

.. i18n: .. note:: Exercice 2 – Installer les modules requis
.. i18n: 
.. i18n:     Afin de configurer le système, vous devez installer et configurer les modules nécessaires à la société NotSoTiny. Relisez les informations sur leurs activités et départements pour pouvoir sélectionner les modules qui correspondront le mieux à leurs besoins. NotSoTiny est une société commerciale de vente et de fabrication de produits. Pour le moment, vous devez donc installer les modules 'sale' (pour gérer la vente, la production, les stocks et la facturation des produits) et 'delivery' (pour gérer la livraison des produits). Concernant la comptabilité, prenez le plan de compte belge.

.. note:: Exercice 2 – Installer les modules requis

    Afin de configurer le système, vous devez installer et configurer les modules nécessaires à la société NotSoTiny. Relisez les informations sur leurs activités et départements pour pouvoir sélectionner les modules qui correspondront le mieux à leurs besoins. NotSoTiny est une société commerciale de vente et de fabrication de produits. Pour le moment, vous devez donc installer les modules 'sale' (pour gérer la vente, la production, les stocks et la facturation des produits) et 'delivery' (pour gérer la livraison des produits). Concernant la comptabilité, prenez le plan de compte belge.

.. i18n: Paramétrage du système
.. i18n: ======================

Paramétrage du système
======================

.. i18n: Ensuite, nous chargeons une personne de la société de nous fournir un inventaire des différents utilisateurs. NotSoTiny nous fournit alors le tableau simplifié suivant:

Ensuite, nous chargeons une personne de la société de nous fournir un inventaire des différents utilisateurs. NotSoTiny nous fournit alors le tableau simplifié suivant:

.. i18n: +---------------+--------+--------------+------------------------------+----------------------------------------------------------------------------+
.. i18n: | Employé       | Login  | Mot de passe | Fonction                     | Activités                                                                  |
.. i18n: +===============+========+==============+==============================+============================================================================+
.. i18n: | Fabien Dupont | fabien | fabien       | CEO                          | Accès à toutes les fonctionnalités, sauf à l'administration de l'ERP       |
.. i18n: +---------------+--------+--------------+------------------------------+----------------------------------------------------------------------------+
.. i18n: | Luc Lecoq     | luc    | luc          | Dir. Commercial et Financier | Accès à tous les documents financiers et commerciaux, responsable clients  |
.. i18n: +---------------+--------+--------------+------------------------------+----------------------------------------------------------------------------+
.. i18n: | Eric Dubois   | eric   | eric         | Ouvrier                      | Accès aux ordres de production, et à la CRM, menu le plus simple possible  |
.. i18n: +---------------+--------+--------------+------------------------------+----------------------------------------------------------------------------+
.. i18n: | Thomas Lebrun | thomas | thomas       | Commercial                   | Accès aux ventes, à la CRM, responsable clients                            |
.. i18n: +---------------+--------+--------------+------------------------------+----------------------------------------------------------------------------+

+---------------+--------+--------------+------------------------------+----------------------------------------------------------------------------+
| Employé       | Login  | Mot de passe | Fonction                     | Activités                                                                  |
+===============+========+==============+==============================+============================================================================+
| Fabien Dupont | fabien | fabien       | CEO                          | Accès à toutes les fonctionnalités, sauf à l'administration de l'ERP       |
+---------------+--------+--------------+------------------------------+----------------------------------------------------------------------------+
| Luc Lecoq     | luc    | luc          | Dir. Commercial et Financier | Accès à tous les documents financiers et commerciaux, responsable clients  |
+---------------+--------+--------------+------------------------------+----------------------------------------------------------------------------+
| Eric Dubois   | eric   | eric         | Ouvrier                      | Accès aux ordres de production, et à la CRM, menu le plus simple possible  |
+---------------+--------+--------------+------------------------------+----------------------------------------------------------------------------+
| Thomas Lebrun | thomas | thomas       | Commercial                   | Accès aux ventes, à la CRM, responsable clients                            |
+---------------+--------+--------------+------------------------------+----------------------------------------------------------------------------+

.. i18n: .. note:: Exercice 3 – Créer les différents utilisateurs
.. i18n: 
.. i18n:     Definissez les différents utilisateurs et selon leurs activités, assignez les aux bons groupes. Etant donné que ceci n'est qu'un prototype pour une démonstration, assignez les groupes existants, sans créer de règles spécifiques. La fonction n'est mentionnée ici qu'à titre informatif.

.. note:: Exercice 3 – Créer les différents utilisateurs

    Definissez les différents utilisateurs et selon leurs activités, assignez les aux bons groupes. Etant donné que ceci n'est qu'un prototype pour une démonstration, assignez les groupes existants, sans créer de règles spécifiques. La fonction n'est mentionnée ici qu'à titre informatif.

.. i18n: Luc Lecoq, le co-fondateur et directeur financier/commercial insiste pour avoir un tableau de bord qui apparaîtra automatiquement lors de sa connection au système. En effet, chaque matin quand il arrive au bureau, la première chose qu'il a besoin de voir ce sont ses statistiques de ventes.

Luc Lecoq, le co-fondateur et directeur financier/commercial insiste pour avoir un tableau de bord qui apparaîtra automatiquement lors de sa connection au système. En effet, chaque matin quand il arrive au bureau, la première chose qu'il a besoin de voir ce sont ses statistiques de ventes.

.. i18n: .. note:: Exercice 4 – Assigner un tableau de bord des ventes à la connection de Luc
.. i18n: 
.. i18n:     Mettez en place un tableau de bord 'Responsable des ventes' à Luc en installant d'abord le module 'board_sale'. Ce tableau de bord doit apparaître quand il se connecte, pour cela, il faut changer la page d'accueil de son utilisateur. Connectez-vous en tant que Luc et voyez si votre première page d'accueil est bien le tableau de bord des ventes.

.. note:: Exercice 4 – Assigner un tableau de bord des ventes à la connection de Luc

    Mettez en place un tableau de bord 'Responsable des ventes' à Luc en installant d'abord le module 'board_sale'. Ce tableau de bord doit apparaître quand il se connecte, pour cela, il faut changer la page d'accueil de son utilisateur. Connectez-vous en tant que Luc et voyez si votre première page d'accueil est bien le tableau de bord des ventes.

.. i18n: Fabien pense que leur base de données clients est la plus grande valeur de leur société. Depuis le début de la création de la société, ils ont définis des règles très strictes sur comment garder et maintenir leur base de données clients. Une des exigences spécifique de Fabien pour son ERP est que personne n'a le droit de supprimer un partenaire de la base de données. Fabien doit être le seul utilisateur à pouvoir le faire.

Fabien pense que leur base de données clients est la plus grande valeur de leur société. Depuis le début de la création de la société, ils ont définis des règles très strictes sur comment garder et maintenir leur base de données clients. Une des exigences spécifique de Fabien pour son ERP est que personne n'a le droit de supprimer un partenaire de la base de données. Fabien doit être le seul utilisateur à pouvoir le faire.

.. i18n: .. note:: Exercice 5 – Modifier les règles de sécurité
.. i18n: 
.. i18n:     Créez un nouveau groupe d'utilisateurs ayant comme nom "Suppression partenaires". Ce groupe ne comportera qu'une seule règle de droit d'accès qui est la permission de supprimer les fiches partenaires. Assignez ce nouveau groupe à l'utilisateur 'Fabien'. Vérifiez que les autres groupes n'ont pas ce droit. Testez vos règles en sécurité en essayant de supprimer un partenaire quand vous êtes connecté en tant que Fabien, puis en tant que Luc. 

.. note:: Exercice 5 – Modifier les règles de sécurité

    Créez un nouveau groupe d'utilisateurs ayant comme nom "Suppression partenaires". Ce groupe ne comportera qu'une seule règle de droit d'accès qui est la permission de supprimer les fiches partenaires. Assignez ce nouveau groupe à l'utilisateur 'Fabien'. Vérifiez que les autres groupes n'ont pas ce droit. Testez vos règles en sécurité en essayant de supprimer un partenaire quand vous êtes connecté en tant que Fabien, puis en tant que Luc. 

.. i18n: Mise en place de la base de données
.. i18n: ===================================

Mise en place de la base de données
===================================

.. i18n: Afin de préparer votre prototype, vous demandez à NotSoTiny de vous fournir les fichiers qui contiennent leur données principales. Le but est d'importer tous leurs partenaires dans la base de données.

Afin de préparer votre prototype, vous demandez à NotSoTiny de vous fournir les fichiers qui contiennent leur données principales. Le but est d'importer tous leurs partenaires dans la base de données.

.. i18n: Ils ont exporté 3 tables de leur ancien logiciel Sage:

Ils ont exporté 3 tables de leur ancien logiciel Sage:

.. i18n: * Catégories de clients et fournisseurs
.. i18n: * Liste des clients
.. i18n: * Liste des fournisseurs

* Catégories de clients et fournisseurs
* Liste des clients
* Liste des fournisseurs

.. i18n: NotSoTiny vous a envoyé 3 fichiers .CSV (Comma Separated Values) contenant ces données. Voici une copie de quelques enregistrements de ces fichiers:

NotSoTiny vous a envoyé 3 fichiers .CSV (Comma Separated Values) contenant ces données. Voici une copie de quelques enregistrements de ces fichiers:

.. i18n: * categories.csv::
.. i18n: 
.. i18n:     Nom
.. i18n:     Clients directs
.. i18n:     Détaillants
.. i18n:     Fournisseurs bois
.. i18n:     Fournisseurs divers
.. i18n: 
.. i18n: * clients.csv::
.. i18n: 
.. i18n:     Nom, Nom contact, Ville, Pays, Catégorie
.. i18n:     The Shelve House, Henry Chard, Paris, France, Détaillants
.. i18n:     ZeroOne Inc, Geoff, Bruxelles, Belgique, Clients directs
.. i18n: 
.. i18n: * fournisseurs.csv::
.. i18n: 
.. i18n:     Nom, Nom contact, Ville, Pays, Catégorie
.. i18n:     Wood y Wood Pecker, Roger Pecker, Kainuu, Finlande, Fournisseurs bois
.. i18n:     Vicking Direct, , Bruxelles, Belgique, Fournisseurs divers

* categories.csv::

    Nom
    Clients directs
    Détaillants
    Fournisseurs bois
    Fournisseurs divers

* clients.csv::

    Nom, Nom contact, Ville, Pays, Catégorie
    The Shelve House, Henry Chard, Paris, France, Détaillants
    ZeroOne Inc, Geoff, Bruxelles, Belgique, Clients directs

* fournisseurs.csv::

    Nom, Nom contact, Ville, Pays, Catégorie
    Wood y Wood Pecker, Roger Pecker, Kainuu, Finlande, Fournisseurs bois
    Vicking Direct, , Bruxelles, Belgique, Fournisseurs divers

.. i18n: .. note:: Exercice 6 – Définir les catégories de partenaires
.. i18n: 
.. i18n:     Etant donné qu'il n'y a que quelques catégories, nous vous suggérons de les encoder manuellement. Dans un but de clareté, vous pouvez structurer leurs catégories en arbre hiérarchique (2 catégories principales: Clients et Fournisseurs qui contiennent les sous-catégories définies dans le fichier).

.. note:: Exercice 6 – Définir les catégories de partenaires

    Etant donné qu'il n'y a que quelques catégories, nous vous suggérons de les encoder manuellement. Dans un but de clareté, vous pouvez structurer leurs catégories en arbre hiérarchique (2 catégories principales: Clients et Fournisseurs qui contiennent les sous-catégories définies dans le fichier).

.. i18n: .. note:: Exercice 7 – Importer les partenaires
.. i18n: 
.. i18n:     NotSoTiny vous a fourni des fichiers d'environ 1200 clients et 200 fournisseurs. Pour votre prototype, vous n'aurez besoin que de quelques données démo. Créez des fichiers dans un tableur avec les données ci-dessus (sans la première ligne de titres des colonnes), sauvegardez-les au format .csv. Importez ces partenaires en utilisant l'outil d'importation .csv d'Open ERP dans lequel vous définirez les champs à importer.

.. note:: Exercice 7 – Importer les partenaires

    NotSoTiny vous a fourni des fichiers d'environ 1200 clients et 200 fournisseurs. Pour votre prototype, vous n'aurez besoin que de quelques données démo. Créez des fichiers dans un tableur avec les données ci-dessus (sans la première ligne de titres des colonnes), sauvegardez-les au format .csv. Importez ces partenaires en utilisant l'outil d'importation .csv d'Open ERP dans lequel vous définirez les champs à importer.

.. i18n: Mise en place des produits
.. i18n: ==========================

Mise en place des produits
==========================

.. i18n: Après une analyse rapide de leurs produits, Luc, le directeur commercial, vous fournit une liste des catégories de leurs produits:

Après une analyse rapide de leurs produits, Luc, le directeur commercial, vous fournit une liste des catégories de leurs produits:

.. i18n: * Produits vendables
.. i18n: 	* Services
.. i18n: 	* Armoires
.. i18n: * Autres produits
.. i18n:     * Matières premières
.. i18n:     * Fournitures diverses

* Produits vendables
	* Services
	* Armoires
* Autres produits
    * Matières premières
    * Fournitures diverses

.. i18n: .. note:: Exercice 8 – Définir les catégories de produits
.. i18n: 
.. i18n:     Avant de mettre en place les produits, vous devez d'abord définir les catégories de produits nécessaires. Créez la structure de catégories de produits en utilisant les données fournies par Luc, le directeur des ventes.

.. note:: Exercice 8 – Définir les catégories de produits

    Avant de mettre en place les produits, vous devez d'abord définir les catégories de produits nécessaires. Créez la structure de catégories de produits en utilisant les données fournies par Luc, le directeur des ventes.

.. i18n: NotSoTiny n'a pas encore fourni le fichier d'exportation de leurs produits. Afin de ne pas prendre de retard dans le projet, vous décidez d'encoder manuellement quelques produits.

NotSoTiny n'a pas encore fourni le fichier d'exportation de leurs produits. Afin de ne pas prendre de retard dans le projet, vous décidez d'encoder manuellement quelques produits.

.. i18n: Voici une liste de quelques produits à encoder, avec leur caractéristiques principales:

Voici une liste de quelques produits à encoder, avec leur caractéristiques principales:

.. i18n: .. csv-table::
.. i18n:     :header: Code, Description, Type, Unité de mesure, Px clients, Coût, Méthode acqui, Méthode appro, Fournisseur, Delai livr., Catégorie, Taxe
.. i18n:     :widths: 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
.. i18n: 
.. i18n:     ARM100  , Armoire 100cm         , Produit , PCE              , 130€     , 50€ , Sur stock      , Produire       , /                  , /           , Armoires        , 21%vente
.. i18n:     ARM200  , Armoire 200cm         , Produit , PCE              , 210€     , 80€ , Sur commande   , Produire       , /                  , /           , Armoires        , 21%vente
.. i18n:     BOIS002 , Bois 2mm              , Produit , Mètre           , 10€      , 5€  , Sur stock      , Acheter        , Wood y Wood Pecker , 2 semaines  , Autres produits , 21%achat
.. i18n:     PROJ    , Projet Design cuisine , Service , Heure            , 90€      , 20€ , Sur commande   , Produire       , /                  , /           , Services        , 21%vente

.. csv-table::
    :header: Code, Description, Type, Unité de mesure, Px clients, Coût, Méthode acqui, Méthode appro, Fournisseur, Delai livr., Catégorie, Taxe
    :widths: 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10

    ARM100  , Armoire 100cm         , Produit , PCE              , 130€     , 50€ , Sur stock      , Produire       , /                  , /           , Armoires        , 21%vente
    ARM200  , Armoire 200cm         , Produit , PCE              , 210€     , 80€ , Sur commande   , Produire       , /                  , /           , Armoires        , 21%vente
    BOIS002 , Bois 2mm              , Produit , Mètre           , 10€      , 5€  , Sur stock      , Acheter        , Wood y Wood Pecker , 2 semaines  , Autres produits , 21%achat
    PROJ    , Projet Design cuisine , Service , Heure            , 90€      , 20€ , Sur commande   , Produire       , /                  , /           , Services        , 21%vente

.. i18n: En analysant ces produits, vous remarquez qu'il y a différentes unités de mesure: les armoires sont vendues à la pièce, le bois est acheté au mètre, les services sont vendus en heure. Il faudra donc vérifier si Open ERP peut déjà gérer ces différentes unités de mesure ou s'il faudra en créer des nouvelles. En vérifiant dans le système actuel, vous constatez que les seules catégories disponibles sont 'Unité' et 'Masse', il faudra donc ajouter des nouvelles catégories pour gérer les mètres et les heures.

En analysant ces produits, vous remarquez qu'il y a différentes unités de mesure: les armoires sont vendues à la pièce, le bois est acheté au mètre, les services sont vendus en heure. Il faudra donc vérifier si Open ERP peut déjà gérer ces différentes unités de mesure ou s'il faudra en créer des nouvelles. En vérifiant dans le système actuel, vous constatez que les seules catégories disponibles sont 'Unité' et 'Masse', il faudra donc ajouter des nouvelles catégories pour gérer les mètres et les heures.

.. i18n: +-----------+-----------------+
.. i18n: | Catégorie | Unité de mesure |
.. i18n: +-----------+-----------------+
.. i18n: | Longueur  | Mètre           |
.. i18n: +-----------+-----------------+
.. i18n: | Temps     | Heure           |
.. i18n: +-----------+-----------------+

+-----------+-----------------+
| Catégorie | Unité de mesure |
+-----------+-----------------+
| Longueur  | Mètre           |
+-----------+-----------------+
| Temps     | Heure           |
+-----------+-----------------+

.. i18n: .. note:: Exercice 9 - Créer les catégories et les unités de mesure
.. i18n: 
.. i18n:     Créez d'abord les catégories avant de créer les unités de mesure définies ci-dessus.

.. note:: Exercice 9 - Créer les catégories et les unités de mesure

    Créez d'abord les catégories avant de créer les unités de mesure définies ci-dessus.

.. i18n: .. note:: Exercice 10 – Encodage des produits
.. i18n: 
.. i18n:     Maintenant que vous avez créé les unités de mesure manquantes, vous êtes en mesure d'encoder les produits définis plus haut dans la base de données de NotSoTiny. Vous allez encoder seulement 4 produits pour le moment, mais vous en encoderez d'autres quand vous recevrez la liste complète des produits.

.. note:: Exercice 10 – Encodage des produits

    Maintenant que vous avez créé les unités de mesure manquantes, vous êtes en mesure d'encoder les produits définis plus haut dans la base de données de NotSoTiny. Vous allez encoder seulement 4 produits pour le moment, mais vous en encoderez d'autres quand vous recevrez la liste complète des produits.

.. i18n: Pour les tests du prototype, afin de pouvoir vendre quelques produits, vous allez encoder un inventaire de départ. Actuellement, voici le niveau de stock des produits décrits ci-dessus:

Pour les tests du prototype, afin de pouvoir vendre quelques produits, vous allez encoder un inventaire de départ. Actuellement, voici le niveau de stock des produits décrits ci-dessus:

.. i18n: +---------+-----------+
.. i18n: | Code    | Stock     |
.. i18n: +=========+===========+
.. i18n: | ARM100  | 50 pièces |
.. i18n: +---------+-----------+
.. i18n: | ARM200  | 20 pièces |
.. i18n: +---------+-----------+
.. i18n: | BOIS002 | 20 mètres |
.. i18n: +---------+-----------+

+---------+-----------+
| Code    | Stock     |
+=========+===========+
| ARM100  | 50 pièces |
+---------+-----------+
| ARM200  | 20 pièces |
+---------+-----------+
| BOIS002 | 20 mètres |
+---------+-----------+

.. i18n: .. note:: Exercice 10 – Créez l'inventaire du stock initial
.. i18n: 
.. i18n:     Créez l'inventaire du stock initial. Une fois l'inventaire confirmé, vous devriez voir le stock réel de chaque produit sur la fiche produit.

.. note:: Exercice 10 – Créez l'inventaire du stock initial

    Créez l'inventaire du stock initial. Une fois l'inventaire confirmé, vous devriez voir le stock réel de chaque produit sur la fiche produit.

.. i18n: .. note:: Exercice 11 – Testez le système
.. i18n: 
.. i18n:     Vous devriez maintenant être capable de tester le système. Pour cela, effectuez les opérations suivantes:

.. note:: Exercice 11 – Testez le système

    Vous devriez maintenant être capable de tester le système. Pour cela, effectuez les opérations suivantes:

.. i18n: * Créez un devis:
.. i18n: 
.. i18n: 	* Client: ZeroOne Inc
.. i18n: 	* Produits: 1 projet design cuisine, 3 armoires 100cm
.. i18n: 
.. i18n: * Convertissez le devis en commande confirmée
.. i18n: * Livrez les armoires au client
.. i18n: * Générez la facture brouillon
.. i18n: * Confirmez la facture et imprimez-la

* Créez un devis:

	* Client: ZeroOne Inc
	* Produits: 1 projet design cuisine, 3 armoires 100cm

* Convertissez le devis en commande confirmée
* Livrez les armoires au client
* Générez la facture brouillon
* Confirmez la facture et imprimez-la

.. i18n: .. note:: Exercice 12 – Vérifiez le niveau de stock
.. i18n: 
.. i18n:     Vous pouvez maintenant tester le niveau de stock du produit ARM100. Il devrait y avoir 47 pièces en stock.

.. note:: Exercice 12 – Vérifiez le niveau de stock

    Vous pouvez maintenant tester le niveau de stock du produit ARM100. Il devrait y avoir 47 pièces en stock.
