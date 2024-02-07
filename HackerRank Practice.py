# # Print Max element from array
# num = int(input("Enter Size of array:"))
# arr = list(map(int, input("Enter nums:").split()))
# ans = arr[0]
# for i in range(1, num):
#     ans = max(ans, arr[i])
# print("Max element: " + str(ans))



# # Print Max element from array
# arr = []
# size = int(input("Enter size: "))
# print("Input elements: ")
#
# for i in range(0, size):
#     nums = int(input())
#     arr.append(nums)
#
# print("Max element: " + str(max(arr)))



# # Print duplicated array
# def duplicate(arr):
#     return arr + arr
#
# arr = list(map(int, input("Enter nums: \n").split()))
# arr1 = duplicate(arr)
# print("List form: \n" + str(arr1))
# print("Space form: \n", *arr1)



# # Print Unique elements from an array
# def unique_elements(arr):
#     store = []
#     for ele in arr:
#         if arr.count(ele) == 1:
#             store.append(ele)
#
#     for ele in store:
#         print(ele, end = ' ')
#
# size = int(input("Enter size: \n"))
# arr = list(map(int, input("Enter nums: \n").split()))
# unique_elements(arr)



# # Print array in reverse without inbuilt functions
# def rev_array(arr):
#     store = []
#     for i in range(len(arr), 0, -1):
#         store.append(arr[i - 1])
#     return store
#     # Using Recursion
#     # if len(arr) == 1:
#     #     return arr
#     # return rev_array(arr) # ==> Error here by me
#
#
# arr = list(map(int, input("Enter nums: \n").split()))
# print("Reversed Array: ", rev_array(arr), end = ' ')



# # Print Sum of odd elements in array
# def sum_odd_elements(arr):
#     sum = 0
#     for i in range(len(arr)):
#         if arr[i] % 2 != 0:
#             sum += arr[i]
#     return sum
#
# arr = list(map(int, input("Enter nums: \n").split()))
# print("Sum of odd elements: ", sum_odd_elements(arr))



# # Find the single duplicate element in array
# def LongestStringOfOnes(arr):
#     temp = 0
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] == 1:
#             temp += 1                   # Alternatively you can compare count and temp for the greater one
#             count = max(count, temp)    # Here max compares the old count(temp) to the new count
#         else:
#             temp = 0
#     return count
#
# arr = list(map(int, input("Enter nums: \n").split()))
# print("Longest String of Ones: ", LongestStringOfOnes(arr))



# Print Max Altitude a Pilot can reach when starting at 0
def MaxAltitude(size, arr):
    maxAltitude = 0
    current = 0
    for i in range(len(arr)):
        current = current + arr[i]
        maxAltitude = max(maxAltitude, current)
    return maxAltitude

size = int(input("Enter array size: \n"))
arr = list(map(int, input("Enter nums: \n").split()))
print("Max Altitude: ", MaxAltitude(size, arr))