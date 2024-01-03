# # *args ==>
# # Unlimited number of Non Keyword Arguments passed in function call (INT, FLOAT, ETC)
# def unli_calc(*nums):
#     total = 0
#     for val in nums:
#         total += val
#
#     print(total)
#
# unli_calc(1,2,3,4,5,6,7,8,9,10)
# unli_calc(1,2,3,4,5)
# unli_calc(1,2,3,4,5,6,7)


# **kwargs ==>
# Unlimited number of Keyword Arguments passed in function call (KEY-VALUE PAIRS)

print()
def unli_str(**kwargs):
    print("Key-Value Pairs: ")
    for str_print in kwargs.items():
        print(str_print)

    print()

    print("Values: "),
    for str_print in kwargs.values():
        print(str_print)

unli_str(Name = "Anshul", age = 20)

# Doesn't work ==>      ONLY VALUES WORK ==> NO DICT OR LIST
# my_list = ["Anshul", 20]      LIST DATA TYPE
# unli_str(my_list)
# my_dict = {"Name": "Anshul", "Age" : 20}      DICTIONARY DATA TYPE
# unli_str(my_dict)