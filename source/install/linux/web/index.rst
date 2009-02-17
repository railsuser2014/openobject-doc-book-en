
.. index::
   single: Installation; Open ERP Web (Linux)
   single: Open ERP Web; Installation (Linux)
.. 

.. _installation-linux-web-link:

===============================================================================
OpenERP Web Installation
===============================================================================

Here is the installation instructions for Debian based Linux distributions.
Tested on Debian Etch and Ubuntu Hardy. The procedure might work with other 
Linux or similar distributions. See the docs on how to install the specified 
Packages on your favourite distribution.

-------------------------------------------------------------------------------
Prerequisites
-------------------------------------------------------------------------------

#. Python >= 2.4
#. TurboGears >= 1.0.7, < 1.1b1

-------------------------------------------------------------------------------
TurboGears
-------------------------------------------------------------------------------

.. code-block:: bash

    $ sudo apt-get install python-setuptools
    $ sudo easy_install TurboGears==1.0.8
    
or

.. code-block:: bash

    $ wget http://peak.telecommunity.com/dist/ez_setup.py
    $ sudo python ez_setup.py
    $ sudo easy_install TurboGears==1.0.8

Check whether TurboGears is properly installed or not...

.. code-block:: bash

    $ tg-admin info

You should see version information of TurboGears and related packages.

-------------------------------------------------------------------------------
OpenERP Web
-------------------------------------------------------------------------------

.. code-block:: bash

    $ sudo easy_install -U openerp-web

-------------------------------------------------------------------------------
Configuration
-------------------------------------------------------------------------------

Locate the *config/default.cfg* in the installed *EGG*, and make appropriate 
changes, especially:

.. code-block:: ini

    [openerp]
    server = "localhost"
    port = 8070
    protocol = "socket"

where:

    | ``server`` is the OpenERP server host...
    | ``port`` is the OpenERP server port...
    | ``protocol`` is the protocol to be used (socket, http or https)

Now start the web server with ``start-openerp-web`` command:

.. code-block:: bash

    $ start-openerp-web

If you see message showing ``cherrypy._cperror.NotReady: Port not free.`` then 
make sure no other application is running on the specified port (8080 is default).

You can change port for by changing ``server.socket_port`` value in *config/default.cfg*.

If everything is fine, open your favourite web browser and type http://localhost:8080, 
and your can see welcome page with login screen.

Please make sure cookies are enabled in your browser.

Of course, OpenERP Server must be running at that time. You should create a 
database from the DBAdmin interface by clicking on Manage button that you can 
see besides the Database selection box. After creating a new database login 
with the admin/admin or demo/demo to see OpenERP in action...

-------------------------------------------------------------------------------
Run as service (daemon)
-------------------------------------------------------------------------------

This has been tested on *ubuntu* only.

.. code-block:: bash

    $ cp /path/to/openerp_web-5.0-py2.5.egg/scripts/openerp-web /etc/init.d
    $ cp /path/to/openerp_web-5.0-py2.5.egg/config/default.cfg /etc/openerp-web.cfg

edit */etc/init.d/openerp-web*:

.. code-block:: ini

    USER="terp"

and */etc/openerp-web.cfg*:

.. code-block:: ini

    args="('server.log',)" ==> args="('/var/log/openerp-web.log',)"

Create ``/var/log/openerp-web.log`` with proper ownership

.. code-block:: bash

    $ sudo touch /var/log/openerp-web.log
    $ sudo chown terp /var/log/openerp-web.log

Now run following command to start the OpenERP Web automatically on system 
startup (Debian/Ubuntu).

.. code-block:: bash

    $ sudo update-rc.d openerp-web defaults

Start the deamon:

.. code-block:: bash

    $ sudo /etc/init.d/openerp-web start

.. note::

     The init script is compatible with all major Linux distributions. Please 
     check docs of your distribution on how to enable services.

-------------------------------------------------------------------------------
Configure HTTPS
-------------------------------------------------------------------------------

The following text describes how to configure OpenERP Web for production 
environment over HTTPS with Apache2.

**mod_proxy + mod_ssl (Apache2)**

See `Apache manual <http://httpd.apache.org/docs/>`_ for more information. 

**Apache configuration**

.. code-block:: apache

    <VirtualHost *:443>

        SSLEngine on
        SSLCertificateFile /etc/apache2/ssl/apache.pem

        <Proxy *>
            Order deny,allow
            Allow from all
        </Proxy>

        ProxyRequests Off

        ProxyPass        /   http://127.0.0.1:8080
        ProxyPassReverse /   http://127.0.0.1:8080

    </VirtualHost>

**OpenERP Web configuration**

.. code-block:: ini

    base_url_filter.on = True
    base_url_filter.use_x_forwarded_host = False
    base_url_filter.base_url = "https://www.example.com"

**Block the OpenERP Web server port (firewall)**

.. code-block:: bash

    $ iptables -A INPUT -i lo -j ACCEPT
    $ iptables -A INPUT -p tcp --dport 8080 -j REJECT

.. note:: 
    
    Don't block the localhost/121.0.0.1 (the first rule)

.. note::

    This method only works if you want your OpenERP Web application at the 
    root of your server (https://www.example.com) and can't be deployed under 
    a subdirectory, e.g. http://www.example.com/openerp.

    To overcome with the issue you can go with `subdomain`, like:

        https://openerp.example.com

-------------------------------------------------------------------------------
Web Browser Compatibilities
-------------------------------------------------------------------------------

Supported browsers
++++++++++++++++++

*OpenERP Web* is known to work best with *Mozilla* based web browsers. Here is 
the list of supported browsers.

#. Firefox >= 1.5
#. Internet Explorer >= 6.0
#. Safari >= 3.0
#. Google Chrome >= 1.0
#. Opera >= 9.0

Flash plugin
++++++++++++

Your browser should have the Flash plugin installed because *OpenERP Web* uses
some Flash components.

Here is how to install the Flash plugin on an Ubuntu system:

.. code-block:: bash

    $ sudo apt-get install flashplugin-nonfree

-------------------------------------------------------------------------------
Support
-------------------------------------------------------------------------------

#. http://openerp.com
#. http://axelor.com

