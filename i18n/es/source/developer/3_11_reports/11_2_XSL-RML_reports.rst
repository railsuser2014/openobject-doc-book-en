
.. i18n: XSL:RML reports
.. i18n: ===============

XSL:RML reports
===============

.. i18n: RML reports don't require programming but require two simple XML files to be written:

RML reports don't require programming but require two simple XML files to be written:

.. i18n:     * a file describing the data to export (\*.xml)
.. i18n:     * a file containing the presentation rules to apply to that data (\*.xsl)

    * a file describing the data to export (\*.xml)
    * a file containing the presentation rules to apply to that data (\*.xsl)

.. i18n: .. figure::  images/automatic-reports.png
.. i18n:    :scale: 85
.. i18n:    :align: center

.. figure::  images/automatic-reports.png
   :scale: 85
   :align: center

.. i18n: The role of the XML template is to describe which fields of the resource have to be exported (by the server). The XSL:RML style sheet deals with the layout of the exported data as well as the "static text" of reports. Static text is referring to the text which is common to all reports of the same type (for example, the title of table columns).

The role of the XML template is to describe which fields of the resource have to be exported (by the server). The XSL:RML style sheet deals with the layout of the exported data as well as the "static text" of reports. Static text is referring to the text which is common to all reports of the same type (for example, the title of table columns).

.. i18n: **Example**

**Example**

.. i18n: Here is, as an example, the different files for the simplest report in the ERP.

Here is, as an example, the different files for the simplest report in the ERP.

.. i18n: .. figure::  images/ids-report.png
.. i18n:    :scale: 85
.. i18n:    :align: center

.. figure::  images/ids-report.png
   :scale: 85
   :align: center

.. i18n: **XML Template**
.. i18n: ::
.. i18n: 
.. i18n: 	<?xml version="1.0"?>

**XML Template**
::

	<?xml version="1.0"?>

.. i18n: 	    <ids> 
.. i18n: 	    <id type="fields" name="id">

	    <ids> 
	    <id type="fields" name="id">

.. i18n: 		<name type="field" name="name"/> 
.. i18n: 		<ref type="field" name="ref"/> 

		<name type="field" name="name"/> 
		<ref type="field" name="ref"/> 

.. i18n: 	    </id> 
.. i18n: 	    </ids> 

	    </id> 
	    </ids> 

.. i18n: **XML data file (generated)**
.. i18n: ::
.. i18n: 
.. i18n: 	<?xml version="1.0"?>

**XML data file (generated)**
::

	<?xml version="1.0"?>

.. i18n: 	    <ids> 
.. i18n: 	    <id>

	    <ids> 
	    <id>

.. i18n: 		<name>Tiny sprl</name> 
.. i18n: 		<ref>pnk00</ref> 

		<name>Tiny sprl</name> 
		<ref>pnk00</ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>ASUS</name> 
.. i18n: 		<ref></ref> 

		<name>ASUS</name> 
		<ref></ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>Agrolait</name> 
.. i18n: 		<ref></ref> 

		<name>Agrolait</name> 
		<ref></ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>Banque Plein-Aux-As</name> 
.. i18n: 		<ref></ref> 

		<name>Banque Plein-Aux-As</name> 
		<ref></ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>China Export</name> 
.. i18n: 		<ref></ref> 

		<name>China Export</name> 
		<ref></ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>Ditrib PC</name> 
.. i18n: 		<ref></ref> 

		<name>Ditrib PC</name> 
		<ref></ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>Ecole de Commerce de Liege</name> 
.. i18n: 		<ref></ref> 

		<name>Ecole de Commerce de Liege</name> 
		<ref></ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>Elec Import</name> 
.. i18n: 		<ref></ref> 

		<name>Elec Import</name> 
		<ref></ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>Maxtor</name> 
.. i18n: 		<ref></ref> 

		<name>Maxtor</name> 
		<ref></ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>Mediapole SPRL</name> 
.. i18n: 		<ref></ref> 

		<name>Mediapole SPRL</name> 
		<ref></ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>Opensides sprl</name> 
.. i18n: 		<ref>os</ref> 

		<name>Opensides sprl</name> 
		<ref>os</ref> 

.. i18n: 	    </id><id>

	    </id><id>

.. i18n: 		<name>Tecsas sarl</name> 
.. i18n: 		<ref></ref> 

		<name>Tecsas sarl</name> 
		<ref></ref> 

.. i18n: 	    </id> 
.. i18n: 	    </ids> 

	    </id> 
	    </ids> 

.. i18n: **XSL stylesheet**
.. i18n: ::
.. i18n: 
.. i18n: 	<?xml version="1.0" encoding="utf-8"?> <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">

**XSL stylesheet**
::

	<?xml version="1.0" encoding="utf-8"?> <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">

.. i18n: 	    <xsl:template match="/">

	    <xsl:template match="/">

.. i18n: 		<xsl:apply-templates select="ids"/> 

		<xsl:apply-templates select="ids"/> 

.. i18n: 	    </xsl:template> 

	    </xsl:template> 

.. i18n: 	    <xsl:template match="ids">

	    <xsl:template match="ids">

.. i18n: 		<document>

		<document>

.. i18n: 		    <template pageSize="21cm,29.7cm">

		    <template pageSize="21cm,29.7cm">

.. i18n: 		        <pageTemplate>

		        <pageTemplate>

.. i18n: 		            <frame id="col1" x1="2cm" y1="2.4cm" width="8cm" height="26cm"/> 
.. i18n: 		            <frame id="col2" x1="11cm" y1="2.4cm" width="8cm" height="26cm"/> 

		            <frame id="col1" x1="2cm" y1="2.4cm" width="8cm" height="26cm"/> 
		            <frame id="col2" x1="11cm" y1="2.4cm" width="8cm" height="26cm"/> 

.. i18n: 		        </pageTemplate> 

		        </pageTemplate> 

.. i18n: 		    </template> 

		    </template> 

.. i18n: 		<stylesheet>

		<stylesheet>

.. i18n: 		    <blockTableStyle id="ids"> 

		    <blockTableStyle id="ids"> 

.. i18n: 		        <blockFont name="Helvetica-BoldOblique" size="12" start="0,0" stop="-1,0"/> 
.. i18n: 		        <lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,0"/> 

		        <blockFont name="Helvetica-BoldOblique" size="12" start="0,0" stop="-1,0"/> 
		        <lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,0"/> 

.. i18n: 		        <lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,-1"/> 

		        <lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,-1"/> 

.. i18n: 		    </blockTableStyle> 

		    </blockTableStyle> 

.. i18n: 		</stylesheet> 

		</stylesheet> 

.. i18n: 		<story>

		<story>

.. i18n: 		    <blockTable colWidths="2cm, 6cm" repeatRows="1" style="ids">

		    <blockTable colWidths="2cm, 6cm" repeatRows="1" style="ids">

.. i18n: 		        <tr>

		        <tr>

.. i18n: 		            <td t="1">Ref.</td> 
.. i18n: 		            <td t="1">Name</td> 

		            <td t="1">Ref.</td> 
		            <td t="1">Name</td> 

.. i18n: 		        </tr> 
.. i18n: 		        <xsl:apply-templates select="id"/> 

		        </tr> 
		        <xsl:apply-templates select="id"/> 

.. i18n: 		    </blockTable> 

		    </blockTable> 

.. i18n: 		</story> 
.. i18n: 		</document> 

		</story> 
		</document> 

.. i18n: 	    </xsl:template> 

	    </xsl:template> 

.. i18n: 	    <xsl:template match="id">

	    <xsl:template match="id">

.. i18n: 		<tr>

		<tr>

.. i18n: 		    <td><xsl:value-of select="ref"/></td> 
.. i18n: 		    <td><para><xsl:value-of select="name"/></para></td> 

		    <td><xsl:value-of select="ref"/></td> 
		    <td><para><xsl:value-of select="name"/></para></td> 

.. i18n: 		</tr> 

		</tr> 

.. i18n: 	    </xsl:template> 
.. i18n: 	    </xsl:stylesheet> 

	    </xsl:template> 
	    </xsl:stylesheet> 

.. i18n: **Resulting RML file (generated)**
.. i18n: ::
.. i18n: 
.. i18n: 	<?xml version="1.0"?>

**Resulting RML file (generated)**
::

	<?xml version="1.0"?>

.. i18n: 	    <document> 
.. i18n: 	    ...

	    <document> 
	    ...

.. i18n: 		<story>

		<story>

.. i18n: 		    <blockTable colWidths="2cm, 6cm" repeatRows="1" style="ids">

		    <blockTable colWidths="2cm, 6cm" repeatRows="1" style="ids">

.. i18n: 		        <tr>

		        <tr>

.. i18n: 		            <td t="1">Ref.</td> 
.. i18n: 		            <td t="1">Name</td> 

		            <td t="1">Ref.</td> 
		            <td t="1">Name</td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td>pnk00</td> 
.. i18n: 		            <td><para>Tiny sprl</para></td> 

		            <td>pnk00</td> 
		            <td><para>Tiny sprl</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>ASUS</para></td> 

		            <td></td> 
		            <td><para>ASUS</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Agrolait</para></td> 

		            <td></td> 
		            <td><para>Agrolait</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Banque Plein-Aux-As</para></td> 

		            <td></td> 
		            <td><para>Banque Plein-Aux-As</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>China Export</para></td> 

		            <td></td> 
		            <td><para>China Export</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Ditrib PC</para></td> 

		            <td></td> 
		            <td><para>Ditrib PC</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Ecole de Commerce de Liege</para></td> 

		            <td></td> 
		            <td><para>Ecole de Commerce de Liege</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Elec Import</para></td> 

		            <td></td> 
		            <td><para>Elec Import</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Maxtor</para></td> 

		            <td></td> 
		            <td><para>Maxtor</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td></td> 
.. i18n: 		            <td><para>Mediapole SPRL</para></td> 

		            <td></td> 
		            <td><para>Mediapole SPRL</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr>

		        </tr> 
		        <tr>

.. i18n: 		            <td>os</td> 
.. i18n: 		            <td><para>Opensides sprl</para></td> 

		            <td>os</td> 
		            <td><para>Opensides sprl</para></td> 

.. i18n: 		        </tr> 
.. i18n: 		        <tr> 
.. i18n: 		        <td></td>

		        </tr> 
		        <tr> 
		        <td></td>

.. i18n: 		            <td><para>Tecsas sarl</para></td> 

		            <td><para>Tecsas sarl</para></td> 

.. i18n: 		        </tr> 

		        </tr> 

.. i18n: 		    </blockTable> 

		    </blockTable> 

.. i18n: 		</story> 

		</story> 

.. i18n: 	    </document> 

	    </document> 

.. i18n: Fore more information on the formats used:

Fore more information on the formats used:

.. i18n:     * RML : http://reportlab.com/docs/RML_UserGuide_1_0.pdf
.. i18n:     * XSL - Specification : http://www.w3.org/TR/xslt
.. i18n:     * XSL - Tutorial : http://www.zvon.org/xxl/XSLTutorial/Books/Output/contents.html 

    * RML : http://reportlab.com/docs/RML_UserGuide_1_0.pdf
    * XSL - Specification : http://www.w3.org/TR/xslt
    * XSL - Tutorial : http://www.zvon.org/xxl/XSLTutorial/Books/Output/contents.html 

.. i18n: All these formats use XML:

All these formats use XML:

.. i18n:     * http://www.w3.org/XML/ 

    * http://www.w3.org/XML/ 

.. i18n: XML Template
.. i18n: ------------

XML Template
------------

.. i18n: XML templates are simple XML files describing which fields among all available object fields are necessary for the report.

XML templates are simple XML files describing which fields among all available object fields are necessary for the report.

.. i18n: File format
.. i18n: """""""""""

File format
"""""""""""

.. i18n: Tag names can be chosen arbitrarily (it must be valid XML though). In the XSL file, you will have to use those names. Most of the time, the name of a tag will be the same as the name of the object field it refers to.

Tag names can be chosen arbitrarily (it must be valid XML though). In the XSL file, you will have to use those names. Most of the time, the name of a tag will be the same as the name of the object field it refers to.

.. i18n: Nodes without **type** attribute are transferred identically into the XML destination file (the data file). Nodes with a type attribute will be parsed by the server and their content will be replaced by data coming from objects. In addition to the type attribute, nodes have other possible attributes. These attributes depend on the type of the node (each node type supports or needs different attributes). Most node types have a name attribute, which refers to the  **name** of a field of the object on which we work.

Nodes without **type** attribute are transferred identically into the XML destination file (the data file). Nodes with a type attribute will be parsed by the server and their content will be replaced by data coming from objects. In addition to the type attribute, nodes have other possible attributes. These attributes depend on the type of the node (each node type supports or needs different attributes). Most node types have a name attribute, which refers to the  **name** of a field of the object on which we work.

.. i18n: As for the "browse" method on objects, field names in reports can use a notation similar to the notation found in object oriented programming languages. It means that "relation fields" can be used as "bridges" to fetch data from other (related) objects.

As for the "browse" method on objects, field names in reports can use a notation similar to the notation found in object oriented programming languages. It means that "relation fields" can be used as "bridges" to fetch data from other (related) objects.

.. i18n: Let's use the "account.transfer" object as an example. It contains a partner_id field. This field is a relation field ("many to one") pointing to the "res.partner" object. Let's suppose that we want to create a report for transfers and in this report, we want to use the name of the recipient partner. This name could be accessed using the following expression as the name of the field:

Let's use the "account.transfer" object as an example. It contains a partner_id field. This field is a relation field ("many to one") pointing to the "res.partner" object. Let's suppose that we want to create a report for transfers and in this report, we want to use the name of the recipient partner. This name could be accessed using the following expression as the name of the field:

.. i18n:     partner_id.name 

    partner_id.name 

.. i18n: Possible types
.. i18n: """"""""""""""

Possible types
""""""""""""""

.. i18n: Here is the list of available field types:

Here is the list of available field types:

.. i18n:     * **field**: It is the simplest type. For nodes of this type, the server replaces the node content by the value of the field whose name is given in the name attribute. 
.. i18n: 
.. i18n:     * **fields**: when this type of node is used, the server will generate a node in the XML data file for each unique value of the field whose name is given in the name attribute. 

    * **field**: It is the simplest type. For nodes of this type, the server replaces the node content by the value of the field whose name is given in the name attribute. 

    * **fields**: when this type of node is used, the server will generate a node in the XML data file for each unique value of the field whose name is given in the name attribute. 

.. i18n:     Notes:

    Notes:

.. i18n:         ** This node type is often used with "id" as its name attribute. This has the effect of creating one node for each resource selected in the interface by the user. 
.. i18n:         ** The semantics of a node <node type="fields" name="field_name"> is similar to an SQL statement of the form "SELECT FROM object_table WHERE id in identifier_list **GROUP BY** field_name" where identifier_list is the list of ids of the resources selected by the ::user (in the interface). 

        ** This node type is often used with "id" as its name attribute. This has the effect of creating one node for each resource selected in the interface by the user. 
        ** The semantics of a node <node type="fields" name="field_name"> is similar to an SQL statement of the form "SELECT FROM object_table WHERE id in identifier_list **GROUP BY** field_name" where identifier_list is the list of ids of the resources selected by the ::user (in the interface). 

.. i18n:     * **eval**: This node type evaluate the expression given in the *expr* attribute. This expression may be any Python expression and may contain objects fields names. 
.. i18n: 
.. i18n:     * **zoom**: This node type allows to "enter" into the resource referenced by the relation field whose name is given in the name attribute. It means that its child nodes will be able to access the fields of that resource without having to prefix them with the field name that makes the link with the other object. In our example above, we could also have accessed the field name of the partner with the following: 

    * **eval**: This node type evaluate the expression given in the *expr* attribute. This expression may be any Python expression and may contain objects fields names. 

    * **zoom**: This node type allows to "enter" into the resource referenced by the relation field whose name is given in the name attribute. It means that its child nodes will be able to access the fields of that resource without having to prefix them with the field name that makes the link with the other object. In our example above, we could also have accessed the field name of the partner with the following: 

.. i18n:   ::
.. i18n: 
.. i18n: 	<partner type="zoom" name="partner_id">

  ::

	<partner type="zoom" name="partner_id">

.. i18n: 		<name type="field" name="name"/> 

		<name type="field" name="name"/> 

.. i18n: 	</partner> 

	</partner> 

.. i18n: 	In this precise case, there is of course no point in using this notation instead of the standard notation below: 

	In this precise case, there is of course no point in using this notation instead of the standard notation below: 

.. i18n: 	<name type="field" name="partner_id.name"/> 

	<name type="field" name="partner_id.name"/> 

.. i18n: The **zoom** type is only useful when we want to recover several fields in the same object.

The **zoom** type is only useful when we want to recover several fields in the same object.

.. i18n:     * **function**: returns the result of the call to the function whose name is given in the name attribute. This function must be part of the list of predefined functions. For the moment, the only available function is today, which returns the current date. 
.. i18n: 
.. i18n:     * **call**: calls the object method whose name is given in the name attribute with the arguments given in the args attribute. The result is stored into a dictionary of the form {'name_of_variable': value, ... } and can be accessed through child nodes. These nodes must have a value attribute which correspond to one of the keys of the dictionary returned by the method. 

    * **function**: returns the result of the call to the function whose name is given in the name attribute. This function must be part of the list of predefined functions. For the moment, the only available function is today, which returns the current date. 

    * **call**: calls the object method whose name is given in the name attribute with the arguments given in the args attribute. The result is stored into a dictionary of the form {'name_of_variable': value, ... } and can be accessed through child nodes. These nodes must have a value attribute which correspond to one of the keys of the dictionary returned by the method. 

.. i18n: **Example**:
.. i18n: ::
.. i18n: 
.. i18n: 	<cost type="call" name="compute_seller_costs" args="">

**Example**:
::

	<cost type="call" name="compute_seller_costs" args="">

.. i18n: 	    <name value="name"/> 
.. i18n: 	    <amount value="amount"/> 

	    <name value="name"/> 
	    <amount value="amount"/> 

.. i18n: 	</cost> 

	</cost> 

.. i18n: **TODO**: documenter format methode appellée def compute_buyer_costs(self, cr, uid, ids, \*args):

**TODO**: documenter format methode appellée def compute_buyer_costs(self, cr, uid, ids, \*args):

.. i18n:     * **attachment**: extract the first attachment of the resource whose id is taken from the field whose name is given in the name attribute, and put it as an image in the report. 

    * **attachment**: extract the first attachment of the resource whose id is taken from the field whose name is given in the name attribute, and put it as an image in the report. 

.. i18n: Example:
.. i18n: 	<image type="attachment" name="id"/> 

Example:
	<image type="attachment" name="id"/> 

.. i18n: **Example**

**Example**

.. i18n: Here is an example of XML file:
.. i18n: ::
.. i18n: 
.. i18n: 	    <?xml version="1.0" encoding="ISO-8859-1"?> 
.. i18n: 	    <transfer-list>

Here is an example of XML file:
::

	    <?xml version="1.0" encoding="ISO-8859-1"?> 
	    <transfer-list>

.. i18n: 		<transfer type="fields" name="id">

		<transfer type="fields" name="id">

.. i18n: 		    <name type="field" name="name"/> 
.. i18n: 		    <partner_id type="field" name="partner_id.name"/> 
.. i18n: 		    <date type="field" name="date"/> 
.. i18n: 		    <type type="field" name="type"/> 
.. i18n: 		    <reference type="field" name="reference"/> 
.. i18n: 		    <amount type="field" name="amount"/> 
.. i18n: 		    <change type="field" name="change"/> 

		    <name type="field" name="name"/> 
		    <partner_id type="field" name="partner_id.name"/> 
		    <date type="field" name="date"/> 
		    <type type="field" name="type"/> 
		    <reference type="field" name="reference"/> 
		    <amount type="field" name="amount"/> 
		    <change type="field" name="change"/> 

.. i18n: 		</transfer> 

		</transfer> 

.. i18n: 	    </transfer-list> 

	    </transfer-list> 

.. i18n: Introduction to RML
.. i18n: -------------------

Introduction to RML
-------------------

.. i18n: For more information on the RML format, please refer to the official Reportlab documentation.

For more information on the RML format, please refer to the official Reportlab documentation.

.. i18n:     * http://www.reportlab.com/docs/RML_UserGuide.pdf 

    * http://www.reportlab.com/docs/RML_UserGuide.pdf 

.. i18n: XSL:RML Stylesheet
.. i18n: ------------------

XSL:RML Stylesheet
------------------

.. i18n: There are two possibilities to do a XSL style sheet for a report. Either making everything by yourself, or use our predefined templates

There are two possibilities to do a XSL style sheet for a report. Either making everything by yourself, or use our predefined templates

.. i18n: Either freestyle or use corporate_defaults + rml_template

Either freestyle or use corporate_defaults + rml_template

.. i18n:     import rml_template.xsl 

    import rml_template.xsl 

.. i18n:         required templates:

        required templates:

.. i18n:             - frames? 
.. i18n:             - stylesheet 
.. i18n:             - story 

            - frames? 
            - stylesheet 
            - story 

.. i18n:         optional templates: 

        optional templates: 

.. i18n: Translations
.. i18n: """"""""""""

Translations
""""""""""""

.. i18n: As Open ERP can be used in several langages, reports must be translatable. But in a report, everything doesn't have to be translated : only the actual text has to be translated, not the formatting codes. A field will be processed by the translation system if the XML tag which surrounds it (whatever it is) has a t="1" attribute. The server will translate all the fields with such attributes in the report generation process.

As Open ERP can be used in several langages, reports must be translatable. But in a report, everything doesn't have to be translated : only the actual text has to be translated, not the formatting codes. A field will be processed by the translation system if the XML tag which surrounds it (whatever it is) has a t="1" attribute. The server will translate all the fields with such attributes in the report generation process.

.. i18n: Useful links:
.. i18n: """""""""""""

Useful links:
"""""""""""""

.. i18n:     * http://www.reportlab.com/docs/RML_UserGuide.pdf RML UserGuide (pdf) (reportlab.com) 
.. i18n: 
.. i18n:     * http://www.zvon.org/xxl/XSLTutorial/Output/index.html XSL Tutorial (zvon.org)
.. i18n:     * http://www.zvon.org/xxl/XSLTreference/Output/index.html XSL Reference (zvon.org)
.. i18n:     * http://www.w3schools.com/xsl/ XSL tutorial and references (W3Schools)
.. i18n:     * http://www.w3.org/TR/xslt/ XSL Specification (W3C) 

    * http://www.reportlab.com/docs/RML_UserGuide.pdf RML UserGuide (pdf) (reportlab.com) 

    * http://www.zvon.org/xxl/XSLTutorial/Output/index.html XSL Tutorial (zvon.org)
    * http://www.zvon.org/xxl/XSLTreference/Output/index.html XSL Reference (zvon.org)
    * http://www.w3schools.com/xsl/ XSL tutorial and references (W3Schools)
    * http://www.w3.org/TR/xslt/ XSL Specification (W3C) 

.. i18n: Example (with corporate defaults):
.. i18n: """""""""""""""""""""""""""""""""""
.. i18n: ::
.. i18n: 
.. i18n: 	    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">

Example (with corporate defaults):
"""""""""""""""""""""""""""""""""""
::

	    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">

.. i18n: 		<xsl:import href="../../custom/corporate_defaults.xsl"/> 
.. i18n: 		<xsl:import href="../../base/report/rml_template.xsl"/> 
.. i18n: 		<xsl:variable name="page_format">a4_normal</xsl:variable> 
.. i18n: 		<xsl:template match="/">

		<xsl:import href="../../custom/corporate_defaults.xsl"/> 
		<xsl:import href="../../base/report/rml_template.xsl"/> 
		<xsl:variable name="page_format">a4_normal</xsl:variable> 
		<xsl:template match="/">

.. i18n: 		    <xsl:call-template name="rml"/> 

		    <xsl:call-template name="rml"/> 

.. i18n: 		</xsl:template> 
.. i18n: 		<xsl:template name="stylesheet">

		</xsl:template> 
		<xsl:template name="stylesheet">

.. i18n: 		    </xsl:template> 

		    </xsl:template> 

.. i18n: 		<xsl:template name="story">

		<xsl:template name="story">

.. i18n: 		    <xsl:apply-templates select="transfer-list"/> 

		    <xsl:apply-templates select="transfer-list"/> 

.. i18n: 		</xsl:template> 
.. i18n: 		<xsl:template match="transfer-list">

		</xsl:template> 
		<xsl:template match="transfer-list">

.. i18n: 		    <xsl:apply-templates select="transfer"/> 

		    <xsl:apply-templates select="transfer"/> 

.. i18n: 		</xsl:template> 
.. i18n: 		<xsl:template match="transfer">

		</xsl:template> 
		<xsl:template match="transfer">

.. i18n: 		    <setNextTemplate name="other_pages"/> 
.. i18n: 		    <para>

		    <setNextTemplate name="other_pages"/> 
		    <para>

.. i18n: 		        Document: <xsl:value-of select="name"/> 

		        Document: <xsl:value-of select="name"/> 

.. i18n: 		    </para><para>

		    </para><para>

.. i18n: 		        Type: <xsl:value-of select="type"/> 

		        Type: <xsl:value-of select="type"/> 

.. i18n: 		    </para><para>

		    </para><para>

.. i18n: 		        Reference: <xsl:value-of select="reference"/> 

		        Reference: <xsl:value-of select="reference"/> 

.. i18n: 		    </para><para>

		    </para><para>

.. i18n: 		        Partner ID: <xsl:value-of select="partner_id"/> 

		        Partner ID: <xsl:value-of select="partner_id"/> 

.. i18n: 		    </para><para>

		    </para><para>

.. i18n: 		        Date: <xsl:value-of select="date"/> 

		        Date: <xsl:value-of select="date"/> 

.. i18n: 		    </para><para>

		    </para><para>

.. i18n: 		        Amount: <xsl:value-of select="amount"/> 

		        Amount: <xsl:value-of select="amount"/> 

.. i18n: 		    </para> 
.. i18n: 		    <xsl:if test="number(change)>0">

		    </para> 
		    <xsl:if test="number(change)>0">

.. i18n: 		        <para>

		        <para>

.. i18n: 		            Change: <xsl:value-of select="change"/> 

		            Change: <xsl:value-of select="change"/> 

.. i18n: 		        </para> 

		        </para> 

.. i18n: 		    </xsl:if> 
.. i18n: 		    <setNextTemplate name="first_page"/> 
.. i18n: 		    <pageBreak/> 

		    </xsl:if> 
		    <setNextTemplate name="first_page"/> 
		    <pageBreak/> 

.. i18n: 		</xsl:template> 

		</xsl:template> 

.. i18n: 	    </xsl:stylesheet> 

	    </xsl:stylesheet> 

.. i18n: Reports without corporate header 
.. i18n: ================================

Reports without corporate header 
================================

.. i18n: **Example (with corporate defaults):**
.. i18n: ::
.. i18n: 
.. i18n: 	<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">
.. i18n: 	     <xsl:import href="../../base/report/rml_template.xsl"/>
.. i18n: 	     <xsl:variable name="page_format">a4_normal</xsl:variable>
.. i18n: 	 
.. i18n: 	     <xsl:template match="/">
.. i18n: 		  <xsl:call-template name="rml"/>
.. i18n: 	     </xsl:template>
.. i18n: 	 
.. i18n: 	     <xsl:template name="stylesheet">
.. i18n: 	      </xsl:template>
.. i18n: 	  
.. i18n: 	      <xsl:template name="story">
.. i18n: 		   <xsl:apply-templates select="transfer-list"/>
.. i18n: 	      </xsl:template>
.. i18n: 	  
.. i18n: 	      <xsl:template match="transfer-list">
.. i18n: 		   <xsl:apply-templates select="transfer"/>
.. i18n: 	      </xsl:template>
.. i18n: 	  
.. i18n: 	      <xsl:template match="transfer">
.. i18n: 		   <setNextTemplate name="other_pages"/>
.. i18n: 	   
.. i18n: 		   <para>
.. i18n: 		         Document: <xsl:value-of select="name"/>
.. i18n: 		   </para><para>
.. i18n: 		         Type: <xsl:value-of select="type"/>
.. i18n: 		   </para><para>
.. i18n: 		         Reference: <xsl:value-of select="reference"/>
.. i18n: 		   </para><para>
.. i18n: 		         Partner ID: <xsl:value-of select="partner_id"/>
.. i18n: 		   </para><para>
.. i18n: 		         Date: <xsl:value-of select="date"/>
.. i18n: 		   </para><para>
.. i18n: 		         Amount: <xsl:value-of select="amount"/>
.. i18n: 		   </para>
.. i18n: 	   
.. i18n: 		   <xsl:if test="number(change)>0">
.. i18n: 		        <para>
.. i18n: 		              Change: <xsl:value-of select="change"/>
.. i18n: 		        </para>
.. i18n: 		   </xsl:if>
.. i18n: 	   
.. i18n: 		   <setNextTemplate name="first_page"/> 
.. i18n: 		  <pageBreak/>
.. i18n: 	     </xsl:template>
.. i18n: 	</xsl:stylesheet>

**Example (with corporate defaults):**
::

	<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">
	     <xsl:import href="../../base/report/rml_template.xsl"/>
	     <xsl:variable name="page_format">a4_normal</xsl:variable>
	 
	     <xsl:template match="/">
		  <xsl:call-template name="rml"/>
	     </xsl:template>
	 
	     <xsl:template name="stylesheet">
	      </xsl:template>
	  
	      <xsl:template name="story">
		   <xsl:apply-templates select="transfer-list"/>
	      </xsl:template>
	  
	      <xsl:template match="transfer-list">
		   <xsl:apply-templates select="transfer"/>
	      </xsl:template>
	  
	      <xsl:template match="transfer">
		   <setNextTemplate name="other_pages"/>
	   
		   <para>
		         Document: <xsl:value-of select="name"/>
		   </para><para>
		         Type: <xsl:value-of select="type"/>
		   </para><para>
		         Reference: <xsl:value-of select="reference"/>
		   </para><para>
		         Partner ID: <xsl:value-of select="partner_id"/>
		   </para><para>
		         Date: <xsl:value-of select="date"/>
		   </para><para>
		         Amount: <xsl:value-of select="amount"/>
		   </para>
	   
		   <xsl:if test="number(change)>0">
		        <para>
		              Change: <xsl:value-of select="change"/>
		        </para>
		   </xsl:if>
	   
		   <setNextTemplate name="first_page"/> 
		  <pageBreak/>
	     </xsl:template>
	</xsl:stylesheet>

.. i18n: Each report with its own corporate header 
.. i18n: =========================================

Each report with its own corporate header 
=========================================

.. i18n: **Example (with corporate defaults):**
.. i18n: ::
.. i18n: 
.. i18n: 	    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">

**Example (with corporate defaults):**
::

	    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" :xmlns:fo="http://www.w3.org/1999/XSL/Format">

.. i18n: 		<xsl:import href="../../custom/corporate_defaults.xsl"/> 
.. i18n: 		<xsl:import href="../../base/report/rml_template.xsl"/> 
.. i18n: 		<xsl:variable name="page_format">a4_normal</xsl:variable> 
.. i18n: 		..................... 
.. i18n: 		</xsl:template> 

		<xsl:import href="../../custom/corporate_defaults.xsl"/> 
		<xsl:import href="../../base/report/rml_template.xsl"/> 
		<xsl:variable name="page_format">a4_normal</xsl:variable> 
		..................... 
		</xsl:template> 

.. i18n: 	    </xsl:stylesheet> 

	    </xsl:stylesheet> 

.. i18n: Bar Codes 
.. i18n: =========

Bar Codes 
=========

.. i18n: Barcodes in RML files
.. i18n: ---------------------

Barcodes in RML files
---------------------

.. i18n: Barcodes can be generated using the <barcode> tag in RML files. The following formats are supported:

Barcodes can be generated using the <barcode> tag in RML files. The following formats are supported:

.. i18n:     * codabar
.. i18n:     * code11
.. i18n:     * code128 (default if no 'code' specified')
.. i18n:     * standard39
.. i18n:     * standard93
.. i18n:     * i2of5
.. i18n:     * extended39
.. i18n:     * extended93
.. i18n:     * msi
.. i18n:     * fim
.. i18n:     * postnet 

    * codabar
    * code11
    * code128 (default if no 'code' specified')
    * standard39
    * standard93
    * i2of5
    * extended39
    * extended93
    * msi
    * fim
    * postnet 

.. i18n: You can change the following attributes for rendering your barcode:

You can change the following attributes for rendering your barcode:

.. i18n:     * 'code': 'char'
.. i18n:     * 'ratio':'float'
.. i18n:     * 'xdim':'unit'
.. i18n:     * 'height':'unit'
.. i18n:     * 'checksum':'bool'
.. i18n:     * 'quiet':'bool' 

    * 'code': 'char'
    * 'ratio':'float'
    * 'xdim':'unit'
    * 'height':'unit'
    * 'checksum':'bool'
    * 'quiet':'bool' 

.. i18n: Examples:

Examples:

.. i18n:     <barcode code="code128" xdim="28cm" ratio="2.2">`SN12345678</barcode> 

    <barcode code="code128" xdim="28cm" ratio="2.2">`SN12345678</barcode> 

.. i18n: How to add a new report
.. i18n: =======================

How to add a new report
=======================

.. i18n: In 4.0.X

In 4.0.X

.. i18n:     Administration -> Custom -> Low Level -> Base->Actions -> ir.actions.report.xml 

    Administration -> Custom -> Low Level -> Base->Actions -> ir.actions.report.xml 

.. i18n: Usual TAGS
.. i18n: ==========

Usual TAGS
==========

.. i18n: Code find in [[ ]] tags is python code.
.. i18n: ---------------------------------------

Code find in [[ ]] tags is python code.
---------------------------------------

.. i18n: The context of the code (the variable's values you can use) is the following:

The context of the code (the variable's values you can use) is the following:

.. i18n: python objects/variables, available when the report start:

python objects/variables, available when the report start:

.. i18n: "objects" the list of objects to be printed (invoices for example)

"objects" the list of objects to be printed (invoices for example)

.. i18n: "data" comes from the wizard

"data" comes from the wizard

.. i18n: "time" see python documentation.

"time" see python documentation.

.. i18n: "user" the user object launching the report.

"user" the user object launching the report.

.. i18n: python functions you can use:

python functions you can use:

.. i18n: "setlang('fr')" change the langage used in automated translation (fields...).

"setlang('fr')" change the langage used in automated translation (fields...).

.. i18n: "repeatIn(list,varname)" repeat the template (whole doc. or current paragraph?) for each object in the list. Use varname in the template's tags.

"repeatIn(list,varname)" repeat the template (whole doc. or current paragraph?) for each object in the list. Use varname in the template's tags.

.. i18n: "setTag('para','xpre')" change the enclosing RML tag (usually 'para') by an other (xpre is a preformatted paragraph), in the (converted from sxw)rml document (?)

"setTag('para','xpre')" change the enclosing RML tag (usually 'para') by an other (xpre is a preformatted paragraph), in the (converted from sxw)rml document (?)

.. i18n: "removeParentNode"

"removeParentNode"

.. i18n: Useful tags:
.. i18n: ------------
.. i18n:     [ repeatIn(objects,'o') ] objects to be printed 
.. i18n:     repeatIn(o.invoice_line,'l') print every line 
.. i18n:     o.quantity * o.price Operations are OK. 
.. i18n:     '07d' int(o.number) number formating 
.. i18n:     reduce(lambda x obj: x+obj.qty , list , 0 ) total qty of list (try "objects" as list) 
.. i18n:     user.name user name. 
.. i18n:     setLang(o.partner_id.lang) Localized printings 
.. i18n:     time.strftime('%d/%m/%Y') format=dd MM YYYY, check python doc for more about "%d", ... 
.. i18n:     [[ time.strftime(time.ctime()[0:10]) ]] [[ time.strftime(time.ctime()[-4:]) ]] prints only date. 
.. i18n:     time.ctime() it prints the actual date & time. 
.. i18n:     [[ time.ctime().split()[3] ]] prints only time 

Useful tags:
------------
    [ repeatIn(objects,'o') ] objects to be printed 
    repeatIn(o.invoice_line,'l') print every line 
    o.quantity * o.price Operations are OK. 
    '07d' int(o.number) number formating 
    reduce(lambda x obj: x+obj.qty , list , 0 ) total qty of list (try "objects" as list) 
    user.name user name. 
    setLang(o.partner_id.lang) Localized printings 
    time.strftime('%d/%m/%Y') format=dd MM YYYY, check python doc for more about "%d", ... 
    [[ time.strftime(time.ctime()[0:10]) ]] [[ time.strftime(time.ctime()[-4:]) ]] prints only date. 
    time.ctime() it prints the actual date & time. 
    [[ time.ctime().split()[3] ]] prints only time 

.. i18n: one more interesting tag: if you want to print out the creator of an entry (create_uid) or the last one who wrote on an entry (write_uid) you have to add something like this to the class your report refers to:

one more interesting tag: if you want to print out the creator of an entry (create_uid) or the last one who wrote on an entry (write_uid) you have to add something like this to the class your report refers to:

.. i18n:     'create_uid': fields.many2one('res.users', 'User', readonly=1) 

    'create_uid': fields.many2one('res.users', 'User', readonly=1) 

.. i18n: and then in your report it's like this to print out the corresponding name:

and then in your report it's like this to print out the corresponding name:

.. i18n:     o.create_uid.name 

    o.create_uid.name 

.. i18n: Sometimes you might want to print out something only if a certain condition is fullfilled. You can construct it with the pyhton logical operators "not", "and" and "or". Because every object in python has a logical value (TRUE or FALSE) you can construct something like this:

Sometimes you might want to print out something only if a certain condition is fullfilled. You can construct it with the pyhton logical operators "not", "and" and "or". Because every object in python has a logical value (TRUE or FALSE) you can construct something like this:

.. i18n:     (o.prop=='draft') and 'YES' or 'NO' print YES or NO 

    (o.prop=='draft') and 'YES' or 'NO' print YES or NO 

.. i18n: it works like this:

it works like this:

.. i18n: and: first value is TRUE then print out the second value. First value is FALSE print out first value.

and: first value is TRUE then print out the second value. First value is FALSE print out first value.

.. i18n: or: first value is TRUE then print out the first value. First value is FALSE print out second value. in this example if o.prop=='draft' -> TRUE then **(o.prop=='draft') and 'YES'** reads **'Yes'**. Next step is 	'Yes' or 'No' which leads to a printed 'YES' (because a string's logical value is TRUE). If o.prop=='draft' -> FALSE then it reads FALSE or 'No'. So 'No' is printed. One can use very comlpex structures. To learn more search for some pyhton reference regarding logical opertors.

or: first value is TRUE then print out the first value. First value is FALSE print out second value. in this example if o.prop=='draft' -> TRUE then **(o.prop=='draft') and 'YES'** reads **'Yes'**. Next step is 	'Yes' or 'No' which leads to a printed 'YES' (because a string's logical value is TRUE). If o.prop=='draft' -> FALSE then it reads FALSE or 'No'. So 'No' is printed. One can use very comlpex structures. To learn more search for some pyhton reference regarding logical opertors.

.. i18n: python function "filter" can... filter: try something like:

python function "filter" can... filter: try something like:

.. i18n:     repeatIn(filter( lambda l: l.product_id.type=='service' ,o.invoice_line), 'line') 

    repeatIn(filter( lambda l: l.product_id.type=='service' ,o.invoice_line), 'line') 

.. i18n: for printing only product with type='service' in a line's section.

for printing only product with type='service' in a line's section.

.. i18n: To display binary field image on report (to be checked)

To display binary field image on report (to be checked)

.. i18n:     [[ setTag('para','image',{'width':'100.0','height':'80.0'}) ]] o.image or setTag('image','para') 
.. i18n:  

    [[ setTag('para','image',{'width':'100.0','height':'80.0'}) ]] o.image or setTag('image','para') 
 

.. i18n: Unicode reports 
.. i18n: ===============

Unicode reports 
===============

.. i18n: As of OpenERP 5.0-rc3 unicode printing with ReportLab is still not available. The problem is that OpenERP uses the PDF standard fonts (14 fonts, they are not embedded in the document but the reader provides them) that are Type1 and have only Latin1 characters.

As of OpenERP 5.0-rc3 unicode printing with ReportLab is still not available. The problem is that OpenERP uses the PDF standard fonts (14 fonts, they are not embedded in the document but the reader provides them) that are Type1 and have only Latin1 characters.

.. i18n: The solution consists of 3 parts
.. i18n: --------------------------------

The solution consists of 3 parts
--------------------------------

.. i18n:     * Provide TrueType fonts and make them accessible for ReportLab.
.. i18n:     * Register the TrueType fonts with ReportLab before using them in the reports.
.. i18n:     * Replace the old fontNames in xsl and rml templates with the TrueType ones. 

    * Provide TrueType fonts and make them accessible for ReportLab.
    * Register the TrueType fonts with ReportLab before using them in the reports.
    * Replace the old fontNames in xsl and rml templates with the TrueType ones. 

.. i18n: All these ideas are taken from the forums
.. i18n: -----------------------------------------

All these ideas are taken from the forums
-----------------------------------------

.. i18n: **Free TrueType fonts**

**Free TrueType fonts**

.. i18n: that can be used for this purpose are in the DejaVu family. http://dejavu-fonts.org/wiki/index.php?title=Main_Page They can be installed

that can be used for this purpose are in the DejaVu family. http://dejavu-fonts.org/wiki/index.php?title=Main_Page They can be installed

.. i18n:     * in the ReportLab's fonts directory,
.. i18n:     * system-wide and include that directory in rl_config.py,
.. i18n:     * in a subdirectory of the OpenERP installation and give that path to ReportLab during the font registration. 

    * in the ReportLab's fonts directory,
    * system-wide and include that directory in rl_config.py,
    * in a subdirectory of the OpenERP installation and give that path to ReportLab during the font registration. 

.. i18n: **In the server/bin/report/render/rml2pdf/__init__.py**
.. i18n: ::
.. i18n: 
.. i18n: 	import reportlab.rl_config
.. i18n: 	reportlab.rl_config.warnOnMissingFontGlyphs = 0

**In the server/bin/report/render/rml2pdf/__init__.py**
::

	import reportlab.rl_config
	reportlab.rl_config.warnOnMissingFontGlyphs = 0

.. i18n: 	from reportlab.pdfbase import pdfmetrics
.. i18n: 	from reportlab.pdfbase.ttfonts import TTFont
.. i18n: 	import reportlab

	from reportlab.pdfbase import pdfmetrics
	from reportlab.pdfbase.ttfonts import TTFont
	import reportlab

.. i18n: 	enc = 'UTF-8'

	enc = 'UTF-8'

.. i18n: 	#repeat these for all the fonts needed
.. i18n: 	pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf',enc))
.. i18n: 	pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', 'DejaVuSans-Bold.ttf',enc))

	#repeat these for all the fonts needed
	pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf',enc))
	pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', 'DejaVuSans-Bold.ttf',enc))

.. i18n: 	from reportlab.lib.fonts import addMapping

	from reportlab.lib.fonts import addMapping

.. i18n: 	#repeat these for all the fonts needed
.. i18n: 	addMapping('DejaVuSans', 0, 0, 'DejaVuSans') #normal
.. i18n: 	addMapping('DejaVuSans-Bold', 1, 0, 'DejaVuSans') #normal

	#repeat these for all the fonts needed
	addMapping('DejaVuSans', 0, 0, 'DejaVuSans') #normal
	addMapping('DejaVuSans-Bold', 1, 0, 'DejaVuSans') #normal

.. i18n: trml2pdf.py should be modified to load this if invoked from the command line.

trml2pdf.py should be modified to load this if invoked from the command line.

.. i18n: **All the xsl and rml files have to be modified**

**All the xsl and rml files have to be modified**

.. i18n: A list of possible alternatives:
.. i18n: ::
.. i18n: 
.. i18n: 	'Times-Roman',       'DejaVuSerif.ttf'
.. i18n: 	'Times-BoldItalic',  'DejaVuSerif-BoldItalic.ttf'
.. i18n: 	'Times-Bold',        'DejaVuSerif-Bold.ttf'
.. i18n: 	'Times-Italic',      'DejaVuSerif-Italic.ttf'

A list of possible alternatives:
::

	'Times-Roman',       'DejaVuSerif.ttf'
	'Times-BoldItalic',  'DejaVuSerif-BoldItalic.ttf'
	'Times-Bold',        'DejaVuSerif-Bold.ttf'
	'Times-Italic',      'DejaVuSerif-Italic.ttf'

.. i18n: 	'Helvetica',     'DejaVuSans.ttf'
.. i18n: 	'Helvetica-BoldItalic',  'DejaVuSans-BoldOblique.ttf'
.. i18n: 	'Helvetica-Bold',    'DejaVuSans-Bold.ttf'
.. i18n: 	'Helvetica-Italic',  'DejaVuSans-Oblique.ttf'

	'Helvetica',     'DejaVuSans.ttf'
	'Helvetica-BoldItalic',  'DejaVuSans-BoldOblique.ttf'
	'Helvetica-Bold',    'DejaVuSans-Bold.ttf'
	'Helvetica-Italic',  'DejaVuSans-Oblique.ttf'

.. i18n: 	'Courier',           'DejaVuSansMono.ttf'
.. i18n: 	'Courier-Bold',      'DejaVuSansMono-Bold.ttf'
.. i18n: 	'Courier-BoldItalic','DejaVuSansMono-BoldOblique.ttf'
.. i18n: 	'Courier-Italic',    'DejaVuSansMono-Oblique.ttf'

	'Courier',           'DejaVuSansMono.ttf'
	'Courier-Bold',      'DejaVuSansMono-Bold.ttf'
	'Courier-BoldItalic','DejaVuSansMono-BoldOblique.ttf'
	'Courier-Italic',    'DejaVuSansMono-Oblique.ttf'

.. i18n: 	'Helvetica-ExtraLight',  'DejaVuSans-ExtraLight.ttf'

	'Helvetica-ExtraLight',  'DejaVuSans-ExtraLight.ttf'

.. i18n: 	'TimesCondensed-Roman',      'DejaVuSerifCondensed.ttf'
.. i18n: 	'TimesCondensed-BoldItalic', 'DejaVuSerifCondensed-BoldItalic.ttf'
.. i18n: 	'TimesCondensed-Bold',       'DejaVuSerifCondensed-Bold.ttf'
.. i18n: 	'TimesCondensed-Italic',     'DejaVuSerifCondensed-Italic.ttf'

	'TimesCondensed-Roman',      'DejaVuSerifCondensed.ttf'
	'TimesCondensed-BoldItalic', 'DejaVuSerifCondensed-BoldItalic.ttf'
	'TimesCondensed-Bold',       'DejaVuSerifCondensed-Bold.ttf'
	'TimesCondensed-Italic',     'DejaVuSerifCondensed-Italic.ttf'

.. i18n: 	'HelveticaCondensed',        'DejaVuSansCondensed.ttf'
.. i18n: 	'HelveticaCondensed-BoldItalic', 'DejaVuSansCondensed-BoldOblique.ttf'
.. i18n: 	'HelveticaCondensed-Bold',   'DejaVuSansCondensed-Bold.ttf'
.. i18n: 	'HelveticaCondensed-Italic', 'DejaVuSansCondensed-Oblique.ttf

	'HelveticaCondensed',        'DejaVuSansCondensed.ttf'
	'HelveticaCondensed-BoldItalic', 'DejaVuSansCondensed-BoldOblique.ttf'
	'HelveticaCondensed-Bold',   'DejaVuSansCondensed-Bold.ttf'
	'HelveticaCondensed-Italic', 'DejaVuSansCondensed-Oblique.ttf

.. i18n: 	

	
