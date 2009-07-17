
.. i18n: .. module:: c2c_fiscal_year_close
.. i18n:     :synopsis: c2c close fiscal year 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: c2c_fiscal_year_close
    :synopsis: c2c close fiscal year 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: c2c close fiscal year (*c2c_fiscal_year_close*)
.. i18n: ===============================================
.. i18n: :Module: c2c_fiscal_year_close
.. i18n: :Name: c2c close fiscal year
.. i18n: :Version: 0.6
.. i18n: :Author: Camptocamp SA
.. i18n: :Directory: c2c_fiscal_year_close
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

c2c close fiscal year (*c2c_fiscal_year_close*)
===============================================
:Module: c2c_fiscal_year_close
:Name: c2c close fiscal year
:Version: 0.6
:Author: Camptocamp SA
:Directory: c2c_fiscal_year_close
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Ce module corrige le wizard de clôture de l'année fiscale de la version
.. i18n:   	4.2 de OpenERP => il permet :
.. i18n:   
.. i18n:   	- clôture possible à n'importe quel moment
.. i18n:   	- report correct des postes ouvert
.. i18n:   	- écriture automatique des report du résultat dans le bilan
.. i18n:   	- clôture des périodes et de l'année fiscales automatique
.. i18n:   	- ajout de nouveaux contrôle des données
.. i18n:   	- contrôle du type de clôture spécifié sur les comptes (par rapport au
.. i18n:   	type de compte)
.. i18n:   
.. i18n:   	Globalement le module fait les étapes suivantes :
.. i18n:   
.. i18n:   	1. tests (journaux utilisés, dates, années précédentes clôturées, etc..)
.. i18n:   	2. transfert du résultat de l'exercice dans le bilan
.. i18n:   	3. transfert du solde des comptes avec le type de clôture à "balance"
.. i18n:   	sur le nouvelle exercice comptable
.. i18n:   	4. transfert des postes ouverts au 31.12 sur l'exercice suivant (en
.. i18n:   	tenant compte des dates des écritures réconciliées)
.. i18n:   	5. réconciliation de l'écriture de "Solde initial" pour ne pas rentrer
.. i18n:   	en conflit avec les écritures initiales des factures
.. i18n:   	5. clôture des périodes et de l'exercice
.. i18n:   
.. i18n:   	Le module ne fait pas :
.. i18n:   	- ne permet pas de dé-clôturer (mais nous sommes à disposition si vous
.. i18n:   	souhaitez que nous le développions :-) )
.. i18n:   	- ne sépare pas le transfert des soldes et la clôture à proprement dit
.. i18n:   	(idem, on peut le faire si besoin)
.. i18n:   
.. i18n:   	Voici les étapes pour permettre une clôture parfaite :
.. i18n:   
.. i18n:   	=> le screencast suivant vous expliquera en détail comment faire :
.. i18n:   	http://www.screencast.com/t/lXLRJoQca
.. i18n:   
.. i18n:   	1. !!!!!!!!!!! FAIRE UNE BACKUP DE LA BASE !!!!!!!!!!!
.. i18n:   	1. vérifier que les "types de clôture" spécifiés sur les "type de
.. i18n:   	comptes" sont correct
.. i18n:   	2. lancer la liste "Finance -> plan comptable -> plan comptable -> trouble accounts" qui donne la liste de tous les comptes
.. i18n:   	dont le type de clôture est différent que celui spécifié sur le type de
.. i18n:   	compte
.. i18n:   	3. lancer le wizard de clôture "Finance -> traitement de fin d'années -> cloturer l'exrecice comptable" en spécifiant les données des champs
.. i18n:   	4. pressez sur OK
.. i18n:   
.. i18n:   	Camptocamp reste à votre entière disposition pour vous soutenir dans le
.. i18n:   	processus de clôture soit sur site ou à distance.
.. i18n:   
.. i18n:   
.. i18n:   
.. i18n:   	--------------------------------------------
.. i18n:   
.. i18n:   
.. i18n:   	This module addresses the wizard "close fiscal year" of the 4.2 version
.. i18n:   	of OpenERP => it allows:
.. i18n:   
.. i18n:   	- Closing at any time
.. i18n:   	- Report correct non reconciles entries (positions open)
.. i18n:   	- Automatic transfert actual year result to the balance sheet
.. i18n:   	- Automatic closing of periods fiscal year
.. i18n:   	- News data checking
.. i18n:   	- Checking of the  "closing type" of the accounts (compared to the
.. i18n:   	"closing type" of the "type of account")
.. i18n:   
.. i18n:   	The module work is :
.. i18n:   
.. i18n:   	1. tests (opening and closing journal, dates, previous fiscal years
.. i18n:   	status, etc. ..)
.. i18n:   	2. transfer the actual year result to the balance sheet
.. i18n:   	3. transfer the account balance of "balance" type to the new fiscal year
.. i18n:   	4. transfer of 31.12 non reconciles entries to the new fiscal year
.. i18n:   	(based on the dates of reconciled entries)
.. i18n:   	5. Reconciliation of the "new entries" entry to remove the conflict with
.. i18n:   	the initial invoice entry
.. i18n:   	5. closing periods and fiscal year
.. i18n:   
.. i18n:   	The module does not:
.. i18n:   	- Be able to re-open closed fiscal year (but we're available if you want
.. i18n:   	that we developp it :-) )
.. i18n:   	- Separate the step of transfering account balance and the step of
.. i18n:   	closing (=> same we can do it if necessary)
.. i18n:   
.. i18n:   	Here are the steps to allow the closing of fiscal year :
.. i18n:   
.. i18n:   	=> The following screencast will explain in detail how to do: http://www.screencast.com/t/lXLRJoQca
.. i18n:   
.. i18n:   	0. !!!!!!!!!!! MAKE A BACKUP OF THE DATABASE !!!!!!!!!!!
.. i18n:   	1. verify that the "types of closing" specified on the "type of
.. i18n:   	accounts" are correct
.. i18n:   	2. launch the "Finance -> Charts -> Charts of Account -> trouble accounts" list which give you the list of all the
.. i18n:   	accounts which the type of closing is different than that specified the
.. i18n:   	type of account
.. i18n:   	3. start the wizard closing "Finance -> End of Year Treatements -> close a fiscal year" specifying the asking fields
.. i18n:   	4. press OK
.. i18n:   
.. i18n:   	Camptocamp is open to support you in the process of closing on site or
.. i18n:   	remotely.
.. i18n:   	

::

  Ce module corrige le wizard de clôture de l'année fiscale de la version
  	4.2 de OpenERP => il permet :
  
  	- clôture possible à n'importe quel moment
  	- report correct des postes ouvert
  	- écriture automatique des report du résultat dans le bilan
  	- clôture des périodes et de l'année fiscales automatique
  	- ajout de nouveaux contrôle des données
  	- contrôle du type de clôture spécifié sur les comptes (par rapport au
  	type de compte)
  
  	Globalement le module fait les étapes suivantes :
  
  	1. tests (journaux utilisés, dates, années précédentes clôturées, etc..)
  	2. transfert du résultat de l'exercice dans le bilan
  	3. transfert du solde des comptes avec le type de clôture à "balance"
  	sur le nouvelle exercice comptable
  	4. transfert des postes ouverts au 31.12 sur l'exercice suivant (en
  	tenant compte des dates des écritures réconciliées)
  	5. réconciliation de l'écriture de "Solde initial" pour ne pas rentrer
  	en conflit avec les écritures initiales des factures
  	5. clôture des périodes et de l'exercice
  
  	Le module ne fait pas :
  	- ne permet pas de dé-clôturer (mais nous sommes à disposition si vous
  	souhaitez que nous le développions :-) )
  	- ne sépare pas le transfert des soldes et la clôture à proprement dit
  	(idem, on peut le faire si besoin)
  
  	Voici les étapes pour permettre une clôture parfaite :
  
  	=> le screencast suivant vous expliquera en détail comment faire :
  	http://www.screencast.com/t/lXLRJoQca
  
  	1. !!!!!!!!!!! FAIRE UNE BACKUP DE LA BASE !!!!!!!!!!!
  	1. vérifier que les "types de clôture" spécifiés sur les "type de
  	comptes" sont correct
  	2. lancer la liste "Finance -> plan comptable -> plan comptable -> trouble accounts" qui donne la liste de tous les comptes
  	dont le type de clôture est différent que celui spécifié sur le type de
  	compte
  	3. lancer le wizard de clôture "Finance -> traitement de fin d'années -> cloturer l'exrecice comptable" en spécifiant les données des champs
  	4. pressez sur OK
  
  	Camptocamp reste à votre entière disposition pour vous soutenir dans le
  	processus de clôture soit sur site ou à distance.
  
  
  
  	--------------------------------------------
  
  
  	This module addresses the wizard "close fiscal year" of the 4.2 version
  	of OpenERP => it allows:
  
  	- Closing at any time
  	- Report correct non reconciles entries (positions open)
  	- Automatic transfert actual year result to the balance sheet
  	- Automatic closing of periods fiscal year
  	- News data checking
  	- Checking of the  "closing type" of the accounts (compared to the
  	"closing type" of the "type of account")
  
  	The module work is :
  
  	1. tests (opening and closing journal, dates, previous fiscal years
  	status, etc. ..)
  	2. transfer the actual year result to the balance sheet
  	3. transfer the account balance of "balance" type to the new fiscal year
  	4. transfer of 31.12 non reconciles entries to the new fiscal year
  	(based on the dates of reconciled entries)
  	5. Reconciliation of the "new entries" entry to remove the conflict with
  	the initial invoice entry
  	5. closing periods and fiscal year
  
  	The module does not:
  	- Be able to re-open closed fiscal year (but we're available if you want
  	that we developp it :-) )
  	- Separate the step of transfering account balance and the step of
  	closing (=> same we can do it if necessary)
  
  	Here are the steps to allow the closing of fiscal year :
  
  	=> The following screencast will explain in detail how to do: http://www.screencast.com/t/lXLRJoQca
  
  	0. !!!!!!!!!!! MAKE A BACKUP OF THE DATABASE !!!!!!!!!!!
  	1. verify that the "types of closing" specified on the "type of
  	accounts" are correct
  	2. launch the "Finance -> Charts -> Charts of Account -> trouble accounts" list which give you the list of all the
  	accounts which the type of closing is different than that specified the
  	type of account
  	3. start the wizard closing "Finance -> End of Year Treatements -> close a fiscal year" specifying the asking fields
  	4. press OK
  
  	Camptocamp is open to support you in the process of closing on site or
  	remotely.
  	

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`

 * :mod:`base`
 * :mod:`account`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n: None

None

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: None

None
