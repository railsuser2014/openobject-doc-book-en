
Library (*library*)
===================
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



:price: Price, float, required





:name: Category, char, required





:product_ids: Books, one2many, readonly




Object: Library Rack
####################



:active: Active, boolean





:code: Code, char





:name: Name, char, required




Object: Library Collection
##########################



:code: Code, char





:name: Name, char, required




Object: Author
##############



:first_name: First Name, char





:name: Name, char, required





:editor_ids: Editors, many2many





:book_ids: Books, many2many





:death_date: Date of death, date





:note: Notes, text





:born_date: Date of birth, date





:biography: Biography, text




Object: author.book.rel
#######################



:author_id: Author, many2one





:product_id: Book, many2one




Object: many2many view for editor relations
###########################################



:junk:  , text, readonly





:supplier_id: Supplier, many2one





:name: Editor, many2one





:sequence: Sequence, integer


