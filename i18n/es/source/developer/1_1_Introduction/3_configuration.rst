
.. i18n: Configuration
.. i18n: =============

Configuración
=============

.. i18n: Two configuration files are available:

Dos archivos de configuración están disponibles:

.. i18n:     * one for the client: ~/.terprc
.. i18n:     * one for the server: ~/.terp_serverrc 

    * Uno para el cliente: ~/.terprc
    * Uno para el servidor: ~/.terp_serverrc 

.. i18n: Those files follow the convention used by python's ConfigParser module.

Estos archivos siguen el estandar usado por el módulo de configuración de Python ConfigParser.

.. i18n: Lines beginning with "#" or ";" are comments.

Líneas al inicio con "#" o ";" son comentarios.

.. i18n: Those files are not necessary. If they are not found, the server and the client will start with the default configuration.

Estos archivos no son necesarios. Si ellos no son encontrados, el servidor y el cliente iniciarán con la confiración por defecto.

.. i18n: The client configuration file is automatically generated upon the first start. The one of the server can automatically be created using the command:

El archivo de configuración del cliente es generado automáticamente cuando inicio la primera vez. El archivo del servidor puede ser generado automáticamente usando el comando:

.. i18n: openerp-server.py -s

openerp-server.py -s

.. i18n:        
.. i18n: Server Configuration File
.. i18n: -------------------------

       
Archivo de Configuración del Servidor
-------------------------------------
.. i18n: The server configuration file .terp_serverrc is used to save server startup options. For the version 5.X configuration file is .openerp_serverrc. Here is the list of the available options:

The server configuration file .terp_serverrc is used to save server startup options. For the version 5.X configuration file is .openerp_serverrc. Here is the list of the available options:

.. i18n: :interface:
.. i18n:     Address to which the server will be bound 

:interface:
    Address to which the server will be bound 

.. i18n: :port:
.. i18n:     Port the server will listen on 

:port:
    Port the server will listen on 

.. i18n: :database:
.. i18n:     Name of the database to use 

:database:
    Name of the database to use 

.. i18n: :user:
.. i18n:     Username used when connecting to the database 

:user:
    Username used when connecting to the database 

.. i18n: :translate_in:
.. i18n:     File used to translate Open ERP to your language 

:translate_in:
    File used to translate Open ERP to your language 

.. i18n: :translate_out:
.. i18n:     File used to export the language Open ERP use 

:translate_out:
    File used to export the language Open ERP use 

.. i18n: :language:
.. i18n:     Use this language as the language of the server. This must be specified as an ISO country code, as specified by the W3C. 

:language:
    Use this language as the language of the server. This must be specified as an ISO country code, as specified by the W3C. 

.. i18n: :verbose:
.. i18n:     Will used debugged output 

:verbose:
    Will used debugged output 

.. i18n: :init:
.. i18n:     init a module (use "all" for all modules) 

:init:
    init a module (use "all" for all modules) 

.. i18n: :update:
.. i18n:     update a module (use "all" for all modules) 

:update:
    update a module (use "all" for all modules) 

.. i18n: :upgrade:
.. i18n:     Upgrade/install/uninstall modules 

:upgrade:
    Upgrade/install/uninstall modules 

.. i18n: :db_name:
.. i18n:     specify the database name 

:db_name:
    specify the database name 

.. i18n: :db_user:
.. i18n:     specify the database user name 

:db_user:
    specify the database user name 

.. i18n: :db_password:
.. i18n:     specify the database password 

:db_password:
    specify the database password 

.. i18n: :pg_path:
.. i18n:     specify the pg executable path 

:pg_path:
    specify the pg executable path 

.. i18n: :db_host:
.. i18n:     specify the database host 

:db_host:
    specify the database host 

.. i18n: :db_port:
.. i18n:     specify the database port 

:db_port:
    specify the database port 

.. i18n: :translate_modules:
.. i18n:     Specify modules to export. Use in combination with --i18n-export 

:translate_modules:
    Specify modules to export. Use in combination with --i18n-export 

.. i18n: You can create your own configuration file by specifying -s or --save on the server command line. If you would like to write an alternativve configuration file, use -c <config file> or --config=<config file>
.. i18n: Here is a basic configuration for a server::
.. i18n: 
.. i18n:         [options]
.. i18n:         verbose = False
.. i18n:         xmlrpc = True
.. i18n:         database = terp
.. i18n:         update = {}
.. i18n:         port = 8069
.. i18n:         init = {}
.. i18n:         interface = 127.0.0.1
.. i18n:         reportgz = False

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

.. i18n: Full Example for Server V5.0 ::
.. i18n: 
.. i18n:         [printer]
.. i18n:         path = none
.. i18n:         softpath_html = none
.. i18n:         preview = True
.. i18n:         softpath = none

Full Example for Server V5.0 ::

        [printer]
        path = none
        softpath_html = none
        preview = True
        softpath = none

.. i18n:         [logging]
.. i18n:         output = stdout
.. i18n:         logger = 
.. i18n:         verbose = True
.. i18n:         level = error

        [logging]
        output = stdout
        logger = 
        verbose = True
        level = error

.. i18n:         [help]
.. i18n:         index = http://www.openerp.com/documentation/user-manual/
.. i18n:         context = http://www.openerp.com/scripts/context_index.php

        [help]
        index = http://www.openerp.com/documentation/user-manual/
        context = http://www.openerp.com/scripts/context_index.php

.. i18n:         [form]
.. i18n:         autosave = False
.. i18n:         toolbar = True

        [form]
        autosave = False
        toolbar = True

.. i18n:         [support]
.. i18n:         recipient = support@openerp.com
.. i18n:         support_id = 

        [support]
        recipient = support@openerp.com
        support_id = 

.. i18n:         [tip]
.. i18n:         position = 0
.. i18n:         autostart = False

        [tip]
        position = 0
        autostart = False

.. i18n:         [client]
.. i18n:         lang = en_US
.. i18n:         default_path = /home/user
.. i18n:         filetype = {}
.. i18n:         theme = none
.. i18n:         toolbar = icons
.. i18n:         form_tab_orientation = 0
.. i18n:         form_tab = top

        [client]
        lang = en_US
        default_path = /home/user
        filetype = {}
        theme = none
        toolbar = icons
        form_tab_orientation = 0
        form_tab = top

.. i18n:         [survey]
.. i18n:         position = 3

        [survey]
        position = 3

.. i18n:         [path]
.. i18n:         pixmaps = /usr/share/pixmaps/openerp-client/
.. i18n:         share = /usr/share/openerp-client/

        [path]
        pixmaps = /usr/share/pixmaps/openerp-client/
        share = /usr/share/openerp-client/

.. i18n:         [login]
.. i18n:         db = eo2
.. i18n:         login = admin
.. i18n:         protocol = http://
.. i18n:         port = 8069
.. i18n:         server = localhost

        [login]
        db = eo2
        login = admin
        protocol = http://
        port = 8069
        server = localhost

.. i18n: GTK-Client Configuration
.. i18n: ------------------------

GTK-Client Configuration
------------------------

.. i18n: .. topic:: login section
.. i18n: 
.. i18n:         :login:
.. i18n:             login name to use to connect to Tiny ERP server 
.. i18n: 
.. i18n:         :server:
.. i18n:             address used by the server 
.. i18n: 
.. i18n:         :port:
.. i18n:             port used by the server 

.. topic:: login section

        :login:
            login name to use to connect to Tiny ERP server 

        :server:
            address used by the server 

        :port:
            port used by the server 

.. i18n: .. topic:: path section
.. i18n: 
.. i18n:         :share:
.. i18n:             path used to find Tiny ERP shared files 
.. i18n: 
.. i18n:         :pixmaps:
.. i18n:             path used to find Tiny ERP pixmaps files 

.. topic:: path section

        :share:
            path used to find Tiny ERP shared files 

        :pixmaps:
            path used to find Tiny ERP pixmaps files 

.. i18n: .. topic:: tip section
.. i18n: 
.. i18n:         :autostart:
.. i18n:             Should the client display tips at startup 
.. i18n: 
.. i18n:         :position:
.. i18n:             Tip number the client will display 

.. topic:: tip section

        :autostart:
            Should the client display tips at startup 

        :position:
            Tip number the client will display 

.. i18n: .. topic:: form section
.. i18n: 
.. i18n:         :autosave:
.. i18n:             Will the client automatically save the change you made to a record 

.. topic:: form section

        :autosave:
            Will the client automatically save the change you made to a record 

.. i18n: .. topic:: printer section
.. i18n: 
.. i18n:         :preview:
.. i18n:             Preview report before printing 
.. i18n: 
.. i18n:         :softpath:
.. i18n:             Path to the pdf previewer 
.. i18n: 
.. i18n:         :softpath_html:
.. i18n:             Path to the html previewer 
.. i18n: 
.. i18n:         :path:
.. i18n:             Command used to print 

.. topic:: printer section

        :preview:
            Preview report before printing 

        :softpath:
            Path to the pdf previewer 

        :softpath_html:
            Path to the html previewer 

        :path:
            Command used to print 

.. i18n: .. topic:: logging section
.. i18n: 
.. i18n:         :logger:
.. i18n:             log channels to display. List values are: @common@, @common.message@, @view@, @view.form@, @common.options@, @rpc.request@, @rpc.result@, @rpc.exception@ 
.. i18n: 
.. i18n:         :level:
.. i18n:             logging level to show 
.. i18n: 
.. i18n:         :output:
.. i18n:             file used by the logger 
.. i18n: 
.. i18n:         :verbose:
.. i18n:             set the log level to INFO 

.. topic:: logging section

        :logger:
            log channels to display. List values are: @common@, @common.message@, @view@, @view.form@, @common.options@, @rpc.request@, @rpc.result@, @rpc.exception@ 

        :level:
            logging level to show 

        :output:
            file used by the logger 

        :verbose:
            set the log level to INFO 

.. i18n: .. topic:: client section
.. i18n: 
.. i18n:         :default_path:
.. i18n:             Default path used by the client when saving/loading datas. 

.. topic:: client section

        :default_path:
            Default path used by the client when saving/loading datas. 

.. i18n: **Default values**::
.. i18n: 
.. i18n:         [login]
.. i18n:         login = admin
.. i18n:         port = 8069
.. i18n:         server = 192.168.1.4
.. i18n:          
.. i18n:         [printer]
.. i18n:         path = none
.. i18n:         preview = True
.. i18n:         softpath = none
.. i18n:          
.. i18n:         [logging]
.. i18n:         output = stdout
.. i18n:         logger =
.. i18n:         verbose = True
.. i18n:         level = ERROR
.. i18n:          
.. i18n:         [form]
.. i18n:         autosave = False
.. i18n:          
.. i18n:         [client]
.. i18n:         default_path = /home/user

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

.. i18n: Web Client Configuration 
.. i18n: ------------------------ 

Web Client Configuration 
------------------------ 

.. i18n: Get a clone of each repository::
.. i18n: 
.. i18n:   bzr clone lp:~openerp/openobject-server/trunk server
.. i18n:   bzr clone lp:~openerp/openobject-client/trunk client
.. i18n:   bzr clone lp:~openerp/openobject-client-web/trunk client-web
.. i18n:   bzr clone lp:~openerp/openobject-addons/trunk addons

Get a clone of each repository::

  bzr clone lp:~openerp/openobject-server/trunk server
  bzr clone lp:~openerp/openobject-client/trunk client
  bzr clone lp:~openerp/openobject-client-web/trunk client-web
  bzr clone lp:~openerp/openobject-addons/trunk addons

.. i18n: If you want to get a clone of the extra-addons repository, you can execute this command::
.. i18n: 
.. i18n:   bzr clone lp:~openerp-commiter/openobject-addons/trunk-extra-addons extra-addons

If you want to get a clone of the extra-addons repository, you can execute this command::

  bzr clone lp:~openerp-commiter/openobject-addons/trunk-extra-addons extra-addons

.. i18n: run the setup scripts in the respective directories::
.. i18n: 
.. i18n:   python2.4 setup.py build
.. i18n:   python2.4 setup.py install

run the setup scripts in the respective directories::

  python2.4 setup.py build
  python2.4 setup.py install

.. i18n: Currently the initialisation procedure of the server parameter --init=all to
.. i18n: populate the database seems to be broken in trunk.

Currently the initialisation procedure of the server parameter --init=all to
populate the database seems to be broken in trunk.

.. i18n: It is recommended to create a new database via the gtk-client. Before that the web-client will not work.

It is recommended to create a new database via the gtk-client. Before that the web-client will not work.

.. i18n: Start OpenERP server like this: ::
.. i18n: 
.. i18n:   ./openerp-server.py --addons-path=/path/to/my/addons

Start OpenERP server like this: ::

  ./openerp-server.py --addons-path=/path/to/my/addons

.. i18n: The ``bin/addons`` will be considered as default addons directory which can be
.. i18n: overriden by the ``/path/to/my/addons/``. That is if an addon exists in
.. i18n: ``bin/addons`` as well as ``/path/to/my/addons`` (custom path) the later one will
.. i18n: be given preference over the ``bin/addons`` (default path).

The ``bin/addons`` will be considered as default addons directory which can be
overriden by the ``/path/to/my/addons/``. That is if an addon exists in
``bin/addons`` as well as ``/path/to/my/addons`` (custom path) the later one will
be given preference over the ``bin/addons`` (default path).
