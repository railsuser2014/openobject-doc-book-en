
.. i18n: Form views
.. i18n: ------------

Form views
------------

.. i18n: The field disposition in a form view always follows the same principle. Fields are distributed on the screen following the rules below:

The field disposition in a form view always follows the same principle. Fields are distributed on the screen following the rules below:

.. i18n:     * By default, each field is preceded by a label, with its name.
.. i18n:     * Fields are placed on the screen from left to right, and from top to bottom, according to the order in which they are declared in the view.
.. i18n:     * Every screen is divided into 4 columns, each column being able to contain either a label, or an "edition" field. As every edition field is preceded (by default) by a label with its name, there will be two fields (and their respective labels) on each line of the screen. The green and red zones on the screen-shot below, illustrate those 4 columns. They designate respectively the labels and their corresponding fields. 

    * By default, each field is preceded by a label, with its name.
    * Fields are placed on the screen from left to right, and from top to bottom, according to the order in which they are declared in the view.
    * Every screen is divided into 4 columns, each column being able to contain either a label, or an "edition" field. As every edition field is preceded (by default) by a label with its name, there will be two fields (and their respective labels) on each line of the screen. The green and red zones on the screen-shot below, illustrate those 4 columns. They designate respectively the labels and their corresponding fields. 

.. i18n: .. figure::  images/sale_order.png
.. i18n:    :scale: 50
.. i18n:    :align: center

.. figure::  images/sale_order.png
   :scale: 50
   :align: center

.. i18n: Views also support more advanced placement options:

Views also support more advanced placement options:

.. i18n:     * A view field can use several columns. For example, on the screen-shot below, the zone in the blue frame is, in fact, the only field of a "one to many". We will come back later on this note, but let's note that it uses the whole width of the screen and not only one column. 

    * A view field can use several columns. For example, on the screen-shot below, the zone in the blue frame is, in fact, the only field of a "one to many". We will come back later on this note, but let's note that it uses the whole width of the screen and not only one column. 

.. i18n:       .. figure::  images/sale_order_sale_order_lines.png
.. i18n:         :scale: 50
.. i18n:         :align: center
.. i18n: 
.. i18n:     * We can also make the opposite operation: take a columns group and divide it in as many columns as desired. The surrounded green zones of the screen above are good examples. Precisely, the green framework up and on the right side takes the place of two columns, but contains 4 columns. 

      .. figure::  images/sale_order_sale_order_lines.png
        :scale: 50
        :align: center

    * We can also make the opposite operation: take a columns group and divide it in as many columns as desired. The surrounded green zones of the screen above are good examples. Precisely, the green framework up and on the right side takes the place of two columns, but contains 4 columns. 

.. i18n: As we can see below in the purple zone of the screen, there is also a way to distribute the fields of an object on different tabs.

As we can see below in the purple zone of the screen, there is also a way to distribute the fields of an object on different tabs.

.. i18n: .. figure::  images/sale_order_notebook.png
.. i18n:    :scale: 50
.. i18n:    :align: center

.. figure::  images/sale_order_notebook.png
   :scale: 50
   :align: center
