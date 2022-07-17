"""

Implement a function that tells whether a given number is present in a row-wise and column wise sorted 2D list or not.

Input#
A sorted 2D list and the number that needs to be checked if it is present or not

Output#
Return True if the target number is found and False otherwise

Sample input#
2D_list  =[[10, 11, 12, 13],
           [14, 15, 16, 17],
           [27, 29, 30, 31],
           [32, 33, 39, 50]]

number = 30
Sample output#
result = True

The time complexity using binary search is O(logn + logm)

"""
def find_in(lst, key):
    rows = len(lst)
    if lst is None:
        return False
    cols = len(lst[0])
    if cols == 0:
        return False
    i = 0
    j = rows - 1
    if rows > 1:
        while i <= j:
            mid = i + (j-i) // 2
            if key == lst[mid][cols - 1]:
                return True
            if key > lst[mid][cols - 1]:
                i = mid + 1
            else:
                j = mid - 1
        if key > lst[mid][cols - 1]:
            rows = mid + 1
        else:
            rows = mid
    else:
        rows = 0
    if rows >= len(lst):
        return False
    i =0
    j = cols - 1
    while i <= j:
        mid = i + (j-i) // 2
        if key == lst[rows][mid]:
            return True
        if key > lst[rows][mid]:
            i = mid + 1
        else:
            j = mid - 1
    return False


# Driver to test above code
if __name__ == '__main__':

    lst = [
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [27, 29, 30, 31],
        [32, 33, 39, 50]
    ]

    # Example 1
    print(find_in(lst, 30))

    # Example 2
    print(find_in(lst, 100))
