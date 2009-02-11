
.. index::
   single: Installation; Open ERP Server (Linux)
   single: Open ERP Server; Installation (Linux)
.. 

.. _installation-linux-server-link:

Open ERP Server Installation
============================

Installing the required packages
--------------------------------

You need to install **python** (at least version 2.4).

You also need to install the following python libraries:

  * **psycopg2**
  * **reportlab**
  * **pychart**
  * **pydot**
  * **mxdatetime**
  * **xml**, **lxml** and **libxslt1**
  * **tz** (timezone library)
  * **PIL**: Python Imaging Library (required for *reportlab*)

Example on Ubuntu
+++++++++++++++++

On Ubuntu, these libraries are available in the following packages:

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

To install the required libraries, you can do the following in your favorite
shell: ::

    sudo apt-get install python python-psycopg2 python-reportlab \
         python-egenix-mxdatetime python-xml python-tz python-pychart \
         python-pydot python-lxml python-libxslt1

.. note::

    There is no need to explicitly install *python-imaging* since it's required
    by *python-reportlab*. The *apt-get* utility will install all these
    packages with their required dependencies.

Downloading the Open ERP Server
-------------------------------

The OpenERP server can be downloaded from
the `OpenERP website's download page <http://www.openerp.com/index.php?option=com_content&view=article&id=18&Itemid=28>`_

Testing the Open ERP Server
---------------------------

.. note::

    If you only want to test the server, you do not need to install it. Just unpack the
    archive and start the openerp-server executable: ::

        tar -xzf openerp-server-5.0.0.tar.gz
        cd openerp-server-5.0.0/bin
        python openerp-server.py

The list of available command line parameters can be obtained with the ``-h``
command line switch: ::

    python openerp-server.py -h

Installing the Open ERP Server
------------------------------

The Open ERP Server can be installed very easily using the *setup.py* file: ::

    tar -xzf openerp-server-5.0.0.tar.gz
    cd openerp-server-5.0.0
    sudo python setup.py install

If your PostgreSQL server is up and running, you can now run the server using
the following command: ::

    openerp-server

If you don't already have a PostgreSQL server up and running, you can read
the :ref:`postgresql-server-installation`.


