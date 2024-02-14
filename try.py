# # def fun(x):
# #     pass
# # help(fun)
#
# # def fun7(f7 = dict()):
# #     print(f7)
# # fun7(1)
#
# # f5 =10
# # def fun6(f5=f5):
# #     print(f5)
# #
# # f5 = 30
# # fun6()
#
# # def fun4(a,c,b=5):
# #     return a,b,c
# #
# # print(fun4(10,20,30))
#
# # num = 1,2,3
# # store = []
# # for i in num:
# #     store.append(lambda: print(i, end=' '))
# # for p in store:
# #     p()
#
# # def outer(x, y):
# #     print(x,y,end=' ')
# #
# #     def inner(p):
# #         p()
# #
# #     return inner
# #
# # @outer(10,20)
# # def fun(x=50):
# #     print('fun')
#
# text = 'A', 'B', 'C'
# lst = []
#
# for t in text:
#     lst.append(lambda t=t: t)
#
# for l in range(len(lst)):
#     print(lst[l](), end=' ')
#
# def fun(*,x,y):
#     return x,y
#
# print(fun(10,y=20)[0])
#
# x = 20
#
# def fun4():
#     def fun5():
#         nonlocal x
#         x = 20
#         return x
#     return fun5()
#
# print(fun4())
#
# def fun1(x):
#     return fun1(x+'1')
# print(fun1(fun1('10')))


#########################
# Functions and Recursions
#
# def fun(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x * fun(x,n-1)
#
# print(fun(2,3))
#
# def is_even(n):
#     if n == 0:
#         return True
#     else:
#         return not is_even(n-1)
#
# print(factorial(5))
#
# def fun(n, temp):
#     if n == 0:
#         return temp
#     temp = (temp * 10) + (n%10)
#     return fun(n//10,temp)
#
# print(fun(1234,0))
#
# def f(s):
#     if len(s) <= 1:
#         return True
#     else:
#         return s[0] == s[-1] and f(s[1:-1])
#
# print(f("ADA"))
#
# def s(n):
#     if n == 0:
#         return n
#     else:
#         return n + s(n-1)
#
# print(s(8))
#
# def fun(num):
#     if num < 2:
#         return False
#     for i in range (2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True
#
# print(fun(9))
# 
# def fun(x,y):
#     if x == 0:
#         return y
#     return fun(x-1,x+y)
#
# print(fun(4,3))
#
# def fun(a,b):
#     if b == 0:
#         return a
#     return fun(b,a%b)
#
# print(fun(24,45))

# nest=[[1,2,3],[4,5,6],[7,8,9]]
# nest[1].pop()
# print(nest)
#
# my_l = [1,2,3,4,5]
# nl = my_l.copy()
# my_l[0] = 10
# print(nl)
#
# my_l = [1,2,[3,4,[5,6]],7]
# print(my_l[2][2][1])
#
# x = [5,10,15,20]
# print(x[:-1])
#
# print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y])
#
# my_l = [x for x in range(10) if x%2==0]
# print(my_l)


# set1 = {1,2,3}
# set2 = set1.copy()
# set2.add(4)
# print(set1)

# tup1 = (1,2,3)
# tup2 = (4,5,6)
# tup3 = tup1 * 2 + tup2
# print(len(tup3))

# dict1 = {"apple": 1, "banana": 2, "cherry":3}
# dict1.clear()
# print(dict1)

# dict1 = {"apple": 1, "banana": 2, "cherry":3}
# dict2 = {key: value for key, value in dict1.items() if key != "banana"}
# print(dict2)

# set1 = {1,2,3}
# set2 = {4,5,6}
# print(len(set1 + set2))


# nested_list = [[1,2,3], [4,5,6], [7,8,9]]
# nested_list.sort(reverse=True)
# print(nested_list)

# nested_list = [[1,2,3], [4,5,6], [7,8,9]]
# transposed_list = [[row[i] for row in nested_list] for i in range(len(nested_list[0]))]
# print(transposed_list)


# class Python:
#     def __init__(self):
#         self.python_dob = None
#     def check_existence(self):
#         if (self.python_dob >= 1991 and self.python_dob <= 2032):
#             print("The python still exists")
#         else:
#             print("The python doesn't exists")
#
# p1 = Python()
# p1.python_dob=1800
# p1.check_existence()
#
# p2 = Python()
# p2.python_dob = 2020
# p2.check_existence()


# class Super:
#     def __init__(self,a ,b):
#         print("1")
#         self.__a = a
#         self.b = b
#     def m1(self):
#         print("m1")
#     def m2(self):
#         print("m2")
#
# class Super2(Super):
#     def m1(self):
#         print("2")
#         super().m1()
#
# s = Super2(20,13)
# s.m1()


# class Customer:
#     def __init__(self, cust_id, name, age, wallet_balance):
#         self.cust_id = cust_id
#         self.name = name
#         self.age = age
#         self.wallet_balance = wallet_balance
#
#     def update_balance(self, amount):
#         if amount < 1000 and amount > 0:
#             self.wallet_balance -= amount
#
#     def show_balance(self):
#         print("The balance is", self.wallet_balance)
#
# c1 = Customer(100, "Abc", 24, 1000)
# c1.update_balance(500)
# c1.show_balance()


# class Play:
#     def __init__(self, game, price):
#         print("Inside Constructor")
#         self.game = game
#         self.price = price
#
# obj1 = Play("FootBall", 20000)
# print("FootBall is game here", obj1.game, "and its price", obj1.price)
#
# obj2 = Play("Cricket", 35000)
# print("Cricket is game here", obj2.game, "and its price", obj2.price)


# class Test:
#     def __init__(self, one, two):
#         print("inside Constructor")
#
# obj1 = Test(100,200,300)


# class Example:
#     def __init__(self,num):
#         self.num = num
#
#     def set_num(self,num):
#         num = num
#     def get_num(self):
#         return self.num
#
# obj = Example(10)
# print(obj.get_num())
#
# obj.set_num(15)
# print(obj.get_num())


# class Mobile:
#     def __init__(self,price,brand):
#         self.price = price
#         self.brand = brand
#
# mob1 = Mobile(1000,"Apple")
# print("Mob 1:", mob1.price)
#
# mob2 = mob1
# mob2.price = 3000
#
# print("mob1:", mob1.price)
# print("mob2:", mob2.price)


# class Example:
#     num = 10
#     @staticmethod
#     def add(n1,n2):
#         res = (n1+n2)*Example.num
#         return res
# print(Example.add(100,200))


# class OOPs:
#     pass
#
# obj1 = OOPs()
# obj2 = OOPs()
#
# obj1.a = 20
# obj1.b = "hello"
# obj1.c = 1
#
# print(obj1.c)
#
# obj2.a = 30
# obj2.b = 'Bye'
# obj2.c = 11
#
# print(obj2.c)


# class Test:
#     def m1(self):
#         print('M1')
#
#     def m2(self):
#         self.m1()
#         print('M2')
#
# Test().m2()