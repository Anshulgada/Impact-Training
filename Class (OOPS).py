class Student:
    # name = 'Anshul'
    # age = 20

    # def __init__(self):
    #     self.age = None
    #     self.name = None

    batch = 2024    # Class attribute ==> accessible as both a property of the class and as a property of objects
    def value(self, name, age):
        self.name = name          # Object Attribute ==> only accessible from the scope of an object
        self.age = age

    def show(self):
        print(self.name, self.age)      # Takes name and age from value function using self argument

    class batch1:
        name = "Ganesha"


print()

objA = Student()
objB = Student()

# print("ObjA object ID: ", objA)                 # prints object id
# print("ObjA object type: ", type(objA))         # prints object type
# print("'name' var: ", objA.name)        # prints name variable from inside class
# print("'age' var: ", objA.age)          # prints age variable from inside class
#
# print( f"\nName: {objA.name} \nAge: {objA.age}" )       # prints name and age using f-string

# Student.value("Anshul", 21 )    # prints name and age when using className directly when self isn't declared
# But when self is declared it takes name input as self and age input as age
# error ==> Student.value() missing 1 required positional argument: 'age'

# Will not print as self takes the name arg and age takes the str inputted
# Only works when function has self argument declared in argument
# objB.value("Anshul", 25)          # error ==> Student.value() takes 2 positional arguments but 3 were given

objA.value("Anshul", 20)
objB.value("Ansh", 25)      # Will not print as it is not called using show(), only objA is called
objA.show()                         # prints name and age from value function called above
Student.show(objA)       # Also prints name and age as we used className but used objName as arg in show function
print("Batch: ", Student.batch)        # batch is class attribute so can be accessed by objects or directly by class
print(Student.batch1.name)       # printing name from one class which is inside another class

objC = Student.batch1()         # Instead of using Student.batch1() everytime we can assign it to an object
print("Batch: ", objC.name)     # and use that whenever we need to print something from that class