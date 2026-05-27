# Code I Super

class A:
    def __init__(self):
        print("super class A constructor")

class B(A):
    def __init__(self):
        print("child class B Constructor")
        super().__init__()

b=B()

# Code II Super II

class A:
    def m1(self):
        print("Super Class A:m1 method")

class B(A):
    def m1(self):
        print("Child class B:m1 method")
        super().m1()

b=B()
b.m1()

# Code III Overloading

class Demo:
    def m1(self):
        print('no arg method')
    def m1(self, a):
        print('one arg method')
    def m1(self, a, b):
        print('two arg method')

d=Demo()
# d.m1() # -> error
# d.m1(10) # -> error
d.m1(10,20) # -> Sucsess

# Code IV Overiding

class Parent():
    def __init__(self):
        self.value = "Inside Parent"

    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Inside Child"

    def show(self):
        print(self.value)

#Driver
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

# Code V Abstract

from abc import *

class Demo1(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    def m3(self):
        print("Implemented Method")