
.. module:: wiki
    :synopsis: Document Management - Wiki (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the Open ERP software, the leading Open Source 
  enterprise management system. If you want to discover Open ERP, check our 
  `screencasts <href="http://openerp.tv>`_ or download 
  `Open ERP <href="http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="wiki"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Document Management - Wiki (*wiki*)
===================================
:Module: wiki
:Name: Document Management - Wiki
:Version: 5.0.1.0
:Author: Tiny & Axelor
:Directory: wiki
:Web: http://openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  The base module to manage documents(wiki) 
      
      keep track for the wiki groups, pages, and history

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 </download/modules/5.0/wiki.zip>`_
  * `trunk </download/modules/trunk/wiki.zip>`_


Dependencies
------------

 * :mod:`base`

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

Object: wiki.wiki (wiki.wiki)
#############################



:create_uid: Author, many2one





:create_date: Created on, datetime





:name: Title, char, required





:tags: Tags, char





:minor_edit: Minor edit, boolean





:history_id: History Lines, one2many





:summary: Summary, char





:write_uid: Last Author, many2one





:text_area: Content, text





:write_date: Modification Date, datetime





:section: Section, char

    *Use page section code like 1.2.1*



:toc: Table of Contents, boolean





:group_id: Wiki Group, many2one





:review: Need Review, boolean




Object: Wiki Groups (wiki.groups)
#################################



:create_date: Created Date, datetime





:name: Wiki Group, char, required





:page_ids: Pages, one2many





:child_ids: Child Groups, one2many





:parent_id: Parent Group, many2one





:template: Wiki Template, text





:section: Make Section ?, boolean





:home: Pages, many2one





:notes: Description, text




Object: Wiki Groups Links (wiki.groups.link)
############################################



:group_id: Parent Group, many2one





:action_id: Menu, many2one




Object: Wiki History (wiki.wiki.history)
########################################



:create_date: Date, datetime





:minor_edit: This is a major edit ?, boolean





:write_uid: Modify By, many2one





:text_area: Text area, text





:wiki_id: Wiki Id, many2one





:summary: Summary, char




Object: wizard.wiki.history.show_diff (wizard.wiki.history.show_diff)
#####################################################################



:diff: Diff, text


