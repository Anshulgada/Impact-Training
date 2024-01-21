n = int(input())

count = 1
count2 = n * (n + 1)

for i in range(n):
    for s in range(i):
        print(" ", end = "")

    for k in range(n-i):
        print(f"{count}*", end = "")
        count += 1

    for k in range(n - i):
        if k == (n - i) - 1:
            print(count2 - (n - k) + 1, end = "")

        else:
            print(f"{count2 - (n - k) + 1}*", end = "")


    count2 -= (n - i)
    count2 += 1
    print()

