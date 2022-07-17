"""

Given a string, find the length of its longest palindromic subsequence. In a palindromic subsequence, elements read the same, backward and forward.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Input#
A string

Output#
The length of the longest palindromic subsequence

Sample input#
s = "abdbca"
Sample output#
The longest palindromic subsequence of the above string will be abdba and the following would be the output

result = 5

Both the space and time complexity of this algorithm is O(N^2)
, where N
 is the length of the input string.



"""
def longest_palindromic_subsequence(s):
    lookup_table = [[0 for x in range(len(s))] for y in range(len(s))]
    # Every sequence with one element is a palindrome of length 1
    for i in range(len(s)):
        lookup_table[i][i] = 1
    for start_index in reversed(range(len(s))):
        for end_index in range(start_index+1, len(s)):
            if s[start_index] == s[end_index]:
                lookup_table[start_index][end_index] = 2 + lookup_table[start_index+1][end_index-1]
            else:
                lookup_table[start_index][end_index] = max(lookup_table[start_index+1][end_index], lookup_table[start_index][end_index-1])
    return lookup_table[0][len(s)-1]

# Driver code to test the above function
if __name__ == '__main__':
    print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("abdbca"))
    print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("pqr"))
