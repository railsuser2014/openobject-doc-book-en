
Standardizing Structures
-------------------------

You now have a configuration that enables you to automatically get a directory structure linke to Open ERP for each resource, such as for projects and orders. The ideal situation would now be to automatically structure the documents about projects, say. For example, you could classify them depending on their type:

* Quotations,

* Meeting Minutes,

* Delivery Documents,

* Documentation.

Open ERP provides you with a system that lets you create a structure type for each type of a given document. It then provides that classification for all documents in the directories structured in that type.

So create the structure above for your project management system. To do that, create the four directories above and give them the following data:

* **Type** : Static Directory

* **Linked Model** : Analytic Account

Then in each project (represented by analytic accounts) you'll get this substructure for organization your documents efficiently.

    .. image::  images/document_shared_structure.png
       :align: center

*Substructure common to all projects.*

.. tip::   **Technique**  *Mapping* 

    In practice, Open Erp doesn't create directories or files for every resource. It actually manages this by mapping between Open ERP resources and the FTP interface

    This approach gives a lot of flexibility because there's no synchronization to do, nor redundancy. Changes in either the document management system or in Open ERP will automatically be reflected over in the other side.

    And at the same time, resources are obviously not used up by storing things twice.

Once a new project has been defined in Open ERP, the system automatically creates a directory corresponding to the project in the right place in the document management system, and creates a structure type there for classifying documents.


