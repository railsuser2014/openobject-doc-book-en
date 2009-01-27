
Module Idea Manager (*idea*)
============================
:Module: idea
:Name: Idea Manager
:Version: 5.0.0.1
:Directory: idea
:Web: http://openerp.com

Description
-----------

::

  This module allows your user to easily and efficiently participate in the innovation of the enterprise. It allows everybody to express ideas about different subjects. Then, others users can comment these ideas and vote for particular ideas. Each idea as a score based on the different votes. The managers can obtain an easy view on best ideas from all the users. Once installed, check the menu 'Ideas' in the 'Tools' main menu.

Dependencies
------------

 * base - installed

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

Object: Category for an idea
############################

.. index::
  single: Category for an idea object
.. 


:parent_id: Parent Categories, many2one



.. index::
  single: parent_id field
.. 




:child_ids: Child Categories, one2many



.. index::
  single: child_ids field
.. 




:name: Category, char, required



.. index::
  single: name field
.. 




:summary: Summary, text



.. index::
  single: summary field
.. 



Object: idea.idea
#################

.. index::
  single: idea.idea object
.. 


:category_id: Category, many2one, required



.. index::
  single: category_id field
.. 




:create_date: Creation date, datetime, readonly



.. index::
  single: create_date field
.. 




:description: Description, text, required

    *Content of the idea*

.. index::
  single: description field
.. 




:title: Idea Summary, char, required



.. index::
  single: title field
.. 




:my_vote: My Vote, selection



.. index::
  single: my_vote field
.. 




:vote_avg: Average Score, float, readonly



.. index::
  single: vote_avg field
.. 




:vote_ids: Vote, one2many



.. index::
  single: vote_ids field
.. 




:state: Status, selection, readonly



.. index::
  single: state field
.. 




:stat_vote_ids: Statistics, one2many, readonly



.. index::
  single: stat_vote_ids field
.. 




:count_comments: Count of comments, integer, readonly



.. index::
  single: count_comments field
.. 




:user_id: Creator, many2one, required, readonly



.. index::
  single: user_id field
.. 




:comment_ids: Comments, one2many



.. index::
  single: comment_ids field
.. 




:count_votes: Count of votes, integer, readonly



.. index::
  single: count_votes field
.. 



Object: Comments
################

.. index::
  single: Comments object
.. 


:content: Comment, text, required



.. index::
  single: content field
.. 




:idea_id: Idea, many2one, required



.. index::
  single: idea_id field
.. 




:create_date: Creation date, datetime, readonly



.. index::
  single: create_date field
.. 




:user_id: User, many2one, required



.. index::
  single: user_id field
.. 



Object: idea.vote
#################

.. index::
  single: idea.vote object
.. 


:idea_id: Idea, many2one, required



.. index::
  single: idea_id field
.. 




:score: Score, selection, required



.. index::
  single: score field
.. 




:user_id: User, many2one



.. index::
  single: user_id field
.. 



Object: Idea Votes Statistics
#############################

.. index::
  single: Idea Votes Statistics object
.. 


:nbr: Number of Votes, integer, readonly



.. index::
  single: nbr field
.. 




:score: Score, selection, readonly



.. index::
  single: score field
.. 




:idea_id: Idea, many2one, readonly



.. index::
  single: idea_id field
.. 

