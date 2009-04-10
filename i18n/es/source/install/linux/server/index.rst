
.. i18n: .. index::
.. i18n:    single: Installation; Open ERP Server (Linux)
.. i18n:    single: Open ERP Server; Installation (Linux)
.. i18n: .. 

.. index::
   single: Installation; Open ERP Server (Linux)
   single: Open ERP Server; Installation (Linux)
.. 

.. i18n: .. _installation-linux-server-link:
.. i18n: 
.. i18n: Open ERP Server Installation
.. i18n: ============================

.. _installation-linux-server-link:

Open ERP Server Installation
============================

.. i18n: Installing the required packages
.. i18n: --------------------------------

Installing the required packages
--------------------------------

.. i18n: You need to install **python** (at least version 2.4).

You need to install **python** (at least version 2.4).

.. i18n: You also need to install the following python libraries:

You also need to install the following python libraries:

.. i18n:   * **psycopg2**
.. i18n:   * **reportlab**
.. i18n:   * **pychart**
.. i18n:   * **pydot**
.. i18n:   * **mxdatetime**
.. i18n:   * **xml**, **lxml** and **libxslt1**
.. i18n:   * **tz** (timezone library)
.. i18n:   * **PIL**: Python Imaging Library (required for *reportlab*)
.. i18n:   * **vobject**: iCalendar and VCards parsing

  * **psycopg2**
  * **reportlab**
  * **pychart**
  * **pydot**
  * **mxdatetime**
  * **xml**, **lxml** and **libxslt1**
  * **tz** (timezone library)
  * **PIL**: Python Imaging Library (required for *reportlab*)
  * **vobject**: iCalendar and VCards parsing

.. i18n: Example on Ubuntu
.. i18n: +++++++++++++++++

Example on Ubuntu
+++++++++++++++++

.. i18n: On Ubuntu, these libraries are available in the following packages:

On Ubuntu, these libraries are available in the following packages:

.. i18n:   * python
.. i18n:   * python-psycopg2
.. i18n:   * python-reportlab
.. i18n:   * python-pychart
.. i18n:   * python-pydot
.. i18n:   * python-egenix-mxdatetime
.. i18n:   * python-xml
.. i18n:   * python-lxml
.. i18n:   * python-libxslt1
.. i18n:   * python-tz
.. i18n:   * python-imaging
.. i18n:   * python-vobject

  * python
  * python-psycopg2
  * python-reportlab
  * python-pychart
  * python-pydot
  * python-egenix-mxdatetime
  * python-xml
  * python-lxml
  * python-libxslt1
  * python-tz
  * python-imaging
  * python-vobject

.. i18n: To install the required libraries, you can do the following in your favorite
.. i18n: shell: ::
.. i18n: 
.. i18n:     sudo apt-get install python python-psycopg2 python-reportlab \
.. i18n:          python-egenix-mxdatetime python-xml python-tz python-pychart \
.. i18n:          python-pydot python-lxml python-libxslt1 python-vobject

To install the required libraries, you can do the following in your favorite
shell: ::

    sudo apt-get install python python-psycopg2 python-reportlab \
         python-egenix-mxdatetime python-xml python-tz python-pychart \
         python-pydot python-lxml python-libxslt1 python-vobject

.. i18n: .. note::
.. i18n: 
.. i18n:     There is no need to explicitly install *python-imaging* since it's required
.. i18n:     by *python-reportlab*. The *apt-get* utility will install all these
.. i18n:     packages with their required dependencies.

.. note::

    There is no need to explicitly install *python-imaging* since it's required
    by *python-reportlab*. The *apt-get* utility will install all these
    packages with their required dependencies.

.. i18n: Downloading the Open ERP Server
.. i18n: -------------------------------

Downloading the Open ERP Server
-------------------------------

.. i18n: The OpenERP server can be downloaded from
.. i18n: the `OpenERP website's download page <http://www.openerp.com/index.php?option=com_content&view=article&id=18&Itemid=28>`_

The OpenERP server can be downloaded from
the `OpenERP website's download page <http://www.openerp.com/index.php?option=com_content&view=article&id=18&Itemid=28>`_

.. i18n: Testing the Open ERP Server
.. i18n: ---------------------------

Testing the Open ERP Server
---------------------------

.. i18n: .. note::
.. i18n: 
.. i18n:     If you only want to test the server, you do not need to install it. Just unpack the
.. i18n:     archive and start the openerp-server executable: ::
.. i18n: 
.. i18n:         tar -xzf openerp-server-5.0.0.tar.gz
.. i18n:         cd openerp-server-5.0.0/bin
.. i18n:         python openerp-server.py

.. note::

    If you only want to test the server, you do not need to install it. Just unpack the
    archive and start the openerp-server executable: ::

        tar -xzf openerp-server-5.0.0.tar.gz
        cd openerp-server-5.0.0/bin
        python openerp-server.py

.. i18n: The list of available command line parameters can be obtained with the ``-h``
.. i18n: command line switch: ::
.. i18n: 
.. i18n:     python openerp-server.py -h

The list of available command line parameters can be obtained with the ``-h``
command line switch: ::

    python openerp-server.py -h

.. i18n: Installing the Open ERP Server
.. i18n: ------------------------------

Installing the Open ERP Server
------------------------------

.. i18n: The Open ERP Server can be installed very easily using the *setup.py* file: ::
.. i18n: 
.. i18n:     tar -xzf openerp-server-5.0.0.tar.gz
.. i18n:     cd openerp-server-5.0.0
.. i18n:     sudo python setup.py install

The Open ERP Server can be installed very easily using the *setup.py* file: ::

    tar -xzf openerp-server-5.0.0.tar.gz
    cd openerp-server-5.0.0
    sudo python setup.py install

.. i18n: If your PostgreSQL server is up and running, you can now run the server using
.. i18n: the following command: ::
.. i18n: 
.. i18n:     openerp-server

If your PostgreSQL server is up and running, you can now run the server using
the following command: ::

    openerp-server

.. i18n: If you don't already have a PostgreSQL server up and running, you can read
.. i18n: the :ref:`postgresql-server-installation`.

If you don't already have a PostgreSQL server up and running, you can read
the :ref:`postgresql-server-installation`.
