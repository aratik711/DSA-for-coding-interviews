"""

Input#
A list of integers

Output#
The first unique element in the list

Sample Input#
[9,2,3,2,6,6]
Sample Output#
9

Time complexity O(n^2)

"""
def find_first_unique(lst):
    unique = []
    count = 0
    for ele in lst:
        if ele in unique:
            unique.remove(ele)
            count =- 1
        else:
            unique.append(ele)
            count += 1
    return unique[0] if len(unique) > 0 else None

print(find_first_unique([9, 2, 3, 2, 6, 6, 9, 3]))
print(find_first_unique([4, 5, 1, 2, 0, 4]))
