def factorial(num):
    if num == 0 or num == 1:
        print(num , "\n")
        return 1
    else:
        print(num)
        return num * factorial(num-1)    # Return is end of Function so print after this won't work

number = int(input("Enter a number: "))
print(factorial(number))