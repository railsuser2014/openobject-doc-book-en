
.. i18n: .. index::
.. i18n:    single: Installation; Open ERP Client (Linux)
.. i18n:    single: Open ERP Client; Installation (Linux)
.. i18n: .. 

.. index::
   single: Installation; Open ERP Client (Linux)
   single: Open ERP Client; Installation (Linux)
.. 

.. i18n: .. _installation-linux-client-link:
.. i18n: 
.. i18n: OpenERP Client Installation
.. i18n: ===========================

.. _installation-linux-client-link:

OpenERP Client Installation
===========================

.. i18n: Installing the required packages
.. i18n: --------------------------------

Installing the required packages
--------------------------------

.. i18n: You need to install **python** (at least version 2.4).

You need to install **python** (at least version 2.4).

.. i18n: You also need to install the following python libraries:

You also need to install the following python libraries:

.. i18n:   * **gtk** and **glade** (at least version 2.10)
.. i18n:   * **matplotlib**
.. i18n:   * **mxdatetime**
.. i18n:   * **xml**
.. i18n:   * **tz** (timezone library)
.. i18n:   * **hippocanvas** (Python bindings to hippo-canvas. Hippocanvas is a canvas library based on GTK+2.0, Cairo and Pango)

  * **gtk** and **glade** (at least version 2.10)
  * **matplotlib**
  * **mxdatetime**
  * **xml**
  * **tz** (timezone library)
  * **hippocanvas** (Python bindings to hippo-canvas. Hippocanvas is a canvas library based on GTK+2.0, Cairo and Pango)

.. i18n: .. note::
.. i18n: 
.. i18n:     You'll also need a pdf viewer (eg. xpdf, acroread, kpdf).
.. i18n: 
.. i18n:     See the :ref:`configure-pdf-viewer-link` Section.

.. note::

    You'll also need a pdf viewer (eg. xpdf, acroread, kpdf).

    See the :ref:`configure-pdf-viewer-link` Section.

.. i18n: Example on Ubuntu
.. i18n: +++++++++++++++++

Example on Ubuntu
+++++++++++++++++

.. i18n: On Ubuntu, these libraries are available in the following packages:

On Ubuntu, these libraries are available in the following packages:

.. i18n:   * python
.. i18n:   * python-gtk2
.. i18n:   * python-glade2
.. i18n:   * python-matplotlib
.. i18n:   * python-egenix-mxdatetime
.. i18n:   * python-xml
.. i18n:   * python-tz
.. i18n:   * python-hippocanvas

  * python
  * python-gtk2
  * python-glade2
  * python-matplotlib
  * python-egenix-mxdatetime
  * python-xml
  * python-tz
  * python-hippocanvas

.. i18n: To install the required libraries, you can do the following in your favorite shell: ::
.. i18n: 
.. i18n:   sudo apt-get install python python-gtk2 python-glade2 \
.. i18n:       python-matplotlib python-egenix-mxdatetime python-xml python-hippocanvas

To install the required libraries, you can do the following in your favorite shell: ::

  sudo apt-get install python python-gtk2 python-glade2 \
      python-matplotlib python-egenix-mxdatetime python-xml python-hippocanvas

.. i18n: Downloading the Open ERP Client
.. i18n: -------------------------------

Downloading the Open ERP Client
-------------------------------

.. i18n: The OpenERP client can be downloaded from
.. i18n: the `OpenERP website's download page <http://www.openerp.com/index.php?option=com_content&view=article&id=18&Itemid=28>`_

The OpenERP client can be downloaded from
the `OpenERP website's download page <http://www.openerp.com/index.php?option=com_content&view=article&id=18&Itemid=28>`_

.. i18n: Testing the Open ERP Client
.. i18n: ---------------------------

Testing the Open ERP Client
---------------------------

.. i18n: .. note::
.. i18n: 
.. i18n:     If you only want to test the client, you do not need to install it. Just unpack the
.. i18n:     archive and start the openerp-client executable: ::
.. i18n: 
.. i18n:         tar -xzf openerp-client-5.0.0.tar.gz
.. i18n:         cd openerp-client-5.0.0/bin
.. i18n:         python openerp-client.py

.. note::

    If you only want to test the client, you do not need to install it. Just unpack the
    archive and start the openerp-client executable: ::

        tar -xzf openerp-client-5.0.0.tar.gz
        cd openerp-client-5.0.0/bin
        python openerp-client.py

.. i18n: Installing the Open ERP Client
.. i18n: ------------------------------

Installing the Open ERP Client
------------------------------

.. i18n: The client can be installed very easily using the *setup.py* file: ::
.. i18n: 
.. i18n:   tar -xzf openerp-client-5.0.0.tar.gz
.. i18n:   cd openerp-client-5.0.0
.. i18n:   sudo python setup.py install

The client can be installed very easily using the *setup.py* file: ::

  tar -xzf openerp-client-5.0.0.tar.gz
  cd openerp-client-5.0.0
  sudo python setup.py install

.. i18n: You can now run the client using the following command: ::
.. i18n: 
.. i18n:   openerp-client

You can now run the client using the following command: ::

  openerp-client

.. i18n: .. index::
.. i18n:    single: Open ERP Client; Configuring a pdf viewer
.. i18n:    single: pdf viewer
.. i18n: .. 

.. index::
   single: Open ERP Client; Configuring a pdf viewer
   single: pdf viewer
.. 

.. i18n: .. _configure-pdf-viewer-link:
.. i18n: 
.. i18n: Configuring a pdf viewer
.. i18n: ------------------------

.. _configure-pdf-viewer-link:

Configuring a pdf viewer
------------------------

.. i18n: Open ERP client by default supports:

Open ERP client by default supports:

.. i18n:  #. evince
.. i18n:  #. xpdf
.. i18n:  #. gpdf
.. i18n:  #. kpdf
.. i18n:  #. epdfview
.. i18n:  #. acroread

 #. evince
 #. xpdf
 #. gpdf
 #. kpdf
 #. epdfview
 #. acroread

.. i18n: for previewing PDF. The client will try to find one of these executables (in this order) in
.. i18n:   your system and open the pdf document with it.

for previewing PDF. The client will try to find one of these executables (in this order) in
  your system and open the pdf document with it.

.. i18n: .. note::
.. i18n: 
.. i18n:     For example, if *xpdf*, *kpdf* and *acroread* are the only pdf viewers installed
.. i18n:     on your system, the Open ERP client will use *xpdf* for previewing pdf document

.. note::

    For example, if *xpdf*, *kpdf* and *acroread* are the only pdf viewers installed
    on your system, the Open ERP client will use *xpdf* for previewing pdf document

.. i18n: If you  want to use another pdf viewer or if you don't want to use the first
.. i18n: one the client will find. You can edit the Open ERP configuration file normally
.. i18n: located in ``~/.terprc``. Find the ``[printer]`` section and edit the
.. i18n: ``softpath`` parameter. For example: ::
.. i18n: 
.. i18n:     [printer]
.. i18n:     softpath = kpdf

If you  want to use another pdf viewer or if you don't want to use the first
one the client will find. You can edit the Open ERP configuration file normally
located in ``~/.terprc``. Find the ``[printer]`` section and edit the
``softpath`` parameter. For example: ::

    [printer]
    softpath = kpdf
