"""

Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the sorted order of the input list.

Output#
A list with negative elements at the left and positive elements at the right

Sample Input#
[10,-1,20,4,5,-9,-6]
Sample Output#
[-1,-9,-6,10,20,4,5]

Time complexity O(n)

"""
def rearrange(lst):
    # Sol 1
    # pos = 0
    # neg = 0
    # for i in range(len(lst)):
    #     ele = lst[i]
    #     if ele < 0:
    #         lst[pos] = lst[neg]
    #         lst[neg] = ele
    #         neg += 1
    #         pos += 1
    #     else:
    #         pos += 1
    # return lst
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

print(rearrange([-1, 2, -3, -4, 5]))
print(rearrange([300, -1, 3, 0]))
print(rearrange([0, 0, 0, -2]))
