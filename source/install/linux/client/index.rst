
.. _installation-linux-client-link:

OpenERP Client Installation on Linux
====================================

Installing the required packages
--------------------------------

You need to install **python** (at least version 2.4).

You also need to install the following python libraries:

  * **gtk** and **glade** (at least version 2.10)
  * **matplotlib**
  * **mxdatetime**
  * **xml**
  * **tz** (timezone library)

.. note::

    You'll also need a pdf viewer (eg. xpdf, acroread, kpdf).

    See the :ref:`Configuring a pdf viewer section <configure-pdf-viewer-link>`

Example on Ubuntu
+++++++++++++++++

On Ubuntu, these libraries are available in the following packages:

  * python
  * python-gtk2
  * python-glade2
  * python-matplotlib
  * python-egenix-mxdatetime
  * python-xml
  * python-tz

To install the required libraries, you can do the following in your favorite shell: ::

  sudo apt-get install python python-gtk2 python-glade2 \
      python-matplotlib python-egenix-mxdatetime python-xml

Downloading the Open ERP Client
-------------------------------

The OpenERP client can be downloaded from
the `OpenERP website's download page <http://www.openerp.com/index.php?option=com_content&view=article&id=18&Itemid=28>`_

Testing the Open ERP Client
---------------------------

.. note::

    If you only want to test the client, you do not need to install it. Just unpack the
    archive and start the openerp-client executable: ::

        tar -xzf openerp-client-5.0.0.tar.gz
        cd openerp-client-5.0.0/bin
        python openerp-client.py

Installing the Open ERP Client
------------------------------

The client can be installed very easily using the *setup.py* file: ::

  tar -xzf openerp-client-5.0.0.tar.gz
  cd openerp-client-5.0.0
  sudo python setup.py install

You can now run the client using the following command: ::

  openerp-client

.. _configure-pdf-viewer-link:

Configuring a pdf viewer
------------------------

Open ERP client by default supports:

 #. evince
 #. xpdf
 #. gpdf
 #. kpdf
 #. epdfview
 #. acroread

for previewing PDF. The client will try to find one of these executables (in this order) in
  your system and open the pdf document with it.

.. note::

    For example, if *xpdf*, *kpdf* and *acroread* are the only pdf viewers installed
    on your system, the Open ERP client will use *xpdf* for previewing pdf document

If you  want to use another pdf viewer or if you don't want to use the first
one the client will find. You can edit the Open ERP configuration file normally
located in ``~/.terprc``. Find the ``[printer`` section and edit the
``softpath`` parameter. For example: ::

    [printer]
    softpath = kpdf

