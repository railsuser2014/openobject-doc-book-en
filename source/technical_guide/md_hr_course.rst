
Pilot Human Resources (*md_hr_course*)
======================================
:Module: md_hr_course
:Name: Pilot Human Resources
:Version: 5.0.1.0
:Directory: md_hr_course
:Web: http://tinyerp.com/module_hr.html

Description
-----------

::

  None

Dependencies
------------

 * hr - installed

Reports
-------

None


Menus
-------

 * Human Resources
 * Human Resources/Courses
 * Human Resources/Courses/Courses
 * Human Resources/Courses/Courses by Employee

Views
-----

 * md.hr.course.form (form)
 * md.hr.course.tree (tree)
 * md.hr.course.student.form (form)
 * md.hr.course.student.tree (tree)


Objects
-------

Object: Course
##############



:code: Code, char, required





:name: Course title, char, required




Object: Course Student
######################



:payback_clause_ends: Pay back clause ends, date





:employee_id: Employee, many2one





:amount: Amount, float





:personal_contribution: Personal Contribution, boolean





:state: State, selection





:payback_clause: Pay back clause (in %), float





:date: Date followed, date





:course_id: Course, many2one


