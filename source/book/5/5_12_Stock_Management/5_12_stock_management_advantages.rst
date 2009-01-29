Advantages of Open ERP's stock management approach
====================================================

Before going any further in discussing the practical application of Open ERP's stock management, review the benefits gained from this approach. 

Stock Management is never correct
----------------------------------

You can have the most organized company in the world, yet you'll quickly find that stock management is never completely correct. If you compare the current stock levels with those shown on your stock management system you'll always find a discrepancy in stock levels that can have a greater or lesser effect on you depending on your company.

That's easy to explain. Manual stock operations quickly result in such discrepancies. It's so easy to forget to code in a goods receipt, or to send too many items to a customer compared with the number specified on the order, or to have thefts or genuinely lost items.

Double-entry stock management gives you very efficient traceability so that you can look for all the stock management errors that you'll get. Classic stock management software gives you the sum of all stock moves for a warehouse and a given product (+3, -2, +5, -1 in this case, giving you a total of +5). In these conditions, with so many stock moves, it's nearly impossible to discover the source of any error.

It's completely different in Open ERP. Double-entry stock management actually gives you two places to look for an error, which significantly improves your chances of finding where errors have occurred. If you forget two stock items the error is automatically reflected in the counterpart location. Such a loss of two items can come from:

* A partner location (forgetting to enter data about a receipt or delivery),

* A production location (too high or low a consumption),

* An inventory location (loss or theft).

Furthermore, you can reconcile it with other Open ERP documents such as sales documents, purchases or production orders, which can help you in your search for problems.

You can compare it with accounts where it's quite straightforward to find errors because you can look for anomolies in accounts or in counterparts. All the time you know that the sum of debits equals the sum of credits.

Stock management must be flexible
----------------------------------

To be efficient, stock management must be as close as possible to reality. But since stock levels aren't possible to predict exactly, it's very important for the stock management system to be flexible. Very few of the available stock management systems provide storespeople and assembly operators with much of the flexibility that they need to manage stocks and production.

Take the case of a new product not yet in stock, and you have forgotten to enter its data when you received it into stores. If he notices it in the set of available products, the storesperson will want to send it to a customer. Few systems can cope with managing this general problem because, if the products haven't been entered into stock then they'll refuse to deliver them. And if the storesperson has actually sent the products on to the customer then such systems won't be able to enter the data about them into the system later. You risk such errors snowballing.

Open ERP's flexibility prevents such a problem. Open ERP supports the concept of negative stock to manage this. The when the storesperson delivers the product to the customer, the stock goes negative because it was never entered at goods in. This poses no problem to Open ERP – the negative value just helps indicate that there's a problem to resolve. Once you've noticed the problem and corrected it by entering the goods-in data the stock returns to its correct level.

This flexibility comes into play whenever it's needed, throughout the most complex operations such as multi-level and lean manufacture. You can always force the system to change the stock values to reflect reality, even in the middle of a complex workflow.

Control of stock management
----------------------------

Stock management must be well controlled to be increasingly effective in meeeting and exceeding company expectations such as improving bottleneck situations, reducing stock quantities, limiting lack of availability, assuring security stocks, and forecasting stock moves.

Double-entry stock management lets you make analyses on several levels. You're not limited to physical stock in your company warehouses, but can also analyze the different virtual locations. All the stock operations in the system can be carried out on both physical and virtual locations such as stock valuation, traceability, historical account valuations, stock forecasts and restocking rules.

Furthermore, the hierarchical location structure enables you to structure both your physical and virtual stocks without limit. For example, you can structure your production locations by product and your partner locations by geography. That gives you all the power of an analytic accounting system applied to stock management.

Stock statistics should be synchronized with stock management
--------------------------------------------------------------

If you have already experienced traditional stock management software you'll already know the problem of getting reliable indicators. If you ask your accountant for a stock valuation or the added value given by production, he'll give you one figure. If you ask the same thing of your stores manager you'll get a rather different figure. It's a terrible situation, because you don't know which figure is more reliable.

Open ERP's stock management is completely integrated with accounts so that both figures are completely synchronized at all times. Stock double entry completely reflects accounting double entry. You can use the system to value stock in real time in your accounts, and this figure will be both up to date and reliable.

Complete traceability
----------------------

The software isn't restricted only to traceability for operations carried out in your warehouse. In certain areas that can pose several problems. For example, in agro-food there are more and more constraints on traceability.

Open ERP enables you to manage not just your own stock but also supplier and customer stocks. Its traceability extends along the whole chain from supplier to customer, not just your warehouse. So you can have products that make the whole circuit from supplier > stock > customer > returned stock.

The figure below shows the traceability for a PC2 computer, which as been assembled in several steps. This figure is based on Open ERP's demonstration data.

    .. image:: images/stock_traceability.png
       :align: center

*Traceability for a computer.*


