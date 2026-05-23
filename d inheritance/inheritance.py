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


#CODE II SUPER FUNCTION

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
        self.sAge = age
        #inheriting the property
        super().__init__("Rahul", age)

    def displayInfo(self):
        print(self.sName, self.sAge)

obj = Student("Mayang", 200)
obj.display()
obj.displayInfo()

#CODE 3 SINGLE INHERITANCE

# Base class
class Parent:
    def func1(self): #define function
        print("This function is in parent class")

# derived class (kelas asal)

class Child(Parent):
    def func2(self):
        print("This function is in child class")

# Driver's code 
object = Child()
object.func1()
object.func2()

# CODE IV MULTIPLE INHERITANCE

#Base class 1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

#Base class 2

class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    sonname = ""

    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

#optional from writer (me)

    def child(self):
        print("Son :", self.sonname)

#Driver's Code -> kode buat manggil semuanya
s1 = Son()
s1.fathername = "SUKI"
s1.mothername = "LIAR"
s1.sonname = "SUKILIAR"
s1.parents()

# CODE V MULTILEVEL INHERITANCE

class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Fathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        Grandfather.__init__(self, grandfathername) # calling grandfather

# child

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        Father.__init__(self, fathername, grandfathername)
    
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

# Driver code (Running the code)
s1 = Son('Prince', 'Rampal', 'Suki')
print(s1.grandfathername)
s1.print_name()

# Code IV Hierarical Inherit
# Similar to Single Inherit Code's

# Base class
class Parent:
    def func1(self):
        print("This function is parent class.")

class Child1(Parent):
    def func2(self):
        print("This is child 1")

class Child2(Parent):
    def func3(self):
        print("This function is in child 3")

# Driver Code (Running Code)

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

# CODE VII HYBRID INHERIT

class School:
    def func1(self):
        print("This function rayka goblok")

class Student1(School):
    def func2(self):
        print("Student 1")

class Student2(School):
    def func3(self):
        print("Student 2")

class Student3(Student1, School):
    def func4(self):
        print("This function is student 3.")

# Driver code
object = Student3()
object.func1()
object.func2()