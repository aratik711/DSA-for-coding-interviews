"""

Given a sorted list lst and an integer target, find and return the closest number to the target in the list.

The list may have duplicate and negative values.

Input#
lst Sorted list of integers
target An integer target number
Output#
Closest number to the given target
Sample input#
lst = [-9, -4, -2, 0, 1, 3, 4, 10]

target = 5
Sample output#
result = 4

The time complexity of this solution is O(lg n)
, since at each step, we are looking at the middle element, essentially dropping one half of the list, and are left with only half the elements we began with.


"""
def find_closest(lst, target):
    length = len(lst)
    if target <= lst[0]:
        return lst[0]
    if target >= lst[length - 1]:
        return lst[length - 1]
    i, j, mid = 0, length, 0
    while i < j:
        mid = (i+j) // 2
        if lst[mid] == target:
            return lst[mid]
        if target < lst[mid]:
            if mid > 0 and target > lst[mid-1]:
                if target - lst[mid] >= lst[mid-1] - target:
                    return lst[mid-1]
                else:
                    return lst[mid]
            j = mid
        else:
            if mid < length - 1 and target < lst[mid+1]:
                if target - lst[mid] >= lst[mid+1] - target:
                    return lst[mid+1]
                else:
                    return lst[mid]
            i = mid + 1
    return lst[mid]


# Driver code to test above function
if __name__ == '__main__':
        print(find_closest([-9, -4, -2, 0, 1, 3, 4, 10], 5))
        print(find_closest([1, 2, 5, 10, 23, 25, 30, 50], 100))
