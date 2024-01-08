from abc import ABC, abstractmethod


class abstraction:

    @abstractmethod
    def func1():
        pass

class new_class(abstraction):
    def func2():
        print("new_class")

c = new_class
# print("func1", c.func1())
# c.func1()
c.func2()