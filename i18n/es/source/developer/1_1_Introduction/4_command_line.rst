
.. i18n: Command line options
.. i18n: ====================

Command line options
====================

.. i18n: General Options
.. i18n: ----------------

General Options
----------------

.. i18n:   --version             show program version number and exit
.. i18n:   -h, --help            show this help message and exit
.. i18n:   -c CONFIG, --config=CONFIG
.. i18n:                         specify alternate config file
.. i18n:   -s, --save            save configuration to ~/.terp_serverrc
.. i18n:   -v, --verbose         enable debugging
.. i18n:   --pidfile=PIDFILE     file where the server pid will be stored
.. i18n:   --logfile=LOGFILE     file where the server log will be stored
.. i18n:   -n INTERFACE, --interface=INTERFACE
.. i18n:                         specify the TCP IP address
.. i18n:   -p PORT, --port=PORT  specify the TCP port
.. i18n:   --net_interface=NETINTERFACE
.. i18n:                         specify the TCP IP address for netrpc
.. i18n:   --net_port=NETPORT    specify the TCP port for netrpc
.. i18n:   --no-netrpc           disable netrpc
.. i18n:   --no-xmlrpc           disable xmlrpc
.. i18n:   -i INIT, --init=INIT  init a module (use "all" for all modules)
.. i18n:   --without-demo=WITHOUT_DEMO
.. i18n:                         load demo data for a module (use "all" for all
.. i18n:                         modules)
.. i18n:   -u UPDATE, --update=UPDATE
.. i18n:                         update a module (use "all" for all modules)
.. i18n:   --stop-after-init     stop the server after it initializes
.. i18n:   --debug               enable debug mode
.. i18n:   -S, --secure          launch server over https instead of http
.. i18n:   --smtp=SMTP_SERVER    specify the SMTP server for sending mail
.. i18n:   --price_accuracy=PRICE_ACCURACY
.. i18n:                         specify the price accuracy
.. i18n:  
.. i18n: Database related options:
.. i18n: -------------------------
.. i18n:  
.. i18n:   -d DB_NAME, --database=DB_NAME
.. i18n:                         specify the database name
.. i18n:   -r DB_USER, --db_user=DB_USER
.. i18n:                         specify the database user name
.. i18n:   -w DB_PASSWORD, --db_password=DB_PASSWORD
.. i18n:                         specify the database password
.. i18n:   --pg_path=PG_PATH   specify the pg executable path
.. i18n:   --db_host=DB_HOST   specify the database host
.. i18n:   --db_port=DB_PORT   specify the database port
.. i18n:  
.. i18n: Internationalization options:
.. i18n: -----------------------------

  --version             show program version number and exit
  -h, --help            show this help message and exit
  -c CONFIG, --config=CONFIG
                        specify alternate config file
  -s, --save            save configuration to ~/.terp_serverrc
  -v, --verbose         enable debugging
  --pidfile=PIDFILE     file where the server pid will be stored
  --logfile=LOGFILE     file where the server log will be stored
  -n INTERFACE, --interface=INTERFACE
                        specify the TCP IP address
  -p PORT, --port=PORT  specify the TCP port
  --net_interface=NETINTERFACE
                        specify the TCP IP address for netrpc
  --net_port=NETPORT    specify the TCP port for netrpc
  --no-netrpc           disable netrpc
  --no-xmlrpc           disable xmlrpc
  -i INIT, --init=INIT  init a module (use "all" for all modules)
  --without-demo=WITHOUT_DEMO
                        load demo data for a module (use "all" for all
                        modules)
  -u UPDATE, --update=UPDATE
                        update a module (use "all" for all modules)
  --stop-after-init     stop the server after it initializes
  --debug               enable debug mode
  -S, --secure          launch server over https instead of http
  --smtp=SMTP_SERVER    specify the SMTP server for sending mail
  --price_accuracy=PRICE_ACCURACY
                        specify the price accuracy
 
Database related options:
-------------------------
 
  -d DB_NAME, --database=DB_NAME
                        specify the database name
  -r DB_USER, --db_user=DB_USER
                        specify the database user name
  -w DB_PASSWORD, --db_password=DB_PASSWORD
                        specify the database password
  --pg_path=PG_PATH   specify the pg executable path
  --db_host=DB_HOST   specify the database host
  --db_port=DB_PORT   specify the database port
 
Internationalization options:
-----------------------------

.. i18n:     Use these options to translate Tiny ERP to another language.See i18n
.. i18n:     section of the user manual. Option '-l' is mandatory.
.. i18n:  
.. i18n:   -l LANGUAGE, --language=LANGUAGE
.. i18n:                        specify the language of the translation file. Use it
.. i18n:                        with --i18n-export and --i18n-import
.. i18n:   --i18n-export=TRANSLATE_OUT
.. i18n:                        export all sentences to be translated to a CSV file
.. i18n:                        and exit
.. i18n:   --i18n-import=TRANSLATE_IN
.. i18n:                        import a CSV file with translations and exit
.. i18n:   --modules=TRANSLATE_MODULES
.. i18n:                        specify modules to export. Use in combination with
.. i18n:                        --i18n-export

    Use these options to translate Tiny ERP to another language.See i18n
    section of the user manual. Option '-l' is mandatory.
 
  -l LANGUAGE, --language=LANGUAGE
                       specify the language of the translation file. Use it
                       with --i18n-export and --i18n-import
  --i18n-export=TRANSLATE_OUT
                       export all sentences to be translated to a CSV file
                       and exit
  --i18n-import=TRANSLATE_IN
                       import a CSV file with translations and exit
  --modules=TRANSLATE_MODULES
                       specify modules to export. Use in combination with
                       --i18n-export
