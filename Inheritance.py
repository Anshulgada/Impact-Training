# class Student:
#     def details(self,name,age,address):
#         print("From Student:")
#         print(name,age,address)
# class Teacher(Student):     # Class Teacher inherited class Student
#     print("From Teacher: ")
#
# T = Teacher()
# T.details("Anshul",20,"Mumbai")


class Base:
    def func1(self):
        return "F1"
        # print("F1")

    def func2(self):
        print("F2")

class derived1(Base):
    def func3(self):
        print("F3")
    def func4(self):
        print("F4")

class derived2(derived1):
    def func4(self):
        print("F5")
        # super().func4()   # Prints F5 and then F4 as super() sends it to 'derived' class

# d = derived1()
# print("Together:", d.func1(), d.func2(), d.func3())
# print("\nDifferent:")
# print(d.func1())
# print(d.func2())
# print(d.func3())

d2 = derived2()     # Will only go to above class if it has super() func used
d2.func4()       # Prints F5 not F4 as derived2 already has a func func4 so it doesn't go to derived class