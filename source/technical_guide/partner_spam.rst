
SMS and Email spam to partner (*partner_spam*)
==============================================
:Module: partner_spam
:Name: SMS and Email spam to partner
:Version: 5.0.1.0
:Directory: partner_spam
:Web: www.zikzakmedia.com

Description
-----------

::

  Improved SMS and Email spam to partner:
    * Spam to partners and to partner.address (contacts)
    * Choice to spam all partner addresses or partner default addresses
    * The email field can contain several email addresses separated by ,
    * A maximum of 3 files can be attached to emails
    * Clickatell gateway to send SMS can be configured by http or by email
    * The spam text can include special [[field]] tags to create personalized messages (they will be replaced to the the corresponding values of each partner contact):
        [[partner_id]] -> Partner name
        [[name]] -> Contact name
        [[function]] -> Function
        [[title]] -> Title
        [[street]] -> Street
        [[street2]] -> Street 2
        [[zip]] -> Zip code
        [[city]] -> City
        [[state_id]] -> State
        [[country_id]] -> Country
        [[email]] -> Email
        [[phone]] -> Phone
        [[fax]] -> Fax
        [[mobile]] -> Mobile
        [[birthdate]] -> Birthday

Dependencies
------------

 * base - installed

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
