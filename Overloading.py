class Ov:
    def func1(self, a=None, b=None):

        if a is not None and b is not None:
            print (a + b)

        elif a is not None:
            print(a)

        else:
            print("No Input")

a1 = Ov()
a1.func1()
a1.func1(10)
a1.func1(10, 20)