"""

Given two strings, write a function to find the length of their shortest common superstring. A superstring is a string which has both input strings as substrings.

Input#
Two strings

Output#
The length of their shortest common supersequence

Sample input#
s1 = "abcf"
s2 = "bdcf"
Sample output#
The shortest common supersequence of the two strings above will be abdcf and the following would be the output:

result = 5

The time complexity of the code is in O(mn)

"""
def shortest_common_supersequence(s1, s2):
    lookup_table = [[0 for x in range(len(s2)+1)] for y in range(len(s1)+1)]
    for i in range(len(s1)+1):
        lookup_table[i][0] = i
    for j in range(len(s2)+1):
        lookup_table[0][j] = j
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                lookup_table[i][j] = 1 + lookup_table[i-1][j-1]
            else:
                lookup_table[i][j] = 1 + min(lookup_table[i-1][j], lookup_table[i][j-1])
    return lookup_table[len(s1)][len(s2)]


# Driver code to test the above function
if __name__ == '__main__':

    print(shortest_common_supersequence("abcdz", "bdcf"))
    print(shortest_common_supersequence("educative", "educative.io"))
