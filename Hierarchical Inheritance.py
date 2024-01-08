class Parent():

    def __init__(self):
        super(Parent, self).__init__()
        print("Parent Init")

class Child1(Parent):

    def __init__(self):                   # Parent Init is called because super is called
        super(Child1,self).__init__()     # Works even without param inside super()
        print("Child 1 Init")


class Child2(Parent):
    def __init__(self):
        # super().__init__()            # No Parent Init called when this Child is called
        print("Child 2 Init")


C1 = Child1()
C2 = Child2()