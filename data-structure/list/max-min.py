"""

Input:#
A sorted list

Output:#
A list with elements stored in max/min form

Sample Input#
lst = [1,2,3,4,5]
Sample Output#
lst = [5,1,4,2,3]

"""
def max_min(lst):
    if len(lst) == 0:
        return []
    minIdx, maxIdx = 0, len(lst)-1
    maxEle = lst[-1] + 1
    for i in range(len(lst)):
        if i %2 == 0:
            lst[i] += (lst[maxIdx] % maxEle) * maxEle
            maxIdx -= 1
        else:
            lst[i] += (lst[minIdx] % maxEle) * maxEle
            minIdx += 1
    for i in range(len(lst)):
        lst[i] = lst[i] // maxEle
    return lst

print(max_min([1, 2, 3, 4, 5, 6, 7]))
print(max_min([1, 2, 3, 4, 5]))
print(max_min([]))
print(max_min([1, 1, 1, 1, 1]))
print(max_min([-10, -1, 1, 1, 1, 1]))
