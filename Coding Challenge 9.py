def minimum_gifts(num, ranks):
    # Initialize gifts array with 1 gift for each staff member
    gifts = [1] * num

    # Forward pass: Assign gifts to higher-ranking staff members
    for i in range(1, num):
        if ranks[i] > ranks[i - 1]:
            gifts[i] = gifts[i - 1] + 1

    # Backward pass: Ensure each staff member receives at least one gift
    for i in range(num - 2, -1, -1):
        if ranks[i] > ranks[i + 1] and gifts[i] <= gifts[i + 1]:
            gifts[i] = gifts[i + 1] + 1

    # Print the minimum number of gifts required
    print("\nMinimum no of gifts required: ", sum(gifts))
    print()

# Input reading and function call
test_cases = int(input("\nEnter no of test cases: "))

for t_num in range(0, test_cases):
    print(f"\nTest case {t_num + 1} ==> ")
    num_of_staff = int(input("\tEnter no of staffs: "))
    staff_ranks = list(map(int, input("\tEnter ranks: ").split()))
    minimum_gifts(num_of_staff, staff_ranks)