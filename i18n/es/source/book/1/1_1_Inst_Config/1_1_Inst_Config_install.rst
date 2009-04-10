
.. i18n: The installation of Open ERP
.. i18n: ============================

The installation of Open ERP
============================

.. i18n: Whether you're from a small company investigating how Open ERP works, or on the IT staff of a
.. i18n: larger organization and have been asked to assess Open ERP's capabilities, your first requirement
.. i18n: is to install it or to find a working installation.

Whether you're from a small company investigating how Open ERP works, or on the IT staff of a
larger organization and have been asked to assess Open ERP's capabilities, your first requirement
is to install it or to find a working installation.

.. i18n: The table below summarizes the various installation methods that will be described in the following
.. i18n: sections.

The table below summarizes the various installation methods that will be described in the following
sections.

.. i18n: .. csv-table:: Comparison of the different methods of installation on Windows or Linux
.. i18n:    :header: "Method","Average Time","Level of Complexity","Notes"
.. i18n:    :widths: 20,15,15,30
.. i18n: 
.. i18n:    "All-in-one Windows Installer","A few minutes","Simple","Very useful for quick evaluations because it installs all of the components pre-configured on one computer (using the GTK client)."
.. i18n:    "Independent installation on Windows","Half an hour","Medium","Enables you to install the components on different computers. Can be put into production use."
.. i18n:    "Ubuntu Linux packages","A few minutes","Simple","Simple and quick but the Ubuntu packages aren't always up to date."
.. i18n:    "From source, for all Linux systems","More than half an hour","Medium to slightly difficult","This is the method recommended for production environments because it's easy to keep it up to date."

.. csv-table:: Comparison of the different methods of installation on Windows or Linux
   :header: "Method","Average Time","Level of Complexity","Notes"
   :widths: 20,15,15,30

   "All-in-one Windows Installer","A few minutes","Simple","Very useful for quick evaluations because it installs all of the components pre-configured on one computer (using the GTK client)."
   "Independent installation on Windows","Half an hour","Medium","Enables you to install the components on different computers. Can be put into production use."
   "Ubuntu Linux packages","A few minutes","Simple","Simple and quick but the Ubuntu packages aren't always up to date."
   "From source, for all Linux systems","More than half an hour","Medium to slightly difficult","This is the method recommended for production environments because it's easy to keep it up to date."

.. i18n: Each time a new release of Open ERP is made, Tiny supplies a complete Windows auto-installer for
.. i18n: it. This contains all of the components you need – the PostgreSQL database server, the Open ERP
.. i18n: application server and the GTK application client.

Each time a new release of Open ERP is made, Tiny supplies a complete Windows auto-installer for
it. This contains all of the components you need – the PostgreSQL database server, the Open ERP
application server and the GTK application client.

.. i18n: This auto-installer enables you to install the whole system in just a few mouse-clicks. The initial
.. i18n: configuration is set up during installation, making it possible to start using it very quickly as
.. i18n: long as you don't want to change the underlying code. It's aimed at the installation of everything
.. i18n: on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as
.. i18n: well.

This auto-installer enables you to install the whole system in just a few mouse-clicks. The initial
configuration is set up during installation, making it possible to start using it very quickly as
long as you don't want to change the underlying code. It's aimed at the installation of everything
on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as
well.

.. i18n: The first step is to download the Open ERP installer. At this stage you must choose which version
.. i18n: to install – the stable version or the development version. If you're planning to put it straight
.. i18n: into production you're strongly advised to choose the stable version.

The first step is to download the Open ERP installer. At this stage you must choose which version
to install – the stable version or the development version. If you're planning to put it straight
into production you're strongly advised to choose the stable version.

.. i18n: .. index::
.. i18n:    single: stable versions

.. index::
   single: stable versions

.. i18n: .. note::  Stable versions and development versions
.. i18n: 
.. i18n: 	Open ERP development proceeds on two parallel tracks: stable versions and development versions.
.. i18n: 
.. i18n: 	New functionality is integrated into the development branch. This branch is more advanced than the
.. i18n: 	stable branch, but it can contain undiscovered and unfixed faults. A new development release is
.. i18n: 	made every month or so, and Tiny have made the code repository available so you can download the
.. i18n: 	very latest revisions if you want.
.. i18n: 
.. i18n: 	The stable branch is designed for production environments. Releases of new functionality there are
.. i18n: 	made only about once a year after a long period of testing and validation. Only fault fixes are
.. i18n: 	released through the year on the stable branch.

.. note::  Stable versions and development versions

	Open ERP development proceeds on two parallel tracks: stable versions and development versions.

	New functionality is integrated into the development branch. This branch is more advanced than the
	stable branch, but it can contain undiscovered and unfixed faults. A new development release is
	made every month or so, and Tiny have made the code repository available so you can download the
	very latest revisions if you want.

	The stable branch is designed for production environments. Releases of new functionality there are
	made only about once a year after a long period of testing and validation. Only fault fixes are
	released through the year on the stable branch.

.. i18n: .. index::
.. i18n:    single: installation; Windows (all-in-one)

.. index::
   single: installation; Windows (all-in-one)

.. i18n: To download the version of Open ERP for Windows, follow these steps:

To download the version of Open ERP for Windows, follow these steps:

.. i18n: #. Navigate to the site http://openerp.com.
.. i18n: 
.. i18n: #. Click :menuselection:`Downloads` on the menu at the left then, under :guilabel:`Windows Installers`,
.. i18n:    :menuselection:`All in One`.
.. i18n: 
.. i18n: #. This brings up the demonstration version Windows installer, 
.. i18n:    currently :program:`openerp-allinone-setup-5.0.0-3`.
.. i18n: 
.. i18n: #. Save the file on your PC - it's quite a substantial size because it downloads everything including
.. i18n:    the PostgreSQL database system, so will take some time.

#. Navigate to the site http://openerp.com.

#. Click :menuselection:`Downloads` on the menu at the left then, under :guilabel:`Windows Installers`,
   :menuselection:`All in One`.

#. This brings up the demonstration version Windows installer, 
   currently :program:`openerp-allinone-setup-5.0.0-3`.

#. Save the file on your PC - it's quite a substantial size because it downloads everything including
   the PostgreSQL database system, so will take some time.

.. i18n: .. index::
.. i18n:    single:  installation; administrator

.. index::
   single:  installation; administrator

.. i18n: To install Open ERP and its database you must be signed in as an Administrator on your PC. Double-
.. i18n: click the installer file to install it and accept the default parameters on each dialog box as you go. 

To install Open ERP and its database you must be signed in as an Administrator on your PC. Double-
click the installer file to install it and accept the default parameters on each dialog box as you go. 

.. i18n: If you had previously tried to install the all-in-one version of Open ERP, you have to uninstall
.. i18n: that first because various elements of a previous installation could interfere with your new installation.
.. i18n: Make sure that all Tiny ERP, Open ERP and PostgreSQL applications are removed:
.. i18n: you're likely to have to restart your PC to finish removing all traces of them.

If you had previously tried to install the all-in-one version of Open ERP, you have to uninstall
that first because various elements of a previous installation could interfere with your new installation.
Make sure that all Tiny ERP, Open ERP and PostgreSQL applications are removed:
you're likely to have to restart your PC to finish removing all traces of them.

.. i18n: The Open ERP client can be opened, ready to use the Open ERP system, once you have completed 
.. i18n: the all--in-one installation. The next step consists
.. i18n: of setting up the database, and is covered in the final section of this chapter :ref:`sect-creatingdb`.

The Open ERP client can be opened, ready to use the Open ERP system, once you have completed 
the all--in-one installation. The next step consists
of setting up the database, and is covered in the final section of this chapter :ref:`sect-creatingdb`.

.. i18n: .. index::
.. i18n:    single: installation; Windows (independent)

.. index::
   single: installation; Windows (independent)

.. i18n: Independent installation on Windows
.. i18n: -----------------------------------

Independent installation on Windows
-----------------------------------

.. i18n: System administrators can have very good reasons for wanting to install the various components of a
.. i18n: Windows installation separately. For example, your company may not support the version of PostgreSQL
.. i18n: or Python that's installed automatically, or you may already have PostgreSQL installed on the server
.. i18n: you're using, or you may want to install the database server, application server and web server on
.. i18n: separate hardware units.

System administrators can have very good reasons for wanting to install the various components of a
Windows installation separately. For example, your company may not support the version of PostgreSQL
or Python that's installed automatically, or you may already have PostgreSQL installed on the server
you're using, or you may want to install the database server, application server and web server on
separate hardware units.

.. i18n: For this situation you can get separate installers for the Open ERP server and client from the same
.. i18n: location as the all-in-one auto-installer. You'll also have to download and install a suitable
.. i18n: version of PostgreSQL independently.

For this situation you can get separate installers for the Open ERP server and client from the same
location as the all-in-one auto-installer. You'll also have to download and install a suitable
version of PostgreSQL independently.

.. i18n: You must install PostgreSQL before the Open ERP server, and you must also set it up with a user
.. i18n: and password so that the Open ERP server can connect to it. Tiny's web-based documentation gives
.. i18n: full and current details.

You must install PostgreSQL before the Open ERP server, and you must also set it up with a user
and password so that the Open ERP server can connect to it. Tiny's web-based documentation gives
full and current details.

.. i18n: Connecting users on other PCs to the Open ERP server
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connecting users on other PCs to the Open ERP server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: To connect other computers to the Open ERP server you must set the server up so that it's
.. i18n: visible to the other PCs, and install a GTK client on each of the those PCs:

To connect other computers to the Open ERP server you must set the server up so that it's
visible to the other PCs, and install a GTK client on each of the those PCs:

.. i18n: #. Make your Open ERP server visible to other PCs by opening the Windows Firewall in the Control
.. i18n:    Panel, then asking the firewall to make an exception of the Open ERP server. In the
.. i18n:    :guilabel:`Exceptions` tab of Windows Firewall click on :guilabel:`Add a program...` and choose
.. i18n:    :guilabel:`Open ERP Server` in the list provided. This step enables other computers to see the
.. i18n:    Open ERP application on this server.
.. i18n: 
.. i18n: #. Install the Open ERP client (:program:`openerp-client-5.X.exe`), which you can download in the
.. i18n:    same way as you downloaded the other Open ERP software, onto the other PCs.

#. Make your Open ERP server visible to other PCs by opening the Windows Firewall in the Control
   Panel, then asking the firewall to make an exception of the Open ERP server. In the
   :guilabel:`Exceptions` tab of Windows Firewall click on :guilabel:`Add a program...` and choose
   :guilabel:`Open ERP Server` in the list provided. This step enables other computers to see the
   Open ERP application on this server.

#. Install the Open ERP client (:program:`openerp-client-5.X.exe`), which you can download in the
   same way as you downloaded the other Open ERP software, onto the other PCs.

.. i18n: .. tip:: Version matching
.. i18n: 
.. i18n: 	You must make sure that the version of the client matches that of the server. The version number is
.. i18n: 	given as part of the name of the downloaded file. Although it's possible that some different
.. i18n: 	revisions of client and server will function together, there's no certainty about that.

.. tip:: Version matching

	You must make sure that the version of the client matches that of the server. The version number is
	given as part of the name of the downloaded file. Although it's possible that some different
	revisions of client and server will function together, there's no certainty about that.

.. i18n: .. index::
.. i18n:    single:  administrator

.. index::
   single:  administrator

.. i18n: To run the client installer on every other PC you'll need to have administrator rights there. The
.. i18n: installation is automated, so you just need to guide it through its different installation steps.

To run the client installer on every other PC you'll need to have administrator rights there. The
installation is automated, so you just need to guide it through its different installation steps.

.. i18n: To test your installation, start by connecting through the Open ERP client on the server machine
.. i18n: while you're still logged in as administrator.

To test your installation, start by connecting through the Open ERP client on the server machine
while you're still logged in as administrator.

.. i18n: .. note:: Why sign in as a PC Administrator?
.. i18n: 
.. i18n: 	You'd not usually be signed on as a PC administrator when you're just running the Open ERP client,
.. i18n: 	but if there have been problems in the installation it's easier to remain as an administrator after
.. i18n: 	the installation so that you can make any necessary fixes than to switch user as you alternate
.. i18n: 	between roles as a tester and a software installer.

.. note:: Why sign in as a PC Administrator?

	You'd not usually be signed on as a PC administrator when you're just running the Open ERP client,
	but if there have been problems in the installation it's easier to remain as an administrator after
	the installation so that you can make any necessary fixes than to switch user as you alternate
	between roles as a tester and a software installer.

.. i18n: Start the GTK client on the server through the Windows Start menu there. The main client window
.. i18n: appears, identifying the server you're connected to (which is \ ``localhost``\   – your own server
.. i18n: PC – by default). If the message :guilabel:`No database found, you must create one` appears then
.. i18n: you've **successfully connected** to an Open ERP server containing, as yet, no databases.

Start the GTK client on the server through the Windows Start menu there. The main client window
appears, identifying the server you're connected to (which is \ ``localhost``\   – your own server
PC – by default). If the message :guilabel:`No database found, you must create one` appears then
you've **successfully connected** to an Open ERP server containing, as yet, no databases.

.. i18n: .. figure:: images/new_login_dlg.png
.. i18n:    :align: center
.. i18n:    :scale: 75
.. i18n: 
.. i18n:    *Dialog box on connecting a GTK client to a new Open ERP server*

.. figure:: images/new_login_dlg.png
   :align: center
   :scale: 75

   *Dialog box on connecting a GTK client to a new Open ERP server*

.. i18n: .. index::
.. i18n:    single: protocol; XML-RPC
.. i18n:    single: protocol; NET-RPC
.. i18n:    single: XML-RPC
.. i18n:    single: NET-RPC

.. index::
   single: protocol; XML-RPC
   single: protocol; NET-RPC
   single: XML-RPC
   single: NET-RPC

.. i18n: .. note:: Connection modes
.. i18n: 
.. i18n: 	In its default configuration at the time of writing, 
.. i18n: 	the Open ERP client connects to port 8069 on the server using the
.. i18n: 	XML-RPC protocol (from Linux) or port 8070 using the NET-RPC protocol instead (from Windows).
.. i18n: 	You can use either protocol from either operating system.
.. i18n: 	NET-RPC is quite a bit quicker, although you may not notice that on the GTK client in normal use.
.. i18n: 	Open ERP can run XML-RPC, but not NET-RPC, as a secure connection.
.. i18n: 	
.. i18n: The all-in-one installer also provides a web server, but this was not yet working at the time
.. i18n: of writing.

.. note:: Connection modes

	In its default configuration at the time of writing, 
	the Open ERP client connects to port 8069 on the server using the
	XML-RPC protocol (from Linux) or port 8070 using the NET-RPC protocol instead (from Windows).
	You can use either protocol from either operating system.
	NET-RPC is quite a bit quicker, although you may not notice that on the GTK client in normal use.
	Open ERP can run XML-RPC, but not NET-RPC, as a secure connection.
	
The all-in-one installer also provides a web server, but this was not yet working at the time
of writing.

.. i18n: Resolving errors with a Windows installation
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resolving errors with a Windows installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: If you can't get Open ERP to work after installing your Windows system you'll find some ideas for
.. i18n: resolving this below:

If you can't get Open ERP to work after installing your Windows system you'll find some ideas for
resolving this below:

.. i18n: #. Is the Open ERP application working? Signed in to the server as an administrator, stop and
.. i18n:    restart the service using :guilabel:`Stop Service` and :guilabel:`Start Service` from the menu
.. i18n:    :menuselection:`Start --> Programs --> OpenERP Server` .
.. i18n: 
.. i18n: #. Is the Open ERP application server set up correctly? Signed in to the server as
.. i18n:    Administrator, open the file \ ``openerp-server.conf``\  in \
.. i18n:    ``C:\Program Files\OpenERP AllInOne``\  and check its content. This file is generated during
.. i18n:    installation with information derived from the database. If you see something strange it's best to
.. i18n:    entirely reinstall the server from the demonstration installer rather than try to work out what's
.. i18n:    happening.

#. Is the Open ERP application working? Signed in to the server as an administrator, stop and
   restart the service using :guilabel:`Stop Service` and :guilabel:`Start Service` from the menu
   :menuselection:`Start --> Programs --> OpenERP Server` .

#. Is the Open ERP application server set up correctly? Signed in to the server as
   Administrator, open the file \ ``openerp-server.conf``\  in \
   ``C:\Program Files\OpenERP AllInOne``\  and check its content. This file is generated during
   installation with information derived from the database. If you see something strange it's best to
   entirely reinstall the server from the demonstration installer rather than try to work out what's
   happening.

.. i18n: 	.. figure:: images/terp_server_conf.png
.. i18n: 	   :align: center
.. i18n: 	   :scale: 80
.. i18n: 	          
.. i18n: 	   *Typical Open ERP configuration file*

	.. figure:: images/terp_server_conf.png
	   :align: center
	   :scale: 80
	          
	   *Typical Open ERP configuration file*

.. i18n: #. Is your PostgreSQL server running? Signed in as administrator, select :guilabel:`Stop Service`
.. i18n:    from the menu :menuselection:`Start --> Programs --> PostgreSQL`.  If, after a couple of seconds,
.. i18n:    you can read :guilabel:`The PostgreSQL4OpenERP service has stopped` then you can be reasonably sure
.. i18n:    that the database server was working. Restart PostgreSQL.
.. i18n: 	   
.. i18n: #. Does PostgreSQL work at all? Still in the PostgreSQL menu, start
.. i18n:    the pgAdmin III application which you can use to explore the database. Double-click on the \
.. i18n:    ``PostgreSQL4OpenERP``\  connection. 
.. i18n:    You can find the password in the Open ERP server configuration file.
.. i18n:    If the database server is working
.. i18n:    you'll be able to see some information about the empty database. If it's not then an error message
.. i18n:    will appear.
.. i18n: 
.. i18n: #. Are your client programs correctly installed? If your Open ERP GTK clients haven't started then
.. i18n:    the swiftest approach is to reinstall them.
.. i18n: 
.. i18n: #. Can remote client computers see the server computer at all? Check this by opening a command prompt
.. i18n:    window (enter \ ``cmd``\  in the window :menuselection:`Start --> Run...` ) and enter \ ``ping
.. i18n:    <address of server>``\  there (where \ ``<address of server>``\  represents the IP address of the
.. i18n:    server). The server should respond with a reply. 
.. i18n: 
.. i18n: #. Have you changed any of the server's parameters? At this point in the installation the port
.. i18n:    number of the server must be 8069 using the protocol XML-RPC.
.. i18n: 
.. i18n: #. Is there anything else in the server's history that can help you identify the problem? Open the file
.. i18n:    \ ``openerp-server.log``\  in \ ``C:\Program Files\OpenERP AllInOne``\  
.. i18n:    (which you can only do when the server is stopped) and scan through the
.. i18n:    history for ideas. If something looks strange there, contributors to the Open ERP forums can often
.. i18n:    help identify the reason.

#. Is your PostgreSQL server running? Signed in as administrator, select :guilabel:`Stop Service`
   from the menu :menuselection:`Start --> Programs --> PostgreSQL`.  If, after a couple of seconds,
   you can read :guilabel:`The PostgreSQL4OpenERP service has stopped` then you can be reasonably sure
   that the database server was working. Restart PostgreSQL.
	   
#. Does PostgreSQL work at all? Still in the PostgreSQL menu, start
   the pgAdmin III application which you can use to explore the database. Double-click on the \
   ``PostgreSQL4OpenERP``\  connection. 
   You can find the password in the Open ERP server configuration file.
   If the database server is working
   you'll be able to see some information about the empty database. If it's not then an error message
   will appear.

#. Are your client programs correctly installed? If your Open ERP GTK clients haven't started then
   the swiftest approach is to reinstall them.

#. Can remote client computers see the server computer at all? Check this by opening a command prompt
   window (enter \ ``cmd``\  in the window :menuselection:`Start --> Run...` ) and enter \ ``ping
   <address of server>``\  there (where \ ``<address of server>``\  represents the IP address of the
   server). The server should respond with a reply. 

#. Have you changed any of the server's parameters? At this point in the installation the port
   number of the server must be 8069 using the protocol XML-RPC.

#. Is there anything else in the server's history that can help you identify the problem? Open the file
   \ ``openerp-server.log``\  in \ ``C:\Program Files\OpenERP AllInOne``\  
   (which you can only do when the server is stopped) and scan through the
   history for ideas. If something looks strange there, contributors to the Open ERP forums can often
   help identify the reason.

.. i18n: .. index::
.. i18n:    single: installation; Linux (Ubuntu)

.. index::
   single: installation; Linux (Ubuntu)

.. i18n: Installation on Linux (Ubuntu)
.. i18n: ------------------------------

Installation on Linux (Ubuntu)
------------------------------

.. i18n: This section guides you through installing the Open ERP server and client on Ubuntu, one of the
.. i18n: most popular Linux distributions. It assumes that you're using a recent release of Desktop Ubuntu
.. i18n: with its graphical user interface on a desktop or laptop PC.

This section guides you through installing the Open ERP server and client on Ubuntu, one of the
most popular Linux distributions. It assumes that you're using a recent release of Desktop Ubuntu
with its graphical user interface on a desktop or laptop PC.

.. i18n: .. note:: Other Linux distributions
.. i18n: 
.. i18n: 	Installation on other distributions of Linux is fairly similar to installation on Ubuntu. Read this
.. i18n: 	section of the book so that you understand the principles, then use the online documentation and
.. i18n: 	the forums for your specific needs on another distribution.

.. note:: Other Linux distributions

	Installation on other distributions of Linux is fairly similar to installation on Ubuntu. Read this
	section of the book so that you understand the principles, then use the online documentation and
	the forums for your specific needs on another distribution.

.. i18n: For information about installation on other distributions, visit the documentation section by
.. i18n: following :menuselection:`Product --> Documentation` on http://www.openerp.com. Detailed instructions
.. i18n: are given there for different distributions and releases, and you should also check if there are
.. i18n: more up to date instructions for the Ubuntu distribution as well.

For information about installation on other distributions, visit the documentation section by
following :menuselection:`Product --> Documentation` on http://www.openerp.com. Detailed instructions
are given there for different distributions and releases, and you should also check if there are
more up to date instructions for the Ubuntu distribution as well.

.. i18n: Installation of Open ERP from packages
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installation of Open ERP from packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: At the time of writing this book, Ubuntu hadn't yet published packages for Open ERP, so this
.. i18n: section describes the installation of version 4.2 of Tiny ERP. This is very similar to Open ERP and
.. i18n: so can be used to test the software.

At the time of writing this book, Ubuntu hadn't yet published packages for Open ERP, so this
section describes the installation of version 4.2 of Tiny ERP. This is very similar to Open ERP and
so can be used to test the software.

.. i18n: Here's a summary of the procedure:

Here's a summary of the procedure:

.. i18n: #. Start Synaptic Package Manager, and enter your root password as required.
.. i18n: 
.. i18n: #. Check that the repositories \ ``main``\   \ ``universe``\  and \ ``restricted``\  are enabled.
.. i18n: 
.. i18n: #. Search for a recent version of PostgreSQL, for example \ ``postgresql-8.3``\ then select it for
.. i18n:    installation along with its dependencies.
.. i18n: 
.. i18n: #. Search for \ ``tinyerp``\  then select \ ``tinyerp-client``\  and \ ``tinyerp-server``\  for
.. i18n:    installation along with their dependencies. Click :guilabel:`Update Now` to install it all.
.. i18n: 
.. i18n: #. Close Synaptic Package Manager.

#. Start Synaptic Package Manager, and enter your root password as required.

#. Check that the repositories \ ``main``\   \ ``universe``\  and \ ``restricted``\  are enabled.

#. Search for a recent version of PostgreSQL, for example \ ``postgresql-8.3``\ then select it for
   installation along with its dependencies.

#. Search for \ ``tinyerp``\  then select \ ``tinyerp-client``\  and \ ``tinyerp-server``\  for
   installation along with their dependencies. Click :guilabel:`Update Now` to install it all.

#. Close Synaptic Package Manager.

.. i18n: Installing PostgreSQL results in a database server that runs and restarts automatically when the PC
.. i18n: is turned on. If all goes as it should with the tinyerp-server package then tinyerp-server will also
.. i18n: install, and restart automatically when the PC is switched on.

Installing PostgreSQL results in a database server that runs and restarts automatically when the PC
is turned on. If all goes as it should with the tinyerp-server package then tinyerp-server will also
install, and restart automatically when the PC is switched on.

.. i18n: Start the Tiny/Open ERP GTK client by clicking its icon in the :menuselection:`Applications`  menu,
.. i18n: or by opening a terminal window and typing \ ``tinyerp-client``\  . The Open ERP login dialog box
.. i18n: should open and show the message :guilabel:`No database found you must create one!`.

Start the Tiny/Open ERP GTK client by clicking its icon in the :menuselection:`Applications`  menu,
or by opening a terminal window and typing \ ``tinyerp-client``\  . The Open ERP login dialog box
should open and show the message :guilabel:`No database found you must create one!`.

.. i18n: Although this installation method is simple and therefore an attractive option, it's better to
.. i18n: install Open ERP using a version downloaded from http://openerp.com. The downloaded revision is
.. i18n: likely to be far more up to date than that available from a Linux distribution.

Although this installation method is simple and therefore an attractive option, it's better to
install Open ERP using a version downloaded from http://openerp.com. The downloaded revision is
likely to be far more up to date than that available from a Linux distribution.

.. i18n: .. note:: Package versions
.. i18n: 
.. i18n: 	Maintaining packages is a process of development, testing and publication that takes time. The
.. i18n: 	releases in Open ERP (or Tiny ERP) packages are therefore not always the latest available. Check
.. i18n: 	the version number from the information on the website before installing a package. If only the
.. i18n: 	third digit group differs (for example 5.0.1 instead of 5.0.2) then you may decide to install it because
.. i18n: 	the differences may be minor – fault fixes rather than functionality changes between the package
.. i18n: 	and the latest version.

.. note:: Package versions

	Maintaining packages is a process of development, testing and publication that takes time. The
	releases in Open ERP (or Tiny ERP) packages are therefore not always the latest available. Check
	the version number from the information on the website before installing a package. If only the
	third digit group differs (for example 5.0.1 instead of 5.0.2) then you may decide to install it because
	the differences may be minor – fault fixes rather than functionality changes between the package
	and the latest version.

.. i18n: Manual installation of the Open ERP server
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Manual installation of the Open ERP server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: In this section you'll see how to install Open ERP by downloading it from the site
.. i18n: http://openerp.com, and how to install the libraries and packages that Open ERP depends on, onto a
.. i18n: desktop version of Ubuntu. Here's a summary of the procedure:

In this section you'll see how to install Open ERP by downloading it from the site
http://openerp.com, and how to install the libraries and packages that Open ERP depends on, onto a
desktop version of Ubuntu. Here's a summary of the procedure:

.. i18n: #. Navigate to the page http://openerp.com with your web browser,
.. i18n: 
.. i18n: #. Click :menuselection:`Downloads` on the left menu,
.. i18n: 
.. i18n: #. Download the client and server files from the *Sources (Linux)* section into your home directory
.. i18n:    (or some other location if you've defined a different download area).

#. Navigate to the page http://openerp.com with your web browser,

#. Click :menuselection:`Downloads` on the left menu,

#. Download the client and server files from the *Sources (Linux)* section into your home directory
   (or some other location if you've defined a different download area).

.. i18n: To download the PostgreSQL database and all of the other dependencies for Open ERP from packages:

To download the PostgreSQL database and all of the other dependencies for Open ERP from packages:

.. i18n: #. Start Synaptic Package Manager, and enter the root password as required.
.. i18n: 
.. i18n: #. Check that the repositories \ ``main``\   \ ``universe``\  and \ ``restricted``\  are enabled.
.. i18n: 
.. i18n: #. Search for a recent version of PostgreSQL (such as \ ``postgresql-8.3``\   then select it for
.. i18n:    installation along with its dependencies.
.. i18n: 
.. i18n: #. Select all of Open ERP's dependences, an up-to-date list of which should be
.. i18n:    found in the installation documents on Tiny's website,
.. i18n:    then click :guilabel:`Update Now` to install them.

#. Start Synaptic Package Manager, and enter the root password as required.

#. Check that the repositories \ ``main``\   \ ``universe``\  and \ ``restricted``\  are enabled.

#. Search for a recent version of PostgreSQL (such as \ ``postgresql-8.3``\   then select it for
   installation along with its dependencies.

#. Select all of Open ERP's dependences, an up-to-date list of which should be
   found in the installation documents on Tiny's website,
   then click :guilabel:`Update Now` to install them.

.. i18n: .. index::
.. i18n:    single: Python

.. index::
   single: Python

.. i18n: .. note::  Python programming language
.. i18n: 
.. i18n: 	Python is the programming language that's been used to develop Open ERP. It's a dynamic, non-typed
.. i18n: 	language that is object-oriented, procedural and functional. It comes with numerous libraries that
.. i18n: 	provide interfaces to other languages and has the great advantage that it can be learnt in only a
.. i18n: 	few days. It's the language of choice for large parts of NASA's, Google's and many other
.. i18n: 	enterprises' code.
.. i18n: 
.. i18n: 	For more information on Python, explore http://www.python.org.

.. note::  Python programming language

	Python is the programming language that's been used to develop Open ERP. It's a dynamic, non-typed
	language that is object-oriented, procedural and functional. It comes with numerous libraries that
	provide interfaces to other languages and has the great advantage that it can be learnt in only a
	few days. It's the language of choice for large parts of NASA's, Google's and many other
	enterprises' code.

	For more information on Python, explore http://www.python.org.

.. i18n: Once all these dependencies and the database are installed, install the server itself using the
.. i18n: instructions on the website.

Once all these dependencies and the database are installed, install the server itself using the
instructions on the website.

.. i18n: Open a terminal window to start the server with the command \ ``sudo -i -u postgres 
.. i18n: openerp-server``\  , which should result in a series of log messages as the server starts up. If the server
.. i18n: is correctly installed, the message :guilabel:`[...] waiting for connections...` should show within 30
.. i18n: seconds or so, which indicates that the server is waiting for a client to connect to it.

Open a terminal window to start the server with the command \ ``sudo -i -u postgres 
openerp-server``\  , which should result in a series of log messages as the server starts up. If the server
is correctly installed, the message :guilabel:`[...] waiting for connections...` should show within 30
seconds or so, which indicates that the server is waiting for a client to connect to it.

.. i18n: .. figure:: images/terps_startup_log.png
.. i18n:    :align: center
.. i18n:    :scale: 90
.. i18n:    
.. i18n:    *Open ERP startup log in the console*

.. figure:: images/terps_startup_log.png
   :align: center
   :scale: 90
   
   *Open ERP startup log in the console*

.. i18n: .. index::
.. i18n:    single: client; GTK
.. i18n:    single: installation; GTK client

.. index::
   single: client; GTK
   single: installation; GTK client

.. i18n: Manual installation of Open ERP GTK clients
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Manual installation of Open ERP GTK clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: To install an Open ERP GTK client, follow the steps outline on the website installation document for
.. i18n: your particular operating system.

To install an Open ERP GTK client, follow the steps outline on the website installation document for
your particular operating system.

.. i18n: .. tip:: Survey: Don't Cancel!
.. i18n: 
.. i18n: 	When you start the GTK client for the first time, a dialog box appears asking for various details
.. i18n: 	that are intended to help the Tiny company assess the prospective user base for its software.
.. i18n: 
.. i18n: 	If you click the :guilabel:`Cancel` button, the window goes away – but Open ERP will ask the
.. i18n: 	same questions again next time you start the client. It's best to click :guilabel:`OK`, even if you
.. i18n: 	choose to enter no data, to prevent that window reappearing next time.

.. tip:: Survey: Don't Cancel!

	When you start the GTK client for the first time, a dialog box appears asking for various details
	that are intended to help the Tiny company assess the prospective user base for its software.

	If you click the :guilabel:`Cancel` button, the window goes away – but Open ERP will ask the
	same questions again next time you start the client. It's best to click :guilabel:`OK`, even if you
	choose to enter no data, to prevent that window reappearing next time.

.. i18n: .. figure:: images/terp_client_startup.png
.. i18n:    :align: center
.. i18n:    :scale: 75
.. i18n:    
.. i18n:    *Open ERP client at startup*

.. figure:: images/terp_client_startup.png
   :align: center
   :scale: 75
   
   *Open ERP client at startup*

.. i18n: Open a terminal window to start the client using the command openerp-client. When you start the
.. i18n: client on the same Linux PC as the server you'll find that the default connection parameters will
.. i18n: just work without needing any change. The message :guilabel:`No database found, you must create
.. i18n: one!`  shows you that the connection to the server has been successful and you need to create a
.. i18n: database on the server.

Open a terminal window to start the client using the command openerp-client. When you start the
client on the same Linux PC as the server you'll find that the default connection parameters will
just work without needing any change. The message :guilabel:`No database found, you must create
one!`  shows you that the connection to the server has been successful and you need to create a
database on the server.

.. i18n: Creating the database
.. i18n: ^^^^^^^^^^^^^^^^^^^^^

Creating the database
^^^^^^^^^^^^^^^^^^^^^

.. i18n: You can connect other GTK clients over the network to your Linux server. Before you leave your
.. i18n: server, make sure you know its network address – either by its name (such as \
.. i18n: ``mycomputer.mycompany.net``\  ) or its IP address (such as \ ``192.168.0.123``\  ).

You can connect other GTK clients over the network to your Linux server. Before you leave your
server, make sure you know its network address – either by its name (such as \
``mycomputer.mycompany.net``\  ) or its IP address (such as \ ``192.168.0.123``\  ).

.. i18n: .. index::
.. i18n:    single: port (network)

.. index::
   single: port (network)

.. i18n: .. note:: Different networks
.. i18n: 
.. i18n: 	Communications between an Open ERP client and server are based on standard protocols. You can
.. i18n: 	connect Windows clients to a Linux server, or vice versa, without problems. It's the same for Mac
.. i18n: 	versions of Open ERP – you can connect Windows and Linux clients and servers to them.

.. note:: Different networks

	Communications between an Open ERP client and server are based on standard protocols. You can
	connect Windows clients to a Linux server, or vice versa, without problems. It's the same for Mac
	versions of Open ERP – you can connect Windows and Linux clients and servers to them.

.. i18n: To install an Open ERP client on a computer under Linux, repeat the procedure shown earlier in this
.. i18n: section. You can connect different clients to the Open ERP server by modifying the connection
.. i18n: parameters on each client. To do that, click the :guilabel:`Change` button on the connection dialog
.. i18n: and set the following field as needed:

To install an Open ERP client on a computer under Linux, repeat the procedure shown earlier in this
section. You can connect different clients to the Open ERP server by modifying the connection
parameters on each client. To do that, click the :guilabel:`Change` button on the connection dialog
and set the following field as needed:

.. i18n: *  :guilabel:`Server` : \ ``name``\   or  \ ``IP address``\   of the server over the network,
.. i18n: 
.. i18n: *  :guilabel:`Port` : the port, whose default is \ ``8069``\   or  \ ``8070``\ ,
.. i18n: 
.. i18n: *  :guilabel:`Connection protocol` : \ ``XML-RPC``\   or  \ ``NET-RPC``\  .

*  :guilabel:`Server` : \ ``name``\   or  \ ``IP address``\   of the server over the network,

*  :guilabel:`Port` : the port, whose default is \ ``8069``\   or  \ ``8070``\ ,

*  :guilabel:`Connection protocol` : \ ``XML-RPC``\   or  \ ``NET-RPC``\  .

.. i18n: .. figure:: images/terp_client_server.png
.. i18n:    :align: center
.. i18n:    :scale: 75
.. i18n: 
.. i18n:    *Dialog box for defining connection parameters to the server*

.. figure:: images/terp_client_server.png
   :align: center
   :scale: 75

   *Dialog box for defining connection parameters to the server*

.. i18n: It's possible to connect the server to the client using a secure protocol to prevent other network
.. i18n: users from listening in, but the installation described here is for direct unencrypted connection.

It's possible to connect the server to the client using a secure protocol to prevent other network
users from listening in, but the installation described here is for direct unencrypted connection.

.. i18n: If your Linux server is protected by a firewall you'll have to provide access to port 
.. i18n:  \ ``8069``\ or \ ``8070``\ for users on other computers with Open ERP GTK clients.

If your Linux server is protected by a firewall you'll have to provide access to port 
 \ ``8069``\ or \ ``8070``\ for users on other computers with Open ERP GTK clients.

.. i18n: .. index::
.. i18n:    single: installation; eTiny web server
.. i18n:    single: installation; Open ERP client-web server

.. index::
   single: installation; eTiny web server
   single: installation; Open ERP client-web server

.. i18n: Installation of an Open ERP web server
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installation of an Open ERP web server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: Just as you installed a GTK client on a Linux server, you can also install the Open ERP client-web
.. i18n: server.
.. i18n: You can install it from sources after installing its dependencies from packages as you did
.. i18n: with the Open ERP server,
.. i18n: but Tiny have provided a simpler way to do this for eTiny – using a system known as ez_setup.

Just as you installed a GTK client on a Linux server, you can also install the Open ERP client-web
server.
You can install it from sources after installing its dependencies from packages as you did
with the Open ERP server,
but Tiny have provided a simpler way to do this for eTiny – using a system known as ez_setup.

.. i18n: Before proceeding, confirm that your Open ERP installation is functioning correctly with a GTK
.. i18n: client.
.. i18n: If it's not you'll need to go back now and fix it, because you need to be able to use it fully for
.. i18n: the next stages.

Before proceeding, confirm that your Open ERP installation is functioning correctly with a GTK
client.
If it's not you'll need to go back now and fix it, because you need to be able to use it fully for
the next stages.

.. i18n: To install client-web follow the up-to-date instructions in the installation document on the website.

To install client-web follow the up-to-date instructions in the installation document on the website.

.. i18n: .. note:: Ez tool
.. i18n: 
.. i18n: 	Ez is the packaging system used by Python. It enables the installation of programs as required just
.. i18n: 	like the packages used by a Linux distribution. The software is downloaded across the network and
.. i18n: 	installed on your computer by ez_install.
.. i18n: 
.. i18n: 	:program:`ez_setup` is a small program that installs ez_install automatically.

.. note:: Ez tool

	Ez is the packaging system used by Python. It enables the installation of programs as required just
	like the packages used by a Linux distribution. The software is downloaded across the network and
	installed on your computer by ez_install.

	:program:`ez_setup` is a small program that installs ez_install automatically.

.. i18n: The Open ERP Web server connects to the Open ERP server in the same way as an Open ERP client
.. i18n: using the NET-RPC protocol. Its default setup corresponds to that of the Open ERP server
.. i18n: you've just installed, so should connect directly at startup.

The Open ERP Web server connects to the Open ERP server in the same way as an Open ERP client
using the NET-RPC protocol. Its default setup corresponds to that of the Open ERP server
you've just installed, so should connect directly at startup.

.. i18n: #.	At the same console as you've just been using, go to the Openerp web directory by typing
.. i18n: 	:command:`cd openerp-web-5.X`.
.. i18n: 
.. i18n: #. At a terminal window type :command:`start-openerp-web` to start the Open ERP Web server.

#.	At the same console as you've just been using, go to the Openerp web directory by typing
	:command:`cd openerp-web-5.X`.

#. At a terminal window type :command:`start-openerp-web` to start the Open ERP Web server.

.. i18n: .. _fig-webwel:
.. i18n: 
.. i18n: .. figure:: images/web_welcome.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Open ERP web client at startup*
.. i18n:    
.. i18n: You can verify the installation by opening a web browser on the server and navigating to
.. i18n: http://localhost:8080 to connect to eTiny as shown in the figure :ref:`fig-webwel`. 
.. i18n: You can also test this from
.. i18n: another computer connected to the same network if you know the name or IP address of the server over
.. i18n: the network – your browser should be set to http://<server_address>:8080 for this.

.. _fig-webwel:

.. figure:: images/web_welcome.png
   :scale: 75
   :align: center

   *Open ERP web client at startup*
   
You can verify the installation by opening a web browser on the server and navigating to
http://localhost:8080 to connect to eTiny as shown in the figure :ref:`fig-webwel`. 
You can also test this from
another computer connected to the same network if you know the name or IP address of the server over
the network – your browser should be set to http://<server_address>:8080 for this.

.. i18n: Verifying your Linux installation
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Verifying your Linux installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: .. index::
.. i18n:    single: pgAdmin III

.. index::
   single: pgAdmin III

.. i18n: You've used default parameters so far during the installation of the various components.
.. i18n: If you've had problems, or you just want to set this up differently,
.. i18n: the following points provide some indicators about how you can set your installation up.

You've used default parameters so far during the installation of the various components.
If you've had problems, or you just want to set this up differently,
the following points provide some indicators about how you can set your installation up.

.. i18n: .. tip:: **psql** and **pgAdmin** tools
.. i18n: 
.. i18n: 	psql is a simple client, executed from the command line, that's delivered with PostgreSQL. It
.. i18n: 	enables you to execute SQL commands on your Open ERP database.
.. i18n: 
.. i18n: 	If you prefer a graphical utility to manipulate your database directly you can install pgAdmin III
.. i18n: 	(it is commonly installed automatically with PostgreSQL on a windowing system, but can also be
.. i18n: 	found at \ ``http://www.pgadmin.org/`` \ ).

.. tip:: **psql** and **pgAdmin** tools

	psql is a simple client, executed from the command line, that's delivered with PostgreSQL. It
	enables you to execute SQL commands on your Open ERP database.

	If you prefer a graphical utility to manipulate your database directly you can install pgAdmin III
	(it is commonly installed automatically with PostgreSQL on a windowing system, but can also be
	found at \ ``http://www.pgadmin.org/`` \ ).

.. i18n: #.	The PostgreSQL database starts automatically and listens locally on port 5432 as standard: check
.. i18n: 	this by entering \ ``sudo netstat -anpt``\  at a terminal to see if port 5432 is visible there.
.. i18n: 
.. i18n: #.	The database system has a default role of \ ``postgres``\   accessible by running under the Linux
.. i18n: 	postgres user: check this by entering \ ``sudo su postgres -c psql``\  at a terminal to see the psql
.. i18n: 	startup message – then type \ ``\q``\  to quit the program.
.. i18n: 
.. i18n: #.	Start the Open ERP server from the postgres user (which enables it to access the PostgreSQL
.. i18n: 	database) by typing \ ``sudo su postgres -c tinyerp-server.``\
.. i18n: 
.. i18n: #.	If you try to start the Open ERP server from a terminal but get the message ``socket.error: (98,
.. i18n: 	'Address already in use')`` then you might be trying to start Open ERP while an instance of
.. i18n: 	Open ERP is already running and using the sockets that you've defined (by default 8069 and 8070).
.. i18n: 	If that's a surprise to you then you may be coming up against a previous installation of Open ERP
.. i18n: 	or Tiny ERP, or something else using one or both of those ports. 
.. i18n: 	
.. i18n: 	Type \ ``sudo netstat -anpt``\  to
.. i18n: 	discover what is running there, and record the PID. You can check that the PID orresponds to a
.. i18n: 	program you can dispense with by typing \ ``ps aux | grep <PID>``\   and you can then stop the
.. i18n: 	program from running by typing \ ``sudo kill <PID>``\ .  You need additional measures to stop it from
.. i18n: 	restarting when you restart the server.
.. i18n: 
.. i18n: #.	The Open ERP server has a large number of configuration options. You can see what they are by
.. i18n: 	starting the server with the argument \ ``–help``\   By efault the server configuration is stored
.. i18n: 	in the file \ ``.terp_serverrc``\  in the user's home directory (and for the postgres user that
.. i18n: 	directory is \ ``/var/lib/postgresql``\  .
.. i18n: 
.. i18n: #.	You can delete the configuration file to be quite sure that the Open ERP server is starting with
.. i18n: 	just the default options. It is quite common for an upgraded system to behave badly because a new
.. i18n: 	version server cannot work with options from a previous version. When the server starts without a
.. i18n: 	configuration file it will write a new one once there is something non-default to write to it – it
.. i18n: 	will operate using defaults until then.
.. i18n: 
.. i18n: #.	To verify that the system works, without becoming entangled in firewall problems, you can start
.. i18n: 	the Open ERP client from a second terminal window on the server computer (which doesn't pass
.. i18n: 	through the firewall). Connect using the XML-RPC protocol on port 8069 or NET-RPC on port 8070. The
.. i18n: 	server can use both ports simultaneously. The window displays the log file when the client is
.. i18n: 	started this way.
.. i18n: 
.. i18n: #.	The client setup is stored in the file \ ``.terprc``\  in the user's home directory.
.. i18n: 	Since a GTK client can be started by any user, each user would have their setup defined in a
.. i18n: 	configuration file in their own home directory.
.. i18n: 
.. i18n: #.	You can delete the configuration file to be quite sure that the Open ERP client is starting with
.. i18n: 	just the default options. When the client starts without a configuration file it will write a new
.. i18n: 	one for itself.
.. i18n: 
.. i18n: #.	The web server uses the NET-RPC protocol. If a GTK client works but the web server doesn't then the
.. i18n: 	problem is either with the NET-RPC port or with the web server itself, and not with the Open ERP server.

#.	The PostgreSQL database starts automatically and listens locally on port 5432 as standard: check
	this by entering \ ``sudo netstat -anpt``\  at a terminal to see if port 5432 is visible there.

#.	The database system has a default role of \ ``postgres``\   accessible by running under the Linux
	postgres user: check this by entering \ ``sudo su postgres -c psql``\  at a terminal to see the psql
	startup message – then type \ ``\q``\  to quit the program.

#.	Start the Open ERP server from the postgres user (which enables it to access the PostgreSQL
	database) by typing \ ``sudo su postgres -c tinyerp-server.``\

#.	If you try to start the Open ERP server from a terminal but get the message ``socket.error: (98,
	'Address already in use')`` then you might be trying to start Open ERP while an instance of
	Open ERP is already running and using the sockets that you've defined (by default 8069 and 8070).
	If that's a surprise to you then you may be coming up against a previous installation of Open ERP
	or Tiny ERP, or something else using one or both of those ports. 
	
	Type \ ``sudo netstat -anpt``\  to
	discover what is running there, and record the PID. You can check that the PID orresponds to a
	program you can dispense with by typing \ ``ps aux | grep <PID>``\   and you can then stop the
	program from running by typing \ ``sudo kill <PID>``\ .  You need additional measures to stop it from
	restarting when you restart the server.

#.	The Open ERP server has a large number of configuration options. You can see what they are by
	starting the server with the argument \ ``–help``\   By efault the server configuration is stored
	in the file \ ``.terp_serverrc``\  in the user's home directory (and for the postgres user that
	directory is \ ``/var/lib/postgresql``\  .

#.	You can delete the configuration file to be quite sure that the Open ERP server is starting with
	just the default options. It is quite common for an upgraded system to behave badly because a new
	version server cannot work with options from a previous version. When the server starts without a
	configuration file it will write a new one once there is something non-default to write to it – it
	will operate using defaults until then.

#.	To verify that the system works, without becoming entangled in firewall problems, you can start
	the Open ERP client from a second terminal window on the server computer (which doesn't pass
	through the firewall). Connect using the XML-RPC protocol on port 8069 or NET-RPC on port 8070. The
	server can use both ports simultaneously. The window displays the log file when the client is
	started this way.

#.	The client setup is stored in the file \ ``.terprc``\  in the user's home directory.
	Since a GTK client can be started by any user, each user would have their setup defined in a
	configuration file in their own home directory.

#.	You can delete the configuration file to be quite sure that the Open ERP client is starting with
	just the default options. When the client starts without a configuration file it will write a new
	one for itself.

#.	The web server uses the NET-RPC protocol. If a GTK client works but the web server doesn't then the
	problem is either with the NET-RPC port or with the web server itself, and not with the Open ERP server.

.. i18n: .. 	hint:: One server for several companies
.. i18n: 
.. i18n: 	You can start several Open ERP application servers on one physical computer server by using
.. i18n: 	different ports. If you have defined multiple database roles in PostgreSQL, each connected through
.. i18n: 	an Open ERP instance to a different port, you can simultaneously serve many companies from one
.. i18n: 	physical server at one time.

.. 	hint:: One server for several companies

	You can start several Open ERP application servers on one physical computer server by using
	different ports. If you have defined multiple database roles in PostgreSQL, each connected through
	an Open ERP instance to a different port, you can simultaneously serve many companies from one
	physical server at one time.

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
