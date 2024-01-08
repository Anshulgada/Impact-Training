from abc import ABC, abstractmethod

class abstract1(ABC):

    @abstractmethod
    def func1(self):
        pass

class new_class(abstract1):
    def func1(self):
        print("new_class")

class new_class2(abstract1):
    def func1(self):
        print("new_class2")

a = new_class()
b = new_class2()
c = new_class()
# print("func1", c.func1())
# c.func1()
b.func1()
# c.func1()