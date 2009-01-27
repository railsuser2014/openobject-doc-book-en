
Module Partner labels (*label*)
===============================
:Module: label
:Name: Partner labels
:Version: 5.0.1.0
:Directory: label
:Web: www.zikzakmedia.com

Description
-----------

::

  Flexible partner labels:
    * Definition of page sizes, label manufacturers and label formats
    * Flexible label formats (page size, portrait or landscape, manufacturer, rows, columns, width, height, top margin, left margin, ...)
    * Initial data for page sizes and label formats (from Avery and Apli manufacturers)
    * Wizard to print labels. The label format, the printer margins, the font type and size, the first label (row and column) to print on the first page can be set.

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Partners/Configuration/Page Sizes
 * Partners/Configuration/Label Manufacturers
 * Partners/Configuration/Label Formats

Views
-----

 * report.pagesize.tree (tree)
 * report.pagesize (form)
 * report.label.tree (tree)
 * report.label (form)


Objects
-------

Object: report.pagesize
#######################

.. index::
  single: report.pagesize object
.. 


:width: Width, char, required

    *Numeric width of the page ended with the unit (cm or in). For example, A4 is 21cm and letter is 8.5in*

.. index::
  single: width field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:height: Height, char, required

    *Numeric height of the page ended with the unit (cm or in). For example, A4 is 29.7cm and letter is 11in*

.. index::
  single: height field
.. 



Object: report.label.manufacturer
#################################

.. index::
  single: report.label.manufacturer object
.. 


:name: Name, char, required



.. index::
  single: name field
.. 



Object: report.label
####################

.. index::
  single: report.label object
.. 


:rows: Number of Rows, integer, required



.. index::
  single: rows field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:label_height: Label Height, char, required

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. index::
  single: label_height field
.. 




:label_width: Label Width, char, required

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. index::
  single: label_width field
.. 




:cols: Number of Columns, integer, required



.. index::
  single: cols field
.. 




:pagesize_id: Page Size, many2one, required



.. index::
  single: pagesize_id field
.. 




:width_incr: Width Increment, char, required

    *Width between start positions of 2 labels. Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. index::
  single: width_incr field
.. 




:margin_top: Top Margin, char, required

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. index::
  single: margin_top field
.. 




:margin_left: Left Margin, char, required

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. index::
  single: margin_left field
.. 




:height_incr: Height Increment, char, required

    *Height between start positions of 2 labels. Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. index::
  single: height_incr field
.. 




:manufacturer_id: Manufacturer, many2one



.. index::
  single: manufacturer_id field
.. 




:landscape: Landscape, boolean

    *No check -> Portrait. Check -> Landscape*

.. index::
  single: landscape field
.. 




:description: Description, text



.. index::
  single: description field
.. 

