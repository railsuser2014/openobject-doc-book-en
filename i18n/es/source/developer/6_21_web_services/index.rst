
.. i18n: Working with Web Services
.. i18n: =========================

Working with Web Services
=========================

.. i18n: How to load data ?
.. i18n: ------------------

How to load data ?
------------------

.. i18n:    1. Postgresql
.. i18n:           * Simple, standard
.. i18n:           * Does not respect the WORKFLOW !!! 
.. i18n:    2. XML files (with –update=)
.. i18n:    3. XML-RPC
.. i18n:           * Script, same as website interface 

   1. Postgresql
          * Simple, standard
          * Does not respect the WORKFLOW !!! 
   2. XML files (with –update=)
   3. XML-RPC
          * Script, same as website interface 

.. i18n: How to backup/restore a Postgresql database?

How to backup/restore a Postgresql database?

.. i18n:     backup

    backup

.. i18n:         pg_dump terp >terp.sql 

        pg_dump terp >terp.sql 

.. i18n:         restore

        restore

.. i18n:         createdb terp --encoding=unicode 
.. i18n:         psql terp < terp.sql 
.. i18n:         or 
.. i18n:         psql -d terp -f terp.sql 

        createdb terp --encoding=unicode 
        psql terp < terp.sql 
        or 
        psql -d terp -f terp.sql 

.. i18n: The objects methods
.. i18n: -------------------

The objects methods
-------------------

.. i18n:    1. create({'field':'value'})
.. i18n:           * return ID created 
.. i18n:    2. search([('arg1','=','value1')...], offset=0, limit=1000)
.. i18n:           * return [IDS] found 
.. i18n:    3. read([IDS], ['field1','field2',...])
.. i18n:           * return [{'id':1, 'field1':..., 'field2':..., ...}, ...] 
.. i18n:    4. write([IDS], {'field1':'value1','field2':3})
.. i18n:           * return True 
.. i18n:    5. unlink([IDS])
.. i18n:           * return True 

   1. create({'field':'value'})
          * return ID created 
   2. search([('arg1','=','value1')...], offset=0, limit=1000)
          * return [IDS] found 
   3. read([IDS], ['field1','field2',...])
          * return [{'id':1, 'field1':..., 'field2':..., ...}, ...] 
   4. write([IDS], {'field1':'value1','field2':3})
          * return True 
   5. unlink([IDS])
          * return True 

.. i18n: 	
.. i18n: 	

	
	
