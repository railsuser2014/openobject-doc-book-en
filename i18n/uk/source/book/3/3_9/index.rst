
.. i18n: .. index::
.. i18n:    single: Configuring Accounts

.. index::
   single: Configuring Accounts

.. i18n: .. _ch-configacct:
.. i18n: 
.. i18n: ********************************
.. i18n: Configuring Accounts from A to Z
.. i18n: ********************************

.. _ch-configacct:

********************************
Configuring Accounts from A to Z
********************************

.. i18n:  *Accounts must be configured to meet your company's needs.
.. i18n:  This chapter explains how to modify your chart of accounts, journals, access rights, initial
.. i18n:  account balances, and default values for the initial configuration of your Open ERP accounts.*

 *Accounts must be configured to meet your company's needs.
 This chapter explains how to modify your chart of accounts, journals, access rights, initial
 account balances, and default values for the initial configuration of your Open ERP accounts.*

.. i18n: Assuming that it calculates sufficiently accurately, the best accounting software would be marked out by
.. i18n: its usability and simplicity of data entry, and flexibility in configuring its different components.
.. i18n: You'd be able to easily modify the accounting module to meet your own needs so that you could
.. i18n: optimize it for the way you want to use it.

Assuming that it calculates sufficiently accurately, the best accounting software would be marked out by
its usability and simplicity of data entry, and flexibility in configuring its different components.
You'd be able to easily modify the accounting module to meet your own needs so that you could
optimize it for the way you want to use it.

.. i18n: Open ERP lets you adapt and reconfigure many functions to ease the task of data entry:

Open ERP lets you adapt and reconfigure many functions to ease the task of data entry:

.. i18n: * adding controls for data entry,
.. i18n: 
.. i18n: * customizing the screens,
.. i18n: 
.. i18n: * filling fields automatically during data entry with data that's already known to the system.

* adding controls for data entry,

* customizing the screens,

* filling fields automatically during data entry with data that's already known to the system.

.. i18n: For this chapter you should start with a fresh database that includes demo data,
.. i18n: with :mod:`sale` and its dependencies installed and no particular chart of accounts configured. 

For this chapter you should start with a fresh database that includes demo data,
with :mod:`sale` and its dependencies installed and no particular chart of accounts configured. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:     chart_of_accounts
.. i18n:     journals
.. i18n:     periods_and_fiscal_years
.. i18n:     payment_terms
.. i18n:     entries_at_the_start_of_a_year

.. toctree::

    chart_of_accounts
    journals
    periods_and_fiscal_years
    payment_terms
    entries_at_the_start_of_a_year

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
