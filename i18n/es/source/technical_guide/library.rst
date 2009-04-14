
.. i18n: .. module:: library
.. i18n:     :synopsis: Library 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: library
    :synopsis: Library 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Library (*library*)
.. i18n: ===================
.. i18n: :Module: library
.. i18n: :Name: Library
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: library
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no

Library (*library*)
===================
:Module: library
:Name: Library
:Version: 5.0.1.0
:Author: Tiny
:Directory: library
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module to manage library.
.. i18n:       Books Information,
.. i18n:       Publisher and Author Information,
.. i18n:       Book Rack Tracking etc...

::

  Module to manage library.
      Books Information,
      Publisher and Author Information,
      Book Rack Tracking etc...

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`point_of_sale`
.. i18n:  * :mod:`report_intrastat`
.. i18n:  * :mod:`purchase`

 * :mod:`point_of_sale`
 * :mod:`report_intrastat`
 * :mod:`purchase`

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

.. i18n:  * Books/Authors
.. i18n:  * Books/Books
.. i18n:  * Books/Books/Books to return before 30 days
.. i18n:  * Sales Management/Orders of the day
.. i18n:  * Sales Management/Orders of the day/My orders of the day
.. i18n:  * Partners/Editor - Suppliers Relations
.. i18n:  * Books/Authors/New Author
.. i18n:  * Books/Configuration/Price Categories

 * Books/Authors
 * Books/Books
 * Books/Books/Books to return before 30 days
 * Sales Management/Orders of the day
 * Sales Management/Orders of the day/My orders of the day
 * Partners/Editor - Suppliers Relations
 * Books/Authors/New Author
 * Books/Configuration/Price Categories

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * product.product.tree (tree)
.. i18n:  * library.author.form (form)
.. i18n:  * library.author.tree (tree)
.. i18n:  * Library Rack (form)
.. i18n:  * product.book.tree.view (tree)
.. i18n:  * product.book.form.view (form)
.. i18n:  * sale.order.tree (tree)
.. i18n:  * account.invoice.tree (tree)
.. i18n:  * stock.picking.tree (tree)
.. i18n:  * library.price.category (tree)
.. i18n:  * library.price.category (form)
.. i18n:  * library.editor.supplier (form)
.. i18n:  * Editor - supplier realtions (tree)
.. i18n:  * \* INHERIT mrp.procurement.form (form)
.. i18n:  * \* INHERIT Stock packing (form)
.. i18n:  * \* INHERIT Stock packing (form)
.. i18n:  * \* INHERIT purchase.order.line.form (form)
.. i18n:  * \* INHERIT sale.order.form (form)
.. i18n:  * \* INHERIT Sale line (form)
.. i18n:  * \* INHERIT Sale Lines (tree)
.. i18n:  * \* INHERIT product.supplierinfo.form.view (form)
.. i18n:  * \* INHERIT purchase.order.line.tree (tree)
.. i18n:  * \* INHERIT account.invoice.line.form (form)

 * product.product.tree (tree)
 * library.author.form (form)
 * library.author.tree (tree)
 * Library Rack (form)
 * product.book.tree.view (tree)
 * product.book.form.view (form)
 * sale.order.tree (tree)
 * account.invoice.tree (tree)
 * stock.picking.tree (tree)
 * library.price.category (tree)
 * library.price.category (form)
 * library.editor.supplier (form)
 * Editor - supplier realtions (tree)
 * \* INHERIT mrp.procurement.form (form)
 * \* INHERIT Stock packing (form)
 * \* INHERIT Stock packing (form)
 * \* INHERIT purchase.order.line.form (form)
 * \* INHERIT sale.order.form (form)
 * \* INHERIT Sale line (form)
 * \* INHERIT Sale Lines (tree)
 * \* INHERIT product.supplierinfo.form.view (form)
 * \* INHERIT purchase.order.line.tree (tree)
 * \* INHERIT account.invoice.line.form (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Book Price Category (library.price.category)
.. i18n: ####################################################

Object: Book Price Category (library.price.category)
####################################################

.. i18n: :price: Price, float, required

:price: Price, float, required

.. i18n: :name: Category, char, required

:name: Category, char, required

.. i18n: :product_ids: Books, one2many, readonly

:product_ids: Books, one2many, readonly

.. i18n: Object: Library Rack (library.rack)
.. i18n: ###################################

Object: Library Rack (library.rack)
###################################

.. i18n: :active: Active, boolean

:active: Active, boolean

.. i18n: :code: Code, char

:code: Code, char

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: Object: Library Collection (library.collection)
.. i18n: ###############################################

Object: Library Collection (library.collection)
###############################################

.. i18n: :code: Code, char

:code: Code, char

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: Object: Author (library.author)
.. i18n: ###############################

Object: Author (library.author)
###############################

.. i18n: :first_name: First Name, char

:first_name: First Name, char

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :editor_ids: Editors, many2many

:editor_ids: Editors, many2many

.. i18n: :book_ids: Books, many2many

:book_ids: Books, many2many

.. i18n: :death_date: Date of death, date

:death_date: Date of death, date

.. i18n: :note: Notes, text

:note: Notes, text

.. i18n: :born_date: Date of birth, date

:born_date: Date of birth, date

.. i18n: :biography: Biography, text

:biography: Biography, text

.. i18n: Object: author.book.rel (author.book.rel)
.. i18n: #########################################

Object: author.book.rel (author.book.rel)
#########################################

.. i18n: :author_id: Author, many2one

:author_id: Author, many2one

.. i18n: :product_id: Book, many2one

:product_id: Book, many2one

.. i18n: Object: many2many view for editor relations (library.editor.supplier)
.. i18n: #####################################################################

Object: many2many view for editor relations (library.editor.supplier)
#####################################################################

.. i18n: :junk:  , text, readonly

:junk:  , text, readonly

.. i18n: :supplier_id: Supplier, many2one

:supplier_id: Supplier, many2one

.. i18n: :name: Editor, many2one

:name: Editor, many2one

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer
