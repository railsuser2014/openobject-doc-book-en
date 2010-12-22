
.. index::
   single: Manufacturing
   single: production; management

.. _ch-mnf:

*************
Manufacturing
*************

 *The management of manufacturing described in this chapter covers
 planning, ordering, stocks and the manufacturing or assembly of products from raw materials and
 components.
 It also discusses consumption and production of products, as well as the necessary operations on
 machinery, tools or human resources.*

The management of manufacturing in Open ERP is based on its stock management and, like it, is very
flexible in both its operations and its financial control. It benefits particularly from the use of
double-entry stock management for production orders.

.. index::
   single: module; mrp

Manufacturing management is implemented by the :mod:`mrp` module. It is used for transforming all
types of products:

* Assemblies of parts: composite products, soldered or welded products, assemblies, packs,

* Machined parts: machining, cutting, planing,

* Foundries: clamping, heating,

* Mixtures: mixing, chemical processes, distillation.

You will work in two areas: on products in the first part of this chapter, and on operations in the
second part. The management of products depends on the concept of classifications while the
management of operations depends on routing and workcenters.

.. index::
   single: bill of materials

.. note:: Bills of Materials

    Bills of Materials, or manufacturing specifications, go by different names depending on their
    application area, for example:

    * Food: Recipes,

    * Chemicals: Equations,

    * Building: Plans.

For this chapter you should start with a fresh database that includes demo data,
with :mod:`mrp` and its dependencies installed and no particular chart of accounts configured.

.. raw:: html

    <div class="all-toctree">

.. toctree::

   5_15_Manufacturing_production
   5_15_Manufacturing_lead

.. raw:: html

    </div>

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

