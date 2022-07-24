"""

Input: #
A list of integers

Output: #
The smallest number in the list

Sample Input #
arr = [9,2,3,6]
Sample Output #
2

Since the entire list is iterated over once, this algorithm is in linear time, O(n)

"""
def find_minimum(arr):
    min = arr[0]
    for ele in arr[1:]:
        if min > ele:
            min = ele
    return min

print(find_minimum([100, 12, 34, 40]))
print(find_minimum([4, 5, 0, 3, 6]))
