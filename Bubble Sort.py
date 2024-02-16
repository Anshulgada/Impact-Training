list = list(map(int, input().split()))
arrLen = len(list)

def bubbleSort(list):
    for i in range(0, arrLen - 1):
        for j in range(i + 1, arrLen):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

bubbleSort(list)
print("Sorted array is:")
for i in range(len(list)):
    print(list[i], end=" ")