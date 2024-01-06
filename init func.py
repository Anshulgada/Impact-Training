class Student:
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        # print("Hello world!")

    def add(self, self2):
        if self.a1 > self2.a1:
            print("S1 > S2")
            # return self.a1 + self2.a1
        else:
            return "S2 > S1"
            # return self.b1 + self2.b1

S1 = Student(10, 12)
S2 = Student(20, 15)

S3 = Student(100, 12)
S4 = Student(50, 15)

print(S1.add(S2))
S3.add(S4)
