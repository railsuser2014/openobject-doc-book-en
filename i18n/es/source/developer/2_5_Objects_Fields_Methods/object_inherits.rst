
.. i18n: Inheritance by Delegation - _inherits
.. i18n: =====================================

Inheritance by Delegation - _inherits
=====================================

.. i18n:  **Syntax :**::
.. i18n: 
.. i18n: 	 class tiny_object(osv.osv)
.. i18n: 	     _name = 'tiny.object'
.. i18n: 	     _table = 'tiny_object'
.. i18n: 	     _inherits = { 'tiny.object'_1_ : name_col'_1_', 'tiny.object'_2_ : name_col'_2_', ..., 'tiny.object'_n_ : name_col'_n_' }
.. i18n: 	     (...)

 **Syntax :**::

	 class tiny_object(osv.osv)
	     _name = 'tiny.object'
	     _table = 'tiny_object'
	     _inherits = { 'tiny.object'_1_ : name_col'_1_', 'tiny.object'_2_ : name_col'_2_', ..., 'tiny.object'_n_ : name_col'_n_' }
	     (...)

.. i18n: The object 'tiny.object' inherits from all the columns and all the methods from the n objects 'tiny.object'_1_, ..., 'tiny.object'_n_.

The object 'tiny.object' inherits from all the columns and all the methods from the n objects 'tiny.object'_1_, ..., 'tiny.object'_n_.

.. i18n: To inherit from multiple tables, the technique consists in adding one column to the table tiny_object per inherited object. This column will store a foreign key (an id from another table). The values *name_col'_1_' name_col'_2_' ... name_col'_n_'* are of type string and determine the title of the columns in which the foreign keys from 'tiny.object'_1_, ..., 'tiny.object'_n_ are stored.

To inherit from multiple tables, the technique consists in adding one column to the table tiny_object per inherited object. This column will store a foreign key (an id from another table). The values *name_col'_1_' name_col'_2_' ... name_col'_n_'* are of type string and determine the title of the columns in which the foreign keys from 'tiny.object'_1_, ..., 'tiny.object'_n_ are stored.

.. i18n: This inheritance mechanism is usually called " *instance inheritance* "  or  " *value inheritance* ". A resource (instance) has the VALUES of its parents. 

This inheritance mechanism is usually called " *instance inheritance* "  or  " *value inheritance* ". A resource (instance) has the VALUES of its parents. 
