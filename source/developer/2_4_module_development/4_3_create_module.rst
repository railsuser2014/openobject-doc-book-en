
Create Module
=============

Getting the skeleton directory
------------------------------

Creating a new module is quickly done by copying the module called "simple" or "custom" (depending on your OpenERP version) into a new directory.

As an example on Ubuntu:
::

	$ cd /usr/lib/openerp-server/addons/
	$ sudo cp -r custom travel

You will need to give yourself permissions over that new directory if you want to be able to modify it:
::

	$ sudo chown -R `whoami` travel

You got yourself the directory for a new module there, and a skeleton structure, but you still need to change a few things inside the module's definition...

Changing the default definition
-------------------------------

To change the default settings of the custom module (which is now the "travel" module), get yourself into the "travel" directory and edit *__terp__.py. gedit*, in the following example, is just a simple text editor. Feel free to use another one.
::

	$ cd travel
	$ gedit __terp__.py

The file looks like this:
::

	#
	# Use the custom module to put your specific code in a separate module.
	# 
	{
		"name" : "Module for custom developments",
		"version" : "1.0",
		"author" : "Tiny",
		"category" : "Generic Modules/Others",
		"website": "http://www.tinyerp.com",
		"description": "Sample custom module where you can put your customer specific developments.",
		"depends" : ["base"],
		"init_xml" : [],
		"update_xml" : ["custom_view.xml"],
		"active": False,
		"installable": True
	}

You will want to change whichever settings you feel right and get something like this:
::

	{
		"name" : "Travel agency module",
		"version" : "1.0",
		"author" : "Tiny",
		"category" : "Generic Modules/Others",
		"website": "http://www.tinyerp.com",
		"description": "A module to manage hotel bookings and a few other useful features.",
		"depends" : ["base"],
		"init_xml" : [],
		"update_xml" : ["custom_view.xml"],
		"active": True,
		"installable": True
	}


Note the "active" field becomes true.

Changing the main module file
-----------------------------

Now you need to update the custom.py script to suit the needs of your module. We suggest you follow the Flash tutorial for this or download the travel agency module from the 20 minutes tutorial page.
::

	The documentation below is overlapping the two next step in this wiki tutorial, 
	so just consider them as a help and head towards the next two pages first...

The custom.py file should initially look like this (intentionally removing the comments):

	from osv import osv, fields
	 
	#class custom_material(osv.osv):
	#       _name = 'network.material'
	#       _inherit = 'network.material'
	#       _columns = {
	#       }
	#       _defaults = {
	#       }
	#custom_material()

The '#' signs represent comments. You'll have to remove them, rename the class and its attributes to something like this:
::

	from osv import osv, fields
	 
	class travel_hostel(osv.osv):
	       _name = 'travel.hostel'
	       _inherit = 'res.partner'
	       _columns = {
		   'rooms_id': fields.one2many('travel.room', 'hostel_id', 'Rooms'),
		   'quality': fields.char('Quality', size=16),
	       }
	       _defaults = {
	       }
	travel_hostel()

Ideally, you would copy that bunch of code several times to create all the entities you need (travel_airport, travel_room, travel_flight). This is what will hold the database structure of your objects, but you don't really need to worry too much about the database side. Just filling this file will create the system structure for you when you install the module.

Customizing the view
--------------------

You can now move on to editing the views. To do this, edit the custom_view.xml file. It should first look like this:
::

	<terp>
	<data>
		<record model="res.groups" id="group_compta_user">
		        <field name="name">grcompta</field>
		</record>
		<record model="res.groups" id="group_compta_admin">
		        <field name="name">grcomptaadmin</field>
		</record>
		<menuitem name="Administration" groups="admin,grcomptaadmin" icon="terp-stock" id="menu_admin_compta"/>
	</data>
	</terp>

This is, as you can see, an example taken from an accounting system (French people call accounting "comptabilité", which explains the compta bit).

Defining a view is defining the interfaces the user will get when accessing your module. Just defining a bunch of fields here should already get you started on a complete interface. However, due to the complexity of doing it right, we recommend, once again, that you take a look at the 20 minutes Flash tutorial or download the travel agency module example.

Next you should be able to create different views using other files to separate them from your basic/admin view. 
