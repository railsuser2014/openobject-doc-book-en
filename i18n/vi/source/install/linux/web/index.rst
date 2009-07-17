
.. i18n: .. index::
.. i18n:    single: Installation; Open ERP Web (Linux)
.. i18n:    single: Open ERP Web; Installation (Linux)
.. i18n: .. 

.. index::
   single: Installation; Open ERP Web (Linux)
   single: Open ERP Web; Installation (Linux)
.. 

.. i18n: .. _installation-linux-web-link:
.. i18n: 
.. i18n: ===============================================================================
.. i18n: OpenERP Web Installation
.. i18n: ===============================================================================

.. _installation-linux-web-link:

===============================================================================
OpenERP Web Installation
===============================================================================

.. i18n: Here is the installation instructions for Debian based Linux distributions.
.. i18n: Tested on Debian Etch and Ubuntu Hardy. The procedure might work with other
.. i18n: Linux or similar distributions. See the docs on how to install the specified
.. i18n: Packages on your favourite distribution.

Here is the installation instructions for Debian based Linux distributions.
Tested on Debian Etch and Ubuntu Hardy. The procedure might work with other
Linux or similar distributions. See the docs on how to install the specified
Packages on your favourite distribution.

.. i18n: -------------------------------------------------------------------------------
.. i18n: Prerequisites
.. i18n: -------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Prerequisites
-------------------------------------------------------------------------------

.. i18n: #. Python >= 2.4
.. i18n: #. TurboGears >= 1.0.7, < 1.1b1

#. Python >= 2.4
#. TurboGears >= 1.0.7, < 1.1b1

.. i18n: -------------------------------------------------------------------------------
.. i18n: TurboGears
.. i18n: -------------------------------------------------------------------------------

-------------------------------------------------------------------------------
TurboGears
-------------------------------------------------------------------------------

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ sudo apt-get install python-setuptools
.. i18n:     $ sudo easy_install TurboGears==1.0.8

.. code-block:: bash

    $ sudo apt-get install python-setuptools
    $ sudo easy_install TurboGears==1.0.8

.. i18n: or

or

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ wget http://peak.telecommunity.com/dist/ez_setup.py
.. i18n:     $ sudo python ez_setup.py
.. i18n:     $ sudo easy_install TurboGears==1.0.8

.. code-block:: bash

    $ wget http://peak.telecommunity.com/dist/ez_setup.py
    $ sudo python ez_setup.py
    $ sudo easy_install TurboGears==1.0.8

.. i18n: Check whether TurboGears is properly installed or not...

Check whether TurboGears is properly installed or not...

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ tg-admin info

.. code-block:: bash

    $ tg-admin info

.. i18n: You should see version information of TurboGears and related packages.

You should see version information of TurboGears and related packages.

.. i18n: -------------------------------------------------------------------------------
.. i18n: OpenERP Web
.. i18n: -------------------------------------------------------------------------------

-------------------------------------------------------------------------------
OpenERP Web
-------------------------------------------------------------------------------

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ sudo easy_install -U openerp-web

.. code-block:: bash

    $ sudo easy_install -U openerp-web

.. i18n: -------------------------------------------------------------------------------
.. i18n: Configuration
.. i18n: -------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Configuration
-------------------------------------------------------------------------------

.. i18n: Locate the *config/default.cfg* in the installed *EGG*, and make appropriate
.. i18n: changes, especially:

Locate the *config/default.cfg* in the installed *EGG*, and make appropriate
changes, especially:

.. i18n: .. code-block:: ini
.. i18n: 
.. i18n:     [openerp]
.. i18n:     server = "localhost"
.. i18n:     port = 8070
.. i18n:     protocol = "socket"

.. code-block:: ini

    [openerp]
    server = "localhost"
    port = 8070
    protocol = "socket"

.. i18n: where:

where:

.. i18n:     | ``server`` is the OpenERP server host...
.. i18n:     | ``port`` is the OpenERP server port...
.. i18n:     | ``protocol`` is the protocol to be used (socket, http or https)

    | ``server`` is the OpenERP server host...
    | ``port`` is the OpenERP server port...
    | ``protocol`` is the protocol to be used (socket, http or https)

.. i18n: Now start the web server with ``start-openerp-web`` command:

Now start the web server with ``start-openerp-web`` command:

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ start-openerp-web

.. code-block:: bash

    $ start-openerp-web

.. i18n: If you see message showing ``cherrypy._cperror.NotReady: Port not free.`` then
.. i18n: make sure no other application is running on the specified port (8080 is default).

If you see message showing ``cherrypy._cperror.NotReady: Port not free.`` then
make sure no other application is running on the specified port (8080 is default).

.. i18n: You can change port for by changing ``server.socket_port`` value in *config/default.cfg*.

You can change port for by changing ``server.socket_port`` value in *config/default.cfg*.

.. i18n: If everything is fine, open your favourite web browser and type http://localhost:8080,
.. i18n: and your can see welcome page with login screen.

If everything is fine, open your favourite web browser and type http://localhost:8080,
and your can see welcome page with login screen.

.. i18n: Please make sure cookies are enabled in your browser.

Please make sure cookies are enabled in your browser.

.. i18n: Of course, OpenERP Server must be running at that time. You should create a
.. i18n: database from the DBAdmin interface by clicking on Manage button that you can
.. i18n: see besides the Database selection box. After creating a new database login
.. i18n: with the admin/admin or demo/demo to see OpenERP in action...

Of course, OpenERP Server must be running at that time. You should create a
database from the DBAdmin interface by clicking on Manage button that you can
see besides the Database selection box. After creating a new database login
with the admin/admin or demo/demo to see OpenERP in action...

.. i18n: .. warning::
.. i18n: 
.. i18n:     Please make sure that the system time is properly set otherwise web browsers
.. i18n:     might fail to establish sessions. We strongly recommend you to synchronize
.. i18n:     system clock with NTP...

.. warning::

    Please make sure that the system time is properly set otherwise web browsers
    might fail to establish sessions. We strongly recommend you to synchronize
    system clock with NTP...

.. i18n: -------------------------------------------------------------------------------
.. i18n: Run as service (daemon)
.. i18n: -------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Run as service (daemon)
-------------------------------------------------------------------------------

.. i18n: This has been tested on *ubuntu* only.

This has been tested on *ubuntu* only.

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ sudo cp /path/to/openerp_web-5.0-py2.5.egg/scripts/openerp-web /etc/init.d
.. i18n:     $ sudo cp /path/to/openerp_web-5.0-py2.5.egg/config/default.cfg /etc/openerp-web.cfg
.. i18n:     $ sudo chmod +x /etc/init.d/openerp-web

.. code-block:: bash

    $ sudo cp /path/to/openerp_web-5.0-py2.5.egg/scripts/openerp-web /etc/init.d
    $ sudo cp /path/to/openerp_web-5.0-py2.5.egg/config/default.cfg /etc/openerp-web.cfg
    $ sudo chmod +x /etc/init.d/openerp-web

.. i18n: edit */etc/init.d/openerp-web*:

edit */etc/init.d/openerp-web*:

.. i18n: .. code-block:: ini
.. i18n: 
.. i18n:     USER="terp"

.. code-block:: ini

    USER="terp"

.. i18n: and */etc/openerp-web.cfg*:

and */etc/openerp-web.cfg*:

.. i18n: .. code-block:: ini
.. i18n: 
.. i18n:     args="('server.log',)" ==> args="('/var/log/openerp-web.log',)"

.. code-block:: ini

    args="('server.log',)" ==> args="('/var/log/openerp-web.log',)"

.. i18n: Create ``/var/log/openerp-web.log`` with proper ownership

Create ``/var/log/openerp-web.log`` with proper ownership

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ sudo touch /var/log/openerp-web.log
.. i18n:     $ sudo chown terp /var/log/openerp-web.log

.. code-block:: bash

    $ sudo touch /var/log/openerp-web.log
    $ sudo chown terp /var/log/openerp-web.log

.. i18n: Now run following command to start the OpenERP Web automatically on system
.. i18n: startup (Debian/Ubuntu).

Now run following command to start the OpenERP Web automatically on system
startup (Debian/Ubuntu).

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ sudo update-rc.d openerp-web defaults

.. code-block:: bash

    $ sudo update-rc.d openerp-web defaults

.. i18n: Start the deamon:

Start the deamon:

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ sudo /etc/init.d/openerp-web start

.. code-block:: bash

    $ sudo /etc/init.d/openerp-web start

.. i18n: .. note::
.. i18n: 
.. i18n:      The init script is compatible with all major Linux distributions. Please
.. i18n:      check docs of your distribution on how to enable services.

.. note::

     The init script is compatible with all major Linux distributions. Please
     check docs of your distribution on how to enable services.

.. i18n: -------------------------------------------------------------------------------
.. i18n: Configure HTTPS
.. i18n: -------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Configure HTTPS
-------------------------------------------------------------------------------

.. i18n: The following text describes how to configure OpenERP Web for production
.. i18n: environment over HTTPS with Apache2.

The following text describes how to configure OpenERP Web for production
environment over HTTPS with Apache2.

.. i18n: **mod_proxy + mod_ssl (Apache2)**

**mod_proxy + mod_ssl (Apache2)**

.. i18n: See `Apache manual <http://httpd.apache.org/docs/>`_ for more information.

See `Apache manual <http://httpd.apache.org/docs/>`_ for more information.

.. i18n: **Apache configuration**

**Apache configuration**

.. i18n: .. code-block:: apache
.. i18n: 
.. i18n:     <VirtualHost *:443>
.. i18n: 
.. i18n:         SSLEngine on
.. i18n:         SSLCertificateFile /etc/apache2/ssl/apache.pem
.. i18n: 
.. i18n:         <Proxy *>
.. i18n:             Order deny,allow
.. i18n:             Allow from all
.. i18n:         </Proxy>
.. i18n: 
.. i18n:         ProxyRequests Off
.. i18n: 
.. i18n:         ProxyPass        /   http://127.0.0.1:8080/
.. i18n:         ProxyPassReverse /   http://127.0.0.1:8080/
.. i18n: 
.. i18n:     </VirtualHost>

.. code-block:: apache

    <VirtualHost *:443>

        SSLEngine on
        SSLCertificateFile /etc/apache2/ssl/apache.pem

        <Proxy *>
            Order deny,allow
            Allow from all
        </Proxy>

        ProxyRequests Off

        ProxyPass        /   http://127.0.0.1:8080/
        ProxyPassReverse /   http://127.0.0.1:8080/

    </VirtualHost>

.. i18n: **OpenERP Web configuration**

**OpenERP Web configuration**

.. i18n: .. code-block:: ini
.. i18n: 
.. i18n:     base_url_filter.on = True
.. i18n:     base_url_filter.use_x_forwarded_host = False
.. i18n:     base_url_filter.base_url = "https://www.example.com"

.. code-block:: ini

    base_url_filter.on = True
    base_url_filter.use_x_forwarded_host = False
    base_url_filter.base_url = "https://www.example.com"

.. i18n: **Block the OpenERP Web server port (firewall)**

**Block the OpenERP Web server port (firewall)**

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ iptables -A INPUT -i lo -j ACCEPT
.. i18n:     $ iptables -A INPUT -p tcp --dport 8080 -j REJECT

.. code-block:: bash

    $ iptables -A INPUT -i lo -j ACCEPT
    $ iptables -A INPUT -p tcp --dport 8080 -j REJECT

.. i18n: .. note::
.. i18n: 
.. i18n:     Don't block the localhost/121.0.0.1 (the first rule)

.. note::

    Don't block the localhost/121.0.0.1 (the first rule)

.. i18n: .. note::
.. i18n: 
.. i18n:     This method only works if you want your OpenERP Web application at the
.. i18n:     root of your server (https://www.example.com) and can't be deployed under
.. i18n:     a subdirectory, e.g. http://www.example.com/openerp.
.. i18n: 
.. i18n:     To overcome with the issue you can go with `subdomain`, like:
.. i18n: 
.. i18n:         https://openerp.example.com

.. note::

    This method only works if you want your OpenERP Web application at the
    root of your server (https://www.example.com) and can't be deployed under
    a subdirectory, e.g. http://www.example.com/openerp.

    To overcome with the issue you can go with `subdomain`, like:

        https://openerp.example.com

.. i18n: -------------------------------------------------------------------------------
.. i18n: Web Browser Compatibilities
.. i18n: -------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Web Browser Compatibilities
-------------------------------------------------------------------------------

.. i18n: Supported browsers
.. i18n: ++++++++++++++++++

Supported browsers
++++++++++++++++++

.. i18n: *OpenERP Web* is known to work best with *Mozilla* based web browsers. Here is
.. i18n: the list of supported browsers.

*OpenERP Web* is known to work best with *Mozilla* based web browsers. Here is
the list of supported browsers.

.. i18n: #. Firefox >= 1.5
.. i18n: #. Internet Explorer >= 6.0
.. i18n: #. Safari >= 3.0
.. i18n: #. Google Chrome >= 1.0
.. i18n: #. Opera >= 9.0

#. Firefox >= 1.5
#. Internet Explorer >= 6.0
#. Safari >= 3.0
#. Google Chrome >= 1.0
#. Opera >= 9.0

.. i18n: Flash plugin
.. i18n: ++++++++++++

Flash plugin
++++++++++++

.. i18n: Your browser should have the Flash plugin installed because *OpenERP Web* uses
.. i18n: some Flash components.

Your browser should have the Flash plugin installed because *OpenERP Web* uses
some Flash components.

.. i18n: Here is how to install the Flash plugin on an Ubuntu system:

Here is how to install the Flash plugin on an Ubuntu system:

.. i18n: .. code-block:: bash
.. i18n: 
.. i18n:     $ sudo apt-get install flashplugin-nonfree

.. code-block:: bash

    $ sudo apt-get install flashplugin-nonfree

.. i18n: -------------------------------------------------------------------------------
.. i18n: Support
.. i18n: -------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Support
-------------------------------------------------------------------------------

.. i18n: #. http://openerp.com
.. i18n: #. http://axelor.com

#. http://openerp.com
#. http://axelor.com
