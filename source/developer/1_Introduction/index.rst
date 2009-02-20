=======================
Development Environment
=======================


Working with Launchpad
======================

Getting the sources
-------------------

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


Create an account on Launchpad
------------------------------

Before you can commit on launchpad, you need to create a login.

Go to: https://launchpad.net --> log in / register on top right.

You enter your e-mail address and you wait for an e-mail which will guide you trough the process needed to create your login.

This login is only needed if you intend to commit on bazaar on openerp-commiter or on your own branch.


Pushing a new branch
--------------------

If you want to contribute on OpenERP or OpenObject, here is the proposed method:

  * You create a branch on launchpad on the project that interest you. It's
    important that you create your branch on launchpad and not on your local
    system so that we can easily merge, share code between projects and
    centralize futur developments.
  * You develop your own features or bugfixes
    in your own branch on launchpad. Don't forget to set the status of your
    branch (new, experimental, development, mature, ...) so that contributors
    knows what they can use or not.
  * Once your code is good enough, you propose your branch for merging
  * Your work will be evaluated by one responsible of the commiters team.

    - If they accept your branch for integration in the official version, they
      will submit to the quality team that will review and merge in the official
      branch.
    - If the commiter team refuses your branch, they will explain why
      so that you can review your code to better fits guidelines (problem for
      futur migrations, ...)

The extra-addons branch, that stores all extra modules, is directly accessible
to all commiters. If you are a commiter, you can work directly on this branch
and commit your own work. This branch do not require a validation of the
quality team. You should put there your special modules for your own customers.

If you want to propose or develop new modules, we suggest you to create your
own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
and develop within your branch. You can fill in a bug to request that
your modules are integrated in one of the two branches:

  * extra-addons : if your module touches a few companies
  * addons : if your module will be usefull for most of the companies

We invite all our partners and contributors to work in that way so that we can
easily integrate and share the work done between the different projects.

Suppose you want to push your addons::

  cd addons
  bzr push lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
  bzr bind lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME

After having done that, your branch is public on Launchpad, in the `OpenObject
project <https://code.launchpad.net/openobject>`_, and commiters can work on
it, review it and propose for integration in the official branch. The last line
allows you to rebind your branch to the one which is on launchpad, after having
done this, your commit will be applied on launchpad directly (unless you use ``--local``)


Development Environment
=======================

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

  * OpenERP-commiter --> they can commit on:

    - lp:~openerp/openobject-addons/4.2-extra-addons
    - lp:~openerp/openobject-addons/trunk-extra-addons

In this group, we include some of our partners who will be selected on a meritocracy basis by the quality team.

  * Contributors --> they can commit on:

    - lp:~openerp-community

[Read more about :ref:`Open ERP Team <openerp-team>`]
        
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
        
Configuration
=============

 Two configuration files are available for Open ERP:

    * one for the client: ~/.openerprc
    * one for the server: ~/.openerp_serverrc

Those files follow the convention used by python's ConfigParser module.

Lines beginning with "#" or ";" are comments.

Those files are not necessary. If they are not found, the server and the client will start with the default configuration.

The client configuration file is automatically generated upon the first start. The one of the server can automatically be created using the command::

        openerp-server.py -s
        
Server Configuration File
-------------------------

The server configuration file .terp_serverrc is used to save server startup options. For the version 5.X configuration file is .openerp_serverrc. Here is the list of the available options:

:interface:
    Address to which the server will be bound 

:port:
    Port the server will listen on 

:database:
    Name of the database to use 

:user:
    Username used when connecting to the database 

:translate_in:
    File used to translate Open ERP to your language 

:translate_out:
    File used to export the language Open ERP use 

:language:
    Use this language as the language of the server. This must be specified as an ISO country code, as specified by the W3C. 

:verbose:
    Will used debugged output 

:init:
    init a module (use "all" for all modules) 

:update:
    update a module (use "all" for all modules) 

:upgrade:
    Upgrade/install/uninstall modules 

:db_name:
    specify the database name 

:db_user:
    specify the database user name 

:db_password:
    specify the database password 

:pg_path:
    specify the pg executable path 

:db_host:
    specify the database host 

:db_port:
    specify the database port 

:translate_modules:
    Specify modules to export. Use in combination with --i18n-export 


You can create your own configuration file by specifying -s or --save on the server command line. If you would like to write an alternativve configuration file, use -c <config file> or --config=<config file>
Here is a basic configuration for a server::

        [options]
        verbose = False
        xmlrpc = True
        database = terp
        update = {}
        port = 8069
        init = {}
        interface = 127.0.0.1
        reportgz = False

Full Example for Server V5.0 ::

        [printer]
        path = none
        softpath_html = none
        preview = True
        softpath = none

        [logging]
        output = stdout
        logger = 
        verbose = True
        level = error

        [help]
        index = http://www.openerp.com/documentation/user-manual/
        context = http://www.openerp.com/scripts/context_index.php

        [form]
        autosave = False
        toolbar = True

        [support]
        recipient = support@openerp.com
        support_id = 

        [tip]
        position = 0
        autostart = False

        [client]
        lang = en_US
        default_path = /home/user
        filetype = {}
        theme = none
        toolbar = icons
        form_tab_orientation = 0
        form_tab = top

        [survey]
        position = 3

        [path]
        pixmaps = /usr/share/pixmaps/openerp-client/
        share = /usr/share/openerp-client/

        [login]
        db = eo2
        login = admin
        protocol = http://
        port = 8069
        server = localhost

Client Configuration File
-------------------------

.. topic:: login section

        :login:
            login name to use to connect to Tiny ERP server 

        :server:
            address used by the server 

        :port:
            port used by the server 

.. topic:: path section

        :share:
            path used to find Tiny ERP shared files 

        :pixmaps:
            path used to find Tiny ERP pixmaps files 

.. topic:: tip section

        :autostart:
            Should the client display tips at startup 

        :position:
            Tip number the client will display 

.. topic:: form section

        :autosave:
            Will the client automatically save the change you made to a record 

.. topic:: printer section

        :preview:
            Preview report before printing 

        :softpath:
            Path to the pdf previewer 

        :softpath_html:
            Path to the html previewer 

        :path:
            Command used to print 

.. topic:: logging section

        :logger:
            log channels to display. List values are: @common@, @common.message@, @view@, @view.form@, @common.options@, @rpc.request@, @rpc.result@, @rpc.exception@ 

        :level:
            logging level to show 

        :output:
            file used by the logger 

        :verbose:
            set the log level to INFO 

.. topic:: client section

        :default_path:
            Default path used by the client when saving/loading datas. 

**Default values**::

        [login]
        login = admin
        port = 8069
        server = 192.168.1.4
         
        [printer]
        path = none
        preview = True
        softpath = none
         
        [logging]
        output = stdout
        logger =
        verbose = True
        level = ERROR
         
        [form]
        autosave = False
         
        [client]
        default_path = /home/user
        
Command Line Options
====================

Checkout method::

  bzr co lp:~openerp/openobject-addons/trunk -- to make a checkout
  bzr up                                     -- to make an update
  bzr ci                                     -- to commit

Creating a branch::

  bzr branch lp:~<url> <local dir>             -- to create a branch locally
  bzr pull                                     -- to update the branch
  bzr push lp:~<url>                           -- to include your changes in the remote branch

In any cases, when you experience some problems, you can do::

  bzr help

or ``bzr help <command>``. e.g.::

  bzr help branch


Open ERP Server & Web Client
============================

Get a clone of each repository::

  bzr clone lp:~openerp/openobject-server/trunk server
  bzr clone lp:~openerp/openobject-client/trunk client
  bzr clone lp:~openerp/openobject-client-web/trunk client-web
  bzr clone lp:~openerp/openobject-addons/trunk addons

If you want to get a clone of the extra-addons repository, you can execute this command::

  bzr clone lp:~openerp-commiter/openobject-addons/trunk-extra-addons extra-addons

run the setup scripts in the respective directories::

  python2.4 setup.py build
  python2.4 setup.py install

Currently the initialisation procedure of the server parameter --init=all to
populate the database seems to be broken in trunk.

It is recommended to create a new database via the gtk-client. Before that the web-client will not work.

Start OpenERP server like this: ::

  ./openerp-server.py --addons-path=/path/to/my/addons

The ``bin/addons`` will be considered as default addons directory which can be
overriden by the ``/path/to/my/addons/``. That is if an addon exists in
``bin/addons`` as well as ``/path/to/my/addons`` (custom path) the later one will
be given preference over the ``bin/addons`` (default path).


