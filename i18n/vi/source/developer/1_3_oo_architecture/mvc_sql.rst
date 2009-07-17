
.. i18n: MVCSQL
.. i18n: ======

MVCSQL
======

.. i18n: Example 1
.. i18n: ---------

Example 1
---------

.. i18n: Suppose sale is a variable on a record of the sale.order object related to the 'sale_order' table. You can acquire such a variable doing this.::
.. i18n: 
.. i18n:     sale = self.browse(cr, uid, ID)

Suppose sale is a variable on a record of the sale.order object related to the 'sale_order' table. You can acquire such a variable doing this.::

    sale = self.browse(cr, uid, ID)

.. i18n: (where cr is the current row, from the database cursor, uid is the current user's ID for security checks, and ID is the sale order's ID or list of IDs if we want more than one)

(where cr is the current row, from the database cursor, uid is the current user's ID for security checks, and ID is the sale order's ID or list of IDs if we want more than one)

.. i18n: Suppose you want to get: the country name of the first contact of a partner related to the ID sale order. You can do the following in Open ERP::
.. i18n: 
.. i18n:     country_name = sale.partner_id.address[0].country_id.name

Suppose you want to get: the country name of the first contact of a partner related to the ID sale order. You can do the following in Open ERP::

    country_name = sale.partner_id.address[0].country_id.name

.. i18n: If you want to write the same thing in traditional SQL development, it will be in python: (we suppose cr is the cursor on the database, with psycopg)

If you want to write the same thing in traditional SQL development, it will be in python: (we suppose cr is the cursor on the database, with psycopg)

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     cr.execute('select partner_id from sale_order where id=%d', (ID,))
.. i18n:     partner_id = cr.fetchone()[0]
.. i18n:     cr.execute('select country_id from res_partner_address where partner_id=%d', (partner_id,))
.. i18n:     country_id = cr.fetchone()[0]
.. i18n:     cr.execute('select name from res_country where id=%d', (country_id,))
.. i18n:     del partner_id
.. i18n:     del country_id
.. i18n:     country_name = cr.fetchone()[0]

.. code-block:: python

    cr.execute('select partner_id from sale_order where id=%d', (ID,))
    partner_id = cr.fetchone()[0]
    cr.execute('select country_id from res_partner_address where partner_id=%d', (partner_id,))
    country_id = cr.fetchone()[0]
    cr.execute('select name from res_country where id=%d', (country_id,))
    del partner_id
    del country_id
    country_name = cr.fetchone()[0]

.. i18n: Of course you can do better if you develop smartly in SQL, using joins or subqueries. But you have to be smart and most of the time you will not be able to make such improvements:

Of course you can do better if you develop smartly in SQL, using joins or subqueries. But you have to be smart and most of the time you will not be able to make such improvements:

.. i18n:     * Maybe some parts are in others functions
.. i18n:     * There may be a loop in different elements
.. i18n:     * You have to use intermediate variables like country_id

    * Maybe some parts are in others functions
    * There may be a loop in different elements
    * You have to use intermediate variables like country_id

.. i18n: The first operation as an object call is much better for several reasons:

The first operation as an object call is much better for several reasons:

.. i18n:     * It uses objects facilities and works with modules inheritances, overload, ...
.. i18n:     * It's simpler, more explicit and uses less code
.. i18n:     * It's much more efficient as you will see in the following examples
.. i18n:     * Some fields do not directly correspond to a SQL field (e.g.: function fields in Python)

    * It uses objects facilities and works with modules inheritances, overload, ...
    * It's simpler, more explicit and uses less code
    * It's much more efficient as you will see in the following examples
    * Some fields do not directly correspond to a SQL field (e.g.: function fields in Python)

.. i18n: Example 2 - Prefetching
.. i18n: -----------------------

Example 2 - Prefetching
-----------------------

.. i18n: Suppose that later in the code, in another function, you want to access the name of the partner associated to your sale order. You can use this::
.. i18n: 
.. i18n:     partner_name = sale.partner_id.name

Suppose that later in the code, in another function, you want to access the name of the partner associated to your sale order. You can use this::

    partner_name = sale.partner_id.name

.. i18n: And this will not generate any SQL query as it has been prefetched by the object relational mapping engine of Open ERP.

And this will not generate any SQL query as it has been prefetched by the object relational mapping engine of Open ERP.

.. i18n: Loops and special fields
.. i18n: ------------------------

Loops and special fields
------------------------

.. i18n: Suppose now that you want to compute the totals of 10 sales order by countries. You can do this in Open ERP within a Open ERP object:

Suppose now that you want to compute the totals of 10 sales order by countries. You can do this in Open ERP within a Open ERP object:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def get_totals(self, cr, uid, ids):
.. i18n:        countries = {}
.. i18n:        for sale in self.browse(cr, uid, ids):
.. i18n:           country = sale.partner_invoice_id.country
.. i18n:           countries.setdefault(country, 0.0)
.. i18n:           countries[country] += sale.amount_untaxed
.. i18n:        return countries

.. code-block:: python

    def get_totals(self, cr, uid, ids):
       countries = {}
       for sale in self.browse(cr, uid, ids):
          country = sale.partner_invoice_id.country
          countries.setdefault(country, 0.0)
          countries[country] += sale.amount_untaxed
       return countries

.. i18n: And, to print them as a good way, you can add this on your object:

And, to print them as a good way, you can add this on your object:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def print_totals(self, cr, uid, ids):
.. i18n:        result = self.get_totals(cr, uid, ids)
.. i18n:        for country in result.keys():
.. i18n:           print '[%s] %s: %.2f' (country.code, country.name, result[country])

.. code-block:: python

    def print_totals(self, cr, uid, ids):
       result = self.get_totals(cr, uid, ids)
       for country in result.keys():
          print '[%s] %s: %.2f' (country.code, country.name, result[country])

.. i18n: The 2 functions will generate 4 SQL queries in total ! This is due to the SQL engine of Open ERP that does prefetching, works on lists and uses caching methods. The 3 queries are:

The 2 functions will generate 4 SQL queries in total ! This is due to the SQL engine of Open ERP that does prefetching, works on lists and uses caching methods. The 3 queries are:

.. i18n:    1. Reading the sale.order to get ID's of the partner's address
.. i18n:    2. Reading the partner's address for the countries
.. i18n:    3. Calling the amount_untaxed function that will compute a total of the sale order lines
.. i18n:    4. Reading the countries info (code and name)

   1. Reading the sale.order to get ID's of the partner's address
   2. Reading the partner's address for the countries
   3. Calling the amount_untaxed function that will compute a total of the sale order lines
   4. Reading the countries info (code and name)

.. i18n: That's great because if you run this code on 1000 sales orders, you have the guarantee to only have 4 SQL queries.

That's great because if you run this code on 1000 sales orders, you have the guarantee to only have 4 SQL queries.

.. i18n: Notes:

Notes:

.. i18n:     * IDS is the list of the 10 ID's: [12,15,18,34, ...,99]
.. i18n:     * The arguments of a function are always the same:
.. i18n: 
.. i18n:           - cr: the cursor database (from psycopg)
.. i18n:           - uid: the user id (for security checks)
.. i18n:     * If you run this code on 5000 sales orders, you may have 8 SQL queries because as SQL queries are not allowed to take too much memory, it may have to do two separate readings.

    * IDS is the list of the 10 ID's: [12,15,18,34, ...,99]
    * The arguments of a function are always the same:

          - cr: the cursor database (from psycopg)
          - uid: the user id (for security checks)
    * If you run this code on 5000 sales orders, you may have 8 SQL queries because as SQL queries are not allowed to take too much memory, it may have to do two separate readings.

.. i18n: A complete example
.. i18n: ------------------

A complete example
------------------

.. i18n: Here is a complete example, from the Open ERP official distribution, of the function that does bill of material explosion and computation of associated routings:

Here is a complete example, from the Open ERP official distribution, of the function that does bill of material explosion and computation of associated routings:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     class mrp_bom(osv.osv):
.. i18n:         ...
.. i18n:         def _bom_find(self, cr, uid, product_id, product_uom, properties=[]):
.. i18n:             bom_result = False
.. i18n:             # Why searching on BoM without parent ?
.. i18n:             cr.execute('select id from mrp_bom where product_id=%d and bom_id is null
.. i18n:                           order by sequence', (product_id,))
.. i18n:             ids = map(lambda x: x[0], cr.fetchall())
.. i18n:             max_prop = 0
.. i18n:             result = False
.. i18n:             for bom in self.pool.get('mrp.bom').browse(cr, uid, ids):
.. i18n:                 prop = 0
.. i18n:                 for prop_id in bom.property_ids:
.. i18n:                     if prop_id.id in properties:
.. i18n:                         prop+=1
.. i18n:                 if (prop>max_prop) or ((max_prop==0) and not result):
.. i18n:                     result = bom.id
.. i18n:                     max_prop = prop
.. i18n:             return result
.. i18n: 
.. i18n:             def _bom_explode(self, cr, uid, bom, factor, properties, addthis=False, level=10):
.. i18n:                 factor = factor / (bom.product_efficiency or 1.0)
.. i18n:                 factor = rounding(factor, bom.product_rounding)
.. i18n:                 if factor<bom.product_rounding:
.. i18n:                     factor = bom.product_rounding
.. i18n:                 result = []
.. i18n:                 result2 = []
.. i18n:                 phantom = False
.. i18n:                 if bom.type=='phantom' and not bom.bom_lines:
.. i18n:                     newbom = self._bom_find(cr, uid, bom.product_id.id,
.. i18n:                                             bom.product_uom.id, properties)
.. i18n:                     if newbom:
.. i18n:                         res = self._bom_explode(cr, uid, self.browse(cr, uid, [newbom])[0],
.. i18n:                               factor*bom.product_qty, properties, addthis=True, level=level+10)
.. i18n:                         result = result + res[0]
.. i18n:                         result2 = result2 + res[1]
.. i18n:                         phantom = True
.. i18n:                     else:
.. i18n:                         phantom = False
.. i18n:                 if not phantom:
.. i18n:                     if addthis and not bom.bom_lines:
.. i18n:                         result.append(
.. i18n:                         {
.. i18n:                             'name': bom.product_id.name,
.. i18n:                             'product_id': bom.product_id.id,
.. i18n:                             'product_qty': bom.product_qty * factor,
.. i18n:                             'product_uom': bom.product_uom.id,
.. i18n:                             'product_uos_qty': bom.product_uos and 
.. i18n:                                                bom.product_uos_qty * factor or False,
.. i18n:                             'product_uos': bom.product_uos and bom.product_uos.id or False,
.. i18n:                         })
.. i18n:                     if bom.routing_id:
.. i18n:                         for wc_use in bom.routing_id.workcenter_lines:
.. i18n:                             wc = wc_use.workcenter_id
.. i18n:                             d, m = divmod(factor, wc_use.workcenter_id.capacity_per_cycle)
.. i18n:                             mult = (d + (m and 1.0 or 0.0))
.. i18n:                             cycle = mult * wc_use.cycle_nbr
.. i18n:                             result2.append({
.. i18n:                                 'name': bom.routing_id.name,
.. i18n:                                 'workcenter_id': wc.id,
.. i18n:                                 'sequence': level+(wc_use.sequence or 0),
.. i18n:                                 'cycle': cycle,
.. i18n:                                 'hour': float(wc_use.hour_nbr*mult +
.. i18n:                                               (wc.time_start+wc.time_stop+cycle*wc.time_cycle) *
.. i18n:                                                (wc.time_efficiency or 1.0)),
.. i18n:                             })
.. i18n:                     for bom2 in bom.bom_lines:
.. i18n:                          res = self._bom_explode(cr, uid, bom2, factor, properties,
.. i18n:                                                      addthis=True, level=level+10)
.. i18n:                          result = result + res[0]
.. i18n:                          result2 = result2 + res[1]
.. i18n:                 return result, result2

.. code-block:: python

    class mrp_bom(osv.osv):
        ...
        def _bom_find(self, cr, uid, product_id, product_uom, properties=[]):
            bom_result = False
            # Why searching on BoM without parent ?
            cr.execute('select id from mrp_bom where product_id=%d and bom_id is null
                          order by sequence', (product_id,))
            ids = map(lambda x: x[0], cr.fetchall())
            max_prop = 0
            result = False
            for bom in self.pool.get('mrp.bom').browse(cr, uid, ids):
                prop = 0
                for prop_id in bom.property_ids:
                    if prop_id.id in properties:
                        prop+=1
                if (prop>max_prop) or ((max_prop==0) and not result):
                    result = bom.id
                    max_prop = prop
            return result

            def _bom_explode(self, cr, uid, bom, factor, properties, addthis=False, level=10):
                factor = factor / (bom.product_efficiency or 1.0)
                factor = rounding(factor, bom.product_rounding)
                if factor<bom.product_rounding:
                    factor = bom.product_rounding
                result = []
                result2 = []
                phantom = False
                if bom.type=='phantom' and not bom.bom_lines:
                    newbom = self._bom_find(cr, uid, bom.product_id.id,
                                            bom.product_uom.id, properties)
                    if newbom:
                        res = self._bom_explode(cr, uid, self.browse(cr, uid, [newbom])[0],
                              factor*bom.product_qty, properties, addthis=True, level=level+10)
                        result = result + res[0]
                        result2 = result2 + res[1]
                        phantom = True
                    else:
                        phantom = False
                if not phantom:
                    if addthis and not bom.bom_lines:
                        result.append(
                        {
                            'name': bom.product_id.name,
                            'product_id': bom.product_id.id,
                            'product_qty': bom.product_qty * factor,
                            'product_uom': bom.product_uom.id,
                            'product_uos_qty': bom.product_uos and 
                                               bom.product_uos_qty * factor or False,
                            'product_uos': bom.product_uos and bom.product_uos.id or False,
                        })
                    if bom.routing_id:
                        for wc_use in bom.routing_id.workcenter_lines:
                            wc = wc_use.workcenter_id
                            d, m = divmod(factor, wc_use.workcenter_id.capacity_per_cycle)
                            mult = (d + (m and 1.0 or 0.0))
                            cycle = mult * wc_use.cycle_nbr
                            result2.append({
                                'name': bom.routing_id.name,
                                'workcenter_id': wc.id,
                                'sequence': level+(wc_use.sequence or 0),
                                'cycle': cycle,
                                'hour': float(wc_use.hour_nbr*mult +
                                              (wc.time_start+wc.time_stop+cycle*wc.time_cycle) *
                                               (wc.time_efficiency or 1.0)),
                            })
                    for bom2 in bom.bom_lines:
                         res = self._bom_explode(cr, uid, bom2, factor, properties,
                                                     addthis=True, level=level+10)
                         result = result + res[0]
                         result2 = result2 + res[1]
                return result, result2
