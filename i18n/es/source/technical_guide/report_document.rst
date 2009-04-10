
.. i18n: .. module:: report_document
.. i18n:     :synopsis: Document Management - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 

.. module:: report_document
    :synopsis: Document Management - Reporting (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Document Management - Reporting (*report_document*)
.. i18n: ===================================================
.. i18n: :Module: report_document
.. i18n: :Name: Document Management - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_document
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes

Document Management - Reporting (*report_document*)
===================================================
:Module: report_document
:Name: Document Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_document
:Web: 
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Reporting for the Document Management module:
.. i18n:       * My Files
.. i18n:       * All users Files

::

  Reporting for the Document Management module:
      * My Files
      * All users Files

.. i18n: Dependencies
.. i18n: ------------

Dependencies
------------

.. i18n:  * :mod:`document`

 * :mod:`document`

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

.. i18n:  * Document Management
.. i18n:  * Document Management/Reporting
.. i18n:  * Document Management/Reporting/This Month
.. i18n:  * Document Management/Reporting/This Month/My files
.. i18n:  * Document Management/Reporting/All Months
.. i18n:  * Document Management/Reporting/All Months/My files
.. i18n:  * Document Management/Reporting/This Month/All Users files
.. i18n:  * Document Management/Reporting/All Months/All Users files
.. i18n:  * Document Management/Reporting/Wall of Shame

 * Document Management
 * Document Management/Reporting
 * Document Management/Reporting/This Month
 * Document Management/Reporting/This Month/My files
 * Document Management/Reporting/All Months
 * Document Management/Reporting/All Months/My files
 * Document Management/Reporting/This Month/All Users files
 * Document Management/Reporting/All Months/All Users files
 * Document Management/Reporting/Wall of Shame

.. i18n: Views
.. i18n: -----

Views
-----

.. i18n:  * report.document.user.form (form)
.. i18n:  * report.document.user.tree (tree)
.. i18n:  * report.document.wall.form (form)
.. i18n:  * report.document.wall.tree (tree)
.. i18n:  * report.document.resource.graph (graph)
.. i18n:  * report.document.user.graph (graph)
.. i18n:  * report.document.user.tree (tree)
.. i18n:  * report.file.month.graph (graph)
.. i18n:  * report.file.month.tree (tree)
.. i18n:  * report.document.user.graph (graph)
.. i18n:  * view.files.partner.graph (graph)
.. i18n:  * view.files.partner.tree (tree)

 * report.document.user.form (form)
 * report.document.user.tree (tree)
 * report.document.wall.form (form)
 * report.document.wall.tree (tree)
 * report.document.resource.graph (graph)
 * report.document.user.graph (graph)
 * report.document.user.tree (tree)
 * report.file.month.graph (graph)
 * report.file.month.tree (tree)
 * report.document.user.graph (graph)
 * view.files.partner.graph (graph)
 * view.files.partner.tree (tree)

.. i18n: Objects
.. i18n: -------

Objects
-------

.. i18n: Object: Files details by Users (report.document.user)
.. i18n: #####################################################

Object: Files details by Users (report.document.user)
#####################################################

.. i18n: :partner: Partner, char, readonly

:partner: Partner, char, readonly

.. i18n: :file_title: File Name, char, readonly

:file_title: File Name, char, readonly

.. i18n: :user_id: Owner, integer, readonly

:user_id: Owner, integer, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :nbr: # of Files, integer, readonly

:nbr: # of Files, integer, readonly

.. i18n: :month: Month, char, readonly

:month: Month, char, readonly

.. i18n: :change_date: Modified Date, datetime, readonly

:change_date: Modified Date, datetime, readonly

.. i18n: :user: User, char, readonly

:user: User, char, readonly

.. i18n: :file_size: File Size, integer, readonly

:file_size: File Size, integer, readonly

.. i18n: :directory: Directory, char, readonly

:directory: Directory, char, readonly

.. i18n: :create_date: Date Created, datetime, readonly

:create_date: Date Created, datetime, readonly

.. i18n: :type: Directory Type, char, readonly

:type: Directory Type, char, readonly

.. i18n: Object: Files details by Partners (report.files.partner)
.. i18n: ########################################################

Object: Files details by Partners (report.files.partner)
########################################################

.. i18n: :file_title: File Name, char, readonly

:file_title: File Name, char, readonly

.. i18n: :create_date: Date Created, datetime, readonly

:create_date: Date Created, datetime, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :nbr: # of Files, integer, readonly

:nbr: # of Files, integer, readonly

.. i18n: :change_date: Modified Date, datetime, readonly

:change_date: Modified Date, datetime, readonly

.. i18n: :file_size: File Size, integer, readonly

:file_size: File Size, integer, readonly

.. i18n: :directory: Directory, char, readonly

:directory: Directory, char, readonly

.. i18n: :partner: Partner, char, readonly

:partner: Partner, char, readonly

.. i18n: :type: Directory Type, char, readonly

:type: Directory Type, char, readonly

.. i18n: Object: Files details by Directory (report.document.file)
.. i18n: #########################################################

Object: Files details by Directory (report.document.file)
#########################################################

.. i18n: :nbr: # of Files, integer, readonly

:nbr: # of Files, integer, readonly

.. i18n: :month: Month, char, readonly

:month: Month, char, readonly

.. i18n: :file_size: File Size, integer, readonly

:file_size: File Size, integer, readonly

.. i18n: Object: Users that did not inserted documents since one month (report.document.wall)
.. i18n: ####################################################################################

Object: Users that did not inserted documents since one month (report.document.wall)
####################################################################################

.. i18n: :user_id: Owner, many2one, readonly

:user_id: Owner, many2one, readonly

.. i18n: :name: Month, date, readonly

:name: Month, date, readonly

.. i18n: :file_name: Last Posted File Name, char, readonly

:file_name: Last Posted File Name, char, readonly

.. i18n: :month: Month, char, readonly

:month: Month, char, readonly

.. i18n: :user: User, char, readonly

:user: User, char, readonly

.. i18n: :last: Last Posted Time, datetime, readonly

:last: Last Posted Time, datetime, readonly
