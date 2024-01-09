# a ==> public datatype
# _a ==> protected datatype
# __a ==> private datatype

class A:
    a = 10          # Public datatype
    _b = 20         # Protected datatype
    __c = 30        # Private datatype

    def __func(self):
        print(1)

    def func1(self):
        self.__func()

d = A()
print(d.a)
print(d._b)
# print(d.__c)      # Cannot access 'private' datatype
print(d.func1())    # Does access 'private' datatype as func1 as access to private __func