
Module Library (*library*)
==========================
:Module: library
:Name: Library
:Version: 5.0.1.0
:Directory: library
:Web: 

Description
-----------

::

  Module to manage library.
      Books Information,
      Publisher and Author Information,
      Book Rack Tracking etc...

Dependencies
------------

 * point_of_sale - installed
 * report_intrastat - installed
 * purchase - installed

Reports
-------

None


Menus
-------

 * Products/Authors
 * Products/Books
 * Products/Books/Books to return before 30 days
 * Sales Management/Orders of the day
 * Sales Management/Orders of the day/My orders of the day
 * Partners/Editor - Suppliers Relations
 * Products/Authors/New Author
 * Books/Configuration/Price Categories

Views
-----

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


Objects
-------

Object: Book Price Category
###########################

.. index::
  single: Book Price Category object
.. 


:price: Price, float, required



.. index::
  single: price field
.. 




:name: Category, char, required



.. index::
  single: name field
.. 




:product_ids: Books, one2many, readonly



.. index::
  single: product_ids field
.. 



Object: Library Rack
####################

.. index::
  single: Library Rack object
.. 


:active: Active, boolean



.. index::
  single: active field
.. 




:code: Code, char



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: Library Collection
##########################

.. index::
  single: Library Collection object
.. 


:code: Code, char



.. index::
  single: code field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: Author
##############

.. index::
  single: Author object
.. 


:first_name: First Name, char



.. index::
  single: first_name field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:editor_ids: Editors, many2many



.. index::
  single: editor_ids field
.. 




:book_ids: Books, many2many



.. index::
  single: book_ids field
.. 




:death_date: Date of death, date



.. index::
  single: death_date field
.. 




:note: Notes, text



.. index::
  single: note field
.. 




:born_date: Date of birth, date



.. index::
  single: born_date field
.. 




:biography: Biography, text



.. index::
  single: biography field
.. 



Object: author.book.rel
#######################

.. index::
  single: author.book.rel object
.. 


:author_id: Author, many2one



.. index::
  single: author_id field
.. 




:product_id: Book, many2one



.. index::
  single: product_id field
.. 



Object: many2many view for editor relations
###########################################

.. index::
  single: many2many view for editor relations object
.. 


:junk:  , text, readonly



.. index::
  single: junk field
.. 




:supplier_id: Supplier, many2one



.. index::
  single: supplier_id field
.. 




:name: Editor, many2one



.. index::
  single: name field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 

