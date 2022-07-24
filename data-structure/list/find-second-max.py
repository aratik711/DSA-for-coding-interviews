"""

Input:#
A List

Output:#
Second largest element in the list

Sample Input#
[9,2,3,6]
Sample Output#
6

This solution is in O(n) since the list is traversed once only.
"""
def find_second_maximum(lst):
    max1 = float('-inf')
    max2 = float('-inf')
    for ele in lst:
        if ele > max1:
            max2 = max1
            max1 = ele
        elif ele > max2 and ele != max1:
            max2 = ele

    return max2



print(find_second_maximum([9, 2, 3, 6]))
print(find_second_maximum([4, 2, 1, 5, 0]))
