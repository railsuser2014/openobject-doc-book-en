
.. _configuration-files-link:

Configuration
=============

Two configuration files are available:

    * one for the client: ~/.openerprc
    * one for the server: ~/.openerp_serverrc

Those files follow the convention used by python's ConfigParser module.

Lines beginning with "#" or ";" are comments.

The client configuration file is automatically generated upon the first start. The one of the server can automatically be created using the command: ::

  openerp-server.py -s

If they are not found, the server and the client will start with the default configuration.

Server Configuration File
-------------------------

The server configuration file .openerp_serverrc is used to save server startup options. Here is the list of the available options:

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


GTK-Client Configuration
------------------------

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

Web Client Configuration 
------------------------ 

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

