
.. _from-packages:

Installation from Packages
++++++++++++++++++++++++++

For LINUX several installation packages are provided, but not all distributions are covered.
(We welcome contributions for any of the distributions not covered)

Debian Step 1
"""""""""""""

For Debian testing and unstable, you can use the official packages from the normal Debian
repository. For Debian stable, you can use the half-official packages from
http://www.backports.org/ (read http://www.backports.org/instructions.html how
to prepare your sources.list etc.). In both cases, install the packages with
the following commands: ::

  apt-get install tinyerp-client xpdf
  apt-get install tinyerp-server postgresql postgresql-client python-imaging python-pyparsing graphviz

Snapshots of newer versions are available on the website of the Debian maintainer and in
Debian experimental:

 http://archive.daniel-baumann.ch/debian/packages/tinyerp-client/
 http://archive.daniel-baumann.ch/debian/packages/tinyerp-server/

Ubuntu
""""""

Below information is obsolete. There is a Page About Installing on Ubuntu

It is recommended that you install stable version 4.0.3.

See this link for installation instructions in Ubuntu Feisty: http://openerp.com/forum/topic4750.html

If you want to install from the repositories, follow the steps below.

Ubuntu Step 1
"""""""""""""

Make sure the Universe repositories are enabled. Then run the following commands in a
terminal: ::

  sudo apt-get install tinyerp-client xpdf python-imaging python-pyparsing graphviz
  sudo apt-get install tinyerp-server postgresql-common postgresql-client-common postgresql-8.1 postgresql-client-8.1

Note: For Ubuntu the versions of Open ERP in the repositories are:

 * Edgy(6.10) = 3.3.0
 * Feisty(7.04) = 4.0.0
 * Gutsy(7.10) = 4.0.3

Debian/Ubuntu Step 2
""""""""""""""""""""

When the installations are done, you have to create a database, see Setup a Postgresql user
and database for details.

OpenERP server is configured to only listen to localhost by default. If you like to change
this, as well as the database settings, please read ``/usr/share/doc/tinyerp-client/README.Debian``

Other usefull link http://doc.ubuntu-fr.org/tinyerp

Now start the client program from Program -> Internet -> Open ERP Client

Fedora
""""""

Open ERP packages exists for Fedora Core 3, 4 and Rawhide. They are stored in the Fedora
Extras repository. You can install it with::

  yum install tinyerp tinyerp-server

Same applies for Fedora 7, OpenERP is in the (now combined) repository and can either be
installed from CLI or via one of the GUI's for software installation.

