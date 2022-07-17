"""

In a given unsorted list, the maximum sum of a continuous sublist is the one whose elements, when added together, give the largest possible sum.
Given an integer list and its size, return the maximum sublist sum. The list may contain both positive and negative integers and is unsorted.

Input#
List of integers lst
Window size k
Output#
Maximum sub-list of size k
Sample input#
lst = [2, 1, 5, 1, 3, 2]
k = 3
Sample output#
result = 9

The time complexity of this solution is O(N)
 because the entire list is iterated over once.

"""
def max_sub_list_of_size_k(lst, k):
    max_sum, window_sum = 0, 0
    window_start = 0
    for window_end in range(len(lst)):
        window_sum += lst[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= lst[window_start]
            window_start += 1
    return max_sum


# Driver code to test above function
if __name__ == '__main__':

  print("Maximum sum of a sub-list of size K: " + str(max_sub_list_of_size_k([2, 1, 5, 1, 3, 2], 3)))
  print("Maximum sum of a sub-list of size K: " + str(max_sub_list_of_size_k([2, 3, 4, 1, 5], 2)))
