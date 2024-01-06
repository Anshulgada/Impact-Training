# Input string is ==> abcdef
# & input num = 2 THEN
# Output string is ==> efabcd

input_string = 'abcdefghijklmnopqrstuvwxyz'
input_num = 3       # No of times to rotate input string
new_string = ''     # Empty string where we will append old string

for num in range(0,input_num):      # Iterate over input string in given range
    if new_string != '':            # Once we have a new string iterate over it and not over input string
        new_string = new_string[-1:] + new_string[0:-1]
        # If new string != empty string then we use it as input string
        # We slice the new string's last element & then append it
        # to the beginning of the new string, then print the rest of new string
    else:
        new_string = input_string[-1:] + input_string[0:-1]
        # Only in first iteration when new string is empty
        # we run this loop to slice last element of input string & append
        # that to new string and lastly add remaining string to new string

print(new_string)


## ==> CAN DO BETTER BY DIRECTLY SLICING SLICING NO OF ELEMENTS
## ==> SPECIFIED FROM STRING AND APPEND TO BEGINNING OF ORIGINAL STRING