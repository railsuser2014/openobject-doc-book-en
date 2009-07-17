
.. i18n: ********************
.. i18n: Gestion des services
.. i18n: ********************

********************
Gestion des services
********************

.. i18n: Gestion de projets
.. i18n: ==================

Gestion de projets
==================

.. i18n: La société NotSoTiny gère 2 types de projets:

La société NotSoTiny gère 2 types de projets:

.. i18n: * Projets de recherche et développement internes
.. i18n: * Projets de design d'armoires sur mesure pour les clients

* Projets de recherche et développement internes
* Projets de design d'armoires sur mesure pour les clients

.. i18n: Vous êtes chargé de mettre en place un système de gestion des projets de NotSoTiny. Pour les 2 types de projets, ils désirent gérer les tâches des différents utilisateurs. Ils ont besoin d'assigner des tâches, faire des plannings, déléguer du travail et suivre l'avancement des projets.

Vous êtes chargé de mettre en place un système de gestion des projets de NotSoTiny. Pour les 2 types de projets, ils désirent gérer les tâches des différents utilisateurs. Ils ont besoin d'assigner des tâches, faire des plannings, déléguer du travail et suivre l'avancement des projets.

.. i18n: Pour les projets clients, ils veulent aussi vérifier la rentabilité par projet. Vu que ces projets sont vendus au client, ils doivent vérifier les coûts exacts du projet, ce qui inclut: Achat de matériel, temps passé sur le projet, dépenses diverses comme les trajets, etc...

Pour les projets clients, ils veulent aussi vérifier la rentabilité par projet. Vu que ces projets sont vendus au client, ils doivent vérifier les coûts exacts du projet, ce qui inclut: Achat de matériel, temps passé sur le projet, dépenses diverses comme les trajets, etc...

.. i18n: .. note:: Exercice 1 – Installez les modules requis
.. i18n: 
.. i18n:     Installez les  modules nécessaires à la gestion financière et opérationnelle de projets. Pour la gestion purement projet (tâches, planning, etc), il s'agit du module 'project', et pour le suivi financier du projet, il faut y ajouter les modules 'project_timesheet' et 'account_analytic_analysis'.
.. i18n: 
.. i18n:     Ces modules vont générer de nouveaux groupes: 'Project Manager', 'Project Financial Manager' et 'Project User'. Fabien, Luc et Thomas auront les 3 groupes pour gérer les projets et suivre l'aspect financier, seul Eric aura uniquement des tâches à faire, donc n'aura que le groupe 'Project User'. Ajoutez donc les groupes nécessaires à chaque utilisateur. Donnez également le groupe 'Extended view' à tout le monde, sauf Eric, cela permettra la délégation de tâches.

.. note:: Exercice 1 – Installez les modules requis

    Installez les  modules nécessaires à la gestion financière et opérationnelle de projets. Pour la gestion purement projet (tâches, planning, etc), il s'agit du module 'project', et pour le suivi financier du projet, il faut y ajouter les modules 'project_timesheet' et 'account_analytic_analysis'.

    Ces modules vont générer de nouveaux groupes: 'Project Manager', 'Project Financial Manager' et 'Project User'. Fabien, Luc et Thomas auront les 3 groupes pour gérer les projets et suivre l'aspect financier, seul Eric aura uniquement des tâches à faire, donc n'aura que le groupe 'Project User'. Ajoutez donc les groupes nécessaires à chaque utilisateur. Donnez également le groupe 'Extended view' à tout le monde, sauf Eric, cela permettra la délégation de tâches.

.. i18n: Gestion des tâches
.. i18n: ==================

Gestion des tâches
==================

.. i18n: Le département de recherche et développement interne a pour objectif de trouver et développer de nouveaux produits. La société NotSoTiny est en pleine croissance, principalement grâce à ses 2 produits phares qui sont les armoires, mais essaie de se diversifier et voudrait introduire un nouveau produit à sa gamme qui serait un bureau nommé 'COLOSS' pour sa solidité à toute épreuve.

Le département de recherche et développement interne a pour objectif de trouver et développer de nouveaux produits. La société NotSoTiny est en pleine croissance, principalement grâce à ses 2 produits phares qui sont les armoires, mais essaie de se diversifier et voudrait introduire un nouveau produit à sa gamme qui serait un bureau nommé 'COLOSS' pour sa solidité à toute épreuve.

.. i18n: L'équipe R&D met donc en place un projet pour gérer les différentes phases et pour distribuer les tâches aux responsables.

L'équipe R&D met donc en place un projet pour gérer les différentes phases et pour distribuer les tâches aux responsables.

.. i18n: Le projet 'Coloss' se répartira comme suit:

Le projet 'Coloss' se répartira comme suit:

.. i18n: * Design & conception
.. i18n: * Tests Qualité

* Design & conception
* Tests Qualité

.. i18n: Le responsable de ce projet 'Coloss' est Luc, qui supervise le département Recherche & Développement et tiens donc à être tenu au courant de l'avancement des projets.

Le responsable de ce projet 'Coloss' est Luc, qui supervise le département Recherche & Développement et tiens donc à être tenu au courant de l'avancement des projets.

.. i18n: Le second type de projet est le design d'armoires sur mesure pour les clients. Lors du salon House&Design à Paris, une cliente était fortement intéressée par une nouvelle cuisine sur mesure. NotSoTiny a donc signé une commande avec Mme Lucie Vonck pour un nouveau projet que NotSoTiny nomme par le nom du client. Ce projet s'appelera donc 'Lucie Vonck' et sera créé sous un projet générique qui sera 'Projet clients'. Ce genre de projet pour les clients ne comporte pas de sous-projet, il sera juste composé d'une liste de tâches.

Le second type de projet est le design d'armoires sur mesure pour les clients. Lors du salon House&Design à Paris, une cliente était fortement intéressée par une nouvelle cuisine sur mesure. NotSoTiny a donc signé une commande avec Mme Lucie Vonck pour un nouveau projet que NotSoTiny nomme par le nom du client. Ce projet s'appelera donc 'Lucie Vonck' et sera créé sous un projet générique qui sera 'Projet clients'. Ce genre de projet pour les clients ne comporte pas de sous-projet, il sera juste composé d'une liste de tâches.

.. i18n: * Analyse des besoins
.. i18n: * Conception en atelier
.. i18n: * Remise du projet

* Analyse des besoins
* Conception en atelier
* Remise du projet

.. i18n: Le responsable de ce projet 'Lucie Vonck' est le commercial Thomas, qui se chargera de la totalité du projet.
.. i18n: .. note:: Exercice 2 - Créer les projets
.. i18n: 
.. i18n:     Créez les 2 projets décrits ci-dessus avec leur structure. Vous pouvez structurer en mettant le projet 'Coloss' sous un projet 'R&D' et le projet 'Lucie Vonck' sous un projet 'Projets Clients'. Cela permettra d'ajouter d'autres projets internes ou clients de façon claire.

Le responsable de ce projet 'Lucie Vonck' est le commercial Thomas, qui se chargera de la totalité du projet.
.. note:: Exercice 2 - Créer les projets

    Créez les 2 projets décrits ci-dessus avec leur structure. Vous pouvez structurer en mettant le projet 'Coloss' sous un projet 'R&D' et le projet 'Lucie Vonck' sous un projet 'Projets Clients'. Cela permettra d'ajouter d'autres projets internes ou clients de façon claire.

.. i18n: Pour le projet 'Coloss', Luc vous fournit la liste des tâches suivantes:

Pour le projet 'Coloss', Luc vous fournit la liste des tâches suivantes:

.. i18n: +-------------------+-----------------------------------------+-------------+------------------+----------+
.. i18n: | Projet            | Description tâche                       | Responsable | Temps estimé (h) | Séquence |
.. i18n: +===================+=========================================+=============+==================+==========+
.. i18n: | Conception&Design | Valider le modèle avec les designers    | Luc         | 4,00             | 10       |
.. i18n: +-------------------+-----------------------------------------+-------------+------------------+----------+
.. i18n: | Conception&Design | Vérifier les aspects techniques         | Eric        | 4,00             | 10       |
.. i18n: +-------------------+-----------------------------------------+-------------+------------------+----------+
.. i18n: | Conception&Design | Montage                                 | Eric        | 2,00             | 13       |
.. i18n: +-------------------+-----------------------------------------+-------------+------------------+----------+
.. i18n: | Tests Qualité     | Passer le produit par les tests qualité | Luc         | 2,00             | 14       |
.. i18n: +-------------------+-----------------------------------------+-------------+------------------+----------+

+-------------------+-----------------------------------------+-------------+------------------+----------+
| Projet            | Description tâche                       | Responsable | Temps estimé (h) | Séquence |
+===================+=========================================+=============+==================+==========+
| Conception&Design | Valider le modèle avec les designers    | Luc         | 4,00             | 10       |
+-------------------+-----------------------------------------+-------------+------------------+----------+
| Conception&Design | Vérifier les aspects techniques         | Eric        | 4,00             | 10       |
+-------------------+-----------------------------------------+-------------+------------------+----------+
| Conception&Design | Montage                                 | Eric        | 2,00             | 13       |
+-------------------+-----------------------------------------+-------------+------------------+----------+
| Tests Qualité     | Passer le produit par les tests qualité | Luc         | 2,00             | 14       |
+-------------------+-----------------------------------------+-------------+------------------+----------+

.. i18n: Pour le projet 'Design cuisine VONCK', Thomas vous fournit la liste des tâches suivantes:

Pour le projet 'Design cuisine VONCK', Thomas vous fournit la liste des tâches suivantes:

.. i18n: +-----------------------+----------------------------------+-------------+------------------+----------+
.. i18n: | Projet                | Description tâche                | Responsable | Temps estimé (h) | Séquence |
.. i18n: +=======================+==================================+=============+==================+==========+
.. i18n: | Analyse des besoins   | Réunions clients                 | Thomas      | 4,00             | 10       |
.. i18n: +-----------------------+----------------------------------+-------------+------------------+----------+
.. i18n: | Analyse des besoins   | Remise cahier des charges        | Thomas      | 6,00             | 11       |
.. i18n: +-----------------------+----------------------------------+-------------+------------------+----------+
.. i18n: | Conception en atelier | Montage selon Cahier des charges | Thomas      | 6,00             | 12       |
.. i18n: +-----------------------+----------------------------------+-------------+------------------+----------+
.. i18n: | Remise du projet      | Installation chez le client      | Thomas      | 8,00             | 13       |
.. i18n: +-----------------------+----------------------------------+-------------+------------------+----------+
.. i18n: | Remise du projet      | Validation de fin de projet      | Thomas      | 2,00             | 14       |
.. i18n: +-----------------------+----------------------------------+-------------+------------------+----------+

+-----------------------+----------------------------------+-------------+------------------+----------+
| Projet                | Description tâche                | Responsable | Temps estimé (h) | Séquence |
+=======================+==================================+=============+==================+==========+
| Analyse des besoins   | Réunions clients                 | Thomas      | 4,00             | 10       |
+-----------------------+----------------------------------+-------------+------------------+----------+
| Analyse des besoins   | Remise cahier des charges        | Thomas      | 6,00             | 11       |
+-----------------------+----------------------------------+-------------+------------------+----------+
| Conception en atelier | Montage selon Cahier des charges | Thomas      | 6,00             | 12       |
+-----------------------+----------------------------------+-------------+------------------+----------+
| Remise du projet      | Installation chez le client      | Thomas      | 8,00             | 13       |
+-----------------------+----------------------------------+-------------+------------------+----------+
| Remise du projet      | Validation de fin de projet      | Thomas      | 2,00             | 14       |
+-----------------------+----------------------------------+-------------+------------------+----------+

.. i18n: .. note:: Exercice 3 - Créer les tâches
.. i18n: 
.. i18n:     Selon la liste des tâches pour les projets 'Coloss' et 'Design cuisine Vonck', créez les tâches dans Open ERP.

.. note:: Exercice 3 - Créer les tâches

    Selon la liste des tâches pour les projets 'Coloss' et 'Design cuisine Vonck', créez les tâches dans Open ERP.

.. i18n: .. note:: Exercice 4 - Diagramme de Gantt
.. i18n: 
.. i18n:     Pour chacun des projets, allez consulter le diagramme de Gantt pour voir le planning des tâches pour chaque utilisateur et estimez la date de fin des projets, s'ils devaient démarrer aujourd'hui. Ce diagramme considère que les employés travaillent tout le temps, car nous n'avons pas défini de feuille de temps spécifiant les jours et les heures de travail.

.. note:: Exercice 4 - Diagramme de Gantt

    Pour chacun des projets, allez consulter le diagramme de Gantt pour voir le planning des tâches pour chaque utilisateur et estimez la date de fin des projets, s'ils devaient démarrer aujourd'hui. Ce diagramme considère que les employés travaillent tout le temps, car nous n'avons pas défini de feuille de temps spécifiant les jours et les heures de travail.

.. i18n: Thomas a commencé le projet d'étude pour la cuisine de Mme Vonck. Il a déjà été chez elle pour l'analyse des besoin, et a même pris moins de temps que prévu, il est resté 3h en tout. Il a commencé la rédaction du cahier des charges, il a déjà travaillé 2h dessus. Par contre, il aimerait déléguer la tâche du montage en atelier à Eric.

Thomas a commencé le projet d'étude pour la cuisine de Mme Vonck. Il a déjà été chez elle pour l'analyse des besoin, et a même pris moins de temps que prévu, il est resté 3h en tout. Il a commencé la rédaction du cahier des charges, il a déjà travaillé 2h dessus. Par contre, il aimerait déléguer la tâche du montage en atelier à Eric.

.. i18n: .. note:: Exercice 5 - Travailler sur les tâches et les déléguer
.. i18n: 
.. i18n:     Thomas va voir ses tâches et encode qu'il a été à la réunion client pendant 3h et que cela a suffit, donc la tâche est terminée. Ensuite, il encode qu'il a travaillé 2h sur la rédaction du cahier des charges et délègue la tâche du montage à Eric. Eric, en se connectant, va donc voir qu'une tâche de plus lui a été ajoutée par Thomas.

.. note:: Exercice 5 - Travailler sur les tâches et les déléguer

    Thomas va voir ses tâches et encode qu'il a été à la réunion client pendant 3h et que cela a suffit, donc la tâche est terminée. Ensuite, il encode qu'il a travaillé 2h sur la rédaction du cahier des charges et délègue la tâche du montage à Eric. Eric, en se connectant, va donc voir qu'une tâche de plus lui a été ajoutée par Thomas.

.. i18n: Contrôle financier
.. i18n: ==================

Contrôle financier
==================

.. i18n: .. note:: Exercice 6 - 

.. note:: Exercice 6 - 

.. i18n: .. note:: Exercice 7 - 

.. note:: Exercice 7 - 
