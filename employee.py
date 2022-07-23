"""
The instruction of the challenge :

Implement a class named Person and two subclasses of Person named Student and Employee.  Make FacultyMember and StaffMember subclasses of Employee.  

A person has a name, address, phone number, and e-mail address. 

An employee has an office, salary, and date-hired. 

Override the toString method in each class to display the class name and the person’s name.

"""

from person import Person

class Employee(Person):

    def __init__(self, name, adress, phonenumber, emailadress,office,salary,dateofhiring):
        super().__init__(name, adress, phonenumber, emailadress)
        self.office = office 
        self.salary = salary
        self.date_hired = dateofhiring # I'm using different strings in order to see the words doesn't have to be the same in ''self.___ = ___'' And understand their meanings.

    def __str__(self):
        print("Class Name :  " + self.__class__.__name__ + "  --  Person's Name :  " + self.name)
        return "Class Name :  " + self.__class__.__name__ + "  --  Person's Name :  " + self.name
