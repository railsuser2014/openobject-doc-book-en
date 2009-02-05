
.. module:: idea
    :synopsis: Idea Manager (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Idea Manager (*idea*)
=====================
:Module: idea
:Name: Idea Manager
:Version: 5.0.0.1
:Author: Tiny
:Directory: idea
:Web: http://openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module allows your user to easily and efficiently participate in the innovation of the enterprise. It allows everybody to express ideas about different subjects. Then, others users can comment these ideas and vote for particular ideas. Each idea as a score based on the different votes. The managers can obtain an easy view on best ideas from all the users. Once installed, check the menu 'Ideas' in the 'Tools' main menu.

Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Tools
 * Tools/Configuration
 * Tools/Configuration/Ideas
 * Tools/Configuration/Ideas/Categories
 * Tools/Ideas
 * Tools/Ideas/Ideas by Categories
 * Tools/Ideas/All Ideas
 * Tools/Ideas/All Ideas/Open Ideas
 * Tools/Ideas/My Ideas
 * Tools/Ideas/My Ideas/My Draft Ideas
 * Tools/Ideas/My Ideas/My Open Ideas
 * Tools/Ideas/Reporting
 * Tools/Ideas/Reporting/Vote Statistics
 * Tools/Configuration/Ideas/All Votes

Views
-----

 * idea.category.form (form)
 * idea.category.tree (tree)
 * idea.stat.form (form)
 * idea.vote.tree (tree)
 * idea.vote.form (form)
 * idea.idea.form (form)
 * idea.idea.tree (tree)
 * idea.comment.tree (tree)
 * idea.vote_stat.graph (graph)
 * idea.vote.stat.form (form)
 * idea.vote.stat.tree (tree)


Objects
-------

Object: Category for an idea (idea.category)
############################################



:parent_id: Parent Categories, many2one





:child_ids: Child Categories, one2many





:name: Category, char, required





:summary: Summary, text




Object: idea.idea (idea.idea)
#############################



:category_id: Category, many2one, required





:create_date: Creation date, datetime, readonly





:description: Description, text, required

    *Content of the idea*



:title: Idea Summary, char, required





:my_vote: My Vote, selection





:vote_avg: Average Score, float, readonly





:vote_ids: Vote, one2many





:state: Status, selection, readonly





:stat_vote_ids: Statistics, one2many, readonly





:count_comments: Count of comments, integer, readonly





:user_id: Creator, many2one, required, readonly





:comment_ids: Comments, one2many





:count_votes: Count of votes, integer, readonly




Object: Comments (idea.comment)
###############################



:content: Comment, text, required





:idea_id: Idea, many2one, required





:create_date: Creation date, datetime, readonly





:user_id: User, many2one, required




Object: idea.vote (idea.vote)
#############################



:idea_id: Idea, many2one, required





:score: Score, selection, required





:user_id: User, many2one




Object: Idea Votes Statistics (idea.vote.stat)
##############################################



:nbr: Number of Votes, integer, readonly





:score: Score, selection, readonly





:idea_id: Idea, many2one, readonly


