
Developping modules
-------------------

Introduction
++++++++++++

Here you will found informations about the organisation of the community in
OpenERP project. It include a description of the different tools used, the role
of the differents actors, and the different process for improvement management.

The whole organisation is managed through our launchpad projects: http://launchpad.net
Our projects on launchpad are currently organised like this:


+----------------------------+----------------------------------------------+--------------------------------------------+
| **Project name**           | **URL**                                      | **Description**                            |
+============================+==============================================+============================================+
|                            |                                              |                                            |
| **openobject**             | https://launchpad.net/openobject             | the main super-project (group) where all   |
|                            |                                              | bugs, features and faq are managed         |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-bi**          | https://launchpad.net/openobject-bin         | business intelligence project              |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-server**      | https://launchpad.net/openobject-server      |  the openobject server                     |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject)client**      | https://launchpad.net/openobject-client      | the openobject application client (gtk)    |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-client-web**  | https://launchpad.net/openobject-client-web  | the openobject web client (previously      |
|                            |                                              | called eTiny)                              |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-addons**      | https://launchpad.net/openobject-addons      | the project for all modules about          |
|                            |                                              | openobject                                 |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openerp**                | https://launchpad.net/openerp                | packaging around openobject (a selection   |
|                            |                                              | of modules to build applications)          |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+

Getting Sources
+++++++++++++++

Please refer to :ref:`how-to-get-the-latest-trunk-source-code-link` in the Bazaar section

If you don't know the Bazaar version control system, please read the :ref:`documentation on Bazaar <bazaar-link>`

.. _coding-guidelines-link:

Coding Guidelines
+++++++++++++++++

Development Guidelines
""""""""""""""""""""""

Modules
^^^^^^^

Organisation of files in modules
################################

.. === Organisation of files in modules ===

The structure of a module should be like this::

 /module_name/
 /module_name/__init__.py
 /module_name/__terp__.py
 /module_name/module.py
 /module_name/module_view.xml
 /module_name/module_wizard.xml
 /module_name/module_report.xml
 /module_name/module_data.xml
 /module_name/module_demo.xml
 /module_name/module_security.xml
 /module_name/wizard/
 /module_name/wizard/__init__.py
 /module_name/wizard/wizard_name.py
 /module_name/wizard/wizard_name_view.xml
 /module_name/wizard/wizard_name_workflow.xml
 /module_name/report/
 /module_name/report/__init__.py
 /module_name/report/report_name.sxw
 /module_name/report/report_name.rml
 /module_name/report/report_name.py

Objects and fields namings
##########################

Security
########

Each object defined in your module must have at least one security rule
defined on it to make it accessible.

.. describe:: Preventing SQL Injection:


Care must be taken not to introduce SQL injection vulnerabilities to SQL
queries. SQL Injection is a kind of vulnerability in which the user is able to
introduce undesirable clauses to a SQL query (such as circumventing filters or
executing **UPDATE** or **DELETE** commands) due to incorrect quoting in
the application.

In order to prevent SQL injection you need to be cautious when constructing SQL
query strings. Good advices are to use %d and %f when only numbers are to be
substituted and always use psycopg formatting parameters. For example the
following expression is incorrect:

.. code-block:: python

  cr.execute( "SELECT * FROM table_name WHERE name='%s'" % client_supplied_string )

.. 

and 

.. code-block:: python

  cr.execute( "SELECT * FROM table_name WHERE name=%s", client_supplied_string )

.. 

should be used instead.

Development
^^^^^^^^^^^

Coding Guidelines
#################

Follow Python PEP 8: http://www.python.org/dev/peps/pep-0008/

Reporting
^^^^^^^^^

General Style
#############

  * use the Helvetica font everywhere
  * margins (in millimeters):

    - top: 14
    - bottom: 16
    - left: between 12 and 13 to allow punching holes without punching in the text area
    - right: between 12 and 13

.. note:: the line separator between the header and the body can overlap slightly in the left and right margins: up to 9 millimeters on the left and up to 12 millimeters on the right

.. 

  * for Titles use the font *Heveltica-Bold* with the size *14.5*

  * put the context on each report: example, for the report account_balance: the context is the fiscal year and periods

  * for the name of cells: use Capital Letter if the name contains more than one word (ex: Date Ordered)
  * content and name of cells should have the same indentation

  * for report, we can define two kinds of arrays:

    - array with general information, like reference, date..., use:

      + *Bold-Helvetica* and size=8 for cells name
      + *Helvetica* size="8" for content
    - array with detailed information, use:

      + *Helvetica-Bold* size *9* for cells names
      + *Helvetica* size *8* for content

.. describe:: Headers and footers for internal reports:

  * Internal report = all accounting reports and other that have only internal use (not sent to customers)
  * height of headers should be shorter
  * take off corporate header and footer for internal report (Use a simplified header for internal reports: Company's name, report title, printing date and page number)

  * header:

    - company's name: in the middle of each page 
    - report's name: is printed centered after the header
    - printing date: not in the middle of the report, but on the left in the header
    - page number: on each page, is printed on the right. This page number should contain the current page number and the total of pages. Ex: page 3/15
  * footer:

    - to avoid wasting paper, we have taken off the footer

.. describe:: table line separator:

* it's prettier if each line in the table have a light grey line as separator
* use a grey column separator only for array containing general information

.. describe:: table breaking

  * a table header should at least have two data rows (no table header alone at the bottom of the page)
  * when a big table is broken, the table header is repeated on every page

.. describe:: how to differentiate parents and children ?

  * When you have more than one level, use these styles:

  - for the levels 1 and 2:fontSize="8.0" fontName="Helvetica-Bold"
  - from the third level, use:fontName="Helvetica" fontSize="8.0" and increase the indentation with  13 (pixels) for each level
  - underline sums when the element is a parent

Modules
"""""""

Naming Convention
^^^^^^^^^^^^^^^^^

The name of the module are all lowercase, each word separated by underscrores.
Start always by the most relevant words, which are preferably names of others
modules on which it depends.

Exemple:

  * account_invoice_layout

Information Required
^^^^^^^^^^^^^^^^^^^^

Each module must contains at least:

  * name
  * description

Modules Description
^^^^^^^^^^^^^^^^^^^

Dependencies
^^^^^^^^^^^^

Each module must contains:

  * A list of dependencies amongst others modules: ['account','sale']

    - Provide only highest requirement level, not need to set ['account','base','product','sale']
  * A version requirement string where base is the Open ERP version as a Python expression

    - account>=1.0 && base=4.4

Module Content
^^^^^^^^^^^^^^

Each module must contains dema data for every object defined in the module.

If you implemented workflows in the module, create demo data that passes
most branches of your workflow. You can use the module recorder to help you
build such demo data.

User Interface Guidelines
"""""""""""""""""""""""""

Menus
^^^^^

Organising menus
################

Here is a good example:

  * Invoices (list)

    - Customer Invoices (list)

      + Draft Customer Invoices (list)
      + Open Customer Invoices (list)
      + New Customer Invoice (form)
    - Supplier Invoices

      + ...

Add a *New ...* menu only if the user requires it, otherwise, open all
menus as lists. The *New ...* menu open as a form instead of a list. For example,
don't put *New ...* in a menu in the configuration part.

If you use folders that are clickable, their child must be of the
same object type. (we suppose that inheritancies are the same objects)

List are plurals:

  * *Customer Invoice*, should be *Customer Invoices*


If you want to create menu that filters on the user (*All* and *My*) put them at the same level:

  * Tasks
  * My Taks

And not:

  * Tasks

    - My Tasks

Avoid Abbreviations in menus if possible. Example:

  * BoM Lines -> Bill of Materials Lines

Reporting Menu
##############

The dashboard menu must be under the report section of each main menu

  * Good: Sales Management / Reporting / Dashboards / Sales Manager
  * Bad: Dashboard / Sales / Sales Manager

If you want to manage the *This Month/ALL months* menu, put them at the latest level:

  * Reporting/Timesheet by User/All Month
  * Reporting/Timesheet by User/This Month

Icons in the menu
#################

  * The icon of the menu, must be set according to the end action of the wizard, example:

    - wizard that prints a report, should use a report icon and not a wizard
    - wizard that opens a list at the end, should use a list icon and not a wizard

Order of the menus
##################

The configuration menu must be at the top of the list, use a sequence=0

The *Reporting* menu is at the bottom of the list, use a sequence=50.

Common Mistakes
###############

  * Edit Categories -> Categories
  * List of Categories -> Categories

Views
^^^^^

Objects with States
###################

  * The state field, if any, must be at the bottom left corner of the view
  * Buttons to make the state change at the right of this state field

Search Criterions
#################

Search criterions: search available on all columns of the list view

Action Names
^^^^^^^^^^^^

.. todo:: write 'Action Names' section

Wizards
^^^^^^^

Terminology
"""""""""""

Default Language
^^^^^^^^^^^^^^^^

The default language for every development must be U.S. english.

For menus and fields, use uppercase for all first letters, excluding conjections:

  * Chart of Accounts

Naming Conventions
^^^^^^^^^^^^^^^^^^

  * Avoid generic terms in fields and use if possible explicit terms, some example:

    - Name -> Sale Order Name
    - Parent -> Bill of Material Parent
    - Rate -> Currency Rate Conversion
    - Amount -> Quantity Sold

Some terms
^^^^^^^^^^

  * All Tree of ressources are called *XXX's Structure*, unless a dedicated term exist for the concept

    - Good: Location' Structure, Chart of Accounts, Categories' Structure
    - Bad: Tree of Category, Tree of Bill of Meterials

Module Recorder
+++++++++++++++

.. todo:: write 'Module Recorder' section

Review quality
++++++++++++++

.. todo:: write 'Review quality' section

