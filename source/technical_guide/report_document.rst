
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

.. index::
  single: Files details by Users object
.. 


:partner: Partner, char, readonly



.. index::
  single: partner field
.. 




:file_title: File Name, char, readonly



.. index::
  single: file_title field
.. 




:user_id: Owner, integer, readonly



.. index::
  single: user_id field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:nbr: # of Files, integer, readonly



.. index::
  single: nbr field
.. 




:month: Month, char, readonly



.. index::
  single: month field
.. 




:change_date: Modified Date, datetime, readonly



.. index::
  single: change_date field
.. 




:user: User, char, readonly



.. index::
  single: user field
.. 




:file_size: File Size, integer, readonly



.. index::
  single: file_size field
.. 




:directory: Directory, char, readonly



.. index::
  single: directory field
.. 




:create_date: Date Created, datetime, readonly



.. index::
  single: create_date field
.. 




:type: Directory Type, char, readonly



.. index::
  single: type field
.. 



Object: Files details by Partners
#################################

.. index::
  single: Files details by Partners object
.. 


:file_title: File Name, char, readonly



.. index::
  single: file_title field
.. 




:create_date: Date Created, datetime, readonly



.. index::
  single: create_date field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:nbr: # of Files, integer, readonly



.. index::
  single: nbr field
.. 




:change_date: Modified Date, datetime, readonly



.. index::
  single: change_date field
.. 




:file_size: File Size, integer, readonly



.. index::
  single: file_size field
.. 




:directory: Directory, char, readonly



.. index::
  single: directory field
.. 




:partner: Partner, char, readonly



.. index::
  single: partner field
.. 




:type: Directory Type, char, readonly



.. index::
  single: type field
.. 



Object: Files details by Directory
##################################

.. index::
  single: Files details by Directory object
.. 


:nbr: # of Files, integer, readonly



.. index::
  single: nbr field
.. 




:month: Month, char, readonly



.. index::
  single: month field
.. 




:file_size: File Size, integer, readonly



.. index::
  single: file_size field
.. 



Object: Users that did not inserted documents since one month
#############################################################

.. index::
  single: Users that did not inserted documents since one month object
.. 


:user_id: Owner, many2one, readonly



.. index::
  single: user_id field
.. 




:name: Month, date, readonly



.. index::
  single: name field
.. 




:file_name: Last Posted File Name, char, readonly



.. index::
  single: file_name field
.. 




:month: Month, char, readonly



.. index::
  single: month field
.. 




:user: User, char, readonly



.. index::
  single: user field
.. 




:last: Last Posted Time, datetime, readonly



.. index::
  single: last field
.. 

