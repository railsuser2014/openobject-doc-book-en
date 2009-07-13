
.. i18n: MVC - Model, View, Controller 
.. i18n: =============================

MVC - Model, View, Controller 
=============================

.. i18n: According to `Wikipedia <http://en.wikipedia.org/wiki/Model-view-controller>`_,"a Model-view-controller (MVC) is an architectural pattern used in software engineering. In complex computer applications that present lots of data to the user, one often wishes to separate data (model) and user interface (view) concerns, so that changes to the user interface do not impact the data handling, and that the data can be reorganized without changing the user interface. The model-view-controller solves this problem by decoupling data access and business logic from data presentation and user interaction, by introducing an intermediate component: the controller."

According to `Wikipedia <http://en.wikipedia.org/wiki/Model-view-controller>`_,"a Model-view-controller (MVC) is an architectural pattern used in software engineering. In complex computer applications that present lots of data to the user, one often wishes to separate data (model) and user interface (view) concerns, so that changes to the user interface do not impact the data handling, and that the data can be reorganized without changing the user interface. The model-view-controller solves this problem by decoupling data access and business logic from data presentation and user interaction, by introducing an intermediate component: the controller."

.. i18n: .. figure::  images/MVCDiagram.png
.. i18n:    :scale: 100
.. i18n:    :align: center

.. figure::  images/MVCDiagram.png
   :scale: 100
   :align: center

.. i18n: For example, in the diagram above, the solid lines for the arrows starting from the controller and going to both the view and the model mean that the controller has a complete access to both the view and the model. The dashed line for the arrow going from the view to the controller means that the view has a limited access to the controller. The reasons of this design are :

For example, in the diagram above, the solid lines for the arrows starting from the controller and going to both the view and the model mean that the controller has a complete access to both the view and the model. The dashed line for the arrow going from the view to the controller means that the view has a limited access to the controller. The reasons of this design are :

.. i18n:     * From **View** to **Model** : the model sends notification to the view when its data has been modified in order the view to redraw its content. The model doesn't need to know the inner workings of the view to perform this operation. However, the view needs to access the internal parts of the controller.
.. i18n:     * From **View** to **Controller** : the reason why the view has limited access to the controller is because the dependencies from the view to the controller need to be minimal: the controller can be replaced at any moment. 

    * From **View** to **Model** : the model sends notification to the view when its data has been modified in order the view to redraw its content. The model doesn't need to know the inner workings of the view to perform this operation. However, the view needs to access the internal parts of the controller.
    * From **View** to **Controller** : the reason why the view has limited access to the controller is because the dependencies from the view to the controller need to be minimal: the controller can be replaced at any moment. 

.. i18n: MVC Model in Tiny ERP
.. i18n: ---------------------
.. i18n: In Tiny ERP, we can apply this model-view-controller semantic with

MVC Model in Tiny ERP
---------------------
In Tiny ERP, we can apply this model-view-controller semantic with

.. i18n:     * model : The PostgreSQL tables.
.. i18n:     * view : views are defined in XML files in Tiny ERP.
.. i18n:     * controller : The objects of TinyERP. 

    * model : The PostgreSQL tables.
    * view : views are defined in XML files in Tiny ERP.
    * controller : The objects of TinyERP. 
