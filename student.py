"""
The instruction of the challenge :

Implement a class named Person and two subclasses of Person named Student and Employee.  Make FacultyMember and StaffMember subclasses of Employee.  

A person has a name, address, phone number, and e-mail address. 

A student has a class status (freshman, sophomore, junior and senior).  

Override the toString method in each class to display the class name and the person’s name.

"""
from person import Person

class Student(Person):
    def __init__(self, name, adress, phonenumber, emailadress,classstatus):
        super().__init__(name, adress, phonenumber, emailadress)
        self.class_status = classstatus
    
    def __str__(self):
        print("Class Name :  " + self.__class__.__name__ + "  --  Person's Name :  " + self.name)
        return "Class Name :  " + self.__class__.__name__ + "  --  Person's Name :  " + self.name

    
    

