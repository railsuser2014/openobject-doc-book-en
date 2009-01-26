
Module Workcenter Production start end workflow (*mrp_operations*)
==================================================================
:Module: mrp_operations
:Name: Workcenter Production start end workflow
:Version: False
:Directory: mrp_operations
:Web: http://www.openerp.com

Description
-----------

::
  
    
       This module adds state, date_start,date_stop in production order operation lines
       (in the "Workcenters" tab)
       State: draft, confirm, done, cancel
       When finishing/confirming,cancelling production orders set all state lines to the according state
       Create menus:
           Production Management > All Operations
           Production Management > All Operations > Operations To Do (state="confirm")
       Which is a view on "Workcenters" lines in production order,
       editable tree
  
      Add buttons in the form view of production order under workcenter tab:
      * start (set state to confirm), set date_start
      * done (set state to done), set date_stop
      * set to draft (set state to draft)
      * cancel set state to cancel
  
      When the production order becomes "ready to produce", operations must
      become 'confirmed'. When the production order is done, all operations
      must become done.
  
      The field delay is the delay(stop date - start date).
      So that we can compare the theoretic delay and real delay.
  
      

Reports
-------

Menus
-------

Views
-----

Dependencies
------------

 * stock - installed

 * hr - uninstalled

 * purchase - uninstalled

 * product - installed

 * mrp - uninstalled

Objects
-------