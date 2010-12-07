
.. index::
   single: recruitments
..

Hire New People
===============

Using OpenERP you can efficiently manage the process of hiring the new people for your organization.
It is a well managed  recruitment process of applicant from initial stage to hiring the applicant.

Recruitments
------------

.. index::
   single: module; hr_recruitment

You need to install :mod:`hr_recruitment` module to efficiently managed  recruitment process.
The configuration wizard to install this module is shown below.

.. figure::  images/config_wiz_recruitment.png
   :scale: 50
   :align: center

   *Configuration wizard to install hr_recruitment module*

The :guilabel:`Applicant` form can be seen from the menu :menuselection:`Human Resources --> Recruitment --> Applicants`.

.. figure::  images/recruitment_applicant_form.png
   :scale: 50
   :align: center

   *Applicant recruitment form*

You can manage following information using applicant form.

* Applicant's Name
* Applied Job
* Department
* Stage : It may be  `Initial Job Demand` or  `Salary Negotiation` stage
* Responsible : Responsible person who conduct the interview
* Contact Information
* Contract Data : That contains Availability, Expected Salary, Proposed Salary
* Qualification of Applicant
* Status : It reflects the actual state of the recruitment process like `In Progress`, `Pending` or `Hired`

Initially the applicant states is `New` after that it can be converted into `In Progress`.
If the applicant is at one of the different stages like it may be in `Waiting for approval by human resource department` or `Waiting for offer acceptance by applicant`,
in these cases applicant states should be `Pending`. When the status is `Hired`, you can find that applicant from the list of employees.

The information about the :guilabel:`Job Position` can be maintained by the menu :menuselection:`Human Resources --> Recruitment --> Job Positions`.

.. figure::  images/recruitment_job_position.png
   :scale: 50
   :align: center

   *Job position in organization*

The key features of OpenERP for the process of hiring the new people using :mod:`hr_recruitment` module.

* Manages job positions and the recruitement process.
* It's integrated with the `survey` module to allow you to define interview for different jobs.
* This module is integrated with the mail gateway to automatically tracks email
  sent to jobs@yourcompany.com.
* It's also integrated with the document management system to store and search in your CV base.

You can analyse data of recruitment process through the menu :menuselection:`Human Resources --> Reporting --> Recruitment Analysis`.

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
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