**************************
Gestion Documentaire (DMS)
**************************

Configuration de la DMS
=======================

Etant donné la croissance rapide de la société NotSoTiny, le besoin de stocker, tracer, indexer et rediriger correctement tous les documents est primordial. Ils ont besoin ... ???

Donc vous décidez de leur installer la gestion documentaire intégrée d'Open ERP afin d'avoir un méchanisme de stockage centralisé et des processus définis pour tous les documents.

..note:: Exercice 1 – Installez la DMS

Installez et configurez le module pour la gestion documentaire.

Vous allez d'abord commencer par créer la structure de la DMS en utilisant l'accès FTP. Donc vous devrez vous connecter au serveur FTP and créer la structure suivante:

* Documents
	* Ventes
	* Projets
	* Employés

..note:: Exercice 2 – Connection au serveur FTP

NotSoTiny a édcidé de classifier tous les documents selon les projets ou commandes associées. Ils ont besoin d'une structure de répertoires générée automatiquement qui reflète les commandes actuelles.

..note:: Exercice 3 – Configurez la DMS pour les commandes clients

Configurez la DMS afin d'avoir automatiquement un répertoire par commande sous le répertoire « Ventes ».

Maintenant, les employés peuvent envoyer au serveur FTP à chaque fois qu'il ont un document lié à une commande client...Expliquez les avantages de cela...

..note:: Exercice 4 – Envoyez un document lié au SO/001

A partir de l'accès FTP, copiez un document dans le répertoire du SO/001. Ensuite, connectez-vous à l'interface d'Open ERP et vérifiez qu'il y a bien un attachement disponible sur le SO/001. Faites ensuite l'inverse: attachez un document au SO/001 à partir de l'interface Open ERP et téléchargez ce document depuis l'accès FTP.

Vous remarquez que le commercial perd beaucoup de temps à envoyez les différents devis par email ou par fax aux clients. Ce dont vous avez besoin, c'est d'un moyen efficace de stocker et rendre disponible les impressions des devis et commandes. Afin d'améliorer l'efficacité de la DMS, vous voulez obtenir automatiquement un fichier .PDF dans chaque répertoire, qui est le résultat de l'impression de la commande.

..note:: Exercice 5 – Fichiers imprimés virtuels

Configurez la DMS afin de voir un fichier « SO001_print.pdf » sous chaque répertoire des commandes. Ce fichier doit être le résultat de l'impression d'une commande.



A faire:

* Modèles de répertoire fixe
* Recherche d'un fichier
	* En utilisant les méta données (partenaire)
	* En utilisant le contenu indexé
* A chaque fois que quelqu'un lit un fichier virtuel, une copie doit être sauvée en attachement.

