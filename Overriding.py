class Parent:
    # def func1 (self):         # Use when trying to use super in Child class
    #     print("Parent")

    def call(self):
        print("Parent called")

class Child:             # To run the super statement below, add Parent class as parameter to Child class
    # def func1 (self):
    #     print("Child")                  # Super here also works without parameters
    #     super(Child, self).func1()      # Super takes it to Parent class

    def call(self, s):
        s.call()


P = Parent()
# P.func1()       # Direct Parent class function is called

C = Child()     # When super class is set inside Child, it will print both Child and Parent
# C.func1()     # Parent & Child both have the same function name, so it only prints Child Function

C.call(P)     # Makes call to Child function call which in turn calls Parent