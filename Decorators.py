# Decorators


# def add(x, y):          # Base function which adds
#     return x + y
# def subtract(x, y):     # Base function which subtracts
#     return x - y
# def multiply(x, y):     # Base function which multiplies
#     return x * y
# def divide(x, y):       # Base function which divides
#     return x / y
#
# def calculate(func, x, y):    # Main function which takes a function as arg and returns that function
#     return func(x, y)
#
# result_add = calculate(add, 4, 6)
# print("Add: ", result_add)  # prints 10         # Using a variable
#
# print("Sub: ", calculate(subtract, 6, 4))   # prints 2
# print("Mul: ", calculate(multiply, 4, 6))   # prints 24
# print("Div: ", calculate(divide, 6, 4))     # prints 1.5


# def my_decorator(pos_arg):
#     def wrapper():
#         print("\nSomething is happening before the function call")
#         pos_arg()       # goes to the function we called
#         print("Something is happening after the function call\n")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("This is hello function")
#
# say_hello()

# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
#
# result = outer_function(10)     # ==> outer_function takes value of 10
# print(result(5))                # ==> inner_function takes value of 5

