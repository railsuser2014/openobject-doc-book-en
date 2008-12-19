
OpenERP Client Installation on Linux
++++++++++++++++++++++++++++++++++++

Perform the following steps:

 1. Install required packages
 2. Install the Open ERP Client
 3. Adjustments for users' convenience

.. describe:: Install required packages:

To install Python modules you may want to use easy_install

  * http://peak.telecommunity.com/DevCenter/EasyInstall

With Linux, the client needs the following dependences:

  * Python 2.4 or a superior version
  * GTK2.4 for Python (must match the version of python installed)
  * Glade2 for Python (must match the version of python installed)
  * a PDF viewer (eg. Xpdf, acroread)

See below on how to install these packages for your Linux distribution.

.. describe:: Install Open ERP Client:

Note: If you only want to test the client, you do not need to install it. Just unpack the
archive and start bin/tinyerp-client'.

Unpack the client archive and copy the contents to a place you like. Something like: ::

  tar -xzf tinyerp-client-2.1.2.tar.gz
  su
  mkdir /opt/TinyERP/
  mv tinyerp-client-2.1.2 /opt/TinyERP/
  ln -s tinyerp-client-2.1.2 /opt/TinyERP/client

You may now start the client using ::

  /opt/TinyERP/client/bin/tinyerp-client

(For those who know Pythons distutil: Open ERP Client comes with a 'setup.py', but this
in not yet fully functional for installation.)

.. describe:: Adjustments for users convenience:

  * For your users convenience, set a link (using relative links is good style):
      ``ln -s ../../opt/TinyERP/client/bin/tinyerp-client /usr/bin/tinyerp``
  * Configuring the preview program

Open ERP by default supports xpdf, evince, gpdf and kpdf for previewing PDF and
openoffice, firefox and mozilla for previewing HTML. For both types the first in the list
which can be found will used.

If you are using a PDF viewer not in the list or want to use a specifc one, set
``softpath`` and ``softpath_html`` in the ``[printer]`` section of your ``~/.terprc``.
Like this: ::

      [printer]
      path = none
      softpath_html = konqueror
      preview = True
      softpath = kghostview

Required Packages
"""""""""""""""""

Debian
^^^^^^

For Debian distributions, you can install the necessary packages with the next order: ::

  apt-get install python2.3 python2.3-gtk2 python2.3-glade2 xpdf

Mandrake 10.1
^^^^^^^^^^^^^

For Mandrake, the rpms are (version sur 10.1):

  * python (python-2.3.4-6mdk)
  * gtk+2.0 (gtk+2.0-2.4.9-9mdk)
  * pygtk2.0 (pygtk2.0-2.3.96-1mdk)
  * pygtk2.0-libglade (pygtk2.0-libglade-2.3.96-1mdk)
  * xpdf (xpdf-3.00-7mdk)

Mandriva 2005 Limited Edition (MDK 10.2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install required packages: ::

  urpmi python-2.4 gtk+2.0 pygtk2.0 pygtk2.0-libglade xpdf

You may use another PDF viewer (gpdf, kpdf or acroread) instead of xpdf.

