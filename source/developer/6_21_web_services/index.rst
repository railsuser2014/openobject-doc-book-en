Working with Web Services
=========================

How to load data ?
------------------


   1. Postgresql
          * Simple, standard
          * Does not respect the WORKFLOW !!! 
   2. XML files (with –update=)
   3. XML-RPC
          * Script, same as website interface 

How to backup/restore a Postgresql database?

    backup

        pg_dump terp >terp.sql 

        restore

        createdb terp --encoding=unicode 
        psql terp < terp.sql 
        or 
        psql -d terp -f terp.sql 

The objects methods
-------------------

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


	
	
