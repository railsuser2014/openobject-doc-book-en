
Installation Manual
-------------------

This manual has used existing resources found in this wiki however it has
outlined the order of installing the various components as well as references
to point you in the right direction. It is hoped that a complete manual will be
able to be compiled from this information and this also helps to rectify any
confusion regarding installing this great software solution

Alternative
-----------

The alternative to installing components separately is to use
`tinyerp-allinone-setup-4.2.3.1.exe <http://openerp.com/downloads.html>`_. This
alternative is a basic one-click installation. It works with XP, Vista, 2003
Server and 2008 Server. Using this method of installation on servers, password
security policies need to be changed to less strict until the installation is
complete otherwise the PostgreSQL component fails due to lack of password
complexity.

System Requirements
+++++++++++++++++++

For advanced users their are three modules to OpenERP, OpenERP Server, OpenERP
Client and PostgreSQL database which can be installed on different computers or
on the same computer. The key to communication is through ports which the
default ports are:

 * **5432** for PostgreSQL,
 * **8070** for communication between OpenERP client and OpenERP Server,
 * **8080** for browser to Client/Server,
 * **8021** for ftp Client/Server if you plan to use the *DMS* (Document Management System),

however for simplicity reasons we will install everything on the same box/node.

Apparently the server auto installation works on windows operating systems
formatted using NTFS (not a FAT or FAT32 partition). Windows 95' 98' or ME'
will NOT WORK for obvious reasons -- they cannot be formatted in NTFS.

If you want to use Open ERP, you have to install both the Open ERP Server and the Open ERP Client

PostgreSQL
++++++++++

Installing PostgreSQL
"""""""""""""""""""""

Download and execute PostreSQL installation from `PostgreSQL Download Page
<http://www.postgresql.org/download/>`_ and follow the instructions written
here.

.. todo:: add link to postgres 8, page 'auto_install_server' (windows)

More Information on Configuration of PostresQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Have a look at some more helpful information on troubleshooting [here] and
`here <http://archives.postgresql.org/pgsql-bugs/2006-03/msg00180.php>`_

.. todo:: add link to http://openerp.com/wiki/index.php/Manual_Installation:Installation_Manual/Setup_a_Postgresql_user_and_database

Preparing the New Database for Open ERP Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the instructions [here]

.. todo:: add link to 'Preparation_of_a_new_database_for_Open_ERP_Server', page 'auto_install_server' (windows)

Installing OpenERP Server
+++++++++++++++++++++++++

Follow instructions listed [here]

.. todo:: add link to 'Open_ERP_Server_Installation', page 'auto_install_server' (windows)

Installing OpenERP (Client - Dependencies) and Client
+++++++++++++++++++++++++++++++++++++++++++++++++++++

Refer to :ref:`openerp-client-for-windows-link`

Additional Install Information
++++++++++++++++++++++++++++++

Read :ref:`additional-install-information-link`

