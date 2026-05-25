class A:
    def __init__(self):
        print("super class A constructor")

class B(A):
    def __init__(self):
        print("child class B Constructor")
        super().__init__()

b=B()

class A:
    def m1(self):
        print("Super Class A:m1 method")

class B(A):
    def m1(self):
        print("Child class B:m1 method")
        super().m1()

b=B()
b.m1()