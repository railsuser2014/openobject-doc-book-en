
Module Document Management - Wiki (*wiki*)
==========================================
:Module: wiki
:Name: Document Management - Wiki
:Version: 5.0.1.0
:Directory: wiki
:Web: http://openerp.com

Description
-----------

::

  The base module to manage documents(wiki) 
      
      keep track for the wiki groups, pages, and history

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------

 * Document Management
 * Document Management/Wiki Configuration
 * Document Management/Wiki
 * Document Management/Wiki Configuration/Wiki Groups
 * Document Management/Wiki/Wiki Groups
 * Document Management/Wiki/Wiki Pages
 * Document Management/Wiki Configuration/All Page Histories

Views
-----

 * wiki.groups.tree (tree)
 * wiki.groups.form (form)
 * wiki.wiki.tree (tree)
 * wiki.wiki.form (form)
 * wiki.wiki.history.tree (tree)
 * wiki.wiki.history.form (form)
 * Differences (form)


Objects
-------

Object: wiki.wiki
#################

.. index::
  single: wiki.wiki object
.. 


:create_uid: Author, many2one



.. index::
  single: create_uid field
.. 




:create_date: Created on, datetime



.. index::
  single: create_date field
.. 




:name: Title, char, required



.. index::
  single: name field
.. 




:tags: Tags, char



.. index::
  single: tags field
.. 




:minor_edit: Minor edit, boolean



.. index::
  single: minor_edit field
.. 




:history_id: History Lines, one2many



.. index::
  single: history_id field
.. 




:summary: Summary, char



.. index::
  single: summary field
.. 




:write_uid: Last Author, many2one



.. index::
  single: write_uid field
.. 




:text_area: Content, text



.. index::
  single: text_area field
.. 




:write_date: Modification Date, datetime



.. index::
  single: write_date field
.. 




:section: Section, char

    *Use page section code like 1.2.1*

.. index::
  single: section field
.. 




:toc: Table of Contents, boolean



.. index::
  single: toc field
.. 




:group_id: Wiki Group, many2one



.. index::
  single: group_id field
.. 




:review: Need Review, boolean



.. index::
  single: review field
.. 



Object: Wiki Groups
###################

.. index::
  single: Wiki Groups object
.. 


:create_date: Created Date, datetime



.. index::
  single: create_date field
.. 




:name: Wiki Group, char, required



.. index::
  single: name field
.. 




:page_ids: Pages, one2many



.. index::
  single: page_ids field
.. 




:child_ids: Child Groups, one2many



.. index::
  single: child_ids field
.. 




:parent_id: Parent Group, many2one



.. index::
  single: parent_id field
.. 




:template: Wiki Template, text



.. index::
  single: template field
.. 




:section: Make Section ?, boolean



.. index::
  single: section field
.. 




:home: Pages, many2one



.. index::
  single: home field
.. 




:notes: Description, text



.. index::
  single: notes field
.. 



Object: Wiki Groups Links
#########################

.. index::
  single: Wiki Groups Links object
.. 


:group_id: Parent Group, many2one



.. index::
  single: group_id field
.. 




:action_id: Menu, many2one



.. index::
  single: action_id field
.. 



Object: Wiki History
####################

.. index::
  single: Wiki History object
.. 


:create_date: Date, datetime



.. index::
  single: create_date field
.. 




:minor_edit: This is a major edit ?, boolean



.. index::
  single: minor_edit field
.. 




:write_uid: Modify By, many2one



.. index::
  single: write_uid field
.. 




:text_area: Text area, text



.. index::
  single: text_area field
.. 




:wiki_id: Wiki Id, many2one



.. index::
  single: wiki_id field
.. 




:summary: Summary, char



.. index::
  single: summary field
.. 



Object: wizard.wiki.history.show_diff
#####################################

.. index::
  single: wizard.wiki.history.show_diff object
.. 


:diff: Diff, text



.. index::
  single: diff field
.. 

