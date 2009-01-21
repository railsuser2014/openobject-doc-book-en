
Solaris 10 OpenERP Installation
"""""""""""""""""""""""""""""""

One needs

 * JDS CBE
 * Sun Studio 12

Install JDS CBE according to guide and set up paths.

Assume the role of Primary Administrator or become a root.

Enable postgreSQL:

::

  # svcadm enable svc:/application/database/postgresql:version_82

or, for 64-bit version:

::

  # svcadm enable svc:/application/database/postgresql:version_82_64bit

Confirm that the service is running.

::

  svcs -x | grep postgresq

or

::

  svcs -l postgresql

