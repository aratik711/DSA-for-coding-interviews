"""

Inversion count represents how far or close a list is from being sorted. If a list is sorted, the inversion count will be 0. But if it’s sorted in the reverse order, the inversion count will be maximum.
Given an array of n integers, find the inversion count for its elements.

Input#
lst - A list containing integers in any order (It can contain negative values too.)


Output#
inversion_count - An integer is returned after counting the total number of inversions

Sample input#
lst = [7, 6, 5, 8]
Sample output#
result = 3

The running time will be O(n log n)
, because when the list is successively divided into halves, the recursion tree has depth lg n
. At each level of the recursion tree, calls to inversion_count touches exactly n elements. Thus, the total running time is O(n log n)

"""
def inversion_count(lst, n):
    temp = [0]*n
    return inversion_count_recursive(lst, temp, 0, n-1)

def inversion_count_recursive(lst, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += inversion_count_recursive(lst, temp, left, mid)
        inv_count += inversion_count_recursive(lst, temp, mid+1, right)
        inv_count += find_inversion_count(lst, temp, left, mid, right)
    return inv_count

def find_inversion_count(lst, temp, left, mid, right):
    i, j, k, inv_count = left, mid+1, left, 0
    while i <=mid and j <= right:
        if lst[i] <= lst[j]:
            temp[k] = lst[i]
            k += 1
            i += 1
        else:
            temp[k] = lst[j]
            inv_count += (mid-i+1)
            k += 1
            j += 1
    while i <= mid:
        temp[k] = lst[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = lst[j]
        k += 1
        j += 1
    for index in range(left, right + 1):
        lst[index] = temp[index]
    return inv_count


# Driver code to test above functions
if __name__ == '__main__':
    lst = [3, 8, 2, 7, 5, 6]
    n = len(lst)
    result = inversion_count(lst, n)
    print("Number of inversions are", result)
