
.. _bazaar-link:

Bazaar, the version control system
----------------------------------

The new development process uses Bazaar via launchpad.net instead of Subversion.
Bazaar offers a flexibility with this distributed model. You can see our
branches on https://code.launchpad.net/~openerp.

.. describe:: Explanation of directories:

Two teams have been created on launchpad:

  * OpenERP quality teams --> they can commit on:

    - lp:~openerp/openobject-addons/4.2
    - lp:~openerp/openobject-addons/trunk
    - lp:~openerp/openobject-addons/4.2-extra-addons
    - lp:~openerp/openobject-addons/trunk-extra-addons
    - lp:~openerp/openobject-bi/trunk-addons
    - lp:~openerp/openobject-bi/trunk-cli
    - lp:~openerp/openobject-bi/trunk-client-web
    - lp:~openerp/openobject-client/4.2
    - lp:~openerp/openobject-client/trunk
    - lp:~openerp/openobject-client-web/4.2
    - lp:~openerp/openobject-client-web/trunk
    - lp:~openerp/openobject-server/4.2
    - lp:~openerp/openobject-server/trunk

  * 0penERP-commiter --> they can commit on:

    - lp:~openerp/openobject-addons/4.2-extra-addons
    - lp:~openerp/openobject-addons/trunk-extra-addons

In this group, we include some of our partners who will be selected on a meritocracy basis by the quality team.

  * Contributors --> they can commit on:

    - lp:~openerp-community

.. describe:: How can I be included in OpenERP-commiter team ?

Any contributor who is interested to become a commiter must show his interest
on working for openerp project and his ability to do it in a proper way as the
selection for this group is based on meritocracy. It can be by proposing bug
fixes, features requested on our :ref:`bug tracker <bug-tracker-link>` system.
You can even suggest additional modules and/or functionalities on our :ref:`bug
tracker <bug-tracker-link>` system.

.. describe:: How can I suggest some additionals modules or functionalities ?

To create some additionals modules and/or functionnalities and include them in
the project, this is the way to do:

  #. open a branch in launchpad
  #. report and suggest your work via your new branch to our :ref:`bug tracker
     <bug-tracker-link>` system (there are two way : bugs report for bug and
     blueprint for idea / functionnality)
  #. wait for approval by our quality team

Or the quality team approved your work and merge it into the official branch
(like explained in the :ref:`bug tracker <bug-tracker-link>` section), or they
refused it and ask you to improve your work before merging it in our official
branch.

Installing Bazaar
+++++++++++++++++

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

Quick Summary
+++++++++++++

This is the official and proposed way to contribute on OpenERP and OpenObject.

To download the latest sources and create your own local branches of OpenERP, do this::

  bzr branch lp:openerp
  cd openerp
  ./bzr_set.py

This will download all the component of openerp (server, client, addons) and create links of modules in addons in your server so that you can use it directly. You can change the bzr_set.py file to select what you want to download exactly. Now, you can edit the code and commit in your local branch.::

  EDIT addons/account/account.py
  cd addons
  bzr ci -m "Testing Modifications"

Once your code is good enough and follow the :ref:`coding-guidelines-link`, you
can push your branch in launchpad. You may have to create an account on
launchpad first, register your public key, and subscribe to the `openerp-community <https://launchpad.net/~openerp-community>`_ team. Then, you
can push your branch. Suppose you want to push your addons::

  cd addons
  bzr push lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
  bzr bind lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME

After having done that, your branch is public on Launchpad, in the `OpenObject
project <https://code.launchpad.net/openobject>`_, and commiters can work on
it, review it and propose for integration in the official branch. The last line
allows you to rebind your branch to the one which is on launchpad, after having
done this, your commit will be applied on launchpad directly (unless you use ``--local``)::

  bzr pull    # Get modifications on your branch from others
  EDIT STUFF
  bzr ci    # commit your changes on your public branch

If your changes fixe a public bug on launchpad, you can use this to mark the bug as fixed by your branch::

  bzr ci --fixes=lp:453123   # Where 453123 is a bug ID

Once your branch is mature, mark it as mature in the web interface of launchpad
and request for merging in the official release. Your branch will be reviewed
by a commiter and then the quality team to be merged in the official release.

.. _how-to-get-the-latest-trunk-source-code-link:

How to get the latest trunk source code
+++++++++++++++++++++++++++++++++++++++

Get a clone of each repository::

  bzr clone lp:~openerp/openobject-server/trunk server
  bzr clone lp:~openerp/openobject-client/trunk client
  bzr clone lp:~openerp/openobject-client-web/trunk client-web
  bzr clone lp:~openerp/openobject-addons/trunk addons

If you want to get a clone of the extra-addons repository, you can execute this command::

  bzr clone lp:~openerp-commiter/openobject-addons/trunk-extra-addons extra-addons

run the setup scripts in the respective directories::

  python2.4 setup.py build
  python2.4 setup.py install

Currently the initialisation procedure of the server parameter --init=all to
populate the database seems to be broken in trunk.

It is recommended to create a new database via the gtk-client. Before that the web-client will not work.

Start OpenERP server like this: ::

  ./tinyerp-server.py --addons-path=/path/to/my/addons

The ``bin/addons`` will be considered as default addons directory which can be
overriden by the ``/path/to/my/addons/``. That is if an addon exists in
``bin/addons`` as well as ``/path/to/my/addons`` (custom path) the later one will
be given preference over the ``bin/addons`` (default path).

How to commit Your Work
+++++++++++++++++++++++

If you want to contribute on OpenERP or OpenObject, here is the proposed method:

  * You create a branch on launchpad on the project that interest you. It's
    important that you create your branch on launchpad and not on your local
    system so that we can easily merge, share code between projects and
    centralize futur developments.
  * You develop your own features or bugfixes
    in your own branch on launchpad. Don't forget to set the status of your
    branch (new, experimental, development, mature, ...) so that contributors
    knows what they can use or not.
  * Once your code is good enough, you propose your branch for merging
  * Your work will be evaluated by one responsible of the commiters team.

    - If they accept your branch for integration in the official version, they
      will submit to the quality team that will review and merge in the official
      branch.
    - If the commiter team refuses your branch, they will explain why
      so that you can review your code to better fits guidelines (problem for
      futur migrations, ...)

The extra-addons branch, that stores all extra modules, is directly accessible
to all commiters. If you are a commiter, you can work directly on this branch
and commit your own work. This branch do not require a validation of the
quality team. You should put there your special modules for your own customers.

If you want to propose or develop new modules, we suggest you to create your
own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
and develop within your branch. You can fill in a bug to request that
your modules are integrated in one of the two branches:

  * extra-addons : if your module touches a few companies
  * addons : if your module will be usefull for most of the companies

We invite all our partners and contributors to work in that way so that we can
easily integrate and share the work done between the different projects.




