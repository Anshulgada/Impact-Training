def insertionSort(data):
    for i in range(1, len(data)):
        temp = data[i]
        j = i - 1

        while j >= 0 and temp < data[j]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = temp

data = list(map(int, input("Enter space-seperated numbers: ").split()))

if len(data) >= 1:
    insertionSort(data)
    print("Sorted array is: \n", data)

else:
    print("No numbers provided!")