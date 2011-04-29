Complete case in multi-company environment
==========================================

Here will be a complete example of the sale process of a product in a multi-company environment.

TOFIX: Problème avec les Record Rules.

RR à modifier:

* Picking
* Procurement
* Stock Location
* Product Template
* Stock move

::

	['|',('company_id','=',False),('company_id','child_of',[user.company_id.id])]
	
		-> Ajouter le fait que le company_id puisse être un enfant de la société mère
			('company_id','child_of','[SOCIETE MERE SI ELLE EXISTE]'*)
			
			* Si on est loggé sur la société mère, y en a pas.


``Nouvelle piste de réflexion:``

Tous les champs commençant par property_* sont nativement multi-société donc ont peut sy stocker des valeur différentes par sociétés (il y' était déjà en 4.2 et 5.0 mais plus compliqué à gérer)

il faut par contre bien définir lorsque l'on est dans telle société, ou enregistrer cette propriété

Administrattion -> Paramétrage ->Multi-Société -> Société par défaut par objet

cette écran sert a gérer l'enregistrement des objets (ex produit) et de propriétés

par exemple 1 holding et 2 sociétés se partage les produits gérés dans la holding, mais les comptes comptables sont propres aux 2 sociétés			
