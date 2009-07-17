
.. i18n: Dashboard 
.. i18n: =========

Dashboard 
=========

.. i18n: Open ERP objects can be created from PostgreSQL views. The technique is as follows :

Open ERP objects can be created from PostgreSQL views. The technique is as follows :

.. i18n:    1. Declare your _columns dictionary. All fields must have the flag **readonly=True.**
.. i18n:    2. Specify the parameter **_auto=False** to the Open ERP object, so no table corresponding to the _columns dictionnary is created automatically.
.. i18n:    3. Add a method **init(self, cr)** that creates a *PostgreSQL* View matching the fields declared in _columns. 

   1. Declare your _columns dictionary. All fields must have the flag **readonly=True.**
   2. Specify the parameter **_auto=False** to the Open ERP object, so no table corresponding to the _columns dictionnary is created automatically.
   3. Add a method **init(self, cr)** that creates a *PostgreSQL* View matching the fields declared in _columns. 

.. i18n: **Example** The object report_crm_case_user follows this model.

**Example** The object report_crm_case_user follows this model.

.. i18n: .. code-block:: python 
.. i18n: 
.. i18n:      class report_crm_case_user(osv.osv):
.. i18n: 	_name = "report.crm.case.user"
.. i18n: 	_description = "Cases by user and section"
.. i18n: 	_auto = False
.. i18n: 	 _columns = {
.. i18n: 	'name': fields.date('Month', readonly=True),
.. i18n: 	'user_id':fields.many2one('res.users', 'User', readonly=True, relate=True),
.. i18n: 	'section_id':fields.many2one('crm.case.section', 'Section', readonly=True, relate=True),
.. i18n: 	'amount_revenue': fields.float('Est.Revenue', readonly=True),
.. i18n: 	   'amount_costs': fields.float('Est.Cost', readonly=True),
.. i18n: 	'amount_revenue_prob': fields.float('Est. Rev*Prob.', readonly=True),
.. i18n: 	'nbr': fields.integer('# of Cases', readonly=True),
.. i18n: 	   'probability': fields.float('Avg. Probability', readonly=True),
.. i18n: 	'state': fields.selection(AVAILABLE_STATES, 'State', size=16, readonly=True),
.. i18n: 	'delay_close': fields.integer('Delay to close', readonly=True),
.. i18n: 	}
.. i18n: 	 _order = 'name desc, user_id, section_id'
.. i18n: 
.. i18n: 	def init(self, cr):
.. i18n: 	cr.execute("""
.. i18n: 	     create or replace view report_crm_case_user as (
.. i18n: 		 select
.. i18n: 		     min(c.id) as id,
.. i18n: 		     substring(c.create_date for 7)||'-01' as name,
.. i18n: 		     c.state,
.. i18n: 		     c.user_id,
.. i18n: 		     c.section_id,
.. i18n: 		     count(*) as nbr,
.. i18n: 		     sum(planned_revenue) as amount_revenue,
.. i18n: 		     sum(planned_cost) as amount_costs,
.. i18n: 		     sum(planned_revenue*probability)::decimal(16,2) as amount_revenue_prob,
.. i18n: 		     avg(probability)::decimal(16,2) as probability,
.. i18n: 		     to_char(avg(date_closed-c.create_date), 'DD"d" `HH24:MI:SS') as delay_close
.. i18n: 		 from
.. i18n: 		     crm_case c
.. i18n: 		 group by substring(c.create_date for 7), c.state, c.user_id, c.section_id
.. i18n: 	)""")
.. i18n: 	report_crm_case_user()

.. code-block:: python 

     class report_crm_case_user(osv.osv):
	_name = "report.crm.case.user"
	_description = "Cases by user and section"
	_auto = False
	 _columns = {
	'name': fields.date('Month', readonly=True),
	'user_id':fields.many2one('res.users', 'User', readonly=True, relate=True),
	'section_id':fields.many2one('crm.case.section', 'Section', readonly=True, relate=True),
	'amount_revenue': fields.float('Est.Revenue', readonly=True),
	   'amount_costs': fields.float('Est.Cost', readonly=True),
	'amount_revenue_prob': fields.float('Est. Rev*Prob.', readonly=True),
	'nbr': fields.integer('# of Cases', readonly=True),
	   'probability': fields.float('Avg. Probability', readonly=True),
	'state': fields.selection(AVAILABLE_STATES, 'State', size=16, readonly=True),
	'delay_close': fields.integer('Delay to close', readonly=True),
	}
	 _order = 'name desc, user_id, section_id'

	def init(self, cr):
	cr.execute("""
	     create or replace view report_crm_case_user as (
		 select
		     min(c.id) as id,
		     substring(c.create_date for 7)||'-01' as name,
		     c.state,
		     c.user_id,
		     c.section_id,
		     count(*) as nbr,
		     sum(planned_revenue) as amount_revenue,
		     sum(planned_cost) as amount_costs,
		     sum(planned_revenue*probability)::decimal(16,2) as amount_revenue_prob,
		     avg(probability)::decimal(16,2) as probability,
		     to_char(avg(date_closed-c.create_date), 'DD"d" `HH24:MI:SS') as delay_close
		 from
		     crm_case c
		 group by substring(c.create_date for 7), c.state, c.user_id, c.section_id
	)""")
	report_crm_case_user()
