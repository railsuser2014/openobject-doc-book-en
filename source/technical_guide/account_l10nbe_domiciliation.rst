
.. module:: account_l10nbe_domiciliation
    :synopsis: Account l10nbe Domiciliation 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

    <style>
      div.body p#module-account_l10nbe_domiciliation {
        display: none;
      }
    </style>

Account l10nbe Domiciliation (*account_l10nbe_domiciliation*)
=============================================================
:Module: account_l10nbe_domiciliation
:Name: Account l10nbe Domiciliation
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_l10nbe_domiciliation
:Web: http://tinyerp.com
:Is certified: no

Description
-----------

::

  Related with l10n_be module.
          Adds Domiciled and Domiciled send date fields on invoice.
          Domiciliation and Domiciliation Number fields on partner.

Dependencies
------------

 * :mod:`base`
 * :mod:`account`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT account.invoice.domicile.form (form)
 * \* INHERIT supplier.invoice.domicile.form (form)
 * \* INHERIT res.partner.domicile.form (form)


Objects
-------

None
