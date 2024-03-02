# Define a function to solve the knapsack problem
# W: maximum capacity of the knapsack
# wt: list of weights of items
# val: list of values of items
# n: number of items
def knapSack(W, wt, val, n):
    # Create a table to store the results of subproblems
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Fill the table in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            # Base case: if no items or knapsack capacity is 0, value is 0
            if i == 0 or w == 0:
                K[i][w] = 0
            # If the current item's weight is less than or equal to the current capacity
            elif wt[i - 1] <= w:
                # Choose the maximum value between including and excluding the current item
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                # If the current item's weight exceeds the current capacity, exclude it
                K[i][w] = K[i - 1][w]

    # Return the maximum value that can be stored in the knapsack
    return K[n][W]


# Main function to test the knapsack algorithm
val = [1,2,5,6]  # Values of items
wt = [2,3,4,5]  # Weights of items
W = 8  # Maximum capacity of the knapsack
n = len(val)  # Number of items
print(knapSack(W, wt, val, n))  # Print the maximum value that can be stored in the knapsack


#p={1,2,5,6}
#w={2,3,4,5}
#w of bag=8
#no.of ele=4
#form=v[i,w]=max{v[i-1,w],v[i-1,w-w(i)]+p[i]}