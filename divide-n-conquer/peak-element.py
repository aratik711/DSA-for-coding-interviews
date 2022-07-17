"""

A peak element in a list is the element that is greater than or equal to its neighbors. For elements at the end of a list, we only consider its single neighbor.
Given a list and its size, return one of its peak elements.

Input#
lst (list of integers)
Output#
integer (a peak element or -1 if there is no peak element)
Sample input#
lst = [47, 85, 85, 35, 49, 49]
Sample output#
result = 85
or
result = 49

Using this technique, we drop half of the list in every recursive call. So after each call, we are only left with half of the work as compared to the last call. Using this divide and conquer technique, we can solve the above problem in O(log n)

"""
def find_peak_recursive(lst, low, high):
    middle = low + (high - low) // 2
    if (middle == len(lst) - 1 or lst[middle+1] <= lst[middle]) and (middle == 0 or lst[middle-1] <= lst[middle]):
        return middle
    elif (lst[middle-1] > lst[middle]) and middle > 0:
        return find_peak_recursive(lst, low, (middle-1))
    else:
        return find_peak_recursive(lst, middle+1, high)

def find_peak(lst):
    return lst[find_peak_recursive(lst, 0, len(lst) - 1)]
# Driver code to test above function
if __name__ == '__main__':

    # Example: 1
    lst = [7, 11, 22, 13, 4, 0]
    print('One peak point is: ', find_peak(lst))

    # Example: 2
    lst = [0, 3, 100, 2, -1, 0]
    print('One peak point is: ', find_peak(lst))

    # Example: 3
    lst = [6, 5, 4, 3, 2, 1]
    print('One peak point is: ', find_peak(lst))
