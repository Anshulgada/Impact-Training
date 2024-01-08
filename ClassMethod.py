class Student:
    # b = 20
    # def fun1(self, a):
    #     print(f"Hi", a)
    #
    # @classmethod
    # def fun2(cls, b):
    #     print(f"Hi", b)

    def __init__(self,a):
        self.a = a
        self.i = self.Students

    class Students:
        b = 20

s = Student(10)
# print(Student.Students.b)
i1 = s.i
i2 = s.i
print(i2.b)

# s.fun1(12)
# Student.fun2(Student.b)