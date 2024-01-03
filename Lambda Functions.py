# Lambda Functions
# One liner functions
# Do not require defining a function

add = lambda x,y: x+y       # Defining function

res = add(3,4)
print ("Add: ", res)            # Print via variable

print("Add: ", add(5,10))  # Print directly


nums = [1,2,3,4,5,6,7,8]                        # Defining List
squared = list(map(lambda x: x**2, nums))
print ("Squared: ", squared)                    # Print via variable

y = lambda y: y**2
print("Power: ", y(5))           # Print directly