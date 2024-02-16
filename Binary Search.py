def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            print("Element found at index: ", mid)
            return
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
    print("Element not found")

arr = list(map(int, input().split()))
target = int(input("Enter target element: "))

binarySearch(arr, target)