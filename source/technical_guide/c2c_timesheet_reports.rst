
.. module:: c2c_timesheet_reports
    :synopsis: Timesheet Reports 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Timesheet Reports (*c2c_timesheet_reports*)
===========================================
:Module: c2c_timesheet_reports
:Name: Timesheet Reports
:Version: 1.0
:Author: camptocamp.com (aw)
:Directory: c2c_timesheet_reports
:Web: http://camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  
          Timesheet Reports Module:
              * Add a report "/HR/report/Timesheets/Timesheet Status" that display the timesheet status for each user: "confirmed", "draft", "missing". 
                It displays 5 periods' status previous to a given date
              * Add a field "ended" to the employee form to define when the employee stopped working for the company
              * Add a tool "/HR/Configuration/Timesheet Reminder" to send automatics emails to those who did not complete their timesheet and add a boolean field to employees to define if they should receive this message or not
      

Dependencies
------------

 * :mod:`hr_timesheet_sheet`
 * :mod:`hr`
 * :mod:`c2c_reporting_tools`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
