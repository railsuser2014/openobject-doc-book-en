
.. i18n: .. index::
.. i18n:    single: Real Case

.. index::
   single: Real Case

.. i18n: .. _ch-real:
.. i18n: 
.. i18n: **********************
.. i18n: Developing a real case
.. i18n: **********************

.. _ch-real:

**********************
Developing a real case
**********************

.. i18n:  *Now that you've discovered some of the many possibilities of Open ERP from a tour of the
.. i18n:  demonstration database, you'll develop a real case. An empty database provides the starting point 
.. i18n:  for testing a classic workflow from product purchase to sale, 
.. i18n:  completing your guided tour and your familiarization with Open ERP.*

 *Now that you've discovered some of the many possibilities of Open ERP from a tour of the
 demonstration database, you'll develop a real case. An empty database provides the starting point 
 for testing a classic workflow from product purchase to sale, 
 completing your guided tour and your familiarization with Open ERP.*

.. i18n: A database loaded with demonstration data is very useful for understanding Open ERP's general
.. i18n: capabilities. But to explore Open ERP through a lens of your own company's needs you should start
.. i18n: with an empty database. You'll work in this chapter on a minimal database containing no
.. i18n: demonstration data so that there is no confusion about what you created. And you'll keep the
.. i18n: database you've created so that you can build on it throughout the rest of this book
.. i18n: if you want to.

A database loaded with demonstration data is very useful for understanding Open ERP's general
capabilities. But to explore Open ERP through a lens of your own company's needs you should start
with an empty database. You'll work in this chapter on a minimal database containing no
demonstration data so that there is no confusion about what you created. And you'll keep the
database you've created so that you can build on it throughout the rest of this book
if you want to.

.. i18n: You'll develop a real case through the following phases:

You'll develop a real case through the following phases:

.. i18n: 	#. Specify a real case.
.. i18n: 
.. i18n: 	#. Describe the functional needs.
.. i18n: 
.. i18n: 	#. Configure the system with the essential modules.
.. i18n: 
.. i18n: 	#. Carry out the necessary data loading.
.. i18n: 
.. i18n: 	#. Test the system with your database.

	#. Specify a real case.

	#. Describe the functional needs.

	#. Configure the system with the essential modules.

	#. Carry out the necessary data loading.

	#. Test the system with your database.

.. i18n: The case is deliberately extremely simple to provide you with a foundation for the more complex
.. i18n: situations you'll handle in reality. Throughout this chapter it's assumed that you're accessing
.. i18n: Open ERP through its web interface. And it's also assumed (as in the rest of this book) that 
.. i18n: you're using the latest download of Open ERP version 5, 
.. i18n: the stable production version at the time of writing
.. i18n: (not the trunk version, which is likely to have new and potentially unstable features).

The case is deliberately extremely simple to provide you with a foundation for the more complex
situations you'll handle in reality. Throughout this chapter it's assumed that you're accessing
Open ERP through its web interface. And it's also assumed (as in the rest of this book) that 
you're using the latest download of Open ERP version 5, 
the stable production version at the time of writing
(not the trunk version, which is likely to have new and potentially unstable features).

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:     1_3_Real_Case_use_case
.. i18n:     1_3_Real_Case_db_setup
.. i18n:     1_3_Real_Case_testing_wf

.. toctree::

    1_3_Real_Case_use_case
    1_3_Real_Case_db_setup
    1_3_Real_Case_testing_wf

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     </div>

.. raw:: html

    </div>

.. i18n: .. Copyright © Open Object Press. All rights reserved.

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the Open ERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium

.. Published by Open Object Press, Grand Rosière, Belgium
