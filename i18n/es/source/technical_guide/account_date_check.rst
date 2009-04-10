
.. i18n: .. module:: account_date_check
.. i18n:     :synopsis: Account Date check (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: account_date_check
    :synopsis: Account Date check (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Account Date check (*account_date_check*)
.. i18n: =========================================
.. i18n: :Module: account_date_check
.. i18n: :Name: Account Date check
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_date_check
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Account Date check (*account_date_check*)
=========================================
:Module: account_date_check
:Name: Account Date check
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_date_check
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   * Adds a field on journals: "Allows date not in the period"
.. i18n:       * By default, this field is checked.
.. i18n:   
.. i18n:   If this field is not checked, the system control that the date is in the period when you create 
.. i18n:   an account entry. Otherwise, it generates an
.. i18n:   error message: "The date of your account move is not in the defined period !"

::

  * Adds a field on journals: "Allows date not in the period"
      * By default, this field is checked.
  
  If this field is not checked, the system control that the date is in the period when you create 
  an account entry. Otherwise, it generates an
  error message: "The date of your account move is not in the defined period !"

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`account`

 * :mod:`account`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n: None

None

.. i18n: Menus
.. i18n: -------

Menus
-------

.. i18n: None

None

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * \* INHERIT account.journal.form.inherit2 (form)

 * \* INHERIT account.journal.form.inherit2 (form)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: None

None
