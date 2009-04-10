
.. i18n: .. module:: product_index
.. i18n:     :synopsis: Manage indexes on products prices 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: product_index
    :synopsis: Manage indexes on products prices 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Manage indexes on products prices (*product_index*)
.. i18n: ===================================================
.. i18n: :Module: product_index
.. i18n: :Name: Manage indexes on products prices
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: product_index
.. i18n: :Web: http://www.openerp.com/
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Manage indexes on products prices (*product_index*)
===================================================
:Module: product_index
:Name: Manage indexes on products prices
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_index
:Web: http://www.openerp.com/
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None

::

  None

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`product`

 * :mod:`product`

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

.. i18n:  * Books/Configuration/Indexes
.. i18n:  * Books/Configuration/Indexes/New index

 * Books/Configuration/Indexes
 * Books/Configuration/Indexes/New index

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * product.index.tree (tree)
.. i18n:  * product.index.form (form)
.. i18n:  * \* INHERIT product.normal.form (form)

 * product.index.tree (tree)
 * product.index.form (form)
 * \* INHERIT product.normal.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Index (product.index)
.. i18n: #############################

Object: Index (product.index)
#############################

.. i18n: :rate_ids: Rates, one2many

:rate_ids: Rates, one2many

.. i18n: :code: Index code, char

:code: Index code, char

.. i18n: :name: Index name, char, required

:name: Index name, char, required

.. i18n: :rounding: Rounding factor, float

:rounding: Rounding factor, float

.. i18n: :rate: Current rate, float, readonly

:rate: Current rate, float, readonly

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: Object: Index Rate (product.index.rate)
.. i18n: #######################################

Object: Index Rate (product.index.rate)
#######################################

.. i18n: :rate: Rate, float, required

:rate: Rate, float, required

.. i18n: :index_id: index, many2one, readonly

:index_id: index, many2one, readonly

.. i18n: :name: Date, date, required

:name: Date, date, required
