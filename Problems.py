#### Problem 1

# To print the string like 'aaaaaaaaaaaascscdddd' from ==> 12a2sc4d
def decode_string(given_string):
    result = ""  # empty string to store the final result
    count = 0  # number of times to repeat the char

    for char in given_string:
        if char.isdigit():
            count = count * 10 + int(char)  # To use nums with 2 or more digits we used count * 10

        elif char.isalpha():

            temp = char  # to store consecutive letters
            index = given_string.index(char)  # index of the char we are currently reading

            # To loop over next character and check if
            # it is in range of str-length & if it is a character we proceed ahead
            while index + 1 < len(given_string) and given_string[index + 1].isalpha():
                # To store the new character to temp variable until we encounter a digit
                temp += given_string[index + 1]

                # increment the index of the char we are reading to go to next char
                index += 1

            result += temp * count
            # Finally add temp var to the result variable 'count' times
            # This way consecutive characters stay together

            count = 0  # Reset count to 0 for next loop

        else:
            print("Wrong Symbol")     # For any other symbols like '*' or '+' or '.'

    return result

input_string = "12a2sc4d"
print(decode_string(input_string))


#### Problem 2

# # To sort elements of a list but with a twist
# # If num of ele == odd, then keep mid ele as it is and sort the rest of them
# # by diving original array into Left Sub Array & Right Sub Array
# # If num of ele == even, sort the elements
# # by diving original array into Left Sub Array & Right Sub Array

# array = [6, 4, 1, 7, 3, 9, 5]
#
# length_of_array = len(array)
# mid = length_of_array // 2
#
# # Directly print the resultant array based on if num of elements are odd or even
#
# if (length_of_array % 2 != 0):
#     print(sorted(array[0:mid]) + [array[mid]] + sorted(array[mid + 1: ]))
#     # Odd num of elements so we just divide it into 2 sub-arrays + mid-element
#     # individually and print them by concatenating L-Array + Mid + R-Array into 1 List
#
# else:
#     print(sorted(array[0:mid]) + sorted(array[mid: ]))
#     # Even num of elements so we just divide it into 2 sub-arrays
#     # & then we sort them individually and print them by concatenating them into 1 List
