

Installation and Configuration
###############################



Summary

* The architecture of Open ERP

* Installing the software

* Configuring a database

Keywords

* downloading

* installation

* SaaS

* database server

* application server

* web server

* GTK client

* web client

* backups

 *Installing Open ERP under Windows or Linux for familiarization use should take you only half an hour or so and needs only a couple of operations. The first operation is installation of the application and database server on a server PC (that's a Windows or Linux or Macintosh computer). You've a choice of approaches for the second operation: either install a web server (most probably on the original server PC) to use with standard web clients that can be found on anybody's PC, or install application clients on each intended user's PC. When you first install Open ERP you'll configure a database containing a little functionality and some demonstration data to test the installation.* 


	.. image:: images/ch1_outline.png

This chapter focuses on the installation of Open ERP so that you can begin to familiarize yourselves with its use. If you're not a systems administrator, or if you've already installed Open ERP, or if you're planning to use an online SaaS provider, then you can skip this chapter and move straight to Chapter 2. If you've already used Open ERP (or Tiny ERP) a bit then you can move past that to Chapter 3 in this section of the book.

.. tip::   **Reminder**  *Renaming from Tiny ERP to Open ERP* 



	Tiny ERP was renamed to Open ERP early in 2008 so somebody who's already used Tiny ERP should be equally at home with Open ERP. The two names refer to the same software, so there's no functional difference between versions 4.2.X of Open ERP and 4.2.X of Tiny ERP. This book applies to all versions of Tiny ERP and Open ERP from 4.2.0 onwards, with references to specific later versions from time to time. 

.. tip::   **Advice**  *The SaaS, or “on-demand”, offer* 



	SaaS (Software as a Service) is delivered by a hosting supplier and paid in the form of a monthly subscription that includes hardware (servers), system maintenance, provision of hosting services, and support.

	You can get a month's free trial on http://ondemand.openerp.com, which enables you to get started quickly without incurring costs for integration or for buying computer systems. Many of Tiny's partner companies will access this, and some may offer their own similar service.

	This service should be particularly useful to small companies that just want to get going quickly and at low cost. It gives them immediate access to an integrated management system that's been built on the type of enterprise architecture used in banks and other large organizations. Open ERP is that system, and is described in detail throughout this book.

Whether you want to test Open ERP or to put it into full production, you have at least two starting points:

* evaluate it on line at  and ask for an SaaS trial hosted at , or the equivalent service at any of Tiny's partner companies,

* install it on your own computers to test it in your company's systems environment.

There are some differences between installing Open ERP on Windows and on Linux systems, but once installed, it gives the same functions from both so you won't generally be able to tell which type of server you're using.

.. tip::   **Alternative**  *Linux, Windows, Mac* 



	Although this book deals only with installation on Windows and Linux systems, the same versions are also available for the Macintosh on the official website of Open ERP.

.. tip::   **URL**  *Web sites for Open ERP* 



	* Main Site: http://openerp.com 

	* SaaS or “on-demand” Site: http://ondemand.openerp.com

	* Community discussion forum where you can often receive informed assistance: http://openerp.com/forum/

.. tip::   **Note**  *Current documentation* 



	The procedure for installing Open ERP and its web server are sure to change and improve with each new version, so you should always check each release's documentation – both packaged with the release and on the website – for exact installation procedures.

Once you've completed this installation, you'll create and configure a database to confirm that your Open ERP installation is working.

The architecture of Open ERP
=============================

To access Open ERP you can:

* use a web browser pointed at the eTiny web server, or

* use an application client (the GTK client) installed on each computer.

The two methods of access give very similar facilities, and you can use both on the same server at the same time. It's best to use the web browser if the Open ERP server is some distance away (such as on another continent) because it's more tolerant of time delays between the two than the GTK client is. The web client is also easier to maintain, because it's generally already installed on users' computers.

Conversely you'd be better off with the application client (called the GTK client because of the technology it's built with) if you're using a local server (such as in the same building). In this case the GTK client will be more responsive, so more satisfying to use.

.. tip::   **Usability**  *Web client and GTK client* 



	The main functional difference between the two Open ERP clients is the presence of the calendar view in the web client, which doesn't exist in the GTK client at present (version 4.2.3). Apart from that you will find that there are small differences in their general usability.

	The Tiny company will continue to support two clients for the foreseeable future, so you can use whichever client you prefer.

An Open ERP system is formed by three main components:

* the PostgreSQL database server, which contains all of the databases, each of which contains all data and most elements of the Open ERP system configuration,

* the Open ERP application server, which contains all of the enterprise logic and ensures that Open ERP runs optimally,

* the web server, a separate application called eTiny, which enables you to connect to Open ERP from standard web browsers and is not needed when you connect using a GTK client.


	.. image:: images/terp_arch_1.png

.. tip::   **Terminology**  *eTiny – server or client?* 



	The eTiny component can be thought of as a server or a client depending on your viewpoint.

	It acts as a web server to an end user connecting from a web browser, but it also acts as a client to the Open ERP application server just as a GTK application client does.

	So in this book its context will determine whether eTiny is referred to as a server or a client.

.. tip::   **Attention**  *eTiny* 



	At present, the web component is known as “eTiny”. Although it's possible that this application's name will change in the coming months to match the renaming of Tiny ERP to Open ERP, its characteristics will stay the same.

.. tip::   **Program**  *PostgreSQL* 



	PostgreSQL is a relational and object database management system.

	It's a free high-performance system that compares with other database management systems such as MySQL and FirebirdSQL (both free), Sybase, DB2 and Microsoft SQL Server (all proprietary). It runs on all types of Operating System, from Unix/Linux to the various releases of Windows, via Mac OS X, Solaris, SunOS and BSD.

These three components can be installed on the same server or can be distributed onto separate computer servers if performance considerations require it.

If you choose to run only with GTK clients you won't need the third component – the eTiny server – at all. In this case Open ERP's GTK client must be installed on the workstation of each Open ERP user in the company.

The installation of Open ERP
=============================

Whether you're from a small company investigating how Open ERP works, or on the IT staff of a larger organization and have been asked to assess Open ERP's capabilities, your first requirement is to install it or to find a working installation.

The table below summarizes the various installation methods that will be described in the following sections.




 .. csv-table:: Comparison of the different methods of installation on Windows or Linux.
   :header: "Method","Average Time","Level of Complexity","Notes"
   :widths: 20, 15, 10,30

   "All-in-one Windows Installer","A few minutes","Simple","Very useful for quick evaluations because it installs all of the components pre-configured on one computer (using the GTK client)."
   "Independent installation on Windows","Half an hour","Medium","Enables you to install the components on different computers. Can be put into production use."
   "Ubuntu Linux packages","A few minutes","Simple","Simple and quick but the Ubuntu packages aren't always up to date."
   "From source, for all Linux systems","More than half an hour","Medium to slightly difficult","This is the method recommended for production environments because it's easy to keep it up to date."
   
   
   

Each time a new release of Open ERP is made, Tiny supplies a complete Windows auto-installer for it. This contains all of the components you need – the PostgreSQL database server, the Open ERP application server and the GTK application client.

This auto-installer enables you to install the whole system in just a few mouse-clicks. The initial configuration is set up during installation, making it possible to start using it very quickly as long as you don't want to change the underlying code. It's aimed at the installation of everything on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as well.

The first step is to download the Open ERP installer. At this stage you must choose which version to install – the stable version or the development version. If you're planning to put it straight into production you're strongly advised to choose the stable version.

.. tip::   **Attention**  *Stable versions and development versions* 



	Open ERP development proceeds on two parallel tracks: stable versions and development versions.

	New functionality is integrated into the development branch. This branch is more advanced than the stable branch, but it can contain undiscovered and unfixed faults. A new development release is made every month or so, and Tiny have made the code repository available so you can download the very latest revisions if you want.

	The stable branch is designed for production environments. Releases of new functionality there are made only about once a year after a long period of testing and validation. Only fault fixes are released through the year on the stable branch.

To download the version of Open ERP for Windows, follow these steps:

Navigate to the site http://openerp.com.

Click Product on the menu at the left, then Download.

Click in the downloads page – either on development or stable, depending which you want to install.

Click win32 to open the download page for Windows files.

Download the file for the demonstration version – for example openerp-allinone-setup-4.2.X.exe.

	#. Save the file on your PC.

To install Open ERP and its database you must be signed in as an Administrator on your PC. Double-click the installer file and accept the default parameters on each dialog box this way:

	#. Run the installer.

	#. Start the installation procedure by clicking  *Next* in the installation window.

	#. Accept the GPL license by clicking  *I Agree* 

	#. Install Open ERP in the location in \ ``Program Files ``\  hat is suggested by the installer.

	#. Wait two or three minutes for the installation to complete, then click  *Next* 

	#. Close the installation window using the middle button,  *Finish* 

The Open ERP client can then be opened, ready to use the Open ERP system. The next step consists of configuring the database, and is covered in the final section of this chapter, *Creating the database.*


Independent installation on Windows
-------------------------------------

System administrators can have very good reasons for wanting to install the various components of a Windows installation separately. For example, your company may not support the version of PostgreSQL or Python that's installed automatically, or you may already have PostgreSQL installed on the server you're using, or you may want to install the database server, application server and web server on separate hardware units. 

For this situation you can get separate installers for the Open ERP server and client from the same location as the all-in-one autoinstaller. You'll also have to download and install a suitable version of PostgreSQL independently. 

You must install PostgreSQL before the Open ERP server, and you must also configure it with a user and password so that the Open ERP server can connect to it. Tiny's web-based documentation gives full and current details.

If you had previously tried to install the all-in-one version of Open ERP, you'd best uninstall that in case its embedded PostgreSQL installation interferes with your stand-alone installation.

Connecting users on other PCs to the Open ERP server
-----------------------------------------------------

To connect other computers to the Open ERP server you must configure the server so that it's visible to the other PCs, and install a GTK client on each of the those PCs:

	#. Make your Open ERP server visible to other PCs by opening the Windows Firewall in the Control Panel, hen asking the firewall to make an exception of the Open ERP server. In the  *Exceptions* tab of Windows Firewall click on  *Add a program...* and choose  *Open ERP Server* in the list provided. This step enables other computers to see the Open ERP application on this server.

	#. Install the Open ERP client (\ ``openerp-client-4.X.exe``\  , which you can download in the same way as you downloaded the other Open ERP software, onto the other PCs.

.. tip::   **Attention**  *Version matching* 



	You must make sure that the version of the client matches that of the server. The version number is given as part of the name of the downloaded file. Although it's possible that some different revisions of client and server will function together, there's no certainty about that.

To run the client installer on every other PC you'll need to have administrator rights there. The installation is automated, so you just need to guide it through its different installation steps.

To test your installation, start by connecting through the Open ERP client on the server machine while you're still logged in as administrator. 

.. tip::   **Note**  *Why signed in as a PC Administrator?* 



	You'd not usually be signed on as a PC administrator when you're just running the Open ERP client, but if there have been problems in the installation it's easier to remain as an administrator after the installation so that you can make any necessary fixes than to switch user as you alternate between roles as a tester and a software installer.

Start the GTK client on the server through the Windows Start menu there. The main client window appears, identifying the server you're connected to (which is \ ``localhost``\   – your own server PC – by default). If the message  *No database found, you must create one*  appears then you've successfully connected to an Open ERP server containing, as yet, no databases.


	.. image:: images/new_login_dlg.png

.. tip::   **Note**  *Connection modes* 



	In its default configuration, the Open ERP client connects to port 8069 on the server using the XML-RPC protocol. You can change this and connect to port 8070 using the NET-RPC protocol instead. NET-RPC is quite a bit quicker, although you may not notice that on the GTK client in normal use.

Resolving errors with a Windows installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your system doesn't work after installing your Windows system you'll find some ideas for resolving this below:

	#. Does your PostgreSQL server work? Signed in as administrator, select  *Stop Service* from the menu  *Start > Programs > PostgreSQL*  If, after a couple of seconds, you can read  *The service PostgreSQL4OpenERP has stopped* then you can be reasonably sure that the database server was working. Restart PostgreSQL then, still in the PostgreSQL menu, start the pgAdmin III application which you can use to explore the database. Double-click on the \ ``PostgreSQL4OpenERP``\  connection as in the figure below. If the database server is working you'll be able to see some information about the empty database. If it's not then an error message will appear.

                .. image:: images/pgadmin_window.png

                *Using pgAdmin III to verify that PostgreSQL is working*
                

	#. Is the Open ERP application working? Signed in to the server as an administrator, stop and restart the service using  *Stop Service* and  *Start Service* from the menu  *Start > Programs > OpenERP Server*  Open the log file \ ``openerp-server.log``\  in \ ``C:\Program Files\OpenERP Server``\   At the end of the file you should see the line  *The server is running, waiting for connections...* 

.. tip::   **Note**  *Automatically starting the server* 



	You might find that the server has not started automatically after installation. If this is the case you should restart your computer to ensure that the service is properly registered. You'll only have to do this once. Once registered the server should restart correctly every time.

	#. Is the Open ERP application server configured correctly? Signed in to the server as Administrator, open the file \ ``openerp-server.conf``\  in \ ``C:\Program Files\OpenERP Server``\  and check its content. This file is generated during installation with information derived from the database. If you see something strange it's best to entirely reinstall the server from the demonstration installer rather than try to work out what's happening.


	        .. image:: images/terp_server_conf.png

	#. Are your client programs correctly installed? If your Open ERP GTK clients haven't started then the swiftest approach is to reinstall them.


	        .. image:: images/cmd_prompt_ping.png

	#. Can the client computers see the server computer at all? Check this by opening a command prompt window (enter \ ``cmd``\  in the window  *Start > Run...* ) and enter \ ``ping <address of server>``\  there (where \ ``<address of server>``\  represents he IP address of the server). The server should respond as shown in the following figure.

	#. Have you changed any of the server's parameters? At this point in the installation the port number of the server must be 8069 using the protocol XML-RPC.

	#. Is there anything in the server's history that can help you identify the problem? Open the file \ ``openerp-server.log``\  in \ ``C:\Program Files\OpenERP Server``\  and scan through the history for ideas. If something looks strange there, contributors to the Open ERP forums can often help identify the reason.

Installation on Linux (Ubuntu)
-------------------------------

This section guides you through installing the Open ERP server and client on Ubuntu, one of the most popular Linux distributions. It assumes that you're using a recent release of Desktop Ubuntu with its graphical user interface on a desktop or laptop PC. 

.. tip::   **Alternative**  *Other Linux distributions* 



	Installation on other distributions of Linux is fairly similar to installation on Ubuntu. Read this section of the book so that you understand the principles, then use the online documentation and the forums for your specific needs on another distribution.

For information about installation on other distributions, visit the documentation section by following  *Product > Documentation*  on . Detailed instructions are given there for different distributions and releases, and you should also check if there are more up to date instructions for the Ubuntu as well.

Installation of Open ERP from packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At the time of writing this book, Ubuntu hadn't yet published packages for Open ERP, so this section describes the installation of version 4.2 of Tiny ERP. This is very similar to Open ERP and so can be used to test the software.

Here's a summary of the procedure:

	#. Start Synaptic Package Manager, and enter your root password as required.

	#. Check that the repositories \ ``main``\   \ ``universe``\  and \ ``restricted``\  are enabled.

	#. Search for a recent version of PostgreSQL, for example \ ``postgresql-8.3``\  (postgresql-8.3 didn't work fully with Tiny ERP 4.2.2, although it does with 4.2.3.3) then select it for installation along with its dependencies.

	#. Search for \ ``tinyerp``\  then select \ ``tinyerp-client``\  and \ ``tinyerp-server``\  for installation along with their dependencies. Click  *Update Now* to install it all.

	#. Close Synaptic Package Manager.

Installing PostgreSQL results in a database server that runs and restarts automatically when the PC is turned on. If all goes well with the tinyerp-server package then tinyerp-server will also install, and restart automatically when the PC is switched on.

Start the Tiny ERP GTK client by clicking its icon in the  *Applications*  menu, or by opening a terminal window and typing \ ``tinyerp-client``\  . The Tiny ERP login dialog box should open and show the message  *No database found you must create one!* 

Although this installation method is simple, and therefore attractive, it's better to install Open ERP using a version downloaded from . The downloaded revision is likely to be far more up to date than that available from a Linux distribution.

.. tip::   **Attention**  *Package versions* 



	Maintaining packages is a process of development, testing and publication that takes time. The releases in Open ERP (or Tiny ERP) packages are therefore not always the latest available. Check the version number from the information on the website before installing a package. If only the third figure differs (for example 4.2.3 instead of 4.2.4) then you may choose to install it because the differences may be minor – fault fixes rather than functionality changes between the package and the latest version.

Manual installation of the Open ERP server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this section you'll see how to install Open ERP by downloading it from the site , and how to install the libraries and packages that Open ERP depends on, onto a desktop version of Ubuntu. Here's a summary of the procedure:

	#. Navigate to the page with your web browser.

	#. Click  *Product* on the left menu, then  *Download* 

	#. Click  *development* or  *stable* in the list of downloads.

	#. Click  *source* to open the page of file downloads.

	#. Download the client and server files into your home directory (or some other location if you've defined a different download area).

To download the PostgreSQL database and all of the other dependencies for Open ERP from packages:

	#. Start Synaptic Package Manager, and enter the root password as required.

	#. Check that the repositories \ ``main``\   \ ``universe``\  and \ ``restricted``\  are enabled.

	#. Search for a recent version of PostgreSQL (such as \ ``postgresql-8.2``\   then select it for installation along with its dependencies.

	#. Select \ ``python-xml``\   \ ``python-libxml2``\   \ ``python-libxslt1``\   \ ``python-psycopg``\  (not \ ``psycopg2``\   and its dependencies, \ ``python-tz``\   \ ``python-imaging``\   \ ``python-pyparsing``\   \ ``python-reportlab``\   \ ``graphviz``\  and its dependences, \ ``python-matplotlib``\  and its ependences (some of which might already be installed), then click  *Update Now* to install them.

.. tip::   **Language**  *Python* 



	Python is the programming language that's been used to develop Tiny ERP and Open ERP. It's a dynamic, non-typed language that is at the same time object-oriented, procedural and functional. It comes with numerous libraries that provide interfaces to other languages and has the great advantage that it can be learnt in only a few days. It's the language of choice for large parts of NASA, Google and many other enterprises.

	For more information on Python, explore http://www.python.org.

Once all these dependencies and the database are installed, install the server itself by following the steps below:

	#. Open a terminal window and change directory to wherever you downloaded the server source files.

	#. Decompress the file using the command \ ``tar xzf openerp-server.4.X.tar.gz``\  

	#. Change directory: \ ``cd openerp-server``\  

	#. Build the Open ERP server: \ ``python setup.py build``\  

	#. Install the Open ERP server: \ ``sudo python setup.py install``\  

Open a terminal window to start the server with the command \ ``sudo su postgres -c openerp-server``\  , which should result in a series of log messages as the server starts up. If the server is correctly installed, the message  *waiting for connections... * should show within 30 seconds or so, which indicates that the server is waiting for a client to connect to it.


	.. image:: images/terps_startup_log.png

Manual installation of Open ERP GTK clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install an Open ERP GTK client, follow the steps below:

	#. Install the \ ``xpdf``\  package using Ubuntu's Synaptic Package Manager.

	#. Open a terminal and change directory to wherever you downloaded the client file.

	#. Decompress the file using the command: \ ``tar xzf openerp-client.4.X.tar.gz``\  

	#. Change directory: \ ``cd openerp-client``\  

	#. Build the Open ERP client: \ ``python setup.py build``\  

	#. Install the Open ERP client: \ ``sudo python setup.py install``\  

.. tip::   **Note**  *Survey: Don't Cancel!* 



	When you start the GTK client for the first time, a dialog box appears asking for various details that are intended to help the Tiny company assess the prospective user base for its software.

	If you click the Cancel button, the window goes away – but Open ERP will ask the same questions again next time you start the client. It's best to click OK, even if you choose to enter no data, to prevent that window reappearing next time.


	.. image:: images/terp_client_startup.png

Open a terminal window to start the client using the command openerp-client. When you start the client on the same Linux PC as the server you'll find that the default connection parameters will just work without needing any change. The message  *No database found, you must create one!*  shows you that the connection to the server has been successful and you need to create a database on the server.

Creating the database

You can connect other GTK clients over the network to your Linux server. Before you leave your server, make sure you know its network address – either by its name (such as \ ``mycomputer.mycompany.net``\  ) or its IP address (such as \ ``192.168.0.123``\  ).

.. tip::   **Note**  *Different networks* 



	Communications between an Open ERP client and server are based on standard protocols. You can connect Windows clients to a Linux server, or vice versa, without problems. It's the same for Mac versions of Open ERP – you can connect Windows and Linux clients and servers to them.

To install an Open ERP client on a computer under Linux, repeat the procedure shown earlier in this section. You can connect different clients to the Open ERP server by modifying the connection parameters on each client. To do that, click the Change button on the connection dialog and set the following field as needed:

*  *Server* : \ ``name``\   or \ ``IP address``\   of the server over the network,

*  *Port* : the port, whose default is \ ``8069``\  ,

*  *Connection protocol* : \ ``XML-RPC``\  .


	.. image:: images/terp_client_server.png

It's possible to connect the server to the client using a secure protocol to prevent other network users from listening in, but the installation described here is for direct unencrypted connection.

If your Linux server is protected by a firewall you'll have to provide access to port \ ``8069``\   for users on other computers with Open ERP GTK clients.

Installation of an eTiny web server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just as you installed a GTK client on a Linux server, you can also install the eTiny web server. It's possible to install eTiny from sources after installing its dependencies from packages as you did with the Open ERP server, but Tiny have provided a much simpler way to do this for eTiny – using a system known as ez_setup.

Before proceeding, confirm that your Open ERP installation is functioning correctly with a GTK client. If it's not you'll need to go back now and fix it, because you need to be able to use it fully for the next stages. 

To install eTiny:

	#. From Synaptic Package Manager install \ ``build-essential,``\  and then check that \ ``python-matplotlib``\  and \ ``python-imaging``\  are installed (which they should have been during the installation of the server).

	#. Now download the web framework directly to your download directory by entering: \ ``wget ``\  

	#. Run the installer using: \ ``python tgsetup.py``\  

	#. Finally, install eTiny by entering the command: \ ``sudo easy_install eTiny.``\  

.. tip::   **Tool**  *Ez* 



	Ez is the packaging system used by Python. It enables the installation of programs as required just like the packages used by a Linux distribution. The software is downloaded across the network and installed on your computer by ez_install.

	ez_setup is a small program that installs ez_install automatically.

The eTiny web server connects to the Open ERP server in the same way as an Open ERP client using the NET-RPC protocol. Its default configuration corresponds to that of the Open ERP server you've just installed, so should connect directly at startup.

	#. At the same console as you've just been using, go to the eTiny directory by typing \ ``cd etiny/trunk``\  .

	#. At a terminal window type \ ``python start-openerp.py``\  to start the eTiny server.


	.. image:: images/web_welcome.png

You can verify the installation by opening a web browser on the server and navigating to http://localhost:8080 to connect to eTiny as shown in the figure below. You can also test this from another computer connected to the same network if you know the name or IP address of the server over the network – your browser should be set to http://<server_address>:8080 for this.

Verifying your Linux installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You've used default parameters so far during the installation of the various components. If you've had problems, or you just want to set this up differently, the following points provide some indicators about how you can configure your installation.

.. tip::   **Tools**  *psql and pgAdmin* 



	psql is a simple client, executed from the command line, that's delivered with PostgreSQL. It enables you to execute SQL commands on your Open ERP database.

	If you prefer a graphical utility to manipulate your database directly you can install pgAdmin III (it is commonly installed automatically with PostgreSQL on a windowing system, but can also be found at http://www.pgadmin.org/). 

	#. The PostgreSQL database starts automatically and listens locally on port 5432 as standard: check this by entering \ ``sudo netstat -anpt ``\  t a terminal to see if port 5432 is visible there.

	#. The database system has a default role of \ ``postgres``\   accessible by running under the Linux postgres user: check this by entering \ ``sudo su postgres -c psql``\  at a terminal to see the psql startup message – then type \ ``\q``\  to quit the program.

	#. Start the Open ERP server from the postgres user (which enables it to access the PostgreSQL database) by typing \ ``sudo su postgres -c tinyerp-server.``\  

	#. If you try to start the Open ERP server from a terminal but get the message  *socket.error: (98, 'Address already in use')* then you might be trying to start Open ERP hile an instance of Open ERP is already running and using the sockets that you've defined (by default 8069 and 8070). If that's a surprise to you then you may be coming up against a previous installation of Open ERP or Tiny ERP, or something else sing one or both of those ports. Type \ ``sudo netstat -anpt``\  to discover what is running there, and record the PID. You can check that the PID orresponds to a program you can dispense with by typing \ ``ps aux | grep <PID>``\   and you can then stop the program from running by typing \ ``sudo kill <PID>``\   You need additional measures to stop it from restarting when you restart the server.

	#. The Open ERP server has a large number of configuration options. You can see what they are by starting the server with the argument \ ``–help``\   By efault the server configuration is stored in the file \ ``.terp_serverrc``\  in the user's home directory (and for the postgres user that directory is \ ``/var/lib/postgresql``\  .

	#. You can delete the configuration file to be quite sure that the Open ERP server is starting with just the default options. It is quite common for an upgraded system to behave badly because a new version server cannot work with options from a previous version. When the server starts without a configuration file it will write a new one once there is something non-default to write to it – it will operate using defaults until then.

	#. To verify that the system works, without becoming entangled in firewall problems, you can start the Open ERP client from a second terminal window on the server computer (which doesn't pass through the firewall). Connect using the XML-RPC protocol on port 8069 or NET-RPC on port 8070. The server can use both ports simultaneously. The window displays the log file when the client is started this way.

	#. The client configuration is stored in the file \ ``.terprc``\  in the user's home directory. Since a GTK client can be started by any user, each user would have their setup defined in a configuration file in their own home directory.

	#. You can delete the configuration file to be quite sure that the Open ERP client is starting with just the default options. When the client starts without a configuration file it will write a new one for itself.

	#. The eTiny web server uses the NET-RPC protocol. If a GTK client works but eTiny doesn't then the problem is either with the NET-RPC port or with eTiny itself, and not with the Open ERP server.

.. tip::   **A step further**  *One server for several companies* 



	You can start several Open ERP application servers on one physical computer server by using different ports. If you have defined multiple database roles in PostgreSQL, each connected through an Open ERP instance to a different port, you can simultaneously serve many companies from one physical server at one time.

Creating the database
=======================

Before walking through an Open ERP business process step by step in the next chapter you'll create a database to check that the installation is working correctly:

* \ ``openerp_ch01``\  : a minimal database containing demonstration data.

To create new databases you must know the super-administrator password which defaults to admin on a new installation.


	

        .. note :: The super-administrator password

			Anyone who knows the super-administrator password has complete access to the data on the server – able to read, change and delete any of the data in any of the databases there.

			After first installation, the password is admin. You can change it through the GTK client from the menu File > Database ... > Administrator Password, or through the web client by logging out (click the Logout link), clicking Manage on the login screen, and then clicking the Password button on the Management screen. This password is stored in a configuration file outside the database, so your server systems administrator can change it if you forget it.


	.. image:: images/change_superadmin_pwd.png

                
*Changing the super-administrator password through the web client*

--------------------------                
                
	.. image:: images/create_new_db_GTK.png
	
*Creating a new database through the GTK client*
	        

* If you're using the GTK client, choose  *Files > Database > New database*  in the menu at the top left. Enter the super-administrator password, then the name of the new database you're creating.

* If you're using the web client, click  *Manage*  on the login screen, then  *Create*  on the database management page. Enter the super-administrator password, then the name of the new database you're creating.

Database openerp_ch01
-----------------------

To create the \ ``openerp_ch01``\   database, enter the database name \ ``openerp_ch01``\   into the  *New database*  field. Make sure that the  *Load Demonstration Data*  checkbox is checked. Each Open ERP module will now be loaded with previously-constructed demonstration data as it's installed. Choose the default language for this database (English for many readers of this book), then click  *Ok* . 

Wait for the message showing that the database has been successfully created, along with the user accounts and passwords (\ ``admin/admin``\   and \ ``demo/demo``\  ). Now you've created this seed database you can extend it without knowing the super administrator password.

.. tip::   **Technique**  *User Access* 



	The combination of username/password is specific to a single database. If you have administrative rights to a database you can modify the predefined users. 

	Alternatively you can install the users_ldap module, which manages the authentication of users in LDAP (the Lightweight Directory Access Protocol, a standard system), and connect it to several Open ERP databases. Using this, many databases can share the same user account details.


--------------

	.. image:: images/create_new_db_web.png
	

        .. note ::  Failure to create a database

			How do you know if you've successfully created your new database? You're told if the database creation has been unsuccessful. If you have entered a database name using prohibited characters (or no name, or too short a name) you will be alerted by the dialog box Bad database name! explaining how to correct the error. If you've entered the wrong super-administrator password or a name already in use (some names can be taken without your knowledge), you'll be alerted by the dialog box Error during database creation!

Connect to the database \ ``openerp_ch01``\   that you just created, using the default administrator account. 

If this is the first time you've connected to this database you'll be asked a series of questions to define the database parameters:

	#.  *Select a profile*  select \ ``Minimal Profile``\  and click  *Next* 

	#.  *Company Details*  replace the proposed default of \ ``Tiny sprl``\  by your own company name, complete as much of your address as you like, and add some lines about your company, such as a slogan and any statutory requirements, to the header and footer fields. Click  *Next*  

	#.  *Summary*  check the information and go back to make any modifications you need before installation. Then click  *Install* 

	#.  *Installation Completed*  click  *Ok* 

Once configuration is complete you're connected to your Open ERP system. Its functionality is very limited because you've selected a minimal installation, but this is sufficient to demonstrate that your installation is working.


	.. image:: images/define_main_co_dlg.png
	   :align: center
	    
*Defining your company during initial database configuration*
	

Managing databases
-------------------

As a super-administrator you've not only got rights to create new databases, but also to:

* delete databases,

* backup databases,

* restore databases.

All of these operations can be carried out from the menu  *File > Databases... > Backup databases*  in the GTK client, or from  *Manage...*  in the web client's Login screen.

.. tip::   **Note**  *Duplicating a database.* 



	To duplicate a database you can:

1make a backup file on your PC from this database.

2restore this database from the backup file on your PC, giving it a new name as you do so.

	This can be a useful way of making a test database from a production database. You can try out the operation of a new configuration, new modules, or just the import of new data.

Future versions of Open ERP may only give you access to some of these database functions in a special development mode, so that your security is enhanced in normal production use.

You are now ready to use databases from your installation to familiarize yourself with the administration and use of Open ERP.

New Open ERP functionality
---------------------------

The database you've created and managed so far is based on the core Open ERP functionality that you installed. The core system is installed in the file system of your Open ERP application server, but only installed into an Open ERP database as you require it, as is described in the next chapter.

What if want to update what's there, or extend what's there with additional modules?

* To update what you have, you'd install a new instance of Open ERP using the same techniques as described earlier in this chapter.

* To extend what you have, you'd install new modules in the addons directory of your current Open ERP installation. There are several ways of doing that.

In both cases you'll need briefly to be a \ ``root``\   user or \ ``Administrator``\   of your Open ERP application server.

Extending Open ERP
^^^^^^^^^^^^^^^^^^^

To extend Open ERP you'll need to copy modules into the \ ``addons``\   directory. That's is in your server's \ ``tinyerp-server``\   directory (which differs between Windows, Mac and some of the various Linux distributions and not available at all in the Windows all-in-one installer). 

If you look there you'll see existing modules such as \ ``product``\   and \ ``purchase``\  . A module can be provided in the form of files within a directory or a a zip-format file containing that same directory structure. 

You can add modules in two main ways – through the server, or through the client. 

To add new modules through the server is a conventional systems administration task. As \ ``root``\   user or other suitable user, you'd put the module in the \ ``addons``\   directory and change its permissions to match those of the other modules.

To add new modules through the client you must first change the permissions of the \ ``addons``\   directory of the server, so that it is writable by the server. That will enable you to install Open ERP modules using the Open ERP client (a task ultimately carried out on the application server by the server software). 

.. tip::   **Note**  *Changing permissions* 



	A very simple way of changing permissions on the Linux system you're using to develop an Open ERP application is to execute the command sudo chmod 777 <path_to_addons> (where <path_to_addons> is the full path to the addons directory, a location like /usr/lib/python2.5/site-packages/openerp-server/addons). 

Any user of Open ERP who has access to the relevant administration menus can then upload any new functionality, so you'd probably disable this capability for production use. You'll see examples of this uploading as you make your way through this book.

