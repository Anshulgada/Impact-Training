# # # Function Overloading
# class FuncOver:
#     def func1(self, a=None, b=None):
#
#         if a is not None and b is not None:
#             print (a + b)
#
#         elif a is not None:
#             print(a)
#
#         else:
#             print("No Input")
#
# a1 = FuncOver()
# a1.func1()
# a1.func1(10)
# a1.func1(10, 20)



# # Operator Overloading
# E.g.
# If two integers are added then normal addition    1 + 2 ==> 3
# If two strings are added then concatenation      '1' + '2' ==> 12

class OpOver:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):        # Defines the behaviour of the '+' operator
        # return
        return f"{self.x + other.x} + {self.y + other.y}"

    def __sub__(self,other):        # Defines the behaviour of the '-' operator
        # return
        return f"{self.x - other.x} - {self.y - other.y}"

    def __mul__(self,other):        # Defines the behaviour of the '*' operator
        # return
        return f"{self.x * other.x} * {self.y * other.y}"

    def __truediv__(self,other):        # Defines the behaviour of the '/' operator
        # return
        return f"{self.x - other.x} / {self.y - other.y}"

    def __mod__(self,other):        # Defines the behaviour of the '%' operator
        # return
        return f"{self.x % other.x} % {self.y % other.y}"


    # __eq__ for checking equality (==)
    # __ne__ for checking inequality (!=)
    # __str__ for checking the string representation

c1 = OpOver(1,5)
c2 = OpOver(3,4)

a = c1 + c2     # c1 + c2 ==> '1 + 3' + '5 + 4'         # 'x.c1 + x.c2' + 'y.c1 + y.c2'
print (a)       # Returns Strings c1 & c2 ==> '4 + 9'
print(type(a))  # Type a ==> 'str'

b = c1 - c2
print (b)
print (type(b))

d = c1 * c2
print (d)
print (type(d))

e = c1 / c2
print (e)
print (type(e))

f = c1 % c2
print (f)
print (type(f))