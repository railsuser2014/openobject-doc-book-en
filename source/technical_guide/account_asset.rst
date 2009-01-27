
Module Asset management (*account_asset*)
=========================================
:Module: account_asset
:Name: Asset management
:Version: 5.0.1.0
:Directory: account_asset
:Web: http://tinyerp.com/module_account.html

Description
-----------

::

  Financial and accounting asset management.
      Allows to define
      * Asset category. 
      * Assets.
      *Asset usage period and property.

Dependencies
------------

 * account - installed
 * account_simulation - installed

Reports
-------

None


Menus
-------

 * Financial Management/Periodical Processing/Compute assets
 * Financial Management/Configuration/Assets
 * Financial Management/Configuration/Assets/Asset Category
 * Financial Management/Configuration/Assets/Asset
 * Financial Management/Assets
 * Financial Management/Assets/Asset Hierarchy
 * Financial Management/Assets/Assets
 * Financial Management/Assets/Assets/Draft Assets
 * Financial Management/Assets/Assets/Open Assets

Views
-----

 * account.asset.category.form (form)
 * account.asset.category.tree (tree)
 * account.asset.property.tree (tree)
 * account.asset.asset.form (form)
 * account.asset.property.history.form (form)
 * account.asset.property.history.tree (tree)
 * account.asset.board.form (form)
 * account.asset.board.tree (tree)
 * account.asset.asset.tree (tree)
 * \* INHERIT account.invoice.line.form (form)


Objects
-------

Object: Asset category
######################

.. index::
  single: Asset category object
.. 


:note: Note, text



.. index::
  single: note field
.. 




:code: Asset code, char



.. index::
  single: code field
.. 




:name: Asset category, char, required



.. index::
  single: name field
.. 



Object: Asset
#############

.. index::
  single: Asset object
.. 


:property_ids: Asset method name, one2many, readonly



.. index::
  single: property_ids field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:code: Asset code, char



.. index::
  single: code field
.. 




:name: Asset, char, required



.. index::
  single: name field
.. 




:sequence: Sequence, integer



.. index::
  single: sequence field
.. 




:child_ids: Childs asset, one2many



.. index::
  single: child_ids field
.. 




:entry_ids: Entries, one2many, readonly



.. index::
  single: entry_ids field
.. 




:localisation: Localisation, char



.. index::
  single: localisation field
.. 




:date: Date, date, required



.. index::
  single: date field
.. 




:state: Global state, selection, required



.. index::
  single: state field
.. 




:period_id: Period, many2one, required, readonly



.. index::
  single: period_id field
.. 




:parent_id: Parent asset, many2one



.. index::
  single: parent_id field
.. 




:value_total: Total value, float, readonly



.. index::
  single: value_total field
.. 




:active: Active, boolean



.. index::
  single: active field
.. 




:category_id: Asset category, many2one



.. index::
  single: category_id field
.. 




:partner_id: Partner, many2one



.. index::
  single: partner_id field
.. 



Object: Asset property
######################

.. index::
  single: Asset property object
.. 


:asset_id: Asset, many2one, required



.. index::
  single: asset_id field
.. 




:board_ids: Asset board, one2many



.. index::
  single: board_ids field
.. 




:entry_asset_ids: Asset Entries, many2many



.. index::
  single: entry_asset_ids field
.. 




:history_ids: History, one2many, readonly



.. index::
  single: history_ids field
.. 




:method_progress_factor: Progressif factor, float, readonly



.. index::
  single: method_progress_factor field
.. 




:method_end: Ending date, date



.. index::
  single: method_end field
.. 




:account_asset_id: Asset account, many2one, required



.. index::
  single: account_asset_id field
.. 




:journal_id: Journal, many2one, required



.. index::
  single: journal_id field
.. 




:method: Computation method, selection, required, readonly



.. index::
  single: method field
.. 




:journal_analytic_id: Analytic journal, many2one



.. index::
  single: journal_analytic_id field
.. 




:date: Date created, date



.. index::
  single: date field
.. 




:method_time: Time method, selection, required, readonly



.. index::
  single: method_time field
.. 




:state: State, selection, required



.. index::
  single: state field
.. 




:method_period: Period per interval, integer, readonly



.. index::
  single: method_period field
.. 




:value_residual: Residual value, float, readonly



.. index::
  single: value_residual field
.. 




:value_total: Gross value, float, readonly



.. index::
  single: value_total field
.. 




:account_analytic_id: Analytic account, many2one



.. index::
  single: account_analytic_id field
.. 




:account_actif_id: Depreciation account, many2one, required



.. index::
  single: account_actif_id field
.. 




:type: Depr. method type, selection, required



.. index::
  single: type field
.. 




:method_delay: Number of interval, integer, readonly



.. index::
  single: method_delay field
.. 




:name: Method name, char



.. index::
  single: name field
.. 



Object: Asset history
#####################

.. index::
  single: Asset history object
.. 


:user_id: User, many2one, required



.. index::
  single: user_id field
.. 




:name: History name, char



.. index::
  single: name field
.. 




:method_end: Ending date, date



.. index::
  single: method_end field
.. 




:asset_property_id: Method, many2one, required



.. index::
  single: asset_property_id field
.. 




:note: Note, text



.. index::
  single: note field
.. 




:method_delay: Number of interval, integer



.. index::
  single: method_delay field
.. 




:method_period: Period per interval, integer



.. index::
  single: method_period field
.. 




:date: Date, date, required



.. index::
  single: date field
.. 



Object: Asset board
###################

.. index::
  single: Asset board object
.. 


:asset_id: Asset, many2one, required



.. index::
  single: asset_id field
.. 




:value_gross: Gross value, float, required



.. index::
  single: value_gross field
.. 




:value_asset_cumul: Cumul. value, float, required



.. index::
  single: value_asset_cumul field
.. 




:name: Asset name, char, required



.. index::
  single: name field
.. 




:value_asset: Asset Value, float, required



.. index::
  single: value_asset field
.. 




:value_net: Net value, float, required



.. index::
  single: value_net field
.. 

