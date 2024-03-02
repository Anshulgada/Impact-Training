# Function to find the Longest Common Subsequence (LCS)
def lcs_algo(S1, S2, m, n):
    # Create a matrix to store the length of LCS for sub problems
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Building the matrix in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                # Base case: if either string is empty, LCS length is 0
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                # If characters match, increment LCS length by 1
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                # If characters don't match, LCS length is maximum of previous lengths
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Length of LCS is stored at L[m][n]
    index = L[m][n]

    # Initialize LCS string
    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""

    i = m
    j = n
    # Backtrack to construct the LCS string
    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            # If characters match, add to LCS string and move diagonally up
            lcs_algo[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            # If length of LCS from top cell is greater, move up
            i -= 1
        else:
            # Otherwise, move left
            j -= 1

    # Printing the input strings and the LCS
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs_algo))


# Input two strings from the user
S1 = input("Enter string 1: ")
S2 = input("Enter string 2: ")
m = len(S1)
n = len(S2)
# Call the function to find and print the LCS
lcs_algo(S1, S2, m, n)
