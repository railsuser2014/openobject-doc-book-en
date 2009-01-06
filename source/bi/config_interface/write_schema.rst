Writing a Schema
----------------

.. describe::  What is Schema ?

Schema in general means shape or more generally plan . In the context of OpenObject BI it defines the logical model, consisting of cubes, hierarchies, and members, and a mapping of this model onto a physical model.

The logical model consists of the constructs used to write queries in MDX language: cubes, dimensions, hierarchies, levels, and members.

The physical model is the source of the data which is presented through the logical model. It is typically a star schema, which is a set of tables in a relational database; later, we shall see examples of other kinds of mappings.

Making Schema
+++++++++++++

In OpenObject BI schemas are represented in a XML file. It can be designed in the way TinyERP does. The details of XML file can be seen at *Creating XML*

