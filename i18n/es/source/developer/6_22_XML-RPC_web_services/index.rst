
.. i18n: XML-RPC Web services
.. i18n: ====================

XML-RPC Web services
====================

.. i18n: Jump to: navigation, search

Jump to: navigation, search

.. i18n:    1. **XML-RPC**
.. i18n:           * standard: http://www.xmlrpc.org
.. i18n:           * RPC Over HTTP
.. i18n:           * Function Parameters & Result encoded in XML 
.. i18n:    2. **Principle**;
.. i18n:           * calls to objects methodes;
.. i18n:                 o read, write
.. i18n:                 o create
.. i18n:                 o unlink (=delete) 

   1. **XML-RPC**
          * standard: http://www.xmlrpc.org
          * RPC Over HTTP
          * Function Parameters & Result encoded in XML 
   2. **Principle**;
          * calls to objects methodes;
                o read, write
                o create
                o unlink (=delete) 

.. i18n: XML-RPC is known as a web service. Web services are a set of tools that let one build distributed applications on top of existing web infrastructures. These applications use the Web as a kind of "transport layer" but don't offer a direct human interface via the browser.[1] Extensible Markup Language (XML) provides a vocabulary for describing Remote Procedure Calls (RPC), which is then transmitted between computers using the HyperText Transfer Protocol (HTTP). Effectively, RPC gives developers a mechanism for defining interfaces that can be called over a network. These interfaces can be as simple as a single function call or as complex as a large API.

XML-RPC is known as a web service. Web services are a set of tools that let one build distributed applications on top of existing web infrastructures. These applications use the Web as a kind of "transport layer" but don't offer a direct human interface via the browser.[1] Extensible Markup Language (XML) provides a vocabulary for describing Remote Procedure Calls (RPC), which is then transmitted between computers using the HyperText Transfer Protocol (HTTP). Effectively, RPC gives developers a mechanism for defining interfaces that can be called over a network. These interfaces can be as simple as a single function call or as complex as a large API.

.. i18n: XML-RPC therefore allows two or more computers running different operating systems and programs written in different languages to share processing. For example, a Java application could talk with a Perl program, which in turn talks with Python application that talks with ASP, and so on. System integrators often build custom connections between different systems, creating their own formats and protocols to make communications possible, but one can often end up with a large number of poorly documented single-use protocols. The RPC approach spares programmers the trouble of having to learn about underlying protocols, networking, and various implementation details.

XML-RPC therefore allows two or more computers running different operating systems and programs written in different languages to share processing. For example, a Java application could talk with a Perl program, which in turn talks with Python application that talks with ASP, and so on. System integrators often build custom connections between different systems, creating their own formats and protocols to make communications possible, but one can often end up with a large number of poorly documented single-use protocols. The RPC approach spares programmers the trouble of having to learn about underlying protocols, networking, and various implementation details.

.. i18n: XML-RPC can be used with Python, Java, Perl, PHP, C, C++, Ruby, Microsoft’s .NET and many other programming languages. Implementations are widely available for platforms such as Unix, Linux, Windows and the Macintosh.

XML-RPC can be used with Python, Java, Perl, PHP, C, C++, Ruby, Microsoft’s .NET and many other programming languages. Implementations are widely available for platforms such as Unix, Linux, Windows and the Macintosh.

.. i18n: An XML-RPC call is conducted between two parties: the client (the calling process) and the server (the called process). A server is made available at a particular URL (such as http://example.org:8080/rpcserv/).

An XML-RPC call is conducted between two parties: the client (the calling process) and the server (the called process). A server is made available at a particular URL (such as http://example.org:8080/rpcserv/).

.. i18n: The above text just touches the surface of XML-RPC. I recommend O'Reilly's "Programming Web Service with XML-RPC" for further reading. One may also wish to review the following links:

The above text just touches the surface of XML-RPC. I recommend O'Reilly's "Programming Web Service with XML-RPC" for further reading. One may also wish to review the following links:

.. i18n: XML-RPC Home Page\\ XML-RPC for C and C++\\ The Apache XML-RPC Project\\ Expat: The XML Parser\\ 

XML-RPC Home Page\\ XML-RPC for C and C++\\ The Apache XML-RPC Project\\ Expat: The XML Parser\\ 

.. i18n: Interfaces
.. i18n: ----------

Interfaces
----------

.. i18n: XML-RPC 
.. i18n: +++++++

XML-RPC 
+++++++

.. i18n: XML-RPC Architecture
.. i18n: """"""""""""""""""""

XML-RPC Architecture
""""""""""""""""""""

.. i18n: Open ERP is a based on a client/server architecture. The server and the client(s) communicate using the XML-RPC protocol. XML-RPC is a very simple protocol which allows the client to do remote procedure calls. The called function, its arguments, and the result of the call are transported using HTTP and encoded using XML. For more information on XML-RPC, please see: http://www.xml-rpc.com.

Open ERP is a based on a client/server architecture. The server and the client(s) communicate using the XML-RPC protocol. XML-RPC is a very simple protocol which allows the client to do remote procedure calls. The called function, its arguments, and the result of the call are transported using HTTP and encoded using XML. For more information on XML-RPC, please see: http://www.xml-rpc.com.

.. i18n: Architecture
.. i18n: """"""""""""

Architecture
""""""""""""

.. i18n: The diagram below synthesizes the client server architecture of Open ERP. Open ERP server and Open ERP clients communicate using XML-RPC.

The diagram below synthesizes the client server architecture of Open ERP. Open ERP server and Open ERP clients communicate using XML-RPC.

.. i18n: .. figure :: images/tech_arch.png
.. i18n:   :scale: 85
.. i18n:   :align: center      

.. figure :: images/tech_arch.png
  :scale: 85
  :align: center      

.. i18n: **Client**

**Client**

.. i18n: The logic of Open ERP is configured on the server side. The client is very simple; it is only used to post data (forms, lists, trees) and to send back the result to the server. The updates and the addition of new functionality don't need the clients to be frequently upgraded. This makes Open ERP easier to maintain.

The logic of Open ERP is configured on the server side. The client is very simple; it is only used to post data (forms, lists, trees) and to send back the result to the server. The updates and the addition of new functionality don't need the clients to be frequently upgraded. This makes Open ERP easier to maintain.

.. i18n: The client doesn't understand what it posts. Even actions like 'Click on the print icon' are sent to the server to ask how to react.

The client doesn't understand what it posts. Even actions like 'Click on the print icon' are sent to the server to ask how to react.

.. i18n: The client operation is very simple; when a user makes an action (save a form, open a menu, print, ...) it sends this action to the server. The server then sends the new action to execute to the client.

The client operation is very simple; when a user makes an action (save a form, open a menu, print, ...) it sends this action to the server. The server then sends the new action to execute to the client.

.. i18n: There are three types of action;

There are three types of action;

.. i18n:     * Open a window (form or tree)
.. i18n:     * Print a document
.. i18n:     * Execute a wizard 

    * Open a window (form or tree)
    * Print a document
    * Execute a wizard 

.. i18n: Python
.. i18n: ++++++

Python
++++++

.. i18n: Access tiny-server using xml-rpc
.. i18n: """"""""""""""""""""""""""""""""

Access tiny-server using xml-rpc
""""""""""""""""""""""""""""""""

.. i18n: Demo script
.. i18n: ~~~~~~~~~~~

Demo script
~~~~~~~~~~~

.. i18n:     * **Create a partner and his address**

    * **Create a partner and his address**

.. i18n: import xmlrpclib
.. i18n: """"""""""""""""
.. i18n: :: 
.. i18n: 	
.. i18n: 	username = 'admin' #the user
.. i18n: 	pwd = 'admin'      #the password of the user
.. i18n: 	dbname = 'terp'    #the database
.. i18n: 	 
.. i18n: 	# Get the uid
.. i18n: 	sock_common = xmlrpclib.ServerProxy ('http://localhost:8069/xmlrpc/common')
.. i18n: 	uid = sock_common.login(dbname, username, pwd)
.. i18n: 	 
.. i18n: 	#replace localhost with the address of the server
.. i18n: 	sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
.. i18n: 	 
.. i18n: 	partner = {
.. i18n: 	   'name': 'Fabien Pinckaers',
.. i18n: 	   'lang': 'fr_FR',
.. i18n: 	}
.. i18n: 	 
.. i18n: 	partner_id = sock.execute(dbname, uid, pwd, 'res.partner', 'create', partner)
.. i18n: 	 
.. i18n: 	address = {
.. i18n: 	   'partner_id': partner_id,
.. i18n: 	   'type' : 'default',
.. i18n: 	   'street': 'Chaussée de Namur 40',
.. i18n: 	   'zip': '1367',
.. i18n: 	   'city': 'Grand-Rosière',
.. i18n: 	   'phone': '+3281813700',
.. i18n: 	   'fax': '+3281733501',
.. i18n: 	}
.. i18n: 	 
.. i18n: 	address_id = sock.execute(dbname, uid, pwd, 'res.partner.address', 'create', address)

import xmlrpclib
""""""""""""""""
:: 
	
	username = 'admin' #the user
	pwd = 'admin'      #the password of the user
	dbname = 'terp'    #the database
	 
	# Get the uid
	sock_common = xmlrpclib.ServerProxy ('http://localhost:8069/xmlrpc/common')
	uid = sock_common.login(dbname, username, pwd)
	 
	#replace localhost with the address of the server
	sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
	 
	partner = {
	   'name': 'Fabien Pinckaers',
	   'lang': 'fr_FR',
	}
	 
	partner_id = sock.execute(dbname, uid, pwd, 'res.partner', 'create', partner)
	 
	address = {
	   'partner_id': partner_id,
	   'type' : 'default',
	   'street': 'Chaussée de Namur 40',
	   'zip': '1367',
	   'city': 'Grand-Rosière',
	   'phone': '+3281813700',
	   'fax': '+3281733501',
	}
	 
	address_id = sock.execute(dbname, uid, pwd, 'res.partner.address', 'create', address)

.. i18n: * **Search a partner** 
.. i18n:   ::
.. i18n: 
.. i18n: 	args = [('vat', '=', 'ZZZZZZ')] #query clause
.. i18n: 	ids = sock.execute(dbname, uid, pwd, 'res.partner', 'search', args)
.. i18n: 
.. i18n: * **Read partner data**
.. i18n:   ::
.. i18n: 
.. i18n: 	fields = ['name', 'active', 'vat', 'ref'] #fields to read
.. i18n: 	data = sock.execute(dbname, uid, pwd, 'res.partner', 'read', ids, fields) #ids is a list of id
.. i18n: 
.. i18n: * **Update partner data** 
.. i18n:   ::
.. i18n: 
.. i18n: 	values = {'vat': 'ZZ1ZZZ'} #data to update
.. i18n: 	result = sock.execute(dbname, uid, pwd, 'res.partner', 'write', ids, values)
.. i18n: 
.. i18n: * **Delete partner**
.. i18n:   ::
.. i18n: 
.. i18n: 	# ids : list of id
.. i18n: 	result = sock.execute(dbname, uid, pwd, 'res.partner', 'unlink', ids)

* **Search a partner** 
  ::

	args = [('vat', '=', 'ZZZZZZ')] #query clause
	ids = sock.execute(dbname, uid, pwd, 'res.partner', 'search', args)

* **Read partner data**
  ::

	fields = ['name', 'active', 'vat', 'ref'] #fields to read
	data = sock.execute(dbname, uid, pwd, 'res.partner', 'read', ids, fields) #ids is a list of id

* **Update partner data** 
  ::

	values = {'vat': 'ZZ1ZZZ'} #data to update
	result = sock.execute(dbname, uid, pwd, 'res.partner', 'write', ids, values)

* **Delete partner**
  ::

	# ids : list of id
	result = sock.execute(dbname, uid, pwd, 'res.partner', 'unlink', ids)

.. i18n: PHP
.. i18n: +++

PHP
+++

.. i18n: Access Open-server using xml-rpc
.. i18n: """"""""""""""""""""""""""""""""

Access Open-server using xml-rpc
""""""""""""""""""""""""""""""""

.. i18n: **Download the XML-RPC framework for PHP**

**Download the XML-RPC framework for PHP**

.. i18n: windows / linux: download the xml-rpc framework for php from http://phpxmlrpc.sourceforge.net/ The latest stable release is version 2.2 released on February 25, 2007

windows / linux: download the xml-rpc framework for php from http://phpxmlrpc.sourceforge.net/ The latest stable release is version 2.2 released on February 25, 2007

.. i18n: **Setup the XML-RPC for PHP**

**Setup the XML-RPC for PHP**

.. i18n: extract file xmlrpc-2.2.tar.gz and take the file xmlrpc.inc from lib directory place the xmlrpc.inc in the php library folder restart the apcahe/iis server

extract file xmlrpc-2.2.tar.gz and take the file xmlrpc.inc from lib directory place the xmlrpc.inc in the php library folder restart the apcahe/iis server

.. i18n: **Demo script**

**Demo script**

.. i18n: * **Login**

* **Login**

.. i18n: .. code-block :: php

.. code-block :: php

.. i18n: 	function connect() {
.. i18n: 	   var $user = 'admin';
.. i18n: 	   var $password = 'admin';
.. i18n: 	   var $dbname = 'db_name';
.. i18n: 	   var $server_url = 'http://localhost:8069/xmlrpc/';
.. i18n: 	 
.. i18n: 	 
.. i18n: 	   if(isset($_COOKIE["user_id"]) == true)  {
.. i18n: 	       if($_COOKIE["user_id"]>0) {
.. i18n: 		   return $_COOKIE["user_id"];
.. i18n: 	       }
.. i18n: 	   }
.. i18n: 	 
.. i18n: 	   $sock = new xmlrpc_client($server_url.'common');
.. i18n: 	   $msg = new xmlrpcmsg('login');
.. i18n: 	   $msg->addParam(new xmlrpcval($dbname, "string"));
.. i18n: 	   $msg->addParam(new xmlrpcval($user, "string"));
.. i18n: 	   $msg->addParam(new xmlrpcval($password, "string"));
.. i18n: 	   $resp =  $sock->send($msg);
.. i18n: 	   $val = $resp->value();
.. i18n: 	   $id = $val->scalarval();
.. i18n: 	   setcookie("user_id",$id,time()+3600);
.. i18n: 	   if($id > 0) {
.. i18n: 	       return $id;
.. i18n: 	   }else{
.. i18n: 	       return -1;
.. i18n: 	   }
.. i18n: 	 }

	function connect() {
	   var $user = 'admin';
	   var $password = 'admin';
	   var $dbname = 'db_name';
	   var $server_url = 'http://localhost:8069/xmlrpc/';
	 
	 
	   if(isset($_COOKIE["user_id"]) == true)  {
	       if($_COOKIE["user_id"]>0) {
		   return $_COOKIE["user_id"];
	       }
	   }
	 
	   $sock = new xmlrpc_client($server_url.'common');
	   $msg = new xmlrpcmsg('login');
	   $msg->addParam(new xmlrpcval($dbname, "string"));
	   $msg->addParam(new xmlrpcval($user, "string"));
	   $msg->addParam(new xmlrpcval($password, "string"));
	   $resp =  $sock->send($msg);
	   $val = $resp->value();
	   $id = $val->scalarval();
	   setcookie("user_id",$id,time()+3600);
	   if($id > 0) {
	       return $id;
	   }else{
	       return -1;
	   }
	 }

.. i18n: * **Search**

* **Search**

.. i18n: .. code-block :: php

.. code-block :: php

.. i18n: 	/** 
.. i18n: 	 * $client = xml-rpc handler 
.. i18n: 	 * $relation = name of the relation ex: res.partner
.. i18n: 	 * $attribute = name of the attribute ex:code 
.. i18n: 	 * $operator = search term operator ex: ilike, =, != 
.. i18n: 	 * $key=search for
.. i18n: 	 */
.. i18n:  
.. i18n: 	function search($client,$relation,$attribute,$operator,$keys) {
.. i18n: 	     var $user = 'admin';
.. i18n: 	     var $password = 'admin';
.. i18n: 	     var $userId = -1;
.. i18n: 	     var $dbname = 'db_name';
.. i18n: 	     var $server_url = 'http://localhost:8069/xmlrpc/';
.. i18n: 	 
.. i18n: 	     $key = array(new xmlrpcval(array(new xmlrpcval($attribute , "string"),
.. i18n: 		          new xmlrpcval($operator,"string"),
.. i18n: 		          new xmlrpcval($keys,"string")),"array"),
.. i18n: 		    );
.. i18n: 	 
.. i18n: 	     if($userId<=0) {
.. i18n: 		 connect();
.. i18n: 	     }
.. i18n: 	 
.. i18n: 	     $msg = new xmlrpcmsg('execute');
.. i18n: 	     $msg->addParam(new xmlrpcval($dbname, "string"));
.. i18n: 	     $msg->addParam(new xmlrpcval($userId, "int"));
.. i18n: 	     $msg->addParam(new xmlrpcval($password, "string"));
.. i18n: 	     $msg->addParam(new xmlrpcval($relation, "string"));
.. i18n: 	     $msg->addParam(new xmlrpcval("search", "string"));
.. i18n: 	     $msg->addParam(new xmlrpcval($key, "array"));
.. i18n: 	 
.. i18n: 	     $resp = $client->send($msg);
.. i18n: 	     $val = $resp->value();
.. i18n: 	     $ids = $val->scalarval();
.. i18n: 	 
.. i18n: 	     return $ids;
.. i18n: 	}

	/** 
	 * $client = xml-rpc handler 
	 * $relation = name of the relation ex: res.partner
	 * $attribute = name of the attribute ex:code 
	 * $operator = search term operator ex: ilike, =, != 
	 * $key=search for
	 */
 
	function search($client,$relation,$attribute,$operator,$keys) {
	     var $user = 'admin';
	     var $password = 'admin';
	     var $userId = -1;
	     var $dbname = 'db_name';
	     var $server_url = 'http://localhost:8069/xmlrpc/';
	 
	     $key = array(new xmlrpcval(array(new xmlrpcval($attribute , "string"),
		          new xmlrpcval($operator,"string"),
		          new xmlrpcval($keys,"string")),"array"),
		    );
	 
	     if($userId<=0) {
		 connect();
	     }
	 
	     $msg = new xmlrpcmsg('execute');
	     $msg->addParam(new xmlrpcval($dbname, "string"));
	     $msg->addParam(new xmlrpcval($userId, "int"));
	     $msg->addParam(new xmlrpcval($password, "string"));
	     $msg->addParam(new xmlrpcval($relation, "string"));
	     $msg->addParam(new xmlrpcval("search", "string"));
	     $msg->addParam(new xmlrpcval($key, "array"));
	 
	     $resp = $client->send($msg);
	     $val = $resp->value();
	     $ids = $val->scalarval();
	 
	     return $ids;
	}

.. i18n: * **Create** 
.. i18n:   ::
.. i18n: 
.. i18n: 	TODO
.. i18n: 
.. i18n: * **Write**
.. i18n:   ::
.. i18n: 
.. i18n: 	TODO

* **Create** 
  ::

	TODO

* **Write**
  ::

	TODO

.. i18n: JAVA
.. i18n: ++++

JAVA
++++

.. i18n: Access Open-server using xml-rpc
.. i18n: """"""""""""""""""""""""""""""""

Access Open-server using xml-rpc
""""""""""""""""""""""""""""""""

.. i18n: **Download the apache XML-RPC framework for JAVA**

**Download the apache XML-RPC framework for JAVA**

.. i18n: Download the xml-rpc framework for java from http://ws.apache.org/xmlrpc/ The latest stable release is version 3.1 released on August 12, 2007 All TinyERP errors throw exception because the framework allows only an int as the error code where Tinyerp return a string.

Download the xml-rpc framework for java from http://ws.apache.org/xmlrpc/ The latest stable release is version 3.1 released on August 12, 2007 All TinyERP errors throw exception because the framework allows only an int as the error code where Tinyerp return a string.

.. i18n: **Demo script**

**Demo script**

.. i18n: * **Find Databases**

* **Find Databases**

.. i18n: .. code-block :: java

.. code-block :: java

.. i18n: 	import java.net.URL;
.. i18n: 	import java.util.Vector;
.. i18n: 	 
.. i18n: 	import org.apache.commons.lang.StringUtils;
.. i18n: 	import org.apache.xmlrpc.XmlRpcException;
.. i18n: 	import org.apache.xmlrpc.client.XmlRpcClient;
.. i18n: 	import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;
.. i18n: 	 
.. i18n: 	public Vector<String> getDatabaseList(String host, int port) 
.. i18n: 	{
.. i18n: 	  XmlRpcClient xmlrpcDb = new XmlRpcClient();
.. i18n: 	 
.. i18n: 	  XmlRpcClientConfigImpl xmlrpcConfigDb = new XmlRpcClientConfigImpl();
.. i18n: 	  xmlrpcConfigDb.setEnabledForExtensions(true);
.. i18n: 	  xmlrpcConfigDb.setServerURL(new URL("http",host,port,"/xmlrpc/db"));
.. i18n: 	 
.. i18n: 	  xmlrpcDb.setConfig(xmlrpcConfigDb);
.. i18n: 	 
.. i18n: 	  try {
.. i18n: 	    //Retrieve databases
.. i18n: 	    Vector<Object> params = new Vector<Object>();
.. i18n: 	    Object result = xmlrpcDb.execute("list", params);
.. i18n: 	    Object[] a = (Object[]) result;
.. i18n: 	 
.. i18n: 	    Vector<String> res = new Vector<String>();
.. i18n: 	    for (int i = 0; i < a.length; i++) {
.. i18n: 	    if (a[i] instanceof String)
.. i18n: 	    {
.. i18n: 	      res.addElement((String)a[i]);
.. i18n: 	    }
.. i18n: 	  }
.. i18n: 	  catch (XmlRpcException e) {
.. i18n: 	    logger.warn("XmlException Error while retrieving TinyERP Databases: ",e);
.. i18n: 	    return -2;
.. i18n: 	  } 
.. i18n: 	  catch (Exception e)
.. i18n: 	  {
.. i18n: 	    logger.warn("Error while retrieving TinyERP Databases: ",e);
.. i18n: 	    return -3;
.. i18n: 	  }
.. i18n: 	}

	import java.net.URL;
	import java.util.Vector;
	 
	import org.apache.commons.lang.StringUtils;
	import org.apache.xmlrpc.XmlRpcException;
	import org.apache.xmlrpc.client.XmlRpcClient;
	import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;
	 
	public Vector<String> getDatabaseList(String host, int port) 
	{
	  XmlRpcClient xmlrpcDb = new XmlRpcClient();
	 
	  XmlRpcClientConfigImpl xmlrpcConfigDb = new XmlRpcClientConfigImpl();
	  xmlrpcConfigDb.setEnabledForExtensions(true);
	  xmlrpcConfigDb.setServerURL(new URL("http",host,port,"/xmlrpc/db"));
	 
	  xmlrpcDb.setConfig(xmlrpcConfigDb);
	 
	  try {
	    //Retrieve databases
	    Vector<Object> params = new Vector<Object>();
	    Object result = xmlrpcDb.execute("list", params);
	    Object[] a = (Object[]) result;
	 
	    Vector<String> res = new Vector<String>();
	    for (int i = 0; i < a.length; i++) {
	    if (a[i] instanceof String)
	    {
	      res.addElement((String)a[i]);
	    }
	  }
	  catch (XmlRpcException e) {
	    logger.warn("XmlException Error while retrieving TinyERP Databases: ",e);
	    return -2;
	  } 
	  catch (Exception e)
	  {
	    logger.warn("Error while retrieving TinyERP Databases: ",e);
	    return -3;
	  }
	}

.. i18n: * **Login**

* **Login**

.. i18n: .. code-block :: java

.. code-block :: java

.. i18n: 	import java.net.URL;
.. i18n: 	 
.. i18n: 	import org.apache.commons.lang.StringUtils;
.. i18n: 	import org.apache.xmlrpc.XmlRpcException;
.. i18n: 	import org.apache.xmlrpc.client.XmlRpcClient;
.. i18n: 	import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;
.. i18n: 	 
.. i18n: 	public int Connect(String host, int port, String tinydb, String login, String password)
.. i18n: 	{
.. i18n: 	  XmlRpcClient xmlrpcLogin = new XmlRpcClient();
.. i18n: 	 
.. i18n: 	  XmlRpcClientConfigImpl xmlrpcConfigLogin = new XmlRpcClientConfigImpl();
.. i18n: 	  xmlrpcConfigLogin.setEnabledForExtensions(true);
.. i18n: 	  xmlrpcConfigLogin.setServerURL(new URL("http",host,port,"/xmlrpc/common"));
.. i18n: 	 
.. i18n: 	  xmlrpcLogin.setConfig(xmlrpcConfigLogin);
.. i18n: 	 
.. i18n: 	  try {
.. i18n: 	    //Connect
.. i18n: 	    params = new Object[] {tinydb,login,password};
.. i18n: 	    Object id = xmlrpcLogin.execute("login", params);
.. i18n: 	    if (id instanceof Integer)
.. i18n: 	      return (Integer)id;
.. i18n: 	    return -1;
.. i18n: 	  }
.. i18n: 	  catch (XmlRpcException e) {
.. i18n: 	    logger.warn("XmlException Error while logging to TinyERP: ",e);
.. i18n: 	    return -2;
.. i18n: 	  } 
.. i18n: 	  catch (Exception e)
.. i18n: 	  {
.. i18n: 	    logger.warn("Error while logging to TinyERP: ",e);
.. i18n: 	    return -3;
.. i18n: 	  }
.. i18n: 	}

	import java.net.URL;
	 
	import org.apache.commons.lang.StringUtils;
	import org.apache.xmlrpc.XmlRpcException;
	import org.apache.xmlrpc.client.XmlRpcClient;
	import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;
	 
	public int Connect(String host, int port, String tinydb, String login, String password)
	{
	  XmlRpcClient xmlrpcLogin = new XmlRpcClient();
	 
	  XmlRpcClientConfigImpl xmlrpcConfigLogin = new XmlRpcClientConfigImpl();
	  xmlrpcConfigLogin.setEnabledForExtensions(true);
	  xmlrpcConfigLogin.setServerURL(new URL("http",host,port,"/xmlrpc/common"));
	 
	  xmlrpcLogin.setConfig(xmlrpcConfigLogin);
	 
	  try {
	    //Connect
	    params = new Object[] {tinydb,login,password};
	    Object id = xmlrpcLogin.execute("login", params);
	    if (id instanceof Integer)
	      return (Integer)id;
	    return -1;
	  }
	  catch (XmlRpcException e) {
	    logger.warn("XmlException Error while logging to TinyERP: ",e);
	    return -2;
	  } 
	  catch (Exception e)
	  {
	    logger.warn("Error while logging to TinyERP: ",e);
	    return -3;
	  }
	}

.. i18n: * **Search** 
.. i18n:   ::
.. i18n: 	
.. i18n: 	TODO
.. i18n: 
.. i18n: * **Create** 
.. i18n:   ::
.. i18n: 
.. i18n: 	TODO
.. i18n: 
.. i18n: * **Write**
.. i18n:   ::
.. i18n:  
.. i18n: 	TODO

* **Search** 
  ::
	
	TODO

* **Create** 
  ::

	TODO

* **Write**
  ::
 
	TODO

.. i18n: Python Example
.. i18n: --------------

Python Example
--------------

.. i18n: Example of creation of a partner and his address.

Example of creation of a partner and his address.

.. i18n: .. code-block :: python

.. code-block :: python

.. i18n: 	import xmlrpclib
.. i18n: 	 
.. i18n: 	sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
.. i18n: 	uid = 1
.. i18n: 	pwd = 'demo'
.. i18n: 	 
.. i18n: 	partner = {
.. i18n: 	    'title': 'Monsieur',
.. i18n: 	    'name': 'Fabien Pinckaers',
.. i18n: 	    'lang': 'fr',
.. i18n: 	    'active': True,
.. i18n: 	}
.. i18n: 	 
.. i18n: 	partner_id = sock.execute(dbname, uid, pwd, 'res.partner', 'create', partner)
.. i18n: 	 
.. i18n: 	address = {
.. i18n: 	    'partner_id': partner_id,
.. i18n: 	    'type': 'default',
.. i18n: 	    'street': 'Rue du vieux chateau, 21',
.. i18n: 	    'zip': '1457',
.. i18n: 	    'city': 'Walhain',
.. i18n: 	    'phone': '(+32)10.68.94.39',
.. i18n: 	    'fax': '(+32)10.68.94.39',
.. i18n: 	}
.. i18n: 	 
.. i18n: 	sock.execute(dbname, uid, pwd, 'res.partner.address', 'create', address)

	import xmlrpclib
	 
	sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
	uid = 1
	pwd = 'demo'
	 
	partner = {
	    'title': 'Monsieur',
	    'name': 'Fabien Pinckaers',
	    'lang': 'fr',
	    'active': True,
	}
	 
	partner_id = sock.execute(dbname, uid, pwd, 'res.partner', 'create', partner)
	 
	address = {
	    'partner_id': partner_id,
	    'type': 'default',
	    'street': 'Rue du vieux chateau, 21',
	    'zip': '1457',
	    'city': 'Walhain',
	    'phone': '(+32)10.68.94.39',
	    'fax': '(+32)10.68.94.39',
	}
	 
	sock.execute(dbname, uid, pwd, 'res.partner.address', 'create', address)

.. i18n: To get the UID of a user, you can use the following script:

To get the UID of a user, you can use the following script:

.. i18n: .. code-block :: python

.. code-block :: python

.. i18n: 	sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
.. i18n: 	 UID = sock.login('terp3', 'admin', 'admin')

	sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
	 UID = sock.login('terp3', 'admin', 'admin')

.. i18n: CRUD example:	

CRUD example:	

.. i18n: .. code-block :: python

.. code-block :: python

.. i18n: 	"""
.. i18n: 	:The login function is under
.. i18n: 	::    http://localhost:8069/xmlrpc/common
.. i18n: 	:For object retrieval use:
.. i18n: 	::    http://localhost:8069/xmlrpc/object 
.. i18n: 	"""
.. i18n: 	import xmlrpclib
.. i18n: 	 
.. i18n: 	user = 'admin'
.. i18n: 	pwd = 'admin'
.. i18n: 	dbname = 'terp3'
.. i18n: 	model = 'res.partner'
.. i18n: 	 
.. i18n: 	sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
.. i18n: 	uid = sock.login(dbname ,user ,pwd)
.. i18n: 	 
.. i18n: 	sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
.. i18n: 	 
.. i18n: 	# CREATE A PARTNER
.. i18n: 	partner_data = {'name':'Tiny', 'active':True, 'vat':'ZZZZZ'}
.. i18n: 	partner_id = sock.execute(dbname, uid, pwd, model, 'create', partner_data)
.. i18n: 	 
.. i18n: 	# The relation between res.partner and res.partner.category is of type many2many
.. i18n: 	# To add  categories to a partner use the following format:
.. i18n: 	partner_data = {'name':'Provider2', 'category_id': [(6,0,[3, 2, 1])]} 
.. i18n: 	# Where [3, 2, 1] are id fields of lines in res.partner.category
.. i18n: 	 
.. i18n: 	# SEARCH PARTNERS
.. i18n: 	args = [('vat', '=', 'ZZZZZ'),]
.. i18n: 	ids = sock.execute(dbname, uid, pwd, model, 'search', args)
.. i18n: 	 
.. i18n: 	# READ PARTNER DATA
.. i18n: 	fields = ['name', 'active', 'vat', 'ref'] 
.. i18n: 	results = sock.execute(dbname, uid, pwd, model, 'read', ids, fields)
.. i18n: 	print results
.. i18n: 	 
.. i18n: 	# EDIT PARTNER DATA
.. i18n: 	values = {'vat':'ZZ1ZZ'}
.. i18n: 	results = sock.execute(dbname, uid, pwd, model, 'write', ids, values)
.. i18n: 	 
.. i18n: 	# DELETE PARTNER DATA
.. i18n: 	results = sock.execute(dbname, uid, pwd, model, 'unlink', ids)

	"""
	:The login function is under
	::    http://localhost:8069/xmlrpc/common
	:For object retrieval use:
	::    http://localhost:8069/xmlrpc/object 
	"""
	import xmlrpclib
	 
	user = 'admin'
	pwd = 'admin'
	dbname = 'terp3'
	model = 'res.partner'
	 
	sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
	uid = sock.login(dbname ,user ,pwd)
	 
	sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
	 
	# CREATE A PARTNER
	partner_data = {'name':'Tiny', 'active':True, 'vat':'ZZZZZ'}
	partner_id = sock.execute(dbname, uid, pwd, model, 'create', partner_data)
	 
	# The relation between res.partner and res.partner.category is of type many2many
	# To add  categories to a partner use the following format:
	partner_data = {'name':'Provider2', 'category_id': [(6,0,[3, 2, 1])]} 
	# Where [3, 2, 1] are id fields of lines in res.partner.category
	 
	# SEARCH PARTNERS
	args = [('vat', '=', 'ZZZZZ'),]
	ids = sock.execute(dbname, uid, pwd, model, 'search', args)
	 
	# READ PARTNER DATA
	fields = ['name', 'active', 'vat', 'ref'] 
	results = sock.execute(dbname, uid, pwd, model, 'read', ids, fields)
	print results
	 
	# EDIT PARTNER DATA
	values = {'vat':'ZZ1ZZ'}
	results = sock.execute(dbname, uid, pwd, model, 'write', ids, values)
	 
	# DELETE PARTNER DATA
	results = sock.execute(dbname, uid, pwd, model, 'unlink', ids)

.. i18n: PRINT example:

PRINT example:

.. i18n:    1. PRINT INVOICE
.. i18n:    2. IDS is the invoice ID, as returned by:
.. i18n:    3. ids = sock.execute(dbname, uid, pwd, 'account.invoice', 'search', [('number', 'ilike', invoicenumber), ('type', '=', 'out_invoice')]) 

   1. PRINT INVOICE
   2. IDS is the invoice ID, as returned by:
   3. ids = sock.execute(dbname, uid, pwd, 'account.invoice', 'search', [('number', 'ilike', invoicenumber), ('type', '=', 'out_invoice')]) 

.. i18n: .. code-block :: python

.. code-block :: python

.. i18n: 	import time
.. i18n: 	import base64
.. i18n: 	printsock = xmlrpclib.ServerProxy('http://server:8069/xmlrpc/report')
.. i18n: 	model = 'account.invoice'
.. i18n: 	id_report = printsock.report(dbname, uid, pwd, model, ids, {'model': model, 'id': ids[0], 'report_type':'pdf'})
.. i18n: 	time.sleep(5)
.. i18n: 	state = False
.. i18n: 	attempt = 0
.. i18n: 	while not state:
.. i18n: 	    report = printsock.report_get(dbname, uid, pwd, id_report)
.. i18n: 	    state = report['state']
.. i18n: 	    if not state:
.. i18n: 		time.sleep(1)
.. i18n: 		attempt += 1
.. i18n: 	    if attempt>200:
.. i18n: 		print 'Printing aborted, too long delay !'
.. i18n: 	 
.. i18n: 	    string_pdf = base64.decodestring(report['result'])
.. i18n: 	    file_pdf = open('/tmp/file.pdf','w')
.. i18n: 	    file_pdf.write(string_pdf)
.. i18n: 	    file_pdf.close()

	import time
	import base64
	printsock = xmlrpclib.ServerProxy('http://server:8069/xmlrpc/report')
	model = 'account.invoice'
	id_report = printsock.report(dbname, uid, pwd, model, ids, {'model': model, 'id': ids[0], 'report_type':'pdf'})
	time.sleep(5)
	state = False
	attempt = 0
	while not state:
	    report = printsock.report_get(dbname, uid, pwd, id_report)
	    state = report['state']
	    if not state:
		time.sleep(1)
		attempt += 1
	    if attempt>200:
		print 'Printing aborted, too long delay !'
	 
	    string_pdf = base64.decodestring(report['result'])
	    file_pdf = open('/tmp/file.pdf','w')
	    file_pdf.write(string_pdf)
	    file_pdf.close()

.. i18n: PHP Example
.. i18n: -----------

PHP Example
-----------

.. i18n: Here is an example on how to insert a new partner using PHP. This example makes use the phpxmlrpc library, available on sourceforge.

Here is an example on how to insert a new partner using PHP. This example makes use the phpxmlrpc library, available on sourceforge.

.. i18n: .. code-block :: php

.. code-block :: php

.. i18n: 	    <?

	    <?

.. i18n: 		include('xmlrpc.inc'); 

		include('xmlrpc.inc'); 

.. i18n: 		$arrayVal = array( 
.. i18n: 		'name'=>new xmlrpcval('Fabien Pinckaers', "string") , 
.. i18n: 		'vat'=>new xmlrpcval('BE477472701' , "string") 
.. i18n: 		); 

		$arrayVal = array( 
		'name'=>new xmlrpcval('Fabien Pinckaers', "string") , 
		'vat'=>new xmlrpcval('BE477472701' , "string") 
		); 

.. i18n: 		$client = new xmlrpc_client("http://localhost:8069/xmlrpc/object"); 

		$client = new xmlrpc_client("http://localhost:8069/xmlrpc/object"); 

.. i18n: 		$msg = new xmlrpcmsg('execute'); 
.. i18n: 		$msg->addParam(new xmlrpcval("dbname", "string")); 
.. i18n: 		$msg->addParam(new xmlrpcval("3", "int")); 
.. i18n: 		$msg->addParam(new xmlrpcval("demo", "string")); 
.. i18n: 		$msg->addParam(new xmlrpcval("res.partner", "string")); 
.. i18n: 		$msg->addParam(new xmlrpcval("create", "string")); 
.. i18n: 		$msg->addParam(new xmlrpcval($arrayVal, "struct")); 

		$msg = new xmlrpcmsg('execute'); 
		$msg->addParam(new xmlrpcval("dbname", "string")); 
		$msg->addParam(new xmlrpcval("3", "int")); 
		$msg->addParam(new xmlrpcval("demo", "string")); 
		$msg->addParam(new xmlrpcval("res.partner", "string")); 
		$msg->addParam(new xmlrpcval("create", "string")); 
		$msg->addParam(new xmlrpcval($arrayVal, "struct")); 

.. i18n: 		$resp = $client->send($msg); 

		$resp = $client->send($msg); 

.. i18n: 		if ($resp->faultCode())

		if ($resp->faultCode())

.. i18n: 		    echo 'Error: '.$resp->faultString(); 

		    echo 'Error: '.$resp->faultString(); 

.. i18n: 		else

		else

.. i18n: 		    echo 'Partner '.$resp->value()->scalarval().' created !'; 

		    echo 'Partner '.$resp->value()->scalarval().' created !'; 

.. i18n: 	    ?> 

	    ?> 

.. i18n: 	
.. i18n: 	

	
	
