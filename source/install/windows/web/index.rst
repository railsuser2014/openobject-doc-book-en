
.. index::
   single: Installation; Open ERP Web (Windows)
   single: Open ERP Web; Installation (Windows)
.. 

.. _installation-windows-web-link:

OpenERP Web Installation
========================

The installation is very simple. There are 5 stages :

  #. Welcome message.
  #. OEPL Licence Acceptation
  #. Shortcut in the Start menu.
  #. Confirmation Choices
  #. Automatic installation

You have to install, configure and run the OpenERP Server before using the
OpenERP Web. The web client needs the server to run. You can install the server
application on your computer, or on an independent server accessible by
network.

Downloading the OpenERP Web
-------------------------------

The OpenERP Web can be downloaded from
the `OpenERP website's download page <http://www.openerp.com/index.php?option=com_content&view=article&id=18&Itemid=28>`_


Installing the OpenERP Web
------------------------------

Click on the executable installation file you've just downloaded and select the installation path.

.. image:: ../../img/Web.01.install_path.png

Preparing the web server for the first time run
+++++++++++++++++++++++++++++++++++++++++++++++

The Windows service for OpenERP Web Server is installed during the installation and it's set up
to start the server automatically on system boot.

The configuration file is now automatically saved in the installation directory, in: ::

 C:\Program Files\OpenERP Web\conf\openerp-web.conf

Starting the web server
-----------------------

Now as the web server is initialized and the settings are saved, you can finally start 
the OpenERP Web Server service.

