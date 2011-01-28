
.. index::
   single: recruitments
..

Hire New People
===============

Using OpenERP, you can efficiently manage the process of hiring new people for your organization.
It is a well managed recruitment process from initial contact to hiring the applicant.

Recruitments
------------

.. index::
   single: module; hr_recruitment

You need to install :mod:`hr_recruitment` module to efficiently manage the recruitment process.
The configuration wizard to install this module is shown below:

.. figure::  images/config_wiz_recruitment.png
   :scale: 75
   :align: center

   *Configuration wizard to install hr_recruitment module*

The :guilabel:`Applicants` form can be seen from the menu :menuselection:`Human Resources --> Recruitment --> Applicants`.

.. figure::  images/recruitment_applicant_form.png
   :scale: 75
   :align: center

   *Applicant recruitment form*

You can manage the following information using the Applicants form:

* :guilabel:`Applicant's Name`
* :guilabel:`Applied Job`
* :guilabel:`Department`
* :guilabel:`Stage`: can be ``Initial Job Demand``, ``Salary Negotiation``, ...
* :guilabel:`Responsible`: Responsible person who conducts the interview
* :guilabel:`Contact` information
* :guilabel:`Contract Data`: including Availability, Expected Salary, Proposed Salary
* :guilabel:`Qualification` of the applicant
* :guilabel:`State`: reflects the actual status of the recruitment process like ``New``, ``In Progress``, ``Pending``, ``Refused`` or ``Hired``

Initially, the applicant state is ``New``, after that it can be converted to ``In Progress``.
If the applicant is at one of the different stages like it may be in `Waiting for approval by human resource department` or `Waiting for offer acceptance by applicant`,
in these cases applicant states should be ``Pending``. When the status is ``Hired``, you can find that applicant from the list of employees.

The information about the :guilabel:`Job Position` can be maintained by the menu :menuselection:`Human Resources --> Recruitment --> Job Positions`.

.. figure::  images/recruitment_job_position.png
   :scale: 75
   :align: center

   *Job Positions in the organization*

The key features of OpenERP for the process of hiring new people using :mod:`hr_recruitment` module are:

* It manages job positions and the recruitment process.
* It is integrated with the `survey` module to allow you to define interviews for different jobs.
* This module is integrated with the mail gateway to automatically track emails
  sent to jobs@yourcompany.com.
* It is also integrated with the document management system to store in and search your CV base.

You can analyse data of recruitment process through the menu :menuselection:`Human Resources --> Reporting --> Recruitment Analysis`.


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
