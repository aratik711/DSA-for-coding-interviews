"""

Given an integer list, return the maximum sublist sum. The list may contain both positive and negative integers and is unsorted.
Input#
a list lst
Output#
a number (maximum subarray sum)

Sample input#
-4,2,-5,1,2,3,6,-5,1

Sample output#
largest_sum = 12

Time complexity O(n)

"""
def find_max_sum_sublist(lst):
    curr_max = lst[0]
    global_max = lst[0]
    for i in range(1, len(lst)):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
        if global_max < curr_max:
            global_max = curr_max
    return global_max


print(find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1]))
