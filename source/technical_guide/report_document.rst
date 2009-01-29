
Module Document Management - Reporting (*report_document*)
==========================================================
:Module: report_document
:Name: Document Management - Reporting
:Version: 5.0.1.0
:Directory: report_document
:Web: 

Description
-----------

::

  Reporting for the Document Management module:
      * My Files
      * All users Files

Dependencies
------------

 * document - installed

Reports
-------

None


Menus
-------

 * Document Management
 * Document Management/Reporting
 * Document Management/Reporting/This Month
 * Document Management/Reporting/This Month/My files
 * Document Management/Reporting/All Months
 * Document Management/Reporting/All Months/My files
 * Document Management/Reporting/This Month/All Users files
 * Document Management/Reporting/All Months/All Users files
 * Document Management/Reporting/Wall of Shame

Views
-----

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


Objects
-------

Object: Files details by Users
##############################



:partner: Partner, char, readonly





:file_title: File Name, char, readonly





:user_id: Owner, integer, readonly





:name: Month, date, readonly





:nbr: # of Files, integer, readonly





:month: Month, char, readonly





:change_date: Modified Date, datetime, readonly





:user: User, char, readonly





:file_size: File Size, integer, readonly





:directory: Directory, char, readonly





:create_date: Date Created, datetime, readonly





:type: Directory Type, char, readonly




Object: Files details by Partners
#################################



:file_title: File Name, char, readonly





:create_date: Date Created, datetime, readonly





:name: Month, date, readonly





:nbr: # of Files, integer, readonly





:change_date: Modified Date, datetime, readonly





:file_size: File Size, integer, readonly





:directory: Directory, char, readonly





:partner: Partner, char, readonly





:type: Directory Type, char, readonly




Object: Files details by Directory
##################################



:nbr: # of Files, integer, readonly





:month: Month, char, readonly





:file_size: File Size, integer, readonly




Object: Users that did not inserted documents since one month
#############################################################



:user_id: Owner, many2one, readonly





:name: Month, date, readonly





:file_name: Last Posted File Name, char, readonly





:month: Month, char, readonly





:user: User, char, readonly





:last: Last Posted Time, datetime, readonly


