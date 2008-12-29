
Customer Relationship Management
#################################

Summary

* Partners

* Case management

* Email gateway

* Profiling

Keywords

* SRM, CRM

* quality

* profiling 

* segmentation

* case

* support

* ISO 9001

 *It's often said that the customer is king. In the business world you'd ideally treat all your customers as royalty, at the center of attention. Open ERP's CRM module is designed to make this aim a reality, helping employees of the business understand their customers' needs better, and automating their communication efforts.* 

.. tip::   **Terminology**  *CRM & SRM* 

	CRM is the abbreviation for Customer Relationship Management, and SRM is Supplier Relationship Management.

If you want to focus on your customers, you need tools to make that focus easy. Tools that will capture all the knowledge you have available, tools that will help you analyze what you know, and tools that will make it easy to use all of that knowledge and analysis.

A crucial advantage that Open ERP gives you over the more specialist CRM applications is that Open ERP knows more about your customers and your ability to supply them because it's handling all of your accounting, sales, purchases, manufacturing and fulfillment as well as linking to all of your internal staff. 

Open ERP's CRM module uses that information and offers several significant features that enable you and your staff to monitor and control your supplier and customer relationships effectively, such as delegating issues to the most appropriate people, keeping a history of communications and events, qualifying prospects and detecting problems. 

It also uses several statistical tools that can analyze relationships quantitatively – your customer service performance and the quality of your suppliers, for example. Using performance analysis, you can easily put a policy of real continuous improvement in place by developing an automatic rules-based system in Open ERP.

To minimize re-typing work, Open ERP provides an email gateway that links your emails to the databases. This is a significant feature – many of your staff will then use Open ERP automatically through email without ever logging into it themselves and having to learn a new system.

Finally, at the end of this chapter you'll see an efficient method of qualifying prospects or customers that enables you to offer a service tailored to the potential value of different prospects.

Open ERP preparation
=====================

You'll need two databases for this chapter:

* \ ``openerp_ch04X``\  , which should be a restored copy of\ `` openerp_ch02``\  , the database you created through Chapter 2. It's referenced throughout the main body of this chapter because it contains demonstration data that illustrates the points made in the chapter.

* \ ``openerp_ch04``\  , which should be a restored copy of \ ``openerp_ch03,``\   the database you created through Chapter 3. If you follow the steps in this chapter you can extend this database.

To be able to backup and restore these databases you'll need to know your super-administrator password.

You'll also need your system's \ ``addons``\   directory to be writable, since you'll load new modules into it later in the chapter – they're not available in the core 4.2.2 release of Open ERP.

And you'll need access to a system administrator for your server system if you want to install the \ ``fetchmail``\   system software that's mentioned later in this chapter.

Once you've created \ ``openerp_ch04``\  , add a new group – \ ``support``\  , and four new users – \ ``General``\  , \ ``Sales``\  , \ ``Support``\  , and \ ``Senior Support``\   (the former two should be put in group \ ``user``\  , and the latter two in \ ``support``\  ). Then also install the \ ``crm``\   module that exists in the Open ERP core installation (but has not yet been installed into this database). You'll need only to know your database's \ ``admin``\   user details to do this.


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Presses) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open ERP Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open ERP Press, Grand Rosière, Belgium

