# rewrite code from lecturer (basic python typing practice)
# hopefully if i can be good at python :)

#CODE 1 INHERIT TYPES
class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name
    
    # To check if this person is an employee
    def isEmployee(self):
        return False
    
# Inheritated or Subclass (Note Person in bracket)
class Employee(Person):

    # Return true here
    def isEmployee(self):
        return True
    
# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") #An Object of Employee
print(emp.getName(), emp.isEmployee())


#CODE 2 SUPER FUNCTION

# parent class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def display(self):
        print(self.name, self.age)

# child class
class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = 