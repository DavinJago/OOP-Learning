class A:
    def __init__(self):
        print("super class A constructor")

class B(A):
    def __init__(self):
        print("child class B Constructor")
        super().__init__()

b=B()

