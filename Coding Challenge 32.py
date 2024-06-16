"""
QUESTION:

**Efficiently Managing Dynamic Updates and Queries on a Rotated Sorted Array**
Max Score: 10 | Difficulty: Medium

Description:
You are given a rotated sorted array of integers that may contain negative numbers and have unique elements. Your task is to implement a program that efficiently handles dynamic updates and queries on this array.
Constraints:
The array may contain negative numbers.
You must handle multiple queries efficiently on the same array.
You are not allowed to sort the entire array explicitly.
You must handle dynamic updates to the array, where elements can be added or removed.
Input
The first line contains two integers, N and Q, representing the number of elements in the array and the number of queries, respectively.
The second line contains N space-separated integers representing the rotated sorted array.
The following Q lines contain queries, each of which is either:
A X: Add the element X to the array.
RX: Remove one occurrence of the element X from the array.
FK: Find the Kth largest unique element.
Q: Quit the program.

Output:
For each query of type FK, output an integer representing the Kth largest unique element in the array at that point in time. If there are fewer than K unique elements, return -1. Queries of type AX and RX do not require any output.

Sample Formatting of the Output:
Added element 5.
Added element 15.
Added element 25.
Added element 10.
Added element 20.
Added element 30.
The 1st largest unique element is: 30
The 2nd largest unique element is: 25
The 3rd largest unique element is: 20
The 4th largest unique element is: 15
The 5th largest unique element is: 10
Removed one occurrence of element 10.
Removed one occurrence of element 30.
The 4th largest unique element is: 5

Sample Input:
7 11
5 6 9 12 1 3 4 
A 30
A 40
F1
R 30
A 50
F2
A 30
F3
R 30
F3
F4
Q

Sample Output:
Added element 30.
Added element 40.
The 1st largest unique element is: 40
Removed one occurrence of element 30.
Added element 50.
The 2nd largest unique element is: 40
Added element 30.
The 3rd largest unique element is: 30
Removed one occurrence of element 30.
-1
-1

Explanation:
Initial State:
Array: [5, 6, 9, 12, 1, 3, 4]
Command: A 30
Action: Adds the element 30 to the array.
Output: Added element 30.
Command: A 40
Action: Adds the element 40 to the array.
Output: Added element 40.
Command: F 1
Action: Finds the 1st largest unique element.
Explanation: The unique elements at this point are [1, 3, 4, 5, 6, 9, 12, 30, 40]. The 1st largest unique element is 40.
Output: The 1st largest unique element is: 40
Command: R 30
Action: Removes one occurrence of the element 30 from the array.
Output: Removed one occurrence of element 30.
Command: A 50
Action: Adds the element 50 to the array.
Output: Added element 50.
Command: F 2
Action: Finds the 2nd largest unique element.
Explanation: The unique elements at this point are [1, 3, 4, 5, 6, 9, 12, 40, 50]. The 2nd largest unique element is 40.
Output: The 2nd largest unique element is: 40
Command: A 30
Action: Adds the element 30 to the array.
Output: Added element 30.
Command: F 3
Action: Finds the 3rd largest unique element.
Explanation: The unique elements at this point are [1, 3, 4, 5, 6, 9, 12, 30, 40, 50]. The 3rd largest unique element is 30.
Output: The 3rd largest unique element is: 30
Command: R 30
Action: Removes one occurrence of the element 30 from the array.
Output: Removed one occurrence of element 30.
Command: F 3
Action: Tries to find the 3rd largest unique element.
Explanation: There are only two unique elements larger than 30 which has just been removed.
Output: -1
Command: F 4
Action: Tries to find the 4th largest unique element.
Explanation: There are only two unique elements larger than 30 which has just been removed.
Output: -1
Command: Q
Action: Quits the program.

**Constraints**

* \(2\le N\le10^{5}\)
* \(-10^{4}\le A_{i},X\le10^{4}\)
* \(1\le Q\le10^{5}\)
* \(1\le K\le N\)

**Notes:**
The array is rotated and sorted, meaning the smallest element could appear after the largest element in a sorted view.
Efficiently handle multiple queries on the same array instance.
Ensure dynamic updates (A X and RX) are handled efficiently, allowing for rapid changes to the array state.
Implement FK queries to return results in optimal time without explicitly sorting the entire array.


NOT SOLVED. WRONG OUTPUT!
"""

from collections import Counter
import bisect

def process_queries():
    import sys
    
    input = sys.stdin
    
    # Read the initial values for N and Q
    first_line = input.readline().strip()
    N, Q = map(int, first_line.split())
    
    # Read the initial array
    second_line = input.readline().strip()
    arr = list(map(int, second_line.split()))
    
    # Initializing the data structures
    element_counter = Counter(arr)
    unique_sorted_elements = sorted(element_counter.keys())

    results = []

    # Process each query
    while True:
        query = input.readline().strip()
        if not query:
            continue
        
        cmd = query.split()[0]
        
        if cmd == 'A':
            X = int(query.split()[1])
            if element_counter[X] == 0:
                bisect.insort(unique_sorted_elements, X)
            element_counter[X] += 1
            results.append(f"Added element {X}.")
        
        elif cmd == 'R':
            X = int(query.split()[1])
            if element_counter[X] > 0:
                element_counter[X] -= 1
                results.append(f"Removed one occurrence of element {X}.")
                # Update unique_sorted_elements after removal
                if element_counter[X] == 0:
                    index = bisect.bisect_left(unique_sorted_elements, X)
                    if index < len(unique_sorted_elements) and unique_sorted_elements[index] == X:
                        unique_sorted_elements.pop(index)
        
        elif cmd == 'F':
            K = int(query.split()[1])
            if K <= len(unique_sorted_elements):
                kth_largest_element = unique_sorted_elements[-K]
                ordinal_suffix = get_ordinal_suffix(K)
                results.append(f"The {K}{ordinal_suffix} largest unique element is: {kth_largest_element}")
            else:
                results.append("-1")  # Handle case where K is greater than number of unique elements
        
        elif cmd == 'Q':
            break

    for result in results:
        print(result)

def get_ordinal_suffix(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return suffix

# Run the process_queries function to handle user input and process queries
if __name__ == "__main__":
    process_queries()


# 7 11
# 5 6 9 12 1 3 4 
# A 30
# A 40
# F 1
# R 30
# A 50
# F 2
# A 30
# F 3
# R 30
# F 3
# F 4
# Q