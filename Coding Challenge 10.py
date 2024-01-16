def trappingWater(arr, N):
    left_max = [0] * N
    right_max = [0] * N

    left_max[0] = arr[0]
    for i in range(1, N):
        left_max[i] = max(left_max[i - 1], arr[i])

    right_max[N - 1] = arr[N - 1]
    for i in range(N - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])

    trapped_water = 0
    for i in range(N):
        trapped_water += min(left_max[i], right_max[i]) - arr[i]

    return trapped_water

# Take user input for the array
arr_input = input()
arr = list(map(int, arr_input.split()))

# Call the trappingWater function with user input
result = trappingWater(arr, len(arr))
print(result)
