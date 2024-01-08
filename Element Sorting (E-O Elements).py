# To sort elements of a list but with a twist
# If num of ele == odd, then keep mid ele as it is and sort the rest of them
# by diving original array into Left Sub Array & Right Sub Array
# If num of ele == even, sort the elements
# by diving original array into Left Sub Array & Right Sub Array

array = [6, 4, 1, 7, 3, 9, 5]

length_of_array = len(array)
mid = length_of_array // 2

# Directly print the resultant array based on if num of elements are odd or even

if (length_of_array % 2 != 0):
    print(sorted(array[0:mid]) + [array[mid]] + sorted(array[mid + 1: ]))
    # Odd num of elements so we just divide it into 2 sub-arrays + mid-element
    # individually and print them by concatenating L-Array + Mid + R-Array into 1 List

else:
    print(sorted(array[0:mid]) + sorted(array[mid: ]))
    # Even num of elements so we just divide it into 2 sub-arrays
    # & then we sort them individually and print them by concatenating them into 1 List
