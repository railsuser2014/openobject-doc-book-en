
.. module:: radiotv
    :synopsis: Tiny ERP TV & Radio Program Grid Module
    :noindex:
.. 

Tiny ERP TV & Radio Program Grid Module (*radiotv*)
===================================================
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

Object: radiotv.program (radiotv.program)
#########################################



:production_year: Production year, integer





:description: Description, text





:classification: Classification, selection, required





:introduction: Introduction, text, required





:channel_ids: Channels, many2many





:approx_duration: Approx. duration, integer

    *Approximate duration in minutes*



:production_country_id: Production country, many2one





:broadcast_language: Broadcast language, char





:original_language: Original language, char





:state: State, selection, required





:production_type: Production type, selection, required





:editor: Editor, char





:team: Team, text





:category_id: Category, many2one





:email: Email, char





:name: Name, char, required




Object: radiotv.category (radiotv.category)
###########################################



:program_ids: Programs, one2many





:name: Name, char, required





:description: Description, text




Object: radiotv.broadcast (radiotv.broadcast)
#############################################



:dt_end: End, datetime





:description: Description, text





:url: URL, text





:dt_start: Start, datetime, required





:program_id: Program, many2one, required





:channel_id: Channel, many2one, required




Object: radiotv.channel (radiotv.channel)
#########################################



:program_ids: Programs, many2many





:name: Name, char, required





:description: Description, text




Object: radiotv.podcast (radiotv.podcast)
#########################################



:category: Category, char





:subtitle: Subtitle, char





:name: Name, char, required





:author: Author, char





:file_name: File name, char, required





:explicit: Explicit, boolean





:keywords: Keywords, char





:broadcast_id: Broadcast, many2one, required





:duration: Duration, char





:pub_date: Publication, datetime, required, readonly





:block: Block, boolean





:description: Description, text




Object: RadioTV website configuration (radiotv.web)
###################################################



:url: URL, char, required





:active: Active, boolean





:name: Name, char, required





:sync: Synchronize, boolean

    *The changes in channels, programs and broadcasts are synchronized automatically to the website*
