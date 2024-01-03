# a = 10        # Normally printing each calc
# b = 10
#
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
#
# print()
#
# def calc():              # Defining a func to calculate
#     a = int(input("Enter num 1: "))
#     b = int(input("Enter num 2: "))
#     print()
#     print("Add: ", a + b)
#     print("Sub: ", a - b)
#     print("Mul: ", a * b)
#     print("Div: ", a / b)
#
# # Instead of printing again use calc function
# calc()

################################################

# def name():
#     print("Anshul")
#
# print("Hi", name())
#
# This function prints ==>
# Anshul
# Hi None
#
# Reason ==>
# Func calls occurs first so 'Anshul' is printed
# Then again it goes to print 'Hi'
# Then upon going to func call there is no return therefore returns 'None'
# Therefore we need to do ==>
#
# def name():
#     return "Anshul"
#
# Output ==>
# Hi Anshul
#
################################################

# Keyword Arguments ==>
# def func_add(a, b):
#     return a + b       # if using return here then need to print func call
#
# print(func_add(b = 10, a = 10))


a = 10
b = 5
def fun():
    global a      # This makes the variable change globally and not internally
    a = 2
    a = 12
    b = 11       # This is only internal so values will be diff
    print("In function", a, b)

fun()
print("Out of func", a, b)