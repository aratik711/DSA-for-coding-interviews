"""

Input#
A list and a positive number by which to rotate that list

Output:#
The given list rotated by k elements

Sample Input#
lst = [10,20,30,40,50]
k = 3
What if the given input k is greater than the length of the lst?

Sample Output#
lst = [30,40,50,10,20]

Time complexity O(n)

"""
def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


print(right_rotate([], 1))
print(right_rotate([1, 2, 3, 4, 5], 2))
print(right_rotate([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
print(right_rotate([300, -1, 3, 0], 3))
print(right_rotate([0, 0, 0, 2], 2))
print(right_rotate(['13', 'a', 'Python'], 3))
print(right_rotate(['right', 'rotate', 'python'], 4))
