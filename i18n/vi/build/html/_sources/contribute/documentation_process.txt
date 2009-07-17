
.. i18n: Documentation Process
.. i18n: ---------------------

Documentation Process
---------------------

.. i18n: Books
.. i18n: +++++

Books
+++++

.. i18n: The main documentation of OpenERP is composed of a set of books according to
.. i18n: the business need. These books are reviewed once a year. We are working with
.. i18n: authors/contributors/employees/translators to build chapters on the different
.. i18n: aspects of the ERP. As to motivate people to write quality documentation, 

The main documentation of OpenERP is composed of a set of books according to
the business need. These books are reviewed once a year. We are working with
authors/contributors/employees/translators to build chapters on the different
aspects of the ERP. As to motivate people to write quality documentation, 

.. i18n: This section describe how we collaborate with authors and translators to
.. i18n: provide a very good documentation on OpenERP. As to motivate people to write
.. i18n: quality documentation/chapters we set up author rights to pay every contributor
.. i18n: and translator according to their effort.

This section describe how we collaborate with authors and translators to
provide a very good documentation on OpenERP. As to motivate people to write
quality documentation/chapters we set up author rights to pay every contributor
and translator according to their effort.

.. i18n: Building a Book
.. i18n: """""""""""""""

Building a Book
"""""""""""""""

.. i18n: We have contract with several editors to publish books in different countries.

We have contract with several editors to publish books in different countries.

.. i18n: Once we have enough chapters written, we can compose a book and publish it.

Once we have enough chapters written, we can compose a book and publish it.

.. i18n: Books are first published in a paper version. Three months after, we release it online.

Books are first published in a paper version. Three months after, we release it online.

.. i18n: ..  Guidelines
.. i18n: ..  """"""""""

..  Guidelines
..  """"""""""

.. i18n: .. todo:: write the 'guidelines' section

.. todo:: write the 'guidelines' section

.. i18n: Author Rights
.. i18n: """""""""""""

Author Rights
"""""""""""""

.. i18n: The typical author rights are between 8% and 10% on the public price, according
.. i18n: to the authors, the country and the editor in which the book will be published.
.. i18n: This commission is on the public price, no matter of the final selling price
.. i18n: per item.

The typical author rights are between 8% and 10% on the public price, according
to the authors, the country and the editor in which the book will be published.
This commission is on the public price, no matter of the final selling price
per item.

.. i18n: These author rights have to be divided according to people working on the book:

These author rights have to be divided according to people working on the book:

.. i18n:   * Reviewers: 10% to be divided by number of reviewers
.. i18n:   * Translators: 30% to be divided by the number of translators
.. i18n:   * Authors: the rest (60%-90%) to be divided by number of authors

  * Reviewers: 10% to be divided by number of reviewers
  * Translators: 30% to be divided by the number of translators
  * Authors: the rest (60%-90%) to be divided by number of authors

.. i18n: As an example, Geoff and Fabien worked on the french and english book on
.. i18n: OpenERP. This book is sold at a public price of 35 EUR with 10% author rights.
.. i18n: We had one reviewer for this book from Eyrolles. So author rights are splitted
.. i18n: in that way:

As an example, Geoff and Fabien worked on the french and english book on
OpenERP. This book is sold at a public price of 35 EUR with 10% author rights.
We had one reviewer for this book from Eyrolles. So author rights are splitted
in that way:

.. i18n:   * Geoff: 1.575 EUR/book (= 35 * 0.1 * (0.9 / 2))
.. i18n:   * Fabien: 1.575 EUR/book
.. i18n:   * Reviewer: 0.35 EUR/book (= 35 * 0.1 * 0.1)

  * Geoff: 1.575 EUR/book (= 35 * 0.1 * (0.9 / 2))
  * Fabien: 1.575 EUR/book
  * Reviewer: 0.35 EUR/book (= 35 * 0.1 * 0.1)

.. i18n: Once this book will be translated to Hungarian, with a public price of 30 EUR
.. i18n: and author rights of 10% (0.1) we will have:

Once this book will be translated to Hungarian, with a public price of 30 EUR
and author rights of 10% (0.1) we will have:

.. i18n:   * Geoff: 1.05 EUR/book (=30 * 0.1 * 0.7 / 2)
.. i18n:   * Fabien: 1.05 EUR/book
.. i18n:   * Hungarian translator: 0.90 EUR/book (=30 * 0.1 * 0.30)

  * Geoff: 1.05 EUR/book (=30 * 0.1 * 0.7 / 2)
  * Fabien: 1.05 EUR/book
  * Hungarian translator: 0.90 EUR/book (=30 * 0.1 * 0.30)

.. i18n: Author rights are paid every 3 months, after one month. (to be verified
.. i18n: according to what we can do with editors)

Author rights are paid every 3 months, after one month. (to be verified
according to what we can do with editors)

.. i18n: People
.. i18n: ++++++

People
++++++

.. i18n: Authors
.. i18n: """""""

Authors
"""""""

.. i18n: Everyone can be an author and write a complete book or just one or several
.. i18n: chapters on particular aspects of OpenERP. Chapters are then review

Everyone can be an author and write a complete book or just one or several
chapters on particular aspects of OpenERP. Chapters are then review

.. i18n: Authors from Tiny
.. i18n: """""""""""""""""

Authors from Tiny
"""""""""""""""""

.. i18n: At Tiny (the editor of OpenERP), each employee can write a few chapters based
.. i18n: on new module he wrote for specific customers, at the end of the project. As
.. i18n: employees get a salary to write these chapters during their working hours,
.. i18n: author rights are computed slightly differently:

At Tiny (the editor of OpenERP), each employee can write a few chapters based
on new module he wrote for specific customers, at the end of the project. As
employees get a salary to write these chapters during their working hours,
author rights are computed slightly differently:

.. i18n:   * Computed rights are divided by two for the employee: 50%
.. i18n:   * Valid until the employee work for Tiny

  * Computed rights are divided by two for the employee: 50%
  * Valid until the employee work for Tiny

.. i18n: ..  Translators
.. i18n: ..  """""""""""

..  Translators
..  """""""""""

.. i18n: ..  Reviewers
.. i18n: ..  """""""""

..  Reviewers
..  """""""""

.. i18n: Modules
.. i18n: +++++++

Modules
+++++++

.. i18n: Each module should have a small and minimal documentation.

Each module should have a small and minimal documentation.

.. i18n: Building the documentation
.. i18n: ++++++++++++++++++++++++++

Building the documentation
++++++++++++++++++++++++++

.. i18n: We use `Sphinx <http://sphinx.pocoo.org>`_, a documentation generator, to build
.. i18n: the documentation. So, Sphinx should be installed on your system and you should
.. i18n: know how to use it.

We use `Sphinx <http://sphinx.pocoo.org>`_, a documentation generator, to build
the documentation. So, Sphinx should be installed on your system and you should
know how to use it.

.. i18n: You can install it with `easy_install
.. i18n: <http://peak.telecommunity.com/DevCenter/EasyInstall>`_. For example, on Ubuntu: ::
.. i18n: 
.. i18n:   sudo easy_install sphinx

You can install it with `easy_install
<http://peak.telecommunity.com/DevCenter/EasyInstall>`_. For example, on Ubuntu: ::

  sudo easy_install sphinx

.. i18n: .. describe:: building the documentation in html:

.. describe:: building the documentation in html:

.. i18n: ::
.. i18n: 
.. i18n:   make clean
.. i18n:   make html

::

  make clean
  make html

.. i18n: .. describe:: building the documentation in pdf:

.. describe:: building the documentation in pdf:

.. i18n: ::
.. i18n: 
.. i18n:   make clean
.. i18n:   make latex
.. i18n:   cd build/latex
.. i18n:   make all

::

  make clean
  make latex
  cd build/latex
  make all

.. i18n: .. describe:: building a book:

.. describe:: building a book:

.. i18n: For example, if you want to build the *Open ERP for Retail and Industrial Management* book:

For example, if you want to build the *Open ERP for Retail and Industrial Management* book:

.. i18n: ::
.. i18n: 
.. i18n:   cd books/book_mrp
.. i18n:   make clean
.. i18n:   make latex
.. i18n:   cd build/latex
.. i18n:   make all

::

  cd books/book_mrp
  make clean
  make latex
  cd build/latex
  make all

.. i18n: FAQ
.. i18n: +++

FAQ
+++

.. i18n: .. describe:: How much items can we expect to sell for a book ?

.. describe:: How much items can we expect to sell for a book ?

.. i18n: The first french book we wrote is sold at 500 items per month. It's good as it
.. i18n: was our the first book on OpenERP but we can expect better results with an
.. i18n: english version. So probably between 250 and 1500 items per month for an
.. i18n: english book.

The first french book we wrote is sold at 500 items per month. It's good as it
was our the first book on OpenERP but we can expect better results with an
english version. So probably between 250 and 1500 items per month for an
english book.
