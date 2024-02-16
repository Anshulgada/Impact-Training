
def fibonacci(num):
    num0 = 0
    num1 = 1

    if num <= 0:
        print("Please enter a valid number!")

    elif num == 1:
        print(num0)

    else:
        for i in range(1, num + 1):
            print(num0, end = ' ')
            newNum = num0 + num1
            num0 = num1
            num1 = newNum

num = int(input("Enter number of digits to print: "))
fibonacci(num)
