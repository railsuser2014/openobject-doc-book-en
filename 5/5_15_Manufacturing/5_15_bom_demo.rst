Demo records need to create
===========================

.. code-block:: xml

         <record id="product_category_marketableproduct0" model="product.category">
            <field name="name">Marketable Products</field>
        </record>

        <record id="product_category_shelves0" model="product.category">
            <field name="parent_id" ref="product_category_marketableproduct0"/>
            <field name="name">Shelves</field>
        </record>

        <record id="product_category_rawmaterial0" model="product.category">
            <field name="parent_id" ref="product.product_category_3"/>
            <field name="name">Raw Materials</field>
        </record>

        <record id="product_category_misc0" model="product.category">
            <field name="parent_id" ref="product.product_category_3"/>
            <field name="name">Misc</field>
        </record>

        <record id="product_product_kitshelfofcm0" model="product.product">
            <field name="default_code">SHE100KIT</field>
            <field name="supply_method">produce</field>
            <field eval="'make_to_order'" name="procure_method"/>
            <field name="list_price">110.0</field>
            <field name="standard_price">48.0</field>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">KIT Shelf of 100cm</field>
            <field eval="0" name="purchase_ok"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_shelves0"/>
        </record>

        <record id="product_product_shelfofcm0" model="product.product">
            <field name="default_code">SHE100</field>
            <field name="supply_method">produce</field>
            <field name="list_price">130.0</field>
            <field name="standard_price">50.0</field>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Shelf of 100cm</field>
            <field name="type">product</field>
           <field name="categ_id" ref="product_category_shelves0"/>
        </record>

        <record id="product_product_shelf1" model="product.product">
            <field name="default_code">RCK200</field>
            <field name="supply_method">buy</field>
            <field name="standard_price">4.0</field>
            <field eval="0" name="sale_ok"/>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Rack 200cm</field>
            <field eval="8" name="seller_delay"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_misc0"/>
        </record>

        <record id="product_product_rearpanelarm1" model="product.product">
            <field name="default_code">RPAN200</field>
            <field name="supply_method">buy</field>
            <field name="standard_price">13.0</field>
            <field eval="0" name="sale_ok"/>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Rear Panel SHE200</field>
            <field eval="5" name="seller_delay"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_misc0"/>
        </record>

        <record id="product_product_shelfofcm1" model="product.product">
            <field name="default_code">SHE200</field>
            <field name="supply_method">produce</field>
            <field eval="'make_to_order'" name="procure_method"/>
            <field name="list_price">210.0</field>
            <field name="standard_price">80.0</field>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Shelf of 200cm</field>
            <field name="type">product</field>
                <field name="categ_id" ref="product_category_shelves0"/>
       </record>

        <record id="product_product_sidepanel0" model="product.product">
            <field name="default_code">SIDEPAN</field>
            <field name="supply_method">buy</field>
            <field name="standard_price">3.0</field>
            <field eval="0" name="sale_ok"/>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Side Panel</field>
            <field eval="5" name="seller_delay"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_misc0"/>
        </record>

        <record id="product_product_assemblysection0" model="product.product">
            <field name="default_code">PROFIL</field>
            <field name="supply_method">produce</field>
            <field name="list_price">1.0</field>
            <field name="standard_price">2.0</field>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Assembly Section</field>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_misc0"/>
        </record>

        <record id="product_product_rearpanelarm0" model="product.product">
            <field name="default_code">RPAN100</field>
            <field name="supply_method">buy</field>
            <field name="standard_price">10.0</field>
            <field eval="0" name="sale_ok"/>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Rear Panel SHE100</field>
            <field eval="5" name="seller_delay"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_misc0"/>
        </record>

        <record id="product_product_shelf0" model="product.product">
            <field name="default_code">RCK100</field>
            <field name="supply_method">buy</field>
            <field name="standard_price">5.0</field>
            <field eval="0" name="sale_ok"/>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Rack 100cm</field>
            <field eval="8" name="seller_delay"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_misc0"/>
        </record>

        <record id="product_product_metalcleats0" model="product.product">
           <field name="default_code">METC000</field>
            <field name="supply_method">buy</field>
            <field eval="0" name="sale_ok"/>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Metal Cleats</field>
            <field eval="20" name="seller_delay"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_misc0"/>
        </record>

        <record id="product_product_woodmm0" model="product.product">
            <field name="default_code">WOOD002</field>
            <field name="supply_method">buy</field>
            <field name="standard_price">5.0</field>
            <field name="uom_id" ref="product.product_uom_meter"/>
            <field name="uom_po_id" ref="product.product_uom_meter"/>
            <field name="name">Wood 2mm</field>
            <field eval="10" name="seller_delay"/>
            <field eval="7.0" name="sale_delay"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_rawmaterial0"/>
        </record>

        <record id="product_product_woodmm10" model="product.product">
            <field name="default_code">WOOD010</field>
            <field name="supply_method">buy</field>
            <field name="standard_price">5.0</field>
            <field name="uom_id" ref="product.product_uom_meter"/>
            <field name="uom_po_id" ref="product.product_uom_meter"/>
           <field name="name">Wood 10mm</field>
            <field eval="10" name="seller_delay"/>
           <field eval="7.0" name="sale_delay"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_rawmaterial0"/>
        </record>

        <record id="product_product_span100" model="product.product">
            <field name="default_code">SPAN100</field>
            <field name="supply_method">buy</field>
            <field name="standard_price">3.0</field>
            <field eval="0" name="sale_ok"/>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Shelf Panel</field>
            <field eval="5" name="seller_delay"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_misc0"/>
        </record>

        <record id="product_product_woodlintelm0" model="product.product">
            <field name="default_code">LIN40</field>
            <field name="supply_method">buy</field>
            <field name="standard_price">8.0</field>
            <field eval="0" name="sale_ok"/>
            <field name="uom_id" ref="product.product_uom_unit"/>
            <field name="uom_po_id" ref="product.product_uom_unit"/>
            <field name="name">Wood Lintel 4m</field>
            <field eval="10" name="seller_delay"/>
            <field name="type">product</field>
            <field name="categ_id" ref="product_category_misc0"/>
        </record>

        <record id="mrp_bom_defaultbomforshelfofcm0" model="mrp.bom">
            <field name="name">Default BOM for Shelf of 100cm</field>
            <field name="sequence">100</field>
            <field name="product_id" ref="product_product_shelfofcm0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">1.0</field>
            <field name="routing_id" ref="mrp.mrp_routing_1"/>
        </record>

        <!-- BoMs for 1 Shelf 100cm
                   Product Ref. Qty     UoM     Type of BoM
                    SIDEPAN      2      PCE     normal
                    PROFIL       4      PCE     phantom
                    RPAN100      1      PCE     phantom
                    RCK100       3      PCE     phantom
        -->

        <record id="mrp_bom_sidepanel0" model="mrp.bom">
            <field name="name">Side Panel</field>
            <field name="sequence">101</field>
            <field name="product_id" ref="product_product_sidepanel0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">2.0</field>
            <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm0"/>
        </record>

        <record id="mrp_bom_metalcleats0" model="mrp.bom">
            <field name="name">Metal Cleats</field>
            <field name="sequence">127</field>
            <field name="product_id" ref="product_product_metalcleats0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">12.0</field>
            <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm0"/>
        </record>

        <record id="mrp_bom_assemblysection0" model="mrp.bom">
            <field name="name">Assembly Section</field>
            <field name="sequence">102</field>
            <field name="product_id" ref="product_product_assemblysection0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">4.0</field>
            <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm0"/>
            <field name="type">phantom</field>
        </record>

        <record id="mrp_bom_rearpanelarm0" model="mrp.bom">
           <field name="sequence">103</field>
           <field name="product_id" ref="product_product_rearpanelarm0"/>
           <field name="product_uom" ref="product.product_uom_unit"/>
           <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm0"/>
           <field name="product_qty">1.0</field>
           <field name="name">Rear panel SHE100</field>
           <field name="type">phantom</field>
        </record>

        <record id="mrp_bom_shelf0" model="mrp.bom">
           <field name="sequence">104</field>
           <field name="product_id" ref="product_product_shelf0"/>
           <field name="product_uom" ref="product.product_uom_unit"/>
           <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm0"/>
           <field name="product_qty">3.0</field>
           <field name="name">RCK100</field>
           <field name="type">phantom</field>
        </record>

        <!--
            BOMs for 1 RCK100 PCE
                        Product Ref     Qty UoM  Type of BoM
                        SPAN100         1   PCE  phantom
                        METC000         4   PCE  normal
        -->
        <record id="mrp_bom_shelf1" model="mrp.bom">
           <field name="sequence">133</field>
           <field name="product_id" ref="product_product_shelf0"/>
           <field name="product_uom" ref="product.product_uom_unit"/>
           <field name="product_qty">1.0</field>
           <field name="name">RCK100</field>
        </record>
        <record id="mrp_bom_shelf0_span100" model="mrp.bom">
           <field name="sequence">1331</field>
           <field name="product_id" ref="product_product_span100"/>
           <field name="product_uom" ref="product.product_uom_unit"/>
           <field name="bom_id" ref="mrp_bom_shelf1"/>
           <field name="product_qty">1.0</field>
           <field name="type">phantom</field> <!-- It should be phantom -->
           <field name="name">SPAN100</field>
        </record>
        <record id="mrp_bom_shelf0_metalcleats0" model="mrp.bom">
           <field name="sequence">1332</field>
           <field name="product_id" ref="product_product_metalcleats0"/>
           <field name="product_uom" ref="product.product_uom_unit"/>
           <field name="bom_id" ref="mrp_bom_shelf1"/>
           <field name="product_qty">4.0</field>
           <field name="name">METC000</field>
        </record>
        <!--
        Bill of Materials for 1 SPAN100 PCE
                        Product Code    Quantity    Unit of Measure
                        WOOD010         0.083       m
        -->
        <record id="mrp_bom_span100" model="mrp.bom">
           <field name="sequence">135</field>
           <field name="product_id" ref="product_product_span100"/>
           <field name="product_uom" ref="product.product_uom_unit"/>
           <field name="product_qty">1.0</field>
           <field name="name">SPAN100</field>
        </record>
        <record id="mrp_bom_span100_wood010" model="mrp.bom">
           <field name="sequence">1351</field>
           <field name="product_id" ref="product_product_woodmm10"/>
           <field name="product_uom" ref="product.product_uom_meter"/>
           <field name="bom_id" ref="mrp_bom_span100"/>
           <field name="product_qty">0.083</field>
           <field name="name">WOOD010</field>
        </record>
        <!-- BoMs for 1 Assembly Section PCE
                Product Ref.    Qty     UoM
                   LIN40        0.25       Meter
        -->
        <record id="mrp_bom_assemblysection1" model="mrp.bom">
            <field name="name">Assembly Section</field>
            <field name="sequence">123</field>
            <field name="product_id" ref="product_product_assemblysection0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">1.0</field>
            <field name="routing_id" ref="mrp.mrp_routing_0"/>
        </record>

        <record id="mrp_bom_woodlintelm0" model="mrp.bom">
           <field name="sequence">1231</field>
           <field name="product_id" ref="product_product_woodlintelm0"/>
           <field name="product_uom" ref="product.product_uom_meter"/>
           <field name="product_qty">0.25</field>
           <field name="bom_id" ref="mrp_bom_assemblysection1"/>
           <field name="name">Wood Lintel 0.25m</field>
        </record>
        <!--
        Bill of Materials for 1 RPAN100 PCE
                        Product Code    Quantity    Unit of Measure
                        WOOD002         0.25        m
        -->
        <record id="mrp_bom_rearpanelarm1" model="mrp.bom">
           <field name="sequence">131</field>
           <field name="product_id" ref="product_product_rearpanelarm0"/>
           <field name="product_uom" ref="product.product_uom_unit"/>
           <field name="product_qty">1.0</field>
           <field name="name">Rear panel SHE100</field>
            <field name="routing_id" ref="mrp.mrp_routing_0"/>
        </record>
        <record id="mrp_bom_rearpanelarm1_wood002" model="mrp.bom">
           <field name="sequence">1311</field>
           <field name="product_id" ref="product_product_woodmm0"/>
           <field name="product_uom" ref="product.product_uom_meter"/>
           <field name="bom_id" ref="mrp_bom_rearpanelarm1"/>
           <field name="product_qty">0.25</field>
           <field name="name">WOOD002 0.25m</field>
        </record>
        <record id="mrp_bom_defaultbomforshelfofcm1" model="mrp.bom">
            <field name="name">Default BOM for Shelf of 200cm</field>
            <field name="code">SHE200</field>
            <field name="sequence">137</field>
            <field name="product_id" ref="product_product_shelfofcm1"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">1.0</field>
        </record>

        <!--Defining BoMs of Shelf 200cm
                Product Ref.    Qty     UoM     Type of BoM
                 RPAN200         1      PCE     normal
                 PROFIL          4      PCE     normal
                 SIDEPAN         2      PCE     normal
                 METC000         12     PCE     normal
                 RCK200          3      PCE     normal
        -->
        <record id="mrp_bom_rearpanelarm2" model="mrp.bom">
           <field name="sequence">147</field>
           <field name="product_id" ref="product_product_rearpanelarm1"/>
           <field name="product_uom" ref="product.product_uom_unit"/>
           <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm1"/>
           <field name="product_qty">1.0</field>
           <field name="name">Rear panel SHE200</field>
        </record>

        <record id="mrp_bom_assemblysection3" model="mrp.bom">
            <field name="name">Assembly Section</field>
            <field name="sequence">149</field>
            <field name="product_id" ref="product_product_assemblysection0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">4.0</field>
            <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm1"/>
        </record>

        <record id="mrp_bom_sidepanel3" model="mrp.bom">
            <field name="name">Side Panel</field>
            <field name="sequence">151</field>
            <field name="product_id" ref="product_product_sidepanel0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">2.0</field>
            <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm1"/>
        </record>

        <record id="mrp_bom_shelf2" model="mrp.bom">
           <field name="sequence">153</field>
           <field name="product_id" ref="product_product_shelf1"/>
           <field name="product_uom" ref="product.product_uom_unit"/>
           <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm1"/>
           <field name="product_qty">3.0</field>
           <field name="name">Shelf 200</field>
        </record>

        <record id="mrp_bom_metalcleats3" model="mrp.bom">
            <field name="name">Metal Cleats</field>
            <field name="sequence">155</field>
            <field name="product_id" ref="product_product_metalcleats0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">12.0</field>
            <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm1"/>
        </record>

        <record id="mrp_bom_defaultbomforkitshelfofcm0" model="mrp.bom">
            <field name="name">Default BOM for KIT Shelf of 100cm</field>
            <field name="code">SHE100KIT</field>
            <field name="sequence">139</field>
            <field name="product_id" ref="product_product_kitshelfofcm0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">1.0</field>
            <field name="type">phantom</field>
        </record>

        <!--Defining BoMs of KIT Shelf 100cm
                Product Ref.    Qty     UoM     Type of BoM
                    PROFIL       4      PCE     normal
                    SIDEPAN      2      PCE     normal
        -->

        <record id="mrp_bom_assemblysection2" model="mrp.bom">
            <field name="name">Assembly Section</field>
            <field name="sequence">143</field>
            <field name="product_id" ref="product_product_assemblysection0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">4.0</field>
            <field name="bom_id" ref="mrp_bom_defaultbomforkitshelfofcm0"/>
        </record>

        <record id="mrp_bom_sidepanel2" model="mrp.bom">
            <field name="name">Side Panel</field>
            <field name="sequence">145</field>
            <field name="product_id" ref="product_product_sidepanel0"/>
            <field name="product_uom" ref="product.product_uom_unit"/>
            <field name="product_qty">2.0</field>
            <field name="bom_id" ref="mrp_bom_defaultbomforkitshelfofcm0"/>
        </record>

       <record id="product.product_uom_dozen" model="product.uom">
                <field name="category_id" ref="product.product_uom_categ_unit"/>
                <field name="name">Dozen</field>
                <field name="factor" eval="0.083"/>
                <field name="uom_type">bigger</field>
        </record>

        <record id="mrp_production_shelf100cm" model="mrp.production">
            <field name="product_id" ref="product_product_shelfofcm0"/>
            <field name="product_uom" ref="product.product_uom_dozen"/>
            <field name="product_qty">3</field>
            <field name="location_src_id" ref="stock.stock_location_stock"/>
            <field name="location_dest_id" ref="stock.stock_location_output"/>
            <field name="bom_id" ref="mrp_bom_defaultbomforshelfofcm0"/>
        </record>

.. tip:: Copy

        To create the above records, copy these records and paste it in mrp_demo.xml upgrade mrp module from Database. 


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

