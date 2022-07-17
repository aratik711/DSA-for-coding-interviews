"""

Suppose that you are given an array of contiguous integers starting from 1 to n, with one integer missing in the middle
Given a list of contiguous integers starting from 1 (with one missing integer in between), find the missing integer. If there is no number missing, return -1.

Input#
List of contiguous integers starting from 1

Output#
integer (missing integer or -1
−1
 if no missing integer)

Sample input#
lst = [1, 2, 3, 4, 6, 7, 8, 9, 10]
Sample output#
result = 5

Since this approach follows the same process as a binary search would, the time complexity of this solution is O(log n)

"""
def missing_number(lst):
    left_limit = 0
    right_limit = len(lst)-1
    if lst[left_limit] is not 1:
        return 1
    while left_limit <= right_limit:
        middle = (left_limit + right_limit) // 2
        if lst[middle] is not middle + 1 and lst[middle-1] is middle:
            return middle+1
        if lst[middle] is not middle + 1:
            right_limit = middle - 1
        else:
            left_limit = middle + 1
    return -1

# Driver code to test above function
if __name__ == '__main__':
  print(missing_number([1, 2, 4]))
  print(missing_number([1, 2, 3, 4, 6]))
  print(missing_number([2, 3, 4, 5, 6]))
  print(missing_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
