
.. i18n: .. module:: l10n_fr_pcg
.. i18n:     :synopsis: France - Plan Comptable Général 
.. i18n:     :noindex:
.. i18n: .. 

.. module:: l10n_fr_pcg
    :synopsis: France - Plan Comptable Général 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: France - Plan Comptable Général (*l10n_fr_pcg*)
.. i18n: ===============================================
.. i18n: :Module: l10n_fr_pcg
.. i18n: :Name: France - Plan Comptable Général
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Simon JAILLET - CrysaLEAD
.. i18n: :Directory: l10n_fr_pcg
.. i18n: :Web: http://www.crysalead.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no

France - Plan Comptable Général (*l10n_fr_pcg*)
===============================================
:Module: l10n_fr_pcg
:Name: France - Plan Comptable Général
:Version: 5.0.1.0
:Author: Simon JAILLET - CrysaLEAD
:Directory: l10n_fr_pcg
:Web: http://www.crysalead.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This is the module to manage the accounting chart for France in Open ERP.
.. i18n:   
.. i18n:   Credits: Sistheo Zeekom CrysaLEAD

::

  This is the module to manage the accounting chart for France in Open ERP.
  
  Credits: Sistheo Zeekom CrysaLEAD

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_chart`
.. i18n:  * :mod:`base_vat`

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_chart`
 * :mod:`base_vat`

.. i18n: Reports
.. i18n: -------

Reports
-------

.. i18n:  * Compte de resultat
.. i18n: 
.. i18n:  * Bilan

 * Compte de resultat

 * Bilan

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

.. i18n: None

None

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Report for l10n_fr (l10n.fr.report)
.. i18n: ###########################################

Object: Report for l10n_fr (l10n.fr.report)
###########################################

.. i18n: :line_ids: Lines, one2many

:line_ids: Lines, one2many

.. i18n: :code: Code, char

:code: Code, char

.. i18n: :name: Name, char

:name: Name, char

.. i18n: Object: Report Lines for l10n_fr (l10n.fr.line)
.. i18n: ###############################################

Object: Report Lines for l10n_fr (l10n.fr.line)
###############################################

.. i18n: :definition: Definition, char

:definition: Definition, char

.. i18n: :code: Variable Name, char

:code: Variable Name, char

.. i18n: :name: Name, char

:name: Name, char

.. i18n: :report_id: Report, many2one

:report_id: Report, many2one
