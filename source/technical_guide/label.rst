
.. module:: label
    :synopsis: Partner labels
    :noindex:
.. 

Partner labels (*label*)
========================
:Module: label
:Name: Partner labels
:Version: 5.0.1.0
:Directory: label
:Web: www.zikzakmedia.com
:Is certified: no

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

Object: report.pagesize (report.pagesize)
#########################################



:width: Width, char, required

    *Numeric width of the page ended with the unit (cm or in). For example, A4 is 21cm and letter is 8.5in*



:name: Name, char, required





:height: Height, char, required

    *Numeric height of the page ended with the unit (cm or in). For example, A4 is 29.7cm and letter is 11in*


Object: report.label.manufacturer (report.label.manufacturer)
#############################################################



:name: Name, char, required




Object: report.label (report.label)
###################################



:rows: Number of Rows, integer, required





:name: Name, char, required





:label_height: Label Height, char, required

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*



:label_width: Label Width, char, required

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*



:cols: Number of Columns, integer, required





:pagesize_id: Page Size, many2one, required





:width_incr: Width Increment, char, required

    *Width between start positions of 2 labels. Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*



:margin_top: Top Margin, char, required

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*



:margin_left: Left Margin, char, required

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*



:height_incr: Height Increment, char, required

    *Height between start positions of 2 labels. Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*



:manufacturer_id: Manufacturer, many2one





:landscape: Landscape, boolean

    *No check -> Portrait. Check -> Landscape*



:description: Description, text


