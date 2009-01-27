Operations
===========

In the first part of this chapter, manufacturing management was handled in terms of products and materials. This section focuses on manufacturing operations. To manufacture or assemble products, as well as using raw materials and finished product you should handle operations such as assembly, drilling wood, and cutting timber.

The different operation will have impacts on the costs of manufacture and the planning as function of the available workload.

Definition of concepts
-----------------------

To manage operations you should understand the following concepts

* Workcenters,

* Routing,

* Operations.

Workcenters
-----------

Workcenters represent units of product, capable of doing material transformation operations. You can distinguish three types of workcenter: machines, tools and human resources.

.. tip::   **Definition** *Workcenter*

    Workcenters are units of manufacture, consisting of one or several people and/or machines, which can be considered as a unit for the purposes of forecasting capacity and planning.

Use the menu *Manufacturing > Configuration > Workcenters* to define a new workcenter. You get a form as shown in the figure below.

    .. image:: images/mrp_workcenter.png
       :align: center

*Definition of a workcenter.*

A workcenter must have a name and a code. You then assign a type: machine, human resource, tool, and a description of operating hours or functionality. The figure below represents the hours from Monday to Friday, from 09:00 to 17:00 with a break of an hour from 12:00.

    .. image:: images/mrp_workcenter_working_hour.png
       :align: center

*Working hours for a workcenter.*

You should show a description of the workcenter and its operations.

Once the database is encoded you should enter data about the production capacity of the workcenter. Depending on whether you have a machine or a person, a workcenter will be defined in cycles or hours. If it represents a set of machines and people you can use both cycles and hours at the same time.

.. tip::   **Definition**  *A Cycle*

    A cycle corresponds to the time required to carry out an assembly operation. The user is free to determine which is the reference operation for a given workcenter. It must be represented by the cost and time of manufacture.

    For example, for a printing workcenter, a cycle will be the printing of 1 page. Or the printing of 1000 pages depending on the printer.

To define the capacity well it is necessary know for each workcenter what will be the reference operation which will serve to determine the cycle. You can then define the data relative to the capacity.

Capacity per cycle (CA): determine the number of operations that can be done in parallel during a cycle. Generally the number defines the number of identical machines or people defined by the workcenter.

Time for a cycle (TC): give the duration in hour for that or the operations defined by a cycle.

Time before production (TS): give the wait in hours to initialise production operations. Generally this represents the machine setup time.

Time after production (TN): give the delay in hours after the end of a production operation. Generally this represents the cleaning time necessary after an operation.

Effective time (ET): is a factor that is applied to the three times above to determine the real production time. This factor enables you to readjust the different times progressively and as a measure of machine utilization. You can't readjust the other times because generally they're taken from the machine's data sheet.

The total time for carrying out X operations is then given by the following formula: ((C / CA) * TC + TS + TN\_ * ET. In this formula the result of the division is rounded upwards. Then if the capacity per cycle is 6 it takes 3 cycles to realize 15 operations.

.. tip::   **Point** *Multi-level routing*

It is possible to define routing on several levels to support multi-level Bills of Materials

Then on each level of a Bill of Materials you can indicate the range. The levels are then linked to hierarchies of Bills of Materials.

The second tab of the production order lets you define the links to analytical account to report the costs of the workcenter operations. If you leave the different fields empty Open ERP won't have any effect on the analytic accounts.

    .. image:: images/mrp_workcenter_tab.png
       :align: center

*Data about analytic accounts for a workcenter.*

Routing
--------

Routings define the assembly operations to be done in workcenters for manufacturing a certain product. They are usually attached to Bills of Materials which will define the assembly of products required for manufacture or for finished products.

A routing can be defined directly in a Bill of Materials or through the menu Manufacturing > Configuration > Routings. A routing has a name, a code and a description. Later in this chapter you'll see that a routing can also be associated with a stock location. That enable you to indicate where assembly takes place.

    .. image:: images/mrp_routing.png
       :align: center

*Definition of a routing with three operations.*

.. tip::  **Point**  *Subcontracting assembly*

    You'll see further on in this chapter that it is possible to link a routing and a stock location for the customer or the supplier. It's the case, for examply. After you've subcontracted the assembly of a product to a supplier.

In the routing you must show the list of operations that must be done. Each operation must be done at a workcenter and possess a number of hours and/or cycles be done.

Impact of the production order
-------------------------------

The routings are then attached to the Bills of Materials which are then also used to generate product order. On a production order one the finds the assembly operations for making on the tab called 'Operations'.

mrp_production_workorder.png


Operations on a production order.

The times and the cycles shown in the production order are in the same way as the materials, theoretical data. The user can change the values to reflect reality for manufacture. 

So if you use routings, Open ERP automatically calculates the operations required for the production order. If the workcenters are linked to analytic accounts, at the end of production, Open Erp will generate the analytic accounts representing the costs of manufacture. This will allow you to work out profitability per workcenter or manufacturing unit through analytic accounting.

But the routings also enable you to manage your production capacity. You will be able to leave the demand charts for the days / weeks / months ahead to validate that you don't forecast more than you are capable of producing.

To see a demand chart, list the workcenters using the menu *Manufacturing > Configuration > Workcenters*. Then select one or several workcenters and click on the action *Workcenter load*. Open ERP then asks you if you work in cycles or in hours and your interval is calculated (by day, week or month).

    .. image:: images/mrp_workcenter_load.png
       :align: center

*Charge by workcenter.*

.. tip::  **Point** *Theoretical times*

Once the routings have been clearly defined, that enables you to determine the effective  working time per assembly worker. The time corresponds to the time for each operation actually taken by the assembly worker. That enables you to compare the real working time in your company and work out the productivity per persons.

Work operations
----------------

A production order is for several products defined in the Bills of Materials, and several operations, defined in the routing. You've seen how to handle manufacturing production by production, Some companies like to have finer-grained control of operations where instead of encoding the production they enter data on each constituent operation of production.

Management of operations
-------------------------

.. tip::   **Definition**  *Operations*

    Operations are often called work orders.

To work using work orders you must install the optional module mrp_operations. Once the module is installed you'll find a new menu called Manufacturing > Operations > Operations to be carried out. The assembly workers must then encode each step operation by operation and, for each step, the real working time for it.

    .. image:: images/mrp_operations_tree.png
       :align: center

*List of operations to be carried out.*

Operations must then be carried out one by one. On each operation the operator can click on 'Start operation' and then 'Close Operation'. The time is then worked out automatically on the operation between the two changes of status. The operator can also put the operation on hold and start again later.

The following process is attached to each operation.

    .. image:: images/mrp_operations_workflow,png
       :align: center

*Process for handling an operation.*

Thanks to this use by operation, the real working time is recorded on the production order.

The production order is automatically put into the state 'Running' once the first operation has been started. That consumes some raw materials. Similarly the production order is closed automatically once the last operation is completed. The finished products are then made.


