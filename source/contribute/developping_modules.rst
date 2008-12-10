
Developping modules
-------------------

Introduction
++++++++++++

Here you will found informations about the organisation of the community in
OpenERP project. It include a description of the different tools used, the role
of the differents actors, and the different process for improvement management.

The whole organisation is managed through our launchpad projects: http://launchpad.net
Our projects on launchpad are currently organised like this:

  * https://launchpad.net/openobject **openobject** : the main super-project (group) where all bugs, features and faq are managed.

    - https://launchpad.net/openobject-bi **openobject-bi** : business intelligence project
    - https://launchpad.net/openobject-server **openobject-server** : the openobject server
    - https://launchpad.net/openobject-client **openobject-client** : the openobject application client (gtk)
    - https://launchpad.net/openobject-client-web **openobject-client-web** : the openobject web client (previously called eTiny)
    - https://launchpad.net/openobject-addons **openobject-addons** : the project for all modules about openobject
    - https://launchpad.net/openerp **openerp** : packaging around openobject (a selection of modules to build applications)

Getting Sources
+++++++++++++++

Bazaar, the version control system
""""""""""""""""""""""""""""""""""

The new development process uses Bazaar via launchpad.net instead of Subversion.
Bazaar offers a flexibility with this distributed model. You can see our
branches on https://code.launchpad.net/~openerp.

.. describe:: Explanation of directories:

Two teams have been created on launchpad:

  * OpenERP quality teams --> they can commit on:

    - lp:~openerp/openobject-addons/4.2
    - lp:~openerp/openobject-addons/trunk
    - lp:~openerp/openobject-addons/4.2-extra-addons
    - lp:~openerp/openobject-addons/trunk-extra-addons
    - lp:~openerp/openobject-bi/trunk-addons
    - lp:~openerp/openobject-bi/trunk-cli
    - lp:~openerp/openobject-bi/trunk-client-web
    - lp:~openerp/openobject-client/4.2
    - lp:~openerp/openobject-client/trunk
    - lp:~openerp/openobject-client-web/4.2
    - lp:~openerp/openobject-client-web/trunk
    - lp:~openerp/openobject-server/4.2
    - lp:~openerp/openobject-server/trunk

  * 0penERP-commiter --> they can commit on:

    - lp:~openerp/openobject-addons/4.2-extra-addons
    - lp:~openerp/openobject-addons/trunk-extra-addons

In this group, we include some of our partners who will be selected on a meritocracy basis by the quality team.

  * Contributors --> they can commit on:

    - lp:~openerp-community

.. describe:: How can I be included in OpenERP-commiter team ?

Any contributor who is interested to become a commiter must show his interest
on working for openerp project and his ability to do it in a proper way as the
selection for this group is based on meritocracy. It can be by proposing bug
fixes, features requested on our :ref:`bug tracker <bug-tracker-link>` system.
You can even suggest additional modules and/or functionalities on our :ref:`bug
tracker <bug-tracker-link>` system.

.. describe:: How can I suggest some additionals modules or functionalities ?

To create some additionals modules and/or functionnalities and include them in
the project, this is the way to do:

  #. open a branch in launchpad
  #. report and suggest your work via your new branch to our :ref:`bug tracker
     <bug-tracker-link>` system (there are two way : bugs report for bug and
     blueprint for idea / functionnality)
  #. wait for approval by our quality team

Or the quality team approved your work and merge it into the official branch
(like explained in the :ref:`bug tracker <bug-tracker-link>` section), or they
refused it and ask you to improve your work before merging it in our official
branch.

Installing Bazaar
"""""""""""""""""

Get Bazaar version control to pull the source from Launchpad.

To install bazaar on any ubuntu distribution, you can edit /etc/apt/sources.list by

::

  sudo gedit /etc/apt/sources.list

and put these lines in it:

::

  deb http://ppa.launchpad.net/bzr/ubuntu intrepid main
  deb-src http://ppa.launchpad.net/bzr/ubuntu intrepid main

Then, do the following

::

  sudo apt-get install bzr

To work correctly, bzr version must be at least 1.3. Check it with the command:

::

  bzr --version

If you don't have at least 1.3 version, you can check this url: http://bazaar-vcs.org/Download
On debian, in any distribution, the 1.5 version is working, you can get it on this url: http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb

If you experience problems with Bazaar, please read the :ref:`bazaar-faq-link` before asking any questions.

Quick Summary
"""""""""""""

This is the official and proposed way to contribute on OpenERP and OpenObject.

To download the latest sources and create your own local branches of OpenERP, do this::

  bzr branch lp:openerp
  cd openerp
  ./bzr_set.py

This will download all the component of openerp (server, client, addons) and create links of modules in addons in your server so that you can use it directly. You can change the bzr_set.py file to select what you want to download exactly. Now, you can edit the code and commit in your local branch.::

  EDIT addons/account/account.py
  cd addons
  bzr ci -m "Testing Modifications"

Once your code is good enough and follow the :ref:`coding-guidelines-link`, you
can push your branch in launchpad. You may have to create an account on
launchpad first, register your public key, and subscribe to the `openerp-community <https://launchpad.net/~openerp-community>`_ team. Then, you
can push your branch. Suppose you want to push your addons::

  cd addons
  bzr push lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
  bzr bind lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME

After having done that, your branch is public on Launchpad, in the `OpenObject
project <https://code.launchpad.net/openobject>`_, and commiters can work on
it, review it and propose for integration in the official branch. The last line
allows you to rebind your branch to the one which is on launchpad, after having
done this, your commit will be applied on launchpad directly (unless you use ``--local``)::

  bzr pull    # Get modifications on your branch from others
  EDIT STUFF
  bzr ci    # commit your changes on your public branch



If your changes fixe a public bug on launchpad, you can use this to mark the bug as fixed by your branch::

  bzr ci --fixes=lp:453123   # Where 453123 is a bug ID

Once your branch is mature, mark it as mature in the web interface of launchpad
and request for merging in the official release. Your branch will be reviewed
by a commiter and then the quality team to be merged in the official release.

How to get the latest trunk source code
"""""""""""""""""""""""""""""""""""""""

Get a clone of each repository

::

  bzr clone lp:~openerp/openobject-server/trunk server
  bzr clone lp:~openerp/openobject-client/trunk client
  bzr clone lp:~openerp/openobject-client-web/trunk client-web
  bzr clone lp:~openerp/openobject-addons/trunk addons

If you want to get a clone of the extra-addons repository, you can execute this command

::

  bzr clone lp:~openerp-commiter/openobject-addons/trunk-extra-addons extra-addons

run the setup scripts in the respective directories

::

  python2.4 setup.py build
  python2.4 setup.py install

Currently the initialisation procedure of the server parameter --init=all to
populate the database seems to be broken in trunk.

It is recommended to create a new database via the gtk-client. Before that the web-client will not work.

Start OpenERP server like this:

::

  ./tinyerp-server.py --addons-path=/path/to/my/addons

The ``bin/addons`` will be considered as default addons directory which can be
overriden by the ``/path/to/my/addons/``. That is if an addon exists in
``bin/addons`` as well as ``/path/to/my/addons`` (custom path) the later one will
be given preference over the ``bin/addons`` (default path).

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

Actions Names
^^^^^^^^^^^^^

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

Review quality
++++++++++++++



