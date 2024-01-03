# Yield Keyword
def count_up_to(n):        # 'yield' keyword is used to create a generator function.
    i = 1                  #  A type of function that is memory efficient
    while i <= n:          #  and can be used like an iterator object.
        yield i
        i += 1

print("Obj_id:", count_up_to(6))
gen = count_up_to(6)

# print(next(gen))            # Generator Function
# print(next(gen))            # Print each generator using next() function
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:                 # Or else use for loop iteration in generator
    print(i)