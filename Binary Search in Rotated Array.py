def rotate_array(nums, k):
    for i in range(0, k):
        temp = nums[-1]  # Store the last element temporarily
        for j in range(len(nums) - 1, 0, -1):
            nums[j] = nums[j - 1]
        nums[0] = temp  # Move the last element to the first position
    return nums

def binary_search(nums, target):
    """
    Perform binary search on a sorted array.
    """
    low = 0
    high = len(nums)
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if target >= nums[low] and target < nums[mid]:
                high = mid
            else:
                low = mid + 1
        else:
            if target <= nums[high - 1] and target > nums[mid]:
                low = mid + 1
            else:
                high = mid
    return -1

def print_array(array):
    for i in range(0, len(array)):
        print(array[i], end=" ")

# Take user inputs
nums_str = input("Enter the sorted array separated by spaces: ")
nums = [int(num) for num in nums_str.split()]
k = int(input("Enter the number of steps to rotate the array to the right: "))
target = int(input("Enter the target element to search for: "))

print("Original array:")
print_array(nums)
print("\n")

# Rotate the array
rotated_array = rotate_array(nums, k)
print("Rotated array after", k, "steps:")
print_array(rotated_array)
print("\n")

# Perform binary search
index = binary_search(rotated_array, target)
if index != -1:
    print("Target", target, "found at index:", index)
else:
    print("Target", target, "not found in the rotated array.")
