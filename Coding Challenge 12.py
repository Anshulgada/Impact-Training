def winner(arr):
    n = len(arr)
    dheeraj = 0
    mansi = 0

    if n == 1:
        print("Dheeraj wins with", arr[0], "cards!")
        return
    elif n == 2:
        ans = max(arr[0], arr[1]) - min(arr[0], arr[1])
        print("Dheeraj wins with", ans, "cards!")
        return

    while len(arr) > 0:
        if n % 2 == 0:
            if arr[0] < arr[-1]:
                dheeraj += arr.pop()
            else:
                dheeraj += arr.pop(0)

            if arr[0] < arr[-1]:
                mansi += arr.pop()
            else:
                mansi += arr.pop(0)
        
        else:
            if arr[0] < arr[-1]:
                dheeraj += arr.pop()
            elif len(arr) == 1:
                dheeraj += arr.pop()
                break
            else:
                dheeraj += arr.pop(0)
                
            if arr[0] < arr[-1]:
                mansi += arr.pop()
            else:
                mansi += arr.pop(0)

    if dheeraj > mansi:
        ans = dheeraj - mansi
        print("Dheeraj wins with", ans, "cards!")
    else:
        ans = mansi - dheeraj
        print("Mansi wins with", ans, "cards!")

    return

inp = list(map(int, input().split()))
winner(inp)