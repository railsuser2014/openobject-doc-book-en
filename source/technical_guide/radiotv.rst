
Module Tiny ERP TV & Radio Program Grid Module (*radiotv*)
==========================================================
:Module: radiotv
:Name: Tiny ERP TV & Radio Program Grid Module
:Version: 5.0.1.1
:Directory: radiotv
:Web: www.zikzakmedia.com

Description
-----------

::

  This module allows to control TV & Radio channels, programs, grid of date/time of broadcasting and podcasts
  
  channel <--n---m--> program <--1---n--> broadcast <--1---n--> podcast
  
  Features:
      * Menu entries to see daily and weekly broadcasts
      * The date/time end of each broadcast is computed automatically
      * The broadcasts can be copied from a range of days to other
      * A TinyERP cron is provided to copy broadcasts every day
      * Several broadcasting reports are included
      * Several wizards to synchronize the channels, programs and broadcasts to a
        mysql-php web site are included. They can be also synchronized automatically.

Dependencies
------------

 * base - installed

Reports
-------

 * Radio TV broadcast report

 * Radio TV broadcast compact report

 * Radio TV broadcast declaration report

Menus
-------

 * Radio TV/Channels
 * Radio TV/Program categories
 * Radio TV/Programs
 * Radio TV/Programs/Archive programs
 * Radio TV/Programs/Published programs
 * Radio TV/Programs/Unpublished programs
 * Radio TV/Broadcasts
 * Radio TV/Broadcasts/Yesterday broadcasts
 * Radio TV/Broadcasts/Today broadcasts
 * Radio TV/Broadcasts/Tomorrow broadcasts
 * Radio TV/Broadcasts/Previous week broadcasts
 * Radio TV/Broadcasts/This week broadcasts
 * Radio TV/Broadcasts/Next week broadcasts
 * Radio TV/Podcasts
 * Radio TV/Configuration/Website configuration
 * Radio TV/Copy broadcasts from a day to other
 * Radio TV/Export channels and programs
 * Radio TV/Export broadcasts
 * Radio TV/Export podcasts
 * Radio TV/Broadcasts compact report
 * Radio TV/Broadcasts declaration report

Views
-----

 * radiotv.channel.tree (tree)
 * radiotv.channel (form)
 * radiotv.program.tree (tree)
 * radiotv.program (form)
 * radiotv.category.tree (tree)
 * radiotv.category (form)
 * radiotv.broadcast.tree (tree)
 * radiotv.broadcast (form)
 * radiotv.podcast.tree (tree)
 * radiotv.podcast (form)
 * radiotv.web.tree (tree)


Objects
-------

Object: radiotv.program
#######################

.. index::
  single: radiotv.program object
.. 


:production_year: Production year, integer



.. index::
  single: production_year field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:classification: Classification, selection, required



.. index::
  single: classification field
.. 




:introduction: Introduction, text, required



.. index::
  single: introduction field
.. 




:channel_ids: Channels, many2many



.. index::
  single: channel_ids field
.. 




:approx_duration: Approx. duration, integer

    *Approximate duration in minutes*

.. index::
  single: approx_duration field
.. 




:production_country_id: Production country, many2one



.. index::
  single: production_country_id field
.. 




:broadcast_language: Broadcast language, char



.. index::
  single: broadcast_language field
.. 




:original_language: Original language, char



.. index::
  single: original_language field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:production_type: Production type, selection, required



.. index::
  single: production_type field
.. 




:editor: Editor, char



.. index::
  single: editor field
.. 




:team: Team, text



.. index::
  single: team field
.. 




:category_id: Category, many2one



.. index::
  single: category_id field
.. 




:email: Email, char



.. index::
  single: email field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 



Object: radiotv.category
########################

.. index::
  single: radiotv.category object
.. 


:program_ids: Programs, one2many



.. index::
  single: program_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: radiotv.broadcast
#########################

.. index::
  single: radiotv.broadcast object
.. 


:dt_end: End, datetime



.. index::
  single: dt_end field
.. 




:description: Description, text



.. index::
  single: description field
.. 




:url: URL, text



.. index::
  single: url field
.. 




:dt_start: Start, datetime, required



.. index::
  single: dt_start field
.. 




:program_id: Program, many2one, required



.. index::
  single: program_id field
.. 




:channel_id: Channel, many2one, required



.. index::
  single: channel_id field
.. 



Object: radiotv.channel
#######################

.. index::
  single: radiotv.channel object
.. 


:program_ids: Programs, many2many



.. index::
  single: program_ids field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: radiotv.podcast
#######################

.. index::
  single: radiotv.podcast object
.. 


:category: Category, char



.. index::
  single: category field
.. 




:subtitle: Subtitle, char



.. index::
  single: subtitle field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:author: Author, char



.. index::
  single: author field
.. 




:file_name: File name, char, required



.. index::
  single: file_name field
.. 




:explicit: Explicit, boolean



.. index::
  single: explicit field
.. 




:keywords: Keywords, char



.. index::
  single: keywords field
.. 




:broadcast_id: Broadcast, many2one, required



.. index::
  single: broadcast_id field
.. 




:duration: Duration, char



.. index::
  single: duration field
.. 




:pub_date: Publication, datetime, required, readonly



.. index::
  single: pub_date field
.. 




:block: Block, boolean



.. index::
  single: block field
.. 




:description: Description, text



.. index::
  single: description field
.. 



Object: RadioTV website configuration
#####################################

.. index::
  single: RadioTV website configuration object
.. 


:url: URL, char, required



.. index::
  single: url field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:name: Name, char, required



.. index::
  single: name field
.. 




:sync: Synchronize, boolean

    *The changes in channels, programs and broadcasts are synchronized automatically to the website*

.. index::
  single: sync field
.. 

