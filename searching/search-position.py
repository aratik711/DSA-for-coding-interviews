"""

Given a sorted list and a target value, return the index of the target value if the value is present in the list. If the value is not present, return the index at which the value should be inserted.

You may assume that no duplicates are in the list.

Input#
A sorted list and a target value

Output#
The index at which the list should be inserted OR the index at which it is already present

Sample input#
  lst = [1, 3, 5, 6]
  value = 5
Sample output#
  result = 2

This is in the same time complexity as binary search, so it will be in O(log(n))

"""
def search_insert_position(lst, key):
    size = len(lst)
    if size < 1:
        return -1
    start = 0
    end = size - 1
    pos = 0
    while start <= end:
        mid = start + (end-start) // 2
        if lst[mid] == key:
            return mid
        if lst[mid] > key:
            end = mid - 1
            pos = mid
        if lst[mid] < key:
            start = mid + 1
            pos = mid + 1
    return pos


# Driver to test above code
if __name__ == '__main__':

    lst = [1, 3, 5, 6]

    value = 5
    print(search_insert_position(lst, value))

    value = 2
    print(search_insert_position(lst, value))
