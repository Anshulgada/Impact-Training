def maximize_stolen_money(house_money):
    n = len(house_money)

    if n == 1:
        return house_money[0], [1]

    elif n == 2:
        max_amount = max(house_money[0], house_money[1])
        selected_house = 1 if max_amount == house_money[0] else 2
        return max_amount, [selected_house]

    dp = [0] * n
    selected_houses = []

    # Base cases (corrected for n >= 3)
    dp[0] = house_money[0]
    dp[1] = house_money[1]  # Choose only the second house for n = 3 base case
    selected_houses.extend([1, 2])

    # Dynamic Programming
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + house_money[i])
        selected_houses.append(i)  # Append current house index

    # Backtracking to find the actual houses (corrected)
    final_houses = []
    i = n - 1
    while i >= 0:
        if dp[i] == dp[i - 1]:
            i -= 1
        else:
            final_houses.append(i + 1)  # Append actual house number
            i -= 2
    final_houses.reverse()

    return dp[n - 1], final_houses

# Sample Input
input_money = list(map(int, input().split()))

# Calculate and print the result
result_money, result_houses = maximize_stolen_money(input_money)
print(result_money)  # Expected output: 8 for input 4 2 3 6
print(result_houses)
