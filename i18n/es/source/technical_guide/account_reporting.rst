
.. i18n: .. module:: account_reporting
.. i18n:     :synopsis: Reporting of Balancesheet for accounting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: account_reporting
    :synopsis: Reporting of Balancesheet for accounting (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Reporting of Balancesheet for accounting (*account_reporting*)
.. i18n: ==============================================================
.. i18n: :Module: account_reporting
.. i18n: :Name: Reporting of Balancesheet for accounting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_reporting
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Reporting of Balancesheet for accounting (*account_reporting*)
==============================================================
:Module: account_reporting
:Name: Reporting of Balancesheet for accounting
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_reporting
:Web: 
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Financial and accounting reporting
.. i18n:       Balance Sheet Report

::

  Financial and accounting reporting
      Balance Sheet Report

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

.. i18n:  * Financial Management/Configuration/Balance Sheet Report
.. i18n:  * Financial Management/Configuration/Balance Sheet Report/Balance Sheet Report
.. i18n:  * Financial Management/Configuration/Balance Sheet Report/Balance Sheet Report Form

 * Financial Management/Configuration/Balance Sheet Report
 * Financial Management/Configuration/Balance Sheet Report/Balance Sheet Report
 * Financial Management/Configuration/Balance Sheet Report/Balance Sheet Report Form

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * account.report.bs.form (form)
.. i18n:  * account.report.report.tree.bs (tree)

 * account.report.bs.form (form)
 * account.report.report.tree.bs (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Rml Colors (color.rml)
.. i18n: ##############################

Object: Rml Colors (color.rml)
##############################

.. i18n: :code: code, char, required

:code: code, char, required

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: Object: Account reporting for Balance Sheet (account.report.bs)
.. i18n: ###############################################################

Object: Account reporting for Balance Sheet (account.report.bs)
###############################################################

.. i18n: :font_style: Font, selection

:font_style: Font, selection

.. i18n: :name: Name, char, required

:name: Name, char, required

.. i18n: :sequence: Sequence, integer

:sequence: Sequence, integer

.. i18n: :note: Note, text

:note: Note, text

.. i18n: :parent_id: Parent, many2one

:parent_id: Parent, many2one

.. i18n: :code: Code, char, required

:code: Code, char, required

.. i18n: :report_type: Report Type, selection

:report_type: Report Type, selection

.. i18n: :child_id: Childs, one2many

:child_id: Childs, one2many

.. i18n: :color_back: Back Color, many2one

:color_back: Back Color, many2one

.. i18n: :color_font: Font Color, many2one

:color_font: Font Color, many2one

.. i18n: :account_id: Accounts, many2many

:account_id: Accounts, many2many
