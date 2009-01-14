.. index::
   single: Communication Tools
.. 


Communication Tools
#####################

Summary

* Thunderbird interface

* Microsoft Outlook interface

* Microsoft Word interface

Keywords

* SRM, CRM

* productivity

* communication

* email

* Office

 *Open ERP provides all the information you need to pursue your company's business opportunities efficiently. But to stay productive with all the information you have to handle it's essential that you can keep using your normal communication tools by interfacing them with Open ERP, and not be restricted just to Open ERP's interface.* 



Open ERP can do most things you need to pursue your business opportunities effectively. But there can be quite a quite a bit to learn, which reduces your efficiency while you're learning. And if that's true for a heavy user of the system, it's doubly true for an occasional user or someone who already makes heavy use of standard Office applications and can't easily change.

So for those who need to continue using their traditional Office applications to maintain their efficiency, Open ERP can be fitted out with interface adapters to some of the most common. Your users can participate in many Open ERP-maintained processes without ever leaving their familiar Office-based environment, and can avoid double data-entry yet link into Open ERP's database automatically.

The three following modules are described:

* Mozilla Thunderbird interface,

* Microsoft Outlook interface,

* Microsoft Word interface.

These three modules were developed by the Axelor company (http://axelor.com/ , located in Paris) and are available through the official Open ERP site in the modules section.

The chapter is a mix of installation and configuration instructions, and basic interaction exercises.

Open ERP preparation
=====================

You'll need only one database for this chapter:

* \ ``openerp_ch05X``\  , which should be a restored copy of\ `` openerp_ch04X``\   the database you created at the start of Chapter 4 and then extended – you'll refer to it from time to time because it contains demonstration data that you can use to exercise some of the functions you encounter in the chapter,

To be able to backup and restore the database you'll need to know your super-administrator password.

You'll probably also need your system's \ ``addons``\   directory to be writable, since some of the modules you'll need may have to be added separately – they weren't available as part of core the 4.2.2 release of Open ERP.

You will need to have administrator access to your Windows PC to install the Outlook and Word interface adapters described in the chapter.


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

