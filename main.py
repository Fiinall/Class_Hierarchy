"""
The instruction of the challenge :

Implement a class named Person and two subclasses of Person named Student and Employee.  Make FacultyMember and StaffMember subclasses of Employee.  

A person has a name, address, phone number, and e-mail address. 

A student has a class status (freshman, sophomore, junior and senior).  

An employee has an office, salary, and date-hired. 


A faculty member has office hours and a rank.  

A staff member has a title.  

Override the toString method in each class to display the class name and the person’s name.

Write a test program that creates a Person, Student, Employee, Faculty, and Staff, and calls their toSting() methods.

""" 

from employee import Employee
from student import *
from facultymember import FacultyMember
from staffmember import StaffMember

person1 = Person("Fatih","istanbul","9323","fatih@gmail.com")

studen1 = Student("Aleyna","Bursa","3900","aleyna@gmail.com","sophomore")

employee1 = Employee("Alperen","London","6701","alpren@gmail.com","Wise","£6000","2020")

facultymember1 = FacultyMember("Professor1","Cambridge","1000","pro@gmail.com","Campus","£8000","2010","3-5 p.m.","professor")

staffmember1 = StaffMember("Staff1","Cambridge","1001","stuff@gmail.com","Kitchen Compartment","£4000","2015","Chef")

person1.__str__()
studen1.__str__()
employee1.__str__()
facultymember1.__str__()
staffmember1.__str__()



