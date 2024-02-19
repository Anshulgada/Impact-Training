def validTicket(ticket):
    stack = []

    for i in ticket:
        if i in "{[(":
            stack.append(i)
        else:
            if len(stack) > 0 and i == ')' and stack[-1] == '(':
                stack.pop()
            elif len(stack) > 0 and i == '}' and stack[-1] == '{':
                stack.pop()
            elif len(stack) > 0 and i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return "NO"

    return "YES" if len(stack) == 0 else "NO"


num_test_cases = int(input())       # To check num of test cases
for _ in range(num_test_cases):
    print(validTicket(input()))

