=======================
Development Environment
=======================


Working with Launchpad
======================

Getting the sources
-------------------

Get Bazaar version control to pull the source from Launchpad.

To install bazaar on any ubuntu distribution, you can edit /etc/apt/sources.list by

::

  sudo gedit /etc/apt/sources.list

and put these lines in it:

::

  deb http://ppa.launchpad.net/bzr/ubuntu intrepid main
  deb-src http://ppa.launchpad.net/bzr/ubuntu intrepid main

Then, do the following

::

  sudo apt-get install bzr

To work correctly, bzr version must be at least 1.3. Check it with the command:

::

  bzr --version

If you don't have at least 1.3 version, you can check this url: http://bazaar-vcs.org/Download
On debian, in any distribution, the 1.5 version is working, you can get it on this url: http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb

If you experience problems with Bazaar, please read the :ref:`bazaar-faq-link` before asking any questions.


Create an account on Launchpad
------------------------------

Before you can commit on launchpad, you need to create a login.

Go to: https://launchpad.net --> log in / register on top right.

You enter your e-mail address and you wait for an e-mail which will guide you trough the process needed to create your login.

This login is only needed if you intend to commit on bazaar on openerp-commiter or on your own branch.


Pushing a new branch
--------------------

You may have to create an account on
launchpad first, register your public key, and subscribe to the `openerp-community <https://launchpad.net/~openerp-community>`_ team. Then, you
can push your branch. Suppose you want to push your addons::

  cd addons
  bzr push lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
  bzr bind lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME

After having done that, your branch is public on Launchpad, in the `OpenObject
project <https://code.launchpad.net/openobject>`_, and commiters can work on
it, review it and propose for integration in the official branch. The last line
allows you to rebind your branch to the one which is on launchpad, after having
done this, your commit will be applied on launchpad directly (unless you use ``--local``)


Development Environment
=======================
        **remaining** (Not any Exact idea about what to put)
        
Configuration
=============

        **remaining** (Config for : bzr or tiny)
        
Command Line Options
====================

        **remaining** (Options for : bzr or tiny)


Open ERP Server & Web Client
============================
        **remaining** (intro/installation/other???)

