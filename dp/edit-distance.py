"""

Given two strings, write code to calculate how many minimum Levenshtein distance operations are needed to convert one into the other.

Input#
Two strings

Output#
A number

Sample input#
str1 = "sunday"
str2 = "saturday"
Sample output#
result = 3

The time complexity is O(mn)
"""
def min_edit_dist_recurse(s1, s2, m, n):
    lookup_table = [[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                lookup_table[i][j] = j
            elif j == 0:
                lookup_table[i][j] = i
            elif s1[i-1] == s2[j-1]:
                lookup_table[i][j] = lookup_table[i-1][j-1]
            else:
                lookup_table[i][j] = 1 + min(lookup_table[i][j-1], lookup_table[i-1][j], lookup_table[i-1][j-1])
    return lookup_table[m][n]

def min_edit_dist(s1, s2):
    return min_edit_dist_recurse(s1, s2, len(s1), len(s2))

# Driver code to test the above function
if __name__ == '__main__':

    str1 = "sunday"
    str2 = "saturday"

    print(min_edit_dist(str1, str2))
