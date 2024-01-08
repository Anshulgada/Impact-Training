class Parent:
    def func1 (self):
        print("Parent")

class Child(Parent):
    def func1 (self):
        print("Child")                  # Super here also works without parameters
        super(Child, self).func1()      # Super takes it to Parent class


P = Parent()
P.func1()       # Direct Parent class function is called

C = Child()     # When super class is set inside Child, it will print both Child and Parent
C.func1()     # Parent & Child both have the same function name so it only prints Child Function