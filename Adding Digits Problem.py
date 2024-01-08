#### Problem 3
# Add digits of strings

# Calculate time taken by code

import time
begin = time.time()

## Method 1
#
# def add_digits(input_str):
#     count = 0
#     for char in input_str:
#         if char.isdigit():
#             count += int(char)
#         else:
#             continue
#
#     c_str = str(count)
#     while len(c_str) > 1:
#         count = add_digits(c_str)
#         c_str = str(count)
#
#     return count
#
# string = '123456789'
# print (add_digits(string))



## Method 2

num = '123456789'
n = int(num)
print(9 if n % 9 == 0 else n % 9)

# Calculate time taken by code
time.sleep(0.1)
end = time.time()
print(end - begin - 0.1)
