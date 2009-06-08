
.. i18n: .. index::
.. i18n:    pair: data; import
.. i18n:    pair: data; export

.. index::
   pair: data; import
   pair: data; export

.. i18n: Importing and exporting data
.. i18n: ============================

Importing and exporting data
============================

.. i18n: Every form in Open ERP has a standard mechanism for importing data from a CSV file through the client user interface. 
.. i18n: That's the same format as used in the language translations.

Every form in Open ERP has a standard mechanism for importing data from a CSV file through the client user interface. 
That's the same format as used in the language translations.

.. i18n: .. note:: Forms and Lists
.. i18n: 
.. i18n:    You have access to the Import and Export functions in the web client on a single form view in read-
.. i18n:    only mode – you can't reach Import or Export in any other view or when the form is editable.
.. i18n:    If you're using the GTK client you can find the functions from the top menu 
.. i18n:    :menuselection:`Form --> Import...` and :menuselection:`Form --> Export...`.

.. note:: Forms and Lists

   You have access to the Import and Export functions in the web client on a single form view in read-
   only mode – you can't reach Import or Export in any other view or when the form is editable.
   If you're using the GTK client you can find the functions from the top menu 
   :menuselection:`Form --> Import...` and :menuselection:`Form --> Export...`.

.. i18n: The CSV file format is a text format compatible with most spreadsheet programs (such as OpenOffice
.. i18n: Calc and Microsoft Excel) and is easily editable as a worksheet. The first line contains the name of
.. i18n: the field in the form. All the subsequent lines are data, aligned in their respective columns.

The CSV file format is a text format compatible with most spreadsheet programs (such as OpenOffice
Calc and Microsoft Excel) and is easily editable as a worksheet. The first line contains the name of
the field in the form. All the subsequent lines are data, aligned in their respective columns.

.. i18n: .. index::
.. i18n:    pair: data; CSV export

.. index::
   pair: data; CSV export

.. i18n: Exporting Open ERP data to CSV
.. i18n: ------------------------------

Exporting Open ERP data to CSV
------------------------------

.. i18n: Start exploring Open ERP's use of the CSV format by exporting a modestly complex set of data,
.. i18n: the partners and partner addresses in the demonstration data.

Start exploring Open ERP's use of the CSV format by exporting a modestly complex set of data,
the partners and partner addresses in the demonstration data.

.. i18n: Go to :menuselection:`Partners --> Partners` for the list of partners and then scroll to the bottom
.. i18n: of the list to click the :guilabel:`Export` link. This pops up the :guilabel:`Export Data` dialog box.
.. i18n: Select the following fields:

Go to :menuselection:`Partners --> Partners` for the list of partners and then scroll to the bottom
of the list to click the :guilabel:`Export` link. This pops up the :guilabel:`Export Data` dialog box.
Select the following fields:

.. i18n: * :guilabel:`Name`,
.. i18n: 
.. i18n: * :guilabel:`Contact Name` under the :guilabel:`Contacts` menu,
.. i18n: 
.. i18n: * :guilabel:`City` under the :guilabel:`Contacts` menu.

* :guilabel:`Name`,

* :guilabel:`Contact Name` under the :guilabel:`Contacts` menu,

* :guilabel:`City` under the :guilabel:`Contacts` menu.

.. i18n: You can either select and add them one at a time, or :kbd:`Ctrl-click` them and add
.. i18n: the multiple selection - the order in which you 
.. i18n: select them is the order in which they'll be displayed.

You can either select and add them one at a time, or :kbd:`Ctrl-click` them and add
the multiple selection - the order in which you 
select them is the order in which they'll be displayed.

.. i18n: Then click :guilabel:`Export` and save the resulting :file:`data.csv` file somewhere accessible - 
.. i18n: perhaps your Desktop. You can open that file in a spreadsheet program or a text editor.

Then click :guilabel:`Export` and save the resulting :file:`data.csv` file somewhere accessible - 
perhaps your Desktop. You can open that file in a spreadsheet program or a text editor.

.. i18n: You'll see that you have a list of partners, with the name and city of each partner's contacts
.. i18n: alongside. In the couple of cases where there is more than one address, the partner name
.. i18n: is left out. So it is important to note that the order of entries is critical - do not sort
.. i18n: that list!

You'll see that you have a list of partners, with the name and city of each partner's contacts
alongside. In the couple of cases where there is more than one address, the partner name
is left out. So it is important to note that the order of entries is critical - do not sort
that list!

.. i18n: .. tip:: List limits
.. i18n: 
.. i18n:    There is a limit to the number of items you can export in the clients - it's the number
.. i18n:    you can actually see and that is limited to a maximum of 100 in the web client, but is
.. i18n:    arbitrary in the GTK client.
.. i18n:    
.. i18n:    So if you want to export everything, use the GTK client. Set the export limit to an 
.. i18n:    arbitrarily large figure (using the :guilabel:`+` button to expose the 
.. i18n:    :guilabel:`Parameters` and :guilabel:`Limit` fields), then click 
.. i18n:    :menuselection:`Form --> Export data...`, set up the fields to export, and
.. i18n:    then prepare to wait.

.. tip:: List limits

   There is a limit to the number of items you can export in the clients - it's the number
   you can actually see and that is limited to a maximum of 100 in the web client, but is
   arbitrary in the GTK client.
   
   So if you want to export everything, use the GTK client. Set the export limit to an 
   arbitrarily large figure (using the :guilabel:`+` button to expose the 
   :guilabel:`Parameters` and :guilabel:`Limit` fields), then click 
   :menuselection:`Form --> Export data...`, set up the fields to export, and
   then prepare to wait.

.. i18n: .. index::
.. i18n:    pair: data; CSV import

.. index::
   pair: data; CSV import

.. i18n: Importing CSV data to Open ERP
.. i18n: ------------------------------

Importing CSV data to Open ERP
------------------------------

.. i18n: Use this export file as a template for an import file by deleting all of the data
.. i18n: and using new data (here you'll just import new data alongside the demonstration data,
.. i18n: but the principle is the same for a blank database).

Use this export file as a template for an import file by deleting all of the data
and using new data (here you'll just import new data alongside the demonstration data,
but the principle is the same for a blank database).

.. i18n: For example, to import partners with several contacts for which you specify a name and a city, you
.. i18n: would create the following CSV file from the export file:

For example, to import partners with several contacts for which you specify a name and a city, you
would create the following CSV file from the export file:

.. i18n: .. csv-table:: Example of importing partner address fields
.. i18n:    :header: "Name", "Contacts/Contact Name", "Contacts/City"
.. i18n:    :widths: 12,10,8
.. i18n: 
.. i18n:    "Whole Globe Technologies","Graham Global","Athens"
.. i18n:    "","Wanda World","Rome"
.. i18n:    "","Emerson Earth","New York"
.. i18n:    "Miles A Minute","",""

.. csv-table:: Example of importing partner address fields
   :header: "Name", "Contacts/Contact Name", "Contacts/City"
   :widths: 12,10,8

   "Whole Globe Technologies","Graham Global","Athens"
   "","Wanda World","Rome"
   "","Emerson Earth","New York"
   "Miles A Minute","",""

.. i18n: From the list of partners, click the :guilabel:`Import` button and then in the 
.. i18n: :guilabel:`Import Data` window click :guilabel:`Open` to search for and import
.. i18n: the new :file:`data.csv` file. The web client automatically matches column names
.. i18n: but the GTK client requires that you click the :guilabel:`Auto detect` button.

From the list of partners, click the :guilabel:`Import` button and then in the 
:guilabel:`Import Data` window click :guilabel:`Open` to search for and import
the new :file:`data.csv` file. The web client automatically matches column names
but the GTK client requires that you click the :guilabel:`Auto detect` button.

.. i18n: You'll get a dialog box showing that you have imported 2 objects, and you can
.. i18n: see the new partners and partner addresses when you refresh the list on screen.

You'll get a dialog box showing that you have imported 2 objects, and you can
see the new partners and partner addresses when you refresh the list on screen.

.. i18n: .. index::
.. i18n:    pair: data; CSV structured

.. index::
   pair: data; CSV structured

.. i18n: The CSV format for complex database structures
.. i18n: ----------------------------------------------

The CSV format for complex database structures
----------------------------------------------

.. i18n: When you import data you have to overcome the problem of representing a database structure in \
.. i18n: ``.csv``\  flat files. To do this, two solutions are possible in Open ERP:

When you import data you have to overcome the problem of representing a database structure in \
``.csv``\  flat files. To do this, two solutions are possible in Open ERP:

.. i18n: * importing a CSV file that's been structured in a particular way to enable you to load several
.. i18n:   different database tables from a single file (such as partners and partner contacts in one CSV
.. i18n:   file, as you have just done above),
.. i18n: 
.. i18n: * importing several CSV files, each corresponding to a specific database table, that have explicit
.. i18n:   links between the tables.

* importing a CSV file that's been structured in a particular way to enable you to load several
  different database tables from a single file (such as partners and partner contacts in one CSV
  file, as you have just done above),

* importing several CSV files, each corresponding to a specific database table, that have explicit
  links between the tables.

.. i18n: .. note:: Server-side importing
.. i18n: 
.. i18n:    You can also import CSV data in through the server interface. The file format is the same, but
.. i18n:    column headings differ slightly. When importing through the user interface it checks that the column
.. i18n:    heading names match the names seen in the forms on the user interface itself. 
.. i18n:    In contrast, when importing through the 
.. i18n:    server the column heading names must match the internal names of the fields.

.. note:: Server-side importing

   You can also import CSV data in through the server interface. The file format is the same, but
   column headings differ slightly. When importing through the user interface it checks that the column
   heading names match the names seen in the forms on the user interface itself. 
   In contrast, when importing through the 
   server the column heading names must match the internal names of the fields.

.. i18n: Start by building the header of the CSV file. Open the import tool on the object that you're
.. i18n: interested in and select the fields that you want to import into your Open ERP database. You must
.. i18n: include every field that's colored in blue because those fields are required (unless you know that they
.. i18n: get filled by default with an appropriate value), and also any other field that's important to you.

Start by building the header of the CSV file. Open the import tool on the object that you're
interested in and select the fields that you want to import into your Open ERP database. You must
include every field that's colored in blue because those fields are required (unless you know that they
get filled by default with an appropriate value), and also any other field that's important to you.

.. i18n: .. figure::  images/csv_column_select.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Selecting fields to import using a CSV file*

.. figure::  images/csv_column_select.png
   :scale: 75
   :align: center

   *Selecting fields to import using a CSV file*

.. i18n: Use the field names as the column names in the first line of your CSV file, adding one field per
.. i18n: column. If your CSV file has these names in the first line then when you import your CSV file,
.. i18n: Open ERP will automatically match the column name to the field name of the table. When you've
.. i18n: created your CSV file you'll do that by clicking the :guilabel:`Nothing` button to clear the
.. i18n: :guilabel:`Fields to Import`, then select your CSV file by browsing for a :guilabel:`File to
.. i18n: import`, and then clicking the :guilabel:`Auto Detect` button.

Use the field names as the column names in the first line of your CSV file, adding one field per
column. If your CSV file has these names in the first line then when you import your CSV file,
Open ERP will automatically match the column name to the field name of the table. When you've
created your CSV file you'll do that by clicking the :guilabel:`Nothing` button to clear the
:guilabel:`Fields to Import`, then select your CSV file by browsing for a :guilabel:`File to
import`, and then clicking the :guilabel:`Auto Detect` button.

.. i18n: To import CSV data that matches your database structure, you should distinguish between the following types
.. i18n: of field in the Open ERP interface:  *many-to-many*  fields (between multiple sources and
.. i18n: destinations),  *many-to-one*  fields (from multiple sources to a single destination), and  *one-to-
.. i18n: many*  fields (from a single origin to multiple destinations).

To import CSV data that matches your database structure, you should distinguish between the following types
of field in the Open ERP interface:  *many-to-many*  fields (between multiple sources and
destinations),  *many-to-one*  fields (from multiple sources to a single destination), and  *one-to-
many*  fields (from a single origin to multiple destinations).

.. i18n: .. note:: Foreground table
.. i18n: 
.. i18n:    Each of these types is described in relation to a foreground table –
.. i18n:    the table whose entry form you're viewing and whose entries would be updated by a simple CSV file.
.. i18n: 
.. i18n:    Just because one of these relation fields appears on the foreground table, does not mean that there
.. i18n:    is an inverse field on the related table – but there may be.
.. i18n: 
.. i18n:    So there is *no* one-to-many field in the User form to reflect the many-to-one :guilabel:`user_id` Salesman field in
.. i18n:    the Partner form,
.. i18n:    but there *is* a many-to-one :guilabel:`partner_id` Partner field in the Partner contact form to reflect the one-to-many
.. i18n:    :guilabel:`child_ids` Partner contacts field in the Partner form.

.. note:: Foreground table

   Each of these types is described in relation to a foreground table –
   the table whose entry form you're viewing and whose entries would be updated by a simple CSV file.

   Just because one of these relation fields appears on the foreground table, does not mean that there
   is an inverse field on the related table – but there may be.

   So there is *no* one-to-many field in the User form to reflect the many-to-one :guilabel:`user_id` Salesman field in
   the Partner form,
   but there *is* a many-to-one :guilabel:`partner_id` Partner field in the Partner contact form to reflect the one-to-many
   :guilabel:`child_ids` Partner contacts field in the Partner form.

.. i18n: Have a look at the screenshots below to see the differences.

Have a look at the screenshots below to see the differences.

.. i18n: .. figure::  images/csv_many2one.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *A many-to-one field: a salesperson linked to a partner*

.. figure::  images/csv_many2one.png
   :scale: 75
   :align: center

   *A many-to-one field: a salesperson linked to a partner*

.. i18n: .. figure::  images/csv_many2many.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *A many-to-many field: partner categories*

.. figure::  images/csv_many2many.png
   :scale: 75
   :align: center

   *A many-to-many field: partner categories*

.. i18n: .. figure::  images/csv_one2many.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *A one-to-many field: partner contacts*

.. figure::  images/csv_one2many.png
   :scale: 75
   :align: center

   *A one-to-many field: partner contacts*

.. i18n: All of the other fields are coded in the CSV file as just one text string in each column.

All of the other fields are coded in the CSV file as just one text string in each column.

.. i18n: .. index:: 
.. i18n:    pair: relation; field

.. index:: 
   pair: relation; field

.. i18n: Many-to-one fields
.. i18n: ^^^^^^^^^^^^^^^^^^

Many-to-one fields
^^^^^^^^^^^^^^^^^^

.. i18n: Many-to-one fields represent a relationship between the foreground table and another table in the
.. i18n: database where the foreground table has a single entry for the other table. Open ERP tries to link 
.. i18n: the new record in the foreground table with the field in the other table by matching the field values.

Many-to-one fields represent a relationship between the foreground table and another table in the
database where the foreground table has a single entry for the other table. Open ERP tries to link 
the new record in the foreground table with the field in the other table by matching the field values.

.. i18n: .. tip:: Field identifiers 
.. i18n: 
.. i18n:    If you're working on the server side you can use identifiers rather than the names of resources
.. i18n:    to link tables. To do this you import the
.. i18n:    first file (for example, Products) with a column named :guilabel:`id` in your CSV file that contains a
.. i18n:    unique identifier for each product. This could be an incrementing number.
.. i18n: 
.. i18n:    When you import other files which link to the first table, you can use the identifier in preference
.. i18n:    to the names (so, for example, when you're saving inventory you can use \ ``product:id``\ 
.. i18n:    instead of the product name). 
.. i18n:    You then don't need any complex conversion to create links between the two tables.
.. i18n:    
.. i18n:    This considerably simplifies the importation of another database into Open ERP.
.. i18n:    You just create a linking ``id`` column for each table that you're importing
.. i18n:    that contains the identifier used in the first table.

.. tip:: Field identifiers 

   If you're working on the server side you can use identifiers rather than the names of resources
   to link tables. To do this you import the
   first file (for example, Products) with a column named :guilabel:`id` in your CSV file that contains a
   unique identifier for each product. This could be an incrementing number.

   When you import other files which link to the first table, you can use the identifier in preference
   to the names (so, for example, when you're saving inventory you can use \ ``product:id``\ 
   instead of the product name). 
   You then don't need any complex conversion to create links between the two tables.
   
   This considerably simplifies the importation of another database into Open ERP.
   You just create a linking ``id`` column for each table that you're importing
   that contains the identifier used in the first table.

.. i18n: Many-to-many fields
.. i18n: ^^^^^^^^^^^^^^^^^^^

Many-to-many fields
^^^^^^^^^^^^^^^^^^^

.. i18n: Many-to-many fields are handled just like many-to-one fields in trying to recreate the relationship
.. i18n: between tables: either by searching for names or by using identifiers.

Many-to-many fields are handled just like many-to-one fields in trying to recreate the relationship
between tables: either by searching for names or by using identifiers.

.. i18n: There are several possible values in a single many-to-many field. Therefore a partner can be given
.. i18n: several associated categories. You must separate the different values with a comma.

There are several possible values in a single many-to-many field. Therefore a partner can be given
several associated categories. You must separate the different values with a comma.

.. i18n: One-to-many fields
.. i18n: ^^^^^^^^^^^^^^^^^^

One-to-many fields
^^^^^^^^^^^^^^^^^^

.. i18n: One-to-many fields are a bit different. Take as an example the :guilabel:`Partner Contacts` field in
.. i18n: the Partner form, which contains all of the linked contacts.

One-to-many fields are a bit different. Take as an example the :guilabel:`Partner Contacts` field in
the Partner form, which contains all of the linked contacts.

.. i18n: To import such a field you don't have to link to an existing entry in another table, but can instead
.. i18n: create and link to several partner contacts using the same file. You can then specify several values
.. i18n: for different fields linked to that object by the one-to-many field. Each field must be put in a
.. i18n: column of the table, and the title of that column must be expressed in the form \ ``field_one-to-
.. i18n: many/field_linked-object``\  . The partner data you imported earlier took that form.

To import such a field you don't have to link to an existing entry in another table, but can instead
create and link to several partner contacts using the same file. You can then specify several values
for different fields linked to that object by the one-to-many field. Each field must be put in a
column of the table, and the title of that column must be expressed in the form \ ``field_one-to-
many/field_linked-object``\  . The partner data you imported earlier took that form.

.. i18n: .. note::  Symmetry in relation fields
.. i18n: 
.. i18n: 	Depending on the structure of your data it can be easier to use the one-to-many form or the many-
.. i18n: 	to-one form in relating two tables, so long as the relevant fields exist on both ends of the relationship.
.. i18n: 
.. i18n: 	For example, you can:
.. i18n: 
.. i18n: 	* import one partner with different contact in a single file (one-to-many),
.. i18n: 
.. i18n: 	* import the partners first, and then contacts with the field linking to the partner in a many-to-
.. i18n: 	  one form).

.. note::  Symmetry in relation fields

	Depending on the structure of your data it can be easier to use the one-to-many form or the many-
	to-one form in relating two tables, so long as the relevant fields exist on both ends of the relationship.

	For example, you can:

	* import one partner with different contact in a single file (one-to-many),

	* import the partners first, and then contacts with the field linking to the partner in a many-to-
	  one form).

.. i18n: .. index::
.. i18n:    single: data; import example

.. index::
   single: data; import example

.. i18n: Another example of a CSV import file
.. i18n: ------------------------------------

Another example of a CSV import file
------------------------------------

.. i18n: To illustrate data importing, you can see another example below. First import partner
.. i18n: categories, and then import some partners and their contacts along with links to the categories
.. i18n: just created. Although you can create new contacts at the same time as creating partners (because
.. i18n: you can do this for *one-to-many* relations), you can't create new categories this way (because they
.. i18n: use *many-to-many* relations). You must create new categories in a separate step.

To illustrate data importing, you can see another example below. First import partner
categories, and then import some partners and their contacts along with links to the categories
just created. Although you can create new contacts at the same time as creating partners (because
you can do this for *one-to-many* relations), you can't create new categories this way (because they
use *many-to-many* relations). You must create new categories in a separate step.

.. i18n: Partner categories
.. i18n: ^^^^^^^^^^^^^^^^^^
.. i18n: Start by creating partner categories in a CSV file:

Partner categories
^^^^^^^^^^^^^^^^^^
Start by creating partner categories in a CSV file:

.. i18n: #. Create the following table in your spreadsheet program:

#. Create the following table in your spreadsheet program:

.. i18n:    .. csv-table:: Partner categories file
.. i18n:       :header: "","Column A","Column B"
.. i18n:       :widths: 5,10,10
.. i18n: 
.. i18n:       "Line 1","Category Name","Parent Category"
.. i18n:       "Line 2","Quality",""
.. i18n:       "Line 3","Gold","Quality"
.. i18n:       "Line 4","Silver","Quality"
.. i18n:       "Line 5","Bronze","Quality"
.. i18n: 
.. i18n:    On the first line, :guilabel:`Category Name` and :guilabel:`Parent Category` are
.. i18n:    the column titles that correspond to field names in the :guilabel:`Partner
.. i18n:    category` form.
.. i18n: 
.. i18n:    :guilabel:`Column A` is for the different partner categories and :guilabel:`Column
.. i18n:    B` indicates if that category has a parent category. If :guilabel:`Column B` is
.. i18n:    blank then the category sits at the top level.

   .. csv-table:: Partner categories file
      :header: "","Column A","Column B"
      :widths: 5,10,10

      "Line 1","Category Name","Parent Category"
      "Line 2","Quality",""
      "Line 3","Gold","Quality"
      "Line 4","Silver","Quality"
      "Line 5","Bronze","Quality"

   On the first line, :guilabel:`Category Name` and :guilabel:`Parent Category` are
   the column titles that correspond to field names in the :guilabel:`Partner
   category` form.

   :guilabel:`Column A` is for the different partner categories and :guilabel:`Column
   B` indicates if that category has a parent category. If :guilabel:`Column B` is
   blank then the category sits at the top level.

.. i18n: #. Save spreadsheet file in CSV format – separated by commas – and name the file 
.. i18n:    \ ``categories.csv``\.
.. i18n: 
.. i18n: #. In Open ERP, select :menuselection:`Partners --> Configuration --> Categories --> Edit
.. i18n:    Categories`.
.. i18n: 
.. i18n: #. Click :guilabel:`Import` (to the bottom left of the list) to bring up the :guilabel:`Import Data` dialog
.. i18n:    box, in which you'll find the ist of fields that can be imported.
.. i18n: 
.. i18n: #. Click :guilabel:`Browse...` on the :guilabel:`File to import` field and select the CSV file you
.. i18n:    just created, \ ``categories.csv``\   Then click :guilabel:`Auto Detect` to atch the column names
.. i18n:    in the CSV file with the field names available in:guilabel:`Partner Categories`.
.. i18n: 
.. i18n: #. Click :guilabel:`Import` at the bottom-right of the dialog box to load your data. You should get
.. i18n:    the message \ ``4 objects imported``\  in a new dialog box. Close both this and the
.. i18n:    :guilabel:`Import Data` dialog box to return to the original page.
.. i18n: 
.. i18n: #. Click :menuselection:`Partners --> Partners by category` to view the tree of categories,
.. i18n:    including the new \ ``Quality``\  branch that you loaded.

#. Save spreadsheet file in CSV format – separated by commas – and name the file 
   \ ``categories.csv``\.

#. In Open ERP, select :menuselection:`Partners --> Configuration --> Categories --> Edit
   Categories`.

#. Click :guilabel:`Import` (to the bottom left of the list) to bring up the :guilabel:`Import Data` dialog
   box, in which you'll find the ist of fields that can be imported.

#. Click :guilabel:`Browse...` on the :guilabel:`File to import` field and select the CSV file you
   just created, \ ``categories.csv``\   Then click :guilabel:`Auto Detect` to atch the column names
   in the CSV file with the field names available in:guilabel:`Partner Categories`.

#. Click :guilabel:`Import` at the bottom-right of the dialog box to load your data. You should get
   the message \ ``4 objects imported``\  in a new dialog box. Close both this and the
   :guilabel:`Import Data` dialog box to return to the original page.

#. Click :menuselection:`Partners --> Partners by category` to view the tree of categories,
   including the new \ ``Quality``\  branch that you loaded.

.. i18n: New partners
.. i18n: ^^^^^^^^^^^^

New partners
^^^^^^^^^^^^

.. i18n: Here's how to create new partners with more than one contact, as you did before, and how to link them to these new categories:

Here's how to create new partners with more than one contact, as you did before, and how to link them to these new categories:

.. i18n: #. Enter the table below into your spreadsheet program.

#. Enter the table below into your spreadsheet program.

.. i18n:    .. csv-table:: Partner data file - partners.csv
.. i18n:       :header: "","Column A","Column B","Column C","Column D"
.. i18n:       :widths: 5,10,10,10,10
.. i18n: 
.. i18n:       "Line 1","Name","Categories","Contacts/Contact Name","Dedicated Salesman"
.. i18n:       "Line 2","Black Advertising","Silver,Gold","George Black","Administrator"
.. i18n:       "Line 3","","","Jean Green",""
.. i18n:       "Line 4","Tiny sprl","","Fabien Pinckaers","Administrator"

   .. csv-table:: Partner data file - partners.csv
      :header: "","Column A","Column B","Column C","Column D"
      :widths: 5,10,10,10,10

      "Line 1","Name","Categories","Contacts/Contact Name","Dedicated Salesman"
      "Line 2","Black Advertising","Silver,Gold","George Black","Administrator"
      "Line 3","","","Jean Green",""
      "Line 4","Tiny sprl","","Fabien Pinckaers","Administrator"

.. i18n: #. The second line corresponds to the creation of a new partner, with two existing categories, that
.. i18n:    has two contacts and is linked to a salesman.
.. i18n: 
.. i18n: #. Save the file using the name \ ``partners.csv``\
.. i18n: 
.. i18n: #. In OpenERP, select :menuselection:`Partners --> Partners` then import the file that you've just
.. i18n:    saved. You'll get a message confirming that you've imported and saved the data.
.. i18n: 
.. i18n: #. Verify that you've imported the data. A new partner should have appeared (``NoirAdvertising``),
.. i18n:    with a salesman (``Administrator``), two contacts (``George Black`` and ``Jean Green``) and two categories
.. i18n:    (``Silver`` and ``Gold``).

#. The second line corresponds to the creation of a new partner, with two existing categories, that
   has two contacts and is linked to a salesman.

#. Save the file using the name \ ``partners.csv``\

#. In OpenERP, select :menuselection:`Partners --> Partners` then import the file that you've just
   saved. You'll get a message confirming that you've imported and saved the data.

#. Verify that you've imported the data. A new partner should have appeared (``NoirAdvertising``),
   with a salesman (``Administrator``), two contacts (``George Black`` and ``Jean Green``) and two categories
   (``Silver`` and ``Gold``).

.. i18n: .. index::
.. i18n:    single: data, export in other forms
.. i18n:    
.. i18n: Exporting data in other forms
.. i18n: -----------------------------

.. index::
   single: data, export in other forms
   
Exporting data in other forms
-----------------------------

.. i18n: Open ERP's generic export mechanism lets you easily export any of your data to any location on your
.. i18n: system. You're not restricted to what you can export, although you can restrict who can export that
.. i18n: data using the rights management facilities discussed above.

Open ERP's generic export mechanism lets you easily export any of your data to any location on your
system. You're not restricted to what you can export, although you can restrict who can export that
data using the rights management facilities discussed above.

.. i18n: You can use this to export your data into spreadsheets or into other systems such as specialist
.. i18n: accounts packages. The export format is usually in the CSV format but you can also connect directly
.. i18n: to Microsoft Excel using Microsoft's COM mechanism.

You can use this to export your data into spreadsheets or into other systems such as specialist
accounts packages. The export format is usually in the CSV format but you can also connect directly
to Microsoft Excel using Microsoft's COM mechanism.

.. i18n: .. tip:: Access to the database
.. i18n: 
.. i18n: 	Developers can also use other techniques to automatically access the Open ERP database. The two
.. i18n: 	most useful are:
.. i18n: 
.. i18n: 	* using the XML-RPC web service,
.. i18n: 
.. i18n: 	* accessing the PostgreSQL database directly.

.. tip:: Access to the database

	Developers can also use other techniques to automatically access the Open ERP database. The two
	most useful are:

	* using the XML-RPC web service,

	* accessing the PostgreSQL database directly.

.. i18n: .. tip:: Module Recorder
.. i18n: 
.. i18n: 	If you want to enter data into Open ERP manually, you should use the Module Recorder, described in
.. i18n: 	the first section of this chapter.
.. i18n: 
.. i18n: 	By doing that you'll generate a module that can easily be reused in different databases.
.. i18n: 	Then if there are problems with a database you'll be able to reinstall the data module you
.. i18n: 	generated
.. i18n: 	with all of the entries and modifications you made for this system.

.. tip:: Module Recorder

	If you want to enter data into Open ERP manually, you should use the Module Recorder, described in
	the first section of this chapter.

	By doing that you'll generate a module that can easily be reused in different databases.
	Then if there are problems with a database you'll be able to reinstall the data module you
	generated
	with all of the entries and modifications you made for this system.

.. i18n: .. Copyright © Open Object Press. All rights reserved.

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the Open ERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium

.. Published by Open Object Press, Grand Rosière, Belgium
