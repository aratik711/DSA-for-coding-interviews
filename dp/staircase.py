"""

A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a function to count the number of possible ways that the child can run up the stairs.

Input#
An integer that represents the number of stairs

Output#
An integer that represents the number of ways that those stairs can be climbed

Sample input#
 n = 4
Sample output#
result = 7

The time complexity remains O(n)
, but the extra space used is reduced to O(1)

"""
def count_ways(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    third_last = 1
    second_last = 1
    last = 2
    current = 0
    for i in range(3, n+1):
        current = last + second_last + third_last
        third_last, second_last, last = second_last, last, current
    return current

# Driver code to test the above function
if __name__ == '__main__':
    print("Number of ways: ", count_ways(3))
