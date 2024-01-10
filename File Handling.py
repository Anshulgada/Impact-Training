# open()        # Also has '+' --> All of them do
# r --> read
# w --> write    --> write and read
# a --> append   --> append  and read
# x --> create
# close()


################################################################
# READ ==>

# open('new.txt', 'x')    # ==> Creates New File named 'new.txt' in same directory
# open('new.txt', 'r')    # ==> Reads File named 'new.txt

# f = open('new.txt','r')     # Creating obj to call open() function
# print(f.read())             # Prints the object

# If '\' is in path use 'r' before string to make it raw string
# Or use '\\' (double string) in path to make it readable to compiler


################################################################
# WRITE ==>

# print(open(r"C:/Users/Anshul/Desktop/WatchLater.txt").read())  # Reads Files from other directory

# w = open(r"C:/Users/Anshul/Desktop/New.txt",'w+')            # Reads File named 'New.txt'
# w.write("Hi, I am Anshul Gada")                             # Writes to file 'New.txt'
# w.seek(0)       # Seek to beginning of file (index [0])
# print("Cursor position:", w.tell())      # Print where the cursor is located in the file
# print("\nFrom write operation: \n", w.read())      # Print the file from the cursor position

# When writing to a file and then directly reading it, it shows empty output
# This is because the print statement works from the current cursor position
# That location is set after the string we write to the file
# Therefore the file is empty from current cursor position
# So output is empty
# To avoid this we use seek(0) to get the current cursor position to the beginning

# w.close()                                                   # Closes this operation
# print(open("C:/Users/Anshul/Desktop/New.txt",'r').read())   # Prints the object 'w'


################################################################
# APPEND ==>

# a = open("C:/Users/Anshul/Desktop/New.txt",'a')
# a.write("\nI am 20 years old")                          # Appends to file (NewLine not by default)
# a.close()
# print("\nFrom append operation: \n", open("C:/Users/Anshul/Desktop/New.txt",'r').read())

# Can also use seek() and slice operations to print end part of string first
# Then print the starting part of the string


################################################################
# Problem Statement ==>

# # Order of write statements is Hello --> Hi
# # But we want to input as Hi --> Hello

# f = open("new1.txt",'w+')
# f.seek(2)
# f.write("Hello")
# f.seek(0)
# f.write("Hi")
# f.seek(0)
# print(f.read())

# # To solve this we used seek to go to index 2 and then write "Hello"
# # Next we back to index 0 using seek and then write "Hi"
# # This way the final output is ==> 'HiHello'
# #
# # To print "Hello" first then print "Hi"
# # That is opposite of what we wrote to the file
# # So we first seek to index of Hello and then print that
# # Next we seek to index of Hi and read only 2 characters and print them only
# f = open("new1.txt",'r+')
# f.seek(2)
# print(f.read())
# f.seek(0)
# print(f.read(2))


################################################################
# READ FROM IMAGE

img = open('android.png', 'rb')         # 'b' states to read file as binary and not the default 't' (text) format
write_img = open('new_img.jpg', 'wb')   # wb to write file as binary and not the default 't' (text) format

for i in img:               # Loop over the binary data of the image
    write_img.write(i)    # Write the binary data of the image to another img file which we create in code itself