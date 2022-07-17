"""

Given a list of integers of size 2^n
2
n

 and taking all the boundary cases in consideration, shuffle the list, without using extra space.

Input#
lst (list of integers)
Output#
lst (shuffled list if the size of the list is in 2^n
2
n

, otherwise the same list)
Sample input#
lst = [1, 2, 3, 4, 5, 6, 7, 8]
Sample output#
lst = [1, 5, 2, 6, 3, 7, 4, 8]

This solution gives the worst-case time complexity of O(n lg n)


"""
import math

def shuffle_list_recursive(lst, left, right):
    if right - left > 1:
        mid = (left+right) // 2
        temp = mid + 1
        middle = (left+mid) // 2
        for i in range(middle + 1, mid+1):
            lst[i], lst[temp] = lst[temp], lst[i]
            temp += 1
        shuffle_list_recursive(lst, left, mid)
        shuffle_list_recursive(lst, mid+1, right)

def shuffle_list(lst):
    log = math.log2(len(lst)) % 2
    if len(lst) != 2 and (log == 1 or log == 0):
        shuffle_list_recursive(lst, 0, len(lst) - 1)

# Driver code to test above function
if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    shuffle_list(lst)
    print(lst)
