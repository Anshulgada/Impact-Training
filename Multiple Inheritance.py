class Parent1():

    def __init__(self):
        super(Parent1, self).__init__()     # This will send the call to Parent2 as it is the other parent
        print("Parent 1 Init")            # & Print that Init first, then later come back here for this Init

    def func5(self):
        print("Parent 1 Function")

class Parent2():

    def __init__(self):
        print("Parent 2 Init")

    def func6(self):
        print("Parent 2 Function")

class derived3(Parent1, Parent2):
    def __init__(self):
        super(derived3,self).__init__()     # Works even without param inside super()
        print("Child Class - Multiple parents (Multiple Inheritance)")

    # def func7(self):
    # pass

d3 = derived3()
# d3.func5()          # Parent Class 1        # Init is only called by first parent in parameter
# d3.func6()          # Parent Class 2        # Here Init is not called, only defined function is called
# d3.func7()          # Child Class
