"""

Given three strings m, n, and p, write a function to find out if p has been formed by interleaving m and n. p should be considered to be an interleaved form of m and n, if it contains all the letters from m and n in a preserved order.

Input#
Three strings

Output#
A boolean

Sample input#
m = "abd"
n = "cef"
p = "abcdef"
Sample output#
result = True

The time complexity of this code is in O(mn)
 since that is the size of the lookup table.
"""
def find_strings_interleaving(m, n, p):
    lookup_table = [[False for x in range(len(n)+1)]for y in range(len(m)+1)]
    if len(m) + len(n) != len(p):
        return False
    for m_index in range(len(m)+1):
        for n_index in range(len(n)+1):
            if m_index == 0 and n_index == 0:
                lookup_table[m_index][n_index] = True
            elif m_index == 0 and n[n_index-1] == p[m_index+n_index-1]:
                lookup_table[m_index][n_index] = lookup_table[m_index][n_index-1]
            elif n_index == 0 and m[m_index-1] == p[m_index+n_index-1]:
                lookup_table[m_index][n_index] = lookup_table[m_index-1][n_index]
            else:
                if m_index > 0 and m[m_index-1] == p[m_index+n_index-1]:
                    lookup_table[m_index][n_index] = lookup_table[m_index-1][n_index]
                if n_index > 0 and n[n_index-1] == p[m_index+n_index-1]:
                    lookup_table[m_index][n_index] |= lookup_table[m_index][n_index-1]
    return lookup_table[len(m)][len(n)]



# Driver code to test the above function
if __name__ == '__main__':

    print(find_strings_interleaving("abd", "cef", "adcbef"))
    print(find_strings_interleaving("abc", "def", "abdccf"))
    print(find_strings_interleaving("abcdef", "mnop", "mnaobcdepf"))
