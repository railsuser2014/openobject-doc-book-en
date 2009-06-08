
.. i18n: Introduction to Views
.. i18n: =====================

Introduction to Views
=====================

.. i18n: As all data of the program is stored in objects, as explained in the Objects section, how are these objects exposed to the user ? We will try to answer this question in this section.

As all data of the program is stored in objects, as explained in the Objects section, how are these objects exposed to the user ? We will try to answer this question in this section.

.. i18n: First of all, let's note that every resource type uses its own interface. For example, the screen to modify a partner's data is not the same as the one to modify an invoice.

First of all, let's note that every resource type uses its own interface. For example, the screen to modify a partner's data is not the same as the one to modify an invoice.

.. i18n: Then, you have to know that the Open ERP user interface is dynamic, it means that it is not described "statically" by some code, but dynamically built from XML descriptions of the client screens.

Then, you have to know that the Open ERP user interface is dynamic, it means that it is not described "statically" by some code, but dynamically built from XML descriptions of the client screens.

.. i18n: From now on, we will call these screen descriptions views.

From now on, we will call these screen descriptions views.

.. i18n: A notable characteristic of these views is that they can be edited at any moment (even during the program execution). After a modification to a displayed view has occurred, you simply need to close the tab corresponding to that 'view' and re-open it for the changes to appear. 

A notable characteristic of these views is that they can be edited at any moment (even during the program execution). After a modification to a displayed view has occurred, you simply need to close the tab corresponding to that 'view' and re-open it for the changes to appear. 

.. i18n: Views principles
.. i18n: -----------------

Views principles
-----------------

.. i18n: Views describe how each object (type of resource) is displayed. More precisely, for each object, we can define one (or several) view(s) to describe which fields should be drawn and how.

Views describe how each object (type of resource) is displayed. More precisely, for each object, we can define one (or several) view(s) to describe which fields should be drawn and how.

.. i18n: There are two types of views:

There are two types of views:

.. i18n:    #. form views
.. i18n:    #. tree views 

   #. form views
   #. tree views 

.. i18n: .. note:: Since Open ERP 4.1, form views can also contain graphs. 

.. note:: Since Open ERP 4.1, form views can also contain graphs. 
