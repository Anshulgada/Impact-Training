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






