
.. i18n: .. index:: payment terms

.. index:: payment terms

.. i18n: Payment Terms
.. i18n: =============

Payment Terms
=============

.. i18n: You can define whatever payment terms you need in Open ERP. Payment terms determine the due dates
.. i18n: for paying an invoice.

You can define whatever payment terms you need in Open ERP. Payment terms determine the due dates
for paying an invoice.

.. i18n: To define new payment terms, use the menu :menuselection:`Financial Management --> 
.. i18n: Configuration --> Payment Terms` and then click :guilabel:`New`.

To define new payment terms, use the menu :menuselection:`Financial Management --> 
Configuration --> Payment Terms` and then click :guilabel:`New`.

.. i18n: The figure below represents the following payment term: 35% on delivery, the balance 15 days after
.. i18n: the end of the month.

The figure below represents the following payment term: 35% on delivery, the balance 15 days after
the end of the month.

.. i18n: .. figure::  images/account_payment_term.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuring payment terms*

.. figure::  images/account_payment_term.png
   :scale: 50
   :align: center

   *Configuring payment terms*

.. i18n: To configure new conditions start by giving a name to the :guilabel:`Payment Term` field. Text that
.. i18n: you put in the field :guilabel:`Description` is used on invoices, so enter a clear description of
.. i18n: the payment terms there.

To configure new conditions start by giving a name to the :guilabel:`Payment Term` field. Text that
you put in the field :guilabel:`Description` is used on invoices, so enter a clear description of
the payment terms there.

.. i18n: Then create individual lines for calculating the terms in the section :guilabel:`Payment Term`. You
.. i18n: must give each line a name (:guilabel:`Line Name`). These give an informative title and don't affect
.. i18n: the actual calculation of terms. The :guilabel:`Sequence` field lets you define the order in which
.. i18n: the rules are evaluated.

Then create individual lines for calculating the terms in the section :guilabel:`Payment Term`. You
must give each line a name (:guilabel:`Line Name`). These give an informative title and don't affect
the actual calculation of terms. The :guilabel:`Sequence` field lets you define the order in which
the rules are evaluated.

.. i18n: The :guilabel:`Value` field enables you to calculate the amount to pay for each line:

The :guilabel:`Value` field enables you to calculate the amount to pay for each line:

.. i18n: * :guilabel:`Percent` : the line corresponds to a percentage of the total amount, the factor being
.. i18n:   given in :guilabel:`Amount`. The number indicated in the Amount must take a value between 0 and 1.
.. i18n: 
.. i18n: * :guilabel:`Fixed amount` : this is a fixed value given by the :guilabel:`Amount` box.
.. i18n: 
.. i18n: * :guilabel:`Balance` : indicates the balance remaining after accounting for the other lines.

* :guilabel:`Percent` : the line corresponds to a percentage of the total amount, the factor being
  given in :guilabel:`Amount`. The number indicated in the Amount must take a value between 0 and 1.

* :guilabel:`Fixed amount` : this is a fixed value given by the :guilabel:`Amount` box.

* :guilabel:`Balance` : indicates the balance remaining after accounting for the other lines.

.. i18n: Think carefully about setting the last line of the calculation to \ ``Balance``\   to avoid rounding
.. i18n: errors. The highest sequence number is evaluated last.

Think carefully about setting the last line of the calculation to \ ``Balance``\   to avoid rounding
errors. The highest sequence number is evaluated last.

.. i18n: The two last fields, :guilabel:`Number of Days` and :guilabel:`Condition`, enable the calculation of
.. i18n: the delay in payment for each line, The delay :guilabel:`Condition` can be set to \ ``Net Days``\
.. i18n: or \ ``End of Month``\  . For example if you set it to 15 days from the end of the month Open ERP
.. i18n: adds 15 days to today's date and then sets the payment date to be the end of the month that the new
.. i18n: date is in. So the payment date for 15 days from month end will be:

The two last fields, :guilabel:`Number of Days` and :guilabel:`Condition`, enable the calculation of
the delay in payment for each line, The delay :guilabel:`Condition` can be set to \ ``Net Days``\
or \ ``End of Month``\  . For example if you set it to 15 days from the end of the month Open ERP
adds 15 days to today's date and then sets the payment date to be the end of the month that the new
date is in. So the payment date for 15 days from month end will be:

.. i18n: * 31 January if today is 5 January,
.. i18n: 
.. i18n: * 28 February if today is 20 January.

* 31 January if today is 5 January,

* 28 February if today is 20 January.

.. i18n: You can then add payment terms to a Partner through the :guilabel:`Properties` on the partner form.

You can then add payment terms to a Partner through the :guilabel:`Properties` on the partner form.

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
