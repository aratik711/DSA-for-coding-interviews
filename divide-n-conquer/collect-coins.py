"""

You’ve been given an integer list representing the height of each stack of coins. The task is to calculate the minimum number of straight lines that pass through all the coins.

Input#
lst A list of coin stacks
Output#
integer Minimum number of steps to collect the coins
Sample input#
lst = [2, 5, 1, 2, 3, 1]
Sample output#
result = 5

The for loop in the initial call requires O(n)
 effort. Subsequently, recursive calls are made to the function, where the for loop runs roughly n/2 steps in each call. In the worst case, the number of times the call is repeated depends on the height of the highest stack of coins. So, the complexity should be O(n*h)


"""
def minimum_steps_recurse(lst, left, right, h):
    if left >= right:
        return 0
    minimum_height = left
    for i in range(left, right):
        if lst[i] < lst[minimum_height]:
            minimum_height = i
    return min(right-left, minimum_steps_recurse(lst, left, minimum_height, lst[minimum_height]) + minimum_steps_recurse(lst, minimum_height+1, right, lst[minimum_height]) + lst[minimum_height]-h)

def minimum_steps(lst):
    return minimum_steps_recurse(lst, 0, len(lst), 0)
# Driver code to test above function
if __name__ == '__main__':
  lst = [2, 1, 2, 5, 1]
  print('Minimum number of steps:', minimum_steps(lst))
