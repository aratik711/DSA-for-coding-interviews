"""

Given two strings, write a function to determine if one is a permutation of the other.

Here is an example of strings that are permutations of each other:

is_permutation_1 = "google"
is_permutation_2 = "ooggle"
The strings below are not permutations of each other.

not_permutation_1 = "not"
not_permutation_2 = "top"


"""
def is_perm_1(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            return False
    return True

def is_perm_2(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    d = dict()
    for i in s1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in s2:
        if i in d:
            d[i] -= 1
        else:
            return False
    return all(value == 0 for value in d.values())

is_permutation_1 = "google"
is_permutation_2 = "ooggle"

not_permutation_1 = "not"
not_permutation_2 = "top"
print(is_perm_1(is_permutation_1, is_permutation_2))
print(is_perm_1(not_permutation_1, not_permutation_2))

print(is_perm_2(is_permutation_1, is_permutation_2))
print(is_perm_2(not_permutation_1, not_permutation_2))
