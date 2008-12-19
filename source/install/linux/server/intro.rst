
Server Installation on Linux
++++++++++++++++++++++++++++

Steps to perform:

  #. Install required Software
  #. a Postgresql user and database
  #. Install OpenERP Server software

    #. you may have to delete (rm) ~/.terp_serverrc on Linux when running a new server version
    #. apt-get install python-pyopenssl
    #. creation of a new private key and digital cert. These 2 files are needed to run
       the server with the -S option (Thanks to Pedro)

       ::

          cd <to_the_directory_where_tinyerp-server.py_is_located>
          openssl genrsa > server.pkey
          openssl req -new -x509 -key server.pkey -out server.cert
          chmod 600 server.pkey
          chmod 600 server.cert

.. note:: GhostScript must be installed on all OS platforms for the WorkFlow
   plugin to work


