"""

Given two strings, s1 and s2, write a function that finds and returns the length of the longest substring of s2 in s1 (if any exists).

Input#
Two strings

Output#
An integer

Sample input#
s1 = "www.educative.io/explore"
s2 = "educative.io/edpresso"
Sample output#
result = 14

The space complexity of the above algorithm is O(n)
, whereas the time complexity remains the same.



"""
def longest_common_substr_length(s1, s2):
    lookup_table = [[0 for x in range(len(s2)+1)] for y in range(2)]
    max_length = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            lookup_table[i%2][j] = 0
            if s1[i-1] == s2[j-1]:
                lookup_table[i%2][j] = 1 + lookup_table[(i-1)%2][j-1]
                max_length = max(max_length, lookup_table[i%2][j])
    return max_length

# Driver code to test the above function
if __name__ == '__main__':

    S1 = "0abc321"
    S2 = "123abcdef"
    print(longest_common_substr_length(S1, S2))

    S1 = "www.educative.io/explore"
    S2 = "educative.io/edpresso"
    print(longest_common_substr_length(S1, S2))
