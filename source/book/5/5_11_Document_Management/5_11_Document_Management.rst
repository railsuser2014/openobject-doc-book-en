Integrated Document Management
###############################

Summary

* Introduction to Document Management

* Installation and initial guide

* FTP access

* Integration with Open ERP

Keywords

* Attachments

* Documents

* Indexation

*Information management has become a major strategic factor in companies' development. It's important to get the right information circulated to the right people as efficiently as possible yet still keep it secure. Documentation management provides a way for companies to organize their information, in all its forms, in one place.*

The objectives of document management include easier archiving, access, and reference, intelligent classification, and distribution of documents and the information they contain. It concerns sets of all sorts of company documents such as work procedures, meeting reports, documents received from customers and suppliers, documents sent to customers, faxes, sales presentations, and product datasheets.

The importance of good document management
-------------------------------------------

Globalization means that workplaces are ever more geographically dispersed. This means that documents are also used more than ever for communicating and collaborating by people in several countries and continents.

You see communication problems between employees even in the same office because they don't have easy access to the documents that they need. You find some documents kept by someone in the accounts office, shared directories that serve everybody, some documents in paper form, others in electronic form – quite a free-for-all.

An explosion in the number of documents that a company needs doesn't help. If their storage and indexation are badly organized, these documents become useless because they're almost impossible to find.

The results of poor document management can lead to a significant loss of time. Ask yourself how often you find yourself looking for:

* A supplier catalogue that's been send to a purchasing manager,

* A customer contract signed several months ago,

* The final set of Terms and Conditions offered to a specific customer,

* The documents required for employing a new member of staff,
* An order confirmation sent by a customer to one of your salespeople or, perhaps even more common when the relevant salesperson has gone on vacation, if you ever received such an order confirmation,

* A procedure from your quality manual if there's been a process fault,

* An email which was sent to one of your colleagues,

* A document that you need to be a template for a specific type of contract,

* A complete history of communications between yourselves and a supplier about a given contract.

Even worse than the loss of time, perhaps, the lack of good document management is bad for the quality of your organization and the service provided by your company. In such a company it's likely that:

* a set of documents doesn't follow a standard layout,

* all the salespeople prepare quotations in their own way and gradually change the way they do it for themselves but not for the group,

* a correction to a type of contract stays with a small group of people and doesn't percolate back into the rest of the company to benefit other users,

* version management is chaotic or even non-existent.

So a good integrated document management system can be a powerful tool to help in day-to-day company management. With it you could also easily:

* Continue the work started by a colleague if she's gone on vacation, and respond to her customers if needed,

* Get hold of examples of all document types with just a few clicks, so that you can follow company standards in such areas as order confirmation, price requests, meeting minutes, customer deliverables, contract examples, and models for faxes and letters,

* Retrieve procedures and other associated documents if you don't know how to do a certain task – such as things you should do when hiring a new employee, organizing a conference, or how to structure meeting minutes,

* Very easily reuse work done by a colleague to meet similar needs and build on all the individual work done in your own company,

* Find all the orders for a customer or from a supplier in just a few seconds to answer questions or two continue a discussion when the initial contact point in your company is not available,

* Build on your working methods and enable your colleagues to benefit from each improvement in a document type or a procedure.

From these examples you can see the importance of a good document management system, and what it might contribute to the improvement of productivity and the quality of the output from each employee.

Classic document management solutions
--------------------------------------

Faced with the need to organize documents, companies have looked at a number of document management solutions that are promoted today, from simple email archiving to complete electronic management systems dedicated to arbitrary documents.

Unfortunately these solutions haven't always been very useful because they're too little integrated in companies' management systems. Most solutions that we've come across are underused by the employees – often used by some of them but not by all.

The primary reason for this is that a document management system that's not integrated imposes extra work on an employee. For example a salesperson should ideally save each customer confirmation in the document management system. Only that means quite a heavy additional workload just for an order confirmation:

#. Receive and read the email from the customer,

#. Save the email and its attachments on the desktop,

#. Connect to the ERP and confirm the order,

#. Connect to the document management system,

#. Look for the best place to store the document,

#. Create a directory for the customer and the order if it doesn't yet exist,

#. Copy the files from the desktop to the right place in the document management system.

This is obviously a lot of operations just to handle a simple order confirmation. You can understand why many companies hardly use their document management system even if they've gone to the cost and effort of purchasing and installing one.

.. tip::   **Going Further** *Free document management systems*

    A number of free document management applications exist. The most well known are:

    * Alfresco: http://www.alfresco.com

    * Quotero: http://www.quotero.com

It's very difficult to keep the information in the company's management system in sycnhronization with that in the document management system. For example when a customer changes his address, users will modify the details in the management software but usually not in the document management system.

Furthermore, since users should create the same storage structure in both systems, you quickly find after only a few months that the information in the document management system is quite disconnected from that in the company's management system if the two are separate. For example, how do you know where to store your least-frequently used documents such as (perhaps) employee car-leasing documents?

Also, document management systems are typically very complex because they must manage user access rights in just the same way as those that are available in the company management system. This means that you have to enter the same sort of data about access rights twice for the system administrators.

You'll see that the total integration of Open ERP's document management system with the main company management system, and plugins to Outlook and Thunderbird email clients, offers an elegant solution that addresses these problems.

The Open ERP solution
----------------------

Open ERP's management of documents is unique and totally innovative in its integrated approach. Its complete integration with the company's management system solves most of the problems that are encountered when you use independent document management systems:

* Login and the management of access rights is integrated with that of Open ERP for controlling access to different document types,

* Ultra-rapid access to documents, which are directly accessible through your email client or through the company management software,

* Automatic assignment of meta-information comes directly from information contained in your Open EPR login registration,

* Document workflow which automatically follow Open ERP's documentation process provide complete synchronization between the systems,

* Document classification is determined by Open ERP itself so that the structure that is created is always synchronized between the systems,

* Automatic indexation and classification of all documents produced by Open ERP for maximum efficiency.

Getting Started
================

This section is about how to get started with the document management system from its installation to advanced use with FTP access.

Installation
-------------

To install Open ERP's document management system you just need is to install the \ ``document``\  and \ ``board_document``\ modules through the menu *Administration > Modules Management > Modules*. After installing the module the system automatically proposes that you configure the document management system.

    .. image::  images/document_config.png
       :align: center

*Screen for configuring document management.*

Once the module has been installed you'll see a new entry in the main menu called *Document Management*.

    .. image::  images/document_menu.png
       :align: center

*The document management menu.*

Internal and external access using FTP
---------------------------------------

The first configuration step is to create a directory structure that will be used to classify your document set. You can use the structure automatically propsoed by Open ERP from the menu *Document Management > Directory Structure*.

    .. image::  images/document_structure.png
       :align: center

*Structure of directories when the document module has been installed.*

In addition to the usual access to documents through Open ERP, you will be able to connect to them directly through the filesystem using the FTP protocol. To connect to the FTP server, use the following address:

========= ===========================================
Parameter Value
========= ===========================================
Server    Your Open ERP server, for example 127.0.0.1
Port      8021
Path      The '/' character, for the root
User      Your user account in Open ERP
Password  Your Open ERP password
========= ===========================================

.. tip::   **Note**  *FTP server* 

    This comment about an FTP server may appear a bit technical, but it's just a standard for getting hold of files without worrying too much about the platform standards (Windows, Mac, Linux, or other Unix-like system). So FTP is just a way of getting access to files without needing to use an Open ERP client. There are other ways, but FTP proved itself to the developers to be the one that performed best at lowest cost.

Once you're connected using FTP you appear to get to the root of a directory for the document management system. Once you enter the directory you find a structure that matches the structure defined in Open ERP.

    .. image::  images/document_ftp_structure_root.png
       :align: center

*Root of the database directory seen through FTP.*

    .. image::  images/document_ftp_structure_tree.png
       :align: center

*Structure of the directories in the document management system.*

Mapping between Open ERP resources and directories
---------------------------------------------------

Each directory can have the type Static or be linked to another resource. A static directory, as with Operating Systems, is the classic directory that can contain a set of files. The directories linked to systems resources automatically possess sub-directores for each resource type defined in the parent directory.

.. tip::   **Note**  *Directories in English* 

    To keep them synchronized to the working language, directory names are not translateable. But Open ERP's demonstration data automatically creates directories in English. You can rename them through the menu *Document Management > Configuration > Directories*.

For example you can look at the directory shown in *Main Repository > Sales Orders > All Sales Orders*. You'll see the directory for all the orders present in Open ERP that was created automatically by the system.

    .. image::  images/document_sale.png
       :align: center

*Orders in Open ERP.*

    .. image::  images/document_ftp_sale.png
       :align: center

*Directories representing all the orders in the document management system..*

Directories can follow a tree like the tree of resources in Open ERP. For example if you go to the directory *Main Repository > Projects* you'll see the structure of the analytic accounts.

To define a directory containing a specific type of resource you have to define parameters when you define the directory itself:

* **Type** : Other Resources

* **Child Models** : Choose one of the system objects

* **Domain** :  an event filtered so that it sees only a subset of the resources

* **Tree structure** : to show the resources hierarchically

    .. image::  images/document_dir_form.png
       :align: center

*Configuration of the directory containing quotations (draft orders).*

This is a very flexible approach because any modification of the resource in Open ERP is automatically reflected in the document management system. So when the quotation gets confirmed in Open ERP the directory no longer appears as a quotation through FTP access.

Here are some examples of directories linked to Open ERP resources that could be helpful if configured in the document management system:

* Quotations and Order: storing documents that relate to orders,

* Products: for storing products' technical datasheets,

* Users: to automatically define a directory owned by each user of the system,

* Employees: to store documents about employees, such as their CVs, your interview notes, contract details, and their annual assessments,

* Support Requests: storing items about requests or about technical support responses,

* Analytic accounts or project: to store project management and tracking documents.

Managing Attachments
---------------------

As you've seen, it's possible to connect any directory in the document management system to an Open ERP resource. The system then manages its creation and keeps the directory synchronized with the reports generated by Open ERP from its own data. You don't have to create or rename these directories because Open ERP does all this automatically as it resychronizes with its database.

You can then copy the files in the directories that correspond to any of the resources. The files are automatically attached to Open ERP's documents through attachment management. Conversely, if you attach a document to one of Open ERP's resource then that document will automatically become visible over FTP in the document management system.

.. tip::   **Technique**  *File storage* 

    If you don't install the document management system then the files that are attached to an Open ERP resource are stored directly in the database. Once the document management system has been installed, the contents of the files are no longer stored in the database but are stored instead on the Open ERP server filesystem in a directory named 'filestore'.

    You can then read and add attachments to Open ERP resources quite independently of the Open ERP interface or the FTP server using simple drag and drop.

Virtual Files
--------------

The most well-organized companies keep track of all the documents they've sent to customers in their document management system. It's very useful to be able to retrieve every document about a customer or a project. But the work of storing these documents can itself often take up quite a bit of time for staff. Each report must be saved in the document management system as well as simply being sent by email to the customer.

That's not the case in Open ERP. To automatically make Open ERP reports available in the FTP server, Open ERP enably the definition of 'virtual files'. You can then put virtual files into directories that have the special type of 'linked resource' and link the virtual files to Open ERP's reports.

.. tip::   **Technique**  *Virtual Files* 

    Virtual files don't actually existing in Open ERP but are made visible with a size of 0 in the FTP server. Once these files have been read by the client software, Open ERP prints the document related to this file and returns a PDF document linked to the resource.

    When you copy or open a virtual file you print the selected resource. You then don't have to go and print a document through Open ERP – you just open the file containing that document in the document management system. The PDF file is then created in real time by Open ERP by reading the relevant data.

The screen below shows the parameters of the virtual files in Orders. You define the virtual files using the name NUMCOMMAND_print.pdf, where NUMCOMMAND represents the reference to the order. To do this you must complete the section Descriptive Contents of the file for a directory. For each report associated with an order you can then find a virtual file.

    .. image::  images/document_virtual_form.png
       :align: center

*Virtual files about purchase orders in Open ERP.*

To see the effect of this configuration, connect to the FTP server and go into a directory for an order, such as Main Repository > Sales Orders > All Sales Orders > SO003. You can then just double-click the file SO003_print.pdf to get a printout of Order SO003. You can attach it to an email or put it on your desktop.

    .. image::  images/document_virtual_ftp.png
       :align: center

*Virtual files about purchase orders through FTP.*

This system of virtual files is very useful in a lot of situations. For example if you must quickly re-send a quotation to a customer you don't have to open Open ERP, you can just attach the relevant virtual file to your email.

Once the files have been read or copied they become real files, taking up real space, rather than just virtual.

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

Searching for documents
------------------------

You've seen several methods of accessing documents quickly:

* From attachments to an Open ERP resource,

* Through FTP access to Open ERP,

* Using the menu Document Management > Structure of Directories.

But if you don't know where a specific document can be found, Open ERP also has a search tool integrated into its document management. To search for a file use the menu *Document Management > Search for a file*. You get to a document search screen that lets you search amongst all the attachments and all the documents in the FTP server.

You can search for a file using various different criteria:

* The filename,

* The owner of a file,

* The title of the resource that the file is attached to,

* The partner that the document is about,

* The directory that it's found in,

* Its creation and modification dates.

Notice here an important advantage for an integrated document management system. Information such as which partner is associated with a document is automatically detected by Open ERP when the document has been stored in a directory. This information is never input by the user – it's detected automatically using the information about the resource when it's being saved as a file.

But your search isn't limited to these few fields. You can also search on the content in the files. Each file is automatically indexed by the system to give you a search engine rather like Google's on the whole set of company documents.

.. tip::   **Note**  *Supported file formats* 

    The Open ERP document management system can index the following file formats:

    * **TXT** : text files,

    * **PDF** : PDF files,

    * **SXW** : Open Office V1 files,

    * **ODT** : Open Office V2 files,

    * **DOC** : Microsoft Word files.

    The other file formats are properly handled in the document management system but their content is not indexed automatically.

This functionality is very significant. All you need to do is search for a partner name or an order number to automatically get all the documents that are referenced there. And you can use a fragment of text to find the document you need from within that subset.

Integration with your emails
=============================

Using Outlook and Thunderbird
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. image::  images/document_shared_structure.png
       :align: center

*Sending an attachment that's in the document management system from Outlook.*

Working with users' changes
============================

To make the document management system's use as unobtrusive as possible the system's users should easily be able to store all the documents that they produce or receive from their customers and suppliers. So Open ERP supplies dashboards to help system users approve their acceptance of such documents.

So you'll find two dashboards in the menu *Dashboards > Document Management* : one dashboard for the document management system manager and one dashboard for follwing use by different users.

The first lets you track the change of documents by month, by customer and by type of resource. You could also quickly assess the use that's made of the system by the various users.

    .. image::  images/document_board1.png
       :align: center

*Dashboard for the document management system manager.*

The second dashboard lets you track the user that's made of the system by different employees. You'll find the number of files sent by user and a classification of the users using document management system the least. That will enable you to know who has been well-trained and if it is necessary to do something about changing work methods.

    .. image::  images/document_board2.png
       :align: center

*Dashboard for the document management system amalyzed by user.*

Version Management
===================

There's usually a need to keep track of all the important documents that you have printed. For example, when you send an invoice to a customer it's a good idea to store a copy of that invoice internally in paper or electronic form. Then you can reprint it exactly in the same format as when you sent it, even if the company's details have changed in the meantime.

To do this, Open ERP can automatically store as attachments the different reports printed by users. By default, only invoices are saved as attachments, and they're saved when they are printed.

But you can configure the system so that it doesn't matter which type of report is printed. To activate that functionality on another type of report, modify this in the menu: *Administration > Configuration > Low Level > Actions > XML Reports*.

    .. image::  images/document_report_modif.png
       :align: center

*Modifying the definition of a report.*

Select the report that you want to change and complete the field 'Prefix for saving as an attachment'. Once you've done that each document print action will automatically be saved as an attachment to the document.

Documents used for company processes
=====================================

Finally, the document management system is also completely linked to the main system that manages company processes. Then on each node of your management process you could store a procedure. Once the user sees a process view of the relevant document he would be able to click on the directory to get all the documents that might be useful for this phase of the process.

So you could also efficiently store the documents required for each phase of a process.

    .. image::  images/document_process.png
       :align: center

*Example of a document linked to process management.*

