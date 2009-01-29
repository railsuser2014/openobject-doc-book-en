Logistics and Stock Management
###############################

*Open ERP's stock management is perhaps the most intelligent stock management system that you can get in any of the integrated management software systems on the market at the time of writing. It's extremely simple, flexible and complete, all at the same time.*

It's based on the concept of double entry that revolutionized accounting. What's unique to Open ERP is that this has now been applied to stock management. The system can be described by Lavoisier's maxim “nothing lost, everything changed” or, better, “everything moved”. Talk of disappearance, consumption or loss of products is not used in Open ERP. Instead you talk only of stock moves from one place to another.

And just as in accounting, the system manages counterparts to each of its operations such as receipts from suppliers, deliveries to customers, profits and losses from inventory, and consumption of raw materials. Stock movements are always made from one location to another. To satisfy the need for a counterpart to each stock movement, the software supports different types of stock location:

* Physical stock locations,

* Partner locations,

* Virtual counterparts.

Physical locations represent warehouses and their hierarchical structure. These are generally the locations that are managed by traditional stock management systems.

Partner locations represent your customers' and suppliers' stocks. To reconcile them with your accounts, these stores play the role of third-party accounts. Reception from a supplier can be shown by the movement of goods from a partner location to a physical location in your own company. As you see, supplier locations usually show negative stocks and customer locations usually show positive stocks.

Virtual counterparts for production are used in manufacturing operations. Manufacturing is characterized by the consumption of raw materials and the production of finished products. Virtual locations are used for the counterparts of these two operations.

Inventory locations are counterparts of the stock operations that represent your company's profits and losses in terms of your stocks.

The following figure shows the initial configuration of the stores locations when the software is installed.

    .. image:: images/stock_location_tree.png
       :align: center

*Stores location structure when Open ERP has just been installed.*

.. tip::   **More information**  *Hierarchical stock locations*

    As well as having several location types, locations are also structured hierarchically. Then it becomes possible for you to tree-structure your locations, dependent on a father-son relationship. This lets you have various levels of detail for your analysis of stock operations.

.. raw:: html

    <div class="all-toctree">

.. toctree::

    5_12_stock_management_illustration
    5_12_stock_management_advantages
    5_12_stock_management_wf
    5_12_stock_management_stocks
    5_12_stock_management_logistic
    5_12_stock_management_import
    5_12_stock_management_warehouses
    5_12_stock_management_production.rst
    5_12_stock_management_lots.rst
    5_12_stock_management_journals.rst
    5_12_stock_management_advanced.rst

.. raw:: html

    </div>
