
.. i18n: Improving Translations
.. i18n: ----------------------

Improving Translations
----------------------

.. i18n: Translating in launchpad
.. i18n: ++++++++++++++++++++++++

Translating in launchpad
++++++++++++++++++++++++

.. i18n: Translations are managed by 
.. i18n: the `Launchpad Web interface <https://translations.launchpad.net/openobject>`_. Here, you'll
.. i18n: find the list of translatable projects.

Translations are managed by 
the `Launchpad Web interface <https://translations.launchpad.net/openobject>`_. Here, you'll
find the list of translatable projects.

.. i18n: Please read the `FAQ <https://answers.launchpad.net/rosetta/+faqs>`_ before asking questions.

Please read the `FAQ <https://answers.launchpad.net/rosetta/+faqs>`_ before asking questions.

.. i18n: Translating your own module
.. i18n: +++++++++++++++++++++++++++

Translating your own module
+++++++++++++++++++++++++++

.. i18n: .. versionchanged:: 5.0

.. versionchanged:: 5.0

.. i18n: Contrary to the 4.2.x version, the translations are now done by module. So,
.. i18n: instead of an unique ``i18n`` folder for the whole application, each module has
.. i18n: its own ``i18n`` folder. In addition, OpenERP can now deal with ``.po`` [#f_po]_
.. i18n: files as import/export format. The translation files of the installed languages
.. i18n: are automatically loaded when installing or updating a module. OpenERP can also
.. i18n: generate a .tgz archive containing well organised ``.po`` files for each selected
.. i18n: module.

Contrary to the 4.2.x version, the translations are now done by module. So,
instead of an unique ``i18n`` folder for the whole application, each module has
its own ``i18n`` folder. In addition, OpenERP can now deal with ``.po`` [#f_po]_
files as import/export format. The translation files of the installed languages
are automatically loaded when installing or updating a module. OpenERP can also
generate a .tgz archive containing well organised ``.po`` files for each selected
module.

.. i18n: .. [#f_po] http://www.gnu.org/software/autoconf/manual/gettext/PO-Files.html#PO-Files

.. [#f_po] http://www.gnu.org/software/autoconf/manual/gettext/PO-Files.html#PO-Files
