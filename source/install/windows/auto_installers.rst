
Automated Install
"""""""""""""""""

All NTFS Formatted Windows 2000, XP or VISTA using Postgres 8.2.9.

You can now download our `Open ERP Downloads <http://openerp.com/downloads.html>`_.

You can choose STABLE or DEVELOPMENT version and if the Open ERP server initializes with or without the demo data.

Follow instructions on Installation Manual Home Page.

Windows 200x Servers
^^^^^^^^^^^^^^^^^^^^

It appears from perusing the forums, many are having problems installing
OpenERP on Windows Servers 2003 and 2008 which has been identified as a
PostgreSQL problem. So this section is going to outline another way of
implementing PostgreSQL which may shed a bit of light into the problem as well

Things to Watch out for with Installing in Windows Servers PostgreSQL under W2Kx Servers
########################################################################################

The main section for installing PostgreSQL if found [here]. Once you have got
to the Service Configuration window be sure to record your passwords because
this is the window that Postgres uses to automatically start the database
through windows services.

Account name PostgreSQL uses is Postgres -- make sure you do not change this name!

If you haven't installed PostgreSQL before a warning window will come up saying
you do not have an user account called postres which is the administrator ...
agree. Subsequently PostgreSQL will make a user account to start it up through
windows services. Make sure the password has a reasonably secure nature i.e.
has numerical, character, symbol and is longer than 6 charecters.

    * When building a dbase using a gui make sure it is UTF-8
    * Make sure PL/pgsql is selected
    * pgAdmin III will be installed by default with the latest version which makes it easier to install databases later if you need to

Another Way to Create a Database for OpenERP
############################################

A suggestion to install a database through the command prompt has been
delineated [here], however if some prefer a gui then try this way:

When PostgreSQL is installed, pgAdmin can be used to create a database suitable for OpenERP to use.
Use pgAdmin

    * Start > All Programs > PostreSQLxx > pgAdmin

A window should appear with Servername and PostreSQL Database Server 8.x in left hand panel

    * Right click on PostgreSQL Databas Server 8.x > Connect > type in the database administrator password.
    * Create a username for OpenERP by right clicking on login roles in the left panel of the window.

HowTo start OpenERP 4.2.2 as Service from source installation on Win 200x servers
#################################################################################

Note

  * Download "Windows Server 2003 Resource Kit Tools"
  * execute in command prompt
    instsrv.exe "TinyService" "C:\Program Files\Windows Resource Kits\Tools\srvany.exe"

  * The return message should be:
    The service was successfuly added

  * Have a close look at how the quotes are set for the path to srvany.exe. If you get an error saying
    "The fully qualified path to the .EXE must be given"
    then this might be due to problems of instsrv f dealing with spaces in pathnames. Just copy instsrv.exe and srvany.exe to temp-folder without spaces and try again.

  * open regedit and go to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TinyService

  * Select the newly created key and right click in the right pane. New > String Value. Name it "Application".

  * Double-click your new "Application" key, enter
    <path to python>python.exe <path to tinyserver\bin>tinyerp-server.py
    and save it. The service is now ready to run.

  * Test run it from within the Control Panel > Administrator Tools > Services. You will see the service "TinyService" now listed and you can start it

Vista Extras
############

  * For Windows Vista installation please review this forum post
  * or its Google translated version
  * see also http://openerp.com/forum/topic4386.html

