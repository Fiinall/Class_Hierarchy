"""
The instruction of the challenge :

Implement a class named Person and two subclasses of Person named Student and Employee.  Make FacultyMember and StaffMember subclasses of Employee.  

A person has a name, address, phone number, and e-mail address. 

A student has a class status (freshman, sophomore, junior and senior).  

An employee has an office, salary, and date-hired. 


A faculty member has office hours and a rank.  

A staff member has a title.  

Override the toString method in each class to display the class name and the person’s name.

"""

from employee import Employee

class StaffMember(Employee):
    def __init__(self, name, adress, phonenumber, emailadress, office, salary, dateofhiring,title):
        super().__init__(name, adress, phonenumber, emailadress, office, salary, dateofhiring)
        self.title = title

    def __str__(self):
        print("Class Name :  " + self.__class__.__name__ + "  --  Person's Name :  " + self.name)
        return "Class Name :  " + self.__class__.__name__ + "  --  Person's Name :  " + self.name
