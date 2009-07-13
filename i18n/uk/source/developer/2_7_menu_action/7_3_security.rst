
.. i18n: Security
.. i18n: ========

Security
========

.. i18n: Three concepts are differentiated into Tiny ERP;

Three concepts are differentiated into Tiny ERP;

.. i18n:    1. The users: person identified by his login/password
.. i18n:    2. The groups: define the access rights of the resources
.. i18n:    3. The roles: determine the roles/duties of the users 

   1. The users: person identified by his login/password
   2. The groups: define the access rights of the resources
   3. The roles: determine the roles/duties of the users 

.. i18n: .. figure::  images/module_base_user.png
.. i18n:    :scale: 120
.. i18n:    :align: center

.. figure::  images/module_base_user.png
   :scale: 120
   :align: center

.. i18n: **The users**

**The users**

.. i18n: They represent physical persons. These are identified with a login and a password. A user may belong to several groups and may have several roles.

They represent physical persons. These are identified with a login and a password. A user may belong to several groups and may have several roles.

.. i18n: A user must have an action set up. This action is executed when the user connects to the program with his login and password. An example of action would be to open the menu at 'Operations'.

A user must have an action set up. This action is executed when the user connects to the program with his login and password. An example of action would be to open the menu at 'Operations'.

.. i18n: The preferences of the user are available with the preference icon. You can, for example, through these preferences, determine the working language of this user. English is set by default.

The preferences of the user are available with the preference icon. You can, for example, through these preferences, determine the working language of this user. English is set by default.

.. i18n: A user can modify his own preferences while he is working with Tiny ERP. To do that, he clicks on this menu: User > Preferences. The Open ERP administrator can also modify some preferences of each and every user.

A user can modify his own preferences while he is working with Tiny ERP. To do that, he clicks on this menu: User > Preferences. The Open ERP administrator can also modify some preferences of each and every user.

.. i18n: **The groups**

**The groups**

.. i18n: The groups determine the access rights to the different resources. There are three types of right:

The groups determine the access rights to the different resources. There are three types of right:

.. i18n:     * The writing access: recording & creation,
.. i18n:     * The reading access: reading of a file,
.. i18n:     * The execution access: the buttons of workflows or wizards. 

    * The writing access: recording & creation,
    * The reading access: reading of a file,
    * The execution access: the buttons of workflows or wizards. 

.. i18n: A user can belong to several groups. If he belongs to several groups, we always use the group with the highest rights for a selected resource.

A user can belong to several groups. If he belongs to several groups, we always use the group with the highest rights for a selected resource.

.. i18n: **The roles**

**The roles**

.. i18n: The roles define a hierarchical structure in tree. They represent the different jobs/roles inside the company. The biggest role has automatically the rights of all the inferior roles.

The roles define a hierarchical structure in tree. They represent the different jobs/roles inside the company. The biggest role has automatically the rights of all the inferior roles.

.. i18n: **Example:**

**Example:**

.. i18n: CEO

CEO

.. i18n:   + Technical manager

  + Technical manager

.. i18n:     - Chief of projects
.. i18n: 
.. i18n:       - Developers
.. i18n:       - Testers

    - Chief of projects

      - Developers
      - Testers

.. i18n:   + Commercial manager

  + Commercial manager

.. i18n:       - Salesmen
.. i18n:       - ...

      - Salesmen
      - ...

.. i18n: If we want to validate the test of a program (=role Testers), it may be done by a user having one of the following roles: Testers, Chief of the project, Technical manager, CEO.

If we want to validate the test of a program (=role Testers), it may be done by a user having one of the following roles: Testers, Chief of the project, Technical manager, CEO.

.. i18n: The roles are used for the transition of Workflow actions into confirmation, choice or validation actions. Their implications will be detailed in the Workflow section. 

The roles are used for the transition of Workflow actions into confirmation, choice or validation actions. Their implications will be detailed in the Workflow section. 

.. i18n: Menu Access
.. i18n: -----------

Menu Access
-----------

.. i18n: It's easy (but risky) to grant grained access to menu based on the user's groups.

It's easy (but risky) to grant grained access to menu based on the user's groups.

.. i18n: First of all, you should know that if a menu is not granted to any group then it is accessible to everybody ! If you want to grant access to some groups just go to **Menu > Administration > Security > Define access to Menu-items** and select the groups that can use this menu item.

First of all, you should know that if a menu is not granted to any group then it is accessible to everybody ! If you want to grant access to some groups just go to **Menu > Administration > Security > Define access to Menu-items** and select the groups that can use this menu item.

.. i18n: .. figure::  images/grant_access.png
.. i18n:    :scale: 85
.. i18n:    :align: center

.. figure::  images/grant_access.png
   :scale: 85
   :align: center

.. i18n: Beware ! If the Administrator does not belong to one of the group, he will not be able to reach this menu again. 

Beware ! If the Administrator does not belong to one of the group, he will not be able to reach this menu again. 
