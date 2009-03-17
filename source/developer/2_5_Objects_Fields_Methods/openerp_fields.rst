Fields Introduction
===================

Objects may contain different types of fields. Those types can be divided into three categories: simple types, relation types and functional fields. The simple types are integers, floats, booleans, strings, etc ... ; the relation types are used to represent relations between objects (one2one, one2many, many2one). Functional fields are special fields because they are not stored in the database but calculated in real time given other fields of the view.

Here's the header of the initialization method of the class any field defined in Open ERP inherits (as you can see in server/bin/osv/fields.py)::

        def __init__(self, string='unknown', required=False, readonly=False,
			domain=[], context="", states={}, priority=0, change_default=False, size=None, 
                        ondelete="setnull", translate=False, select=False, **args) :


