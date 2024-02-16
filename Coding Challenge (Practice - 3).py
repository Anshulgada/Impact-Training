def max_sum_subarray(arr):
    n = len(arr)

    if n <= 2:
        return max(arr)

    # Initialize two variables to keep track of the maximum sums for the previous and current elements
    prev_max = arr[0]
    curr_max = max(arr[0], arr[1])

    # Iterate from the third element to the end of the array
    for i in range(2, n):
        # Calculate the maximum sum considering the current element and the maximum sum without the previous element
        new_max = max(curr_max, prev_max + arr[i])

        # Update the previous and current maximum sums
        prev_max = curr_max
        curr_max = new_max

    return curr_max

# Example usage:
arr = [2, 7, 1, 9, 3]
result = max_sum_subarray(arr)
print(result)
