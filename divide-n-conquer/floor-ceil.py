"""

A floor function takes a real number x
 and returns the greatest Integer less than or equal to x.
A ceiling function takes a real number x
 and returns the smallest Integer greater than or equal to x.

A list lst containing integers
An integer x
Output#
Two Integer variables containing floor
floor
 and ceiling
ceiling
 value of x
Sample input#
lst = [1, 2, 3, 5, 7]
x = 3
Sample output#
result = 2, 5

The running complexity for this is same as the binary search i.e., O(log(n))
, where n
 is the size of the list.



"""
def find_floor(lst, low, high, x):
    if low > high:
        return -1
    if x >= lst[high]:
        return lst[high]
    mid = (low+high) // 2
    if lst[mid] == x:
        return lst[mid]
    if x < lst[mid]:
        return find_floor(lst, low, mid - 1, x)
    return find_floor(lst, mid+1, high, x)

def find_ceiling(lst, low, high, x):
    if x <= lst[low]:
        return lst[low]
    if x > lst[high]:
        return -1
    mid = (low+high) // 2
    if lst[mid] == x:
        return lst[mid]
    elif lst[mid] < x:
        if mid+1 <= high and x <= lst[mid+1]:
            return lst[mid+1]
        else:
            return find_ceiling(lst, mid+1, high, x)
    else:
        if mid - 1 >= low and x > lst[mid-1]:
            return lst[mid]
        else:
            return find_ceiling(lst, low, mid - 1, x)


# Driver code to test above function
if __name__ == '__main__':
    lst = [1, 2, 3, 5, 7]
    x = 4
    print("Floor and Ceil of ", x, ": ", find_floor_ceiling(lst, x))
