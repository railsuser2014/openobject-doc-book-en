
.. _installation-linux-client-link:

OpenERP Client Installation on Linux
====================================

Install the required packages
-----------------------------

You need to install **python** (at least version 2.4).

You also need to install the following python libraries:

  * **gtk** and **glade** (at least version 2.10)
  * **matplotlib**
  * **mxdatetime**
  * **xml**
  * **tz** (timezone library)

Exemple on Ubuntu
+++++++++++++++++

On Ubuntu, these libraries are available in the following packages:

  * python (at least version 2.4)
  * python-gtk2
  * python-glade2
  * python-matplotlib
  * python-egenix-mxdatetime
  * python-xml
  * python-tz

To install the required libraries, you can do the following in your favorite shell: ::

  sudo apt-get install python python-gtk2 python-glade2 python-matplotlib python-egenix-mxdatetime python-xml

Install the Open ERP Client
---------------------------

The OpenERP client can be downloaded from
the `OpenERP website's download page <http://www.openerp.com/index.php?option=com_content&view=article&id=18&Itemid=28>`_

The client can be installed very easily using the *setup.py* file: ::

  tar -xzf openerp-client-5.0.0.tar.gz
  cd openerp-client-5.0.0
  sudo python setup.py install

You can now run the client using the following command: ::

  openerp-client


