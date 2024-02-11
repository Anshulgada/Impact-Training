'''

Problem ==> CHECK THE STRUCTURE

Description:
A binary tree uses a multi-node data structure where each node may have 0 to 2 child nodes, and has one stored value, its node number in this case. A tree may either be:
    • An empty tree, the root is null.
    • A non-empty tree with a non-null root node that contains a value and up to 2 sub-trees, left and right which are also binary trees

A Binary tree classified as a binary search tree (BST) with all the non-null nodes exhibit two properties:
	• The left subtree of each node contains only nodes with values that are lower than its own value.
	• The right subtree of each node contains only nodes with values that are higher than its own value.

A preorder traversal is a recursive tree traversal method where the current node is visited first, then the left subtree and then the right subtree. The following pseudocode parses a tree into a list using preorder traversal:
    • If the route is null, return the null list.
    • For a non-null root node:
        1.	Create a preorder traversal list, left, of the left subtree.
        2.	Create a preorder traversal list, right, of the right subtree.
        3.	Return the concatenated list: the non-null node + left + right.

Given a preorder traversal history of a binary tree, check whether the path represents a valid BST or not. Return a string, either YES if the path can represent a valid BST, or NO if it cannot.



EXAMPLE:
nodes = [2,1,3,4,5]
	• The root node will always be the first node in the array. In this case, the root node is at node 2.
	• The next value. 1 is less than 2. Place the node 1 at the left of node 2.
	• The next value, 3 is greater than 2. Place the node 3 at the right of node 2.
	• The next value, 4 is greater than 3. Place the node 4 at the right of node 3.
	• The next value, 5 is greater than 4. Place the node 5 at the right of node 4.
	• The graph meets the definition of a BST.

Constraints:
    • 1 <= q <= 10
    • 1 <= n, a[i] <= 100



Input format:
The first line contains an integer q. The number of queries nodes.
The next q sets of lines are defined as:
The first line contains an integer n, The number of nodes in the tree.
The next line contains a[n]: A list of space separated integers that denote values encountered in the traversal of a tree.

Output format:
Print either the string YES if the path represents a valid BST or NO otherwise.

Sample Input:
5			    => Number of queries q = 5
3			    => a[] size n = 3 (query 0)
1 3 2		    => a = [1, 3, 2]
3			    => a[] size n = 3 (query 1)
2 1 3		    => a = [2, 1, 3]
6			    => a[] size n = 6 (query 2)
3 2 1 5 4 6		=> a = [3, 2, 1, 5, 4, 6]
4			    => a[] size n = 4 (query 3)
1 3 4 2			=> a = [1, 3, 4, 2]
5			    => a[] size n = 5 (query 4)
3 4 5 1 2		=> a = [3, 4, 5, 1, 2]

Sample Output:
YES
YES
YES
NO
NO


Explanation:
An explanation of q = 5 queries:
1.	Query 0 is valid so that return the string YES.
2.	Query 1 is valid so return the string YES.
3.	Query 2 is valid so return the string YES.

4.	In Query 3, the query 1 3 4 2 is not valid. The root is 1 because it is the first value in the list. The second value of 3 must be the right child of 1, because it is greater. Likewise, the third value, 4 must be the right child of 3. For 2 to be the last value in traversal, it has to be the left child of4. It is less than the root value 3 above it, and is so on its right subtree. Return the string NO.

5.	In Query 4, the query 3 4 5 1 2 is not valid. The root, the first value in the list, is 3. The second value, 4, must be the right child of 3. The third value, 5, must be the right child of 4. For the fourth value to be 1, it must be the left child of 5, but that is less than the root at 4 and is in its right subtree. Return the string NO.

'''


def is_valid_BST(n, a):
    stack = []
    root = float('-inf')

    for i in range(n):
        while stack and a[i] > stack[-1]:
            root = stack.pop()

        if a[i] < root:
            return "NO"

        stack.append(a[i])

    return "YES"

def main():
    q = int(input().strip())
    results = []

    for _ in range(q):
        n = int(input().strip())
        a = list(map(int, input().split()))

        result = is_valid_BST(n, a)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()