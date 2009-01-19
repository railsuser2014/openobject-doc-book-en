=================================
Creation of Reports (The Reports)
=================================

Introduction
============

This chapter is dedicated to detailed objects definition:

* reports

* rml-reports

* report designer tools

* xml-xslt reports


There are mainly ''three types'' of reports in Open ERP:

#. OpenOffice.org reports
#. RML reports
#. Custom reports (based on `PostgreSQL views and displayed within the interface)


Open Office - Designer
============================
.. Explain to design Report without Plugins, and then translate using the tiny_sxw2rml translator


Introduction
------------

In order to create a report, the general idea is to

* Declare a report in a XML file that must be added in the update_xml section of the __terp__.py file.
* Create a report model with OpenOffice.org writer, convert it to RML using Open sxw2rml (which can be downloaded here).
* Optionally declare a custom parser in order to be able to use more functions than the functions provided by the default parser. We won't detail this third step here and only use the automatic parser. 

* The XML file that declares the report will be named travel_report.xml in the folder travel and will contain 

.. code-block:: xml

        <terp>
           <data>
                 <report id="travel_agency_room_booking_tickets"
                      string="Room Booking Tickets"
                      model="travel.room"
                      name="travel_agency_room_booking_tickets_report"
                      rml="travel/report/tickets.rml"
                      auto="True"/>
           </data>
        </terp>

* As travel_report.xml also needs to be loaded, we modify the file __terp__.py so that the information associated with update_xml is now ['travel_view.xml', 'travel_report.xml'].
* We create a report subfolder in the travel folder. This folder must contain the file tickets.rml.Open Office writer will first be used to create tickets.sxw. 

::

        $ cd ~/tinyerp/server/bin/addons/travel
        $ mkdir report
        $ cd report
        $ oowriter &


Access Objects and Fields
-------------------------

* In **Open Office writer**, we insert a new section inside which we create a 2x2 table, and type the same Python code, inside double brackets, as shown in the screenshot below : 

.. image:: images/OOoReportModel.png

The model must be saved as sxw !

To carry trhough the next steps you will need to download and to untar `Open Report`_:

.. _Open Report: http://tinyforge.org/projects/tinyreport/

* In tiny_sxw2rml script folder, we do the following::

        ~/tiny_sxw2rml$ ./tiny_sxw2rml.py ~/tinyerp/server/bin/addons/travel/report/tickets.sxw > ~/tinyerp/server/bin/addons/travel/report/tickets.rml

        .. note::
                sxw2rml always outputs rml data on the screen or an error message. So it could be wise to check that the path to your sxw is correct and that sxw2rml can read it correctly before redirecting stdout (and possibly overwriting an old working rml).

* We restart the server and ask to update the travel module::

        ~/tinyerp/server/bin$ ./tinyerp-server.py --database=terp --update=travel

We should have a report installed. Here is an example with two rooms booked in two different hostels 

.. image:: images/HostelOfTheBeach_report.png



Registering Report
------------------
Explain to register the report to the Server in XML and py if Required 
also explain for the header = True/False

Design Complex Report
======================

Introduction
------------

Sections
--------

Loops / Tables
---------------

Expressions
-----------

Custom Parser
-------------

.. tip::   **Important**  *Print Multiple Copies of Report.*

Tiny API in Reports - Functions
-------------------------------

XML-XSLT Report
---------------


Improvement of school management module
=======================================

Adding reports
--------------

Adding upgrade reports
----------------------

OpenOffice Report Designer
==========================
Explain about the Report Designer Tools

