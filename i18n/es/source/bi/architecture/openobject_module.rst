
.. i18n: Introduction to the OpenObject Module
.. i18n: =====================================

Introduction to the OpenObject Module
=====================================

.. i18n: The OLAP module is used in validating , running  and formatting the output of MDXExamples

The OLAP module is used in validating , running  and formatting the output of MDXExamples

.. i18n: The general flow is of OLAP module is shown in following diagram:

The general flow is of OLAP module is shown in following diagram:

.. i18n: .. image::  images/Cube_olap_schema.png

.. image::  images/Cube_olap_schema.png

.. i18n: Explanation of the components
.. i18n: -----------------------------

Explanation of the components
-----------------------------

.. i18n: Web-Services
.. i18n: ++++++++++++

Web-Services
++++++++++++

.. i18n: This is the layer provided by the base of Open  ERP, protocols: NET-RPC (fast binary), XML-RPC, over HTTP or HTTPS

This is the layer provided by the base of Open  ERP, protocols: NET-RPC (fast binary), XML-RPC, over HTTP or HTTPS

.. i18n: Services
.. i18n: ++++++++

Services
++++++++

.. i18n: Layer provided by Open  ERP that provides: authentification (normal/ldap), users management, access rights, workflows, module management, ...

Layer provided by Open  ERP that provides: authentification (normal/ldap), users management, access rights, workflows, module management, ...

.. i18n: MDX Parser
.. i18n: ++++++++++

MDX Parser
++++++++++

.. i18n: It parses the MDX query and convert it in the form of python objects. It uses pyparsing module of python to do this . It split the query in form of objects of axis, level, sub level, slicer (if any) and measures. 

It parses the MDX query and convert it in the form of python objects. It uses pyparsing module of python to do this . It split the query in form of objects of axis, level, sub level, slicer (if any) and measures. 

.. i18n: MDX Validator
.. i18n: +++++++++++++

MDX Validator
+++++++++++++

.. i18n: It parse all the objects created and map it to the browse object ofOpen  ERP resource. For example, the axis object will receive a link to the Open  ERP browse record on the related olap.axis object.

It parse all the objects created and map it to the browse object ofOpen  ERP resource. For example, the axis object will receive a link to the Open  ERP browse record on the related olap.axis object.

.. i18n: MDX Runner
.. i18n: ++++++++++

MDX Runner
++++++++++

.. i18n: It will run the query on the basis of objects using SQLAlchemy and return different subsets.
.. i18n: On the basis of it the cube is virtually made in the form of matrix.
.. i18n: And it fills the cube by values using axis mapping

It will run the query on the basis of objects using SQLAlchemy and return different subsets.
On the basis of it the cube is virtually made in the form of matrix.
And it fills the cube by values using axis mapping

.. i18n: RDBMS connectors
.. i18n: ++++++++++++++++

RDBMS connectors
++++++++++++++++

.. i18n: The layer provided by SQL Alchemy, it supports: mysql, postgresql, oracle, ...

The layer provided by SQL Alchemy, it supports: mysql, postgresql, oracle, ...

.. i18n: The schema definition is in the Open  ERP database.

The schema definition is in the Open  ERP database.
