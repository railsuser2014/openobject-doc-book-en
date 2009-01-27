
Module Sale Inter-Company - Fully Automatic (*sale_intercompany_auto*)
======================================================================
:Module: sale_intercompany_auto
:Name: Sale Inter-Company - Fully Automatic
:Version: 5.0.1.0
:Directory: sale_intercompany_auto
:Web: http://tinyerp.com/module_sale.html

Description
-----------

::

  This module automatically generates inter-company documents, without
      confirmations or validation steps. When a purchase order is confirmed,
      if the partner exist in one of the company <> from the current one, it
      generates a SO.
  
      Company C1: Sale order -> Purchase Order (MTO)
      Inter-Co : Confirm Purchase Order (C1)
      Inter-Co : Purchase Order (C1) -> Sale Order (C2)
      Inter-Co : Confirm Sale Order (C2)
      Company C2: Continue... picking/porduction/C3
  
      It also works in cascade if you installed the mrp_jit module.

Dependencies
------------

 * sale - installed
 * purchase - installed

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
