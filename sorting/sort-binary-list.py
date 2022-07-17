"""

Implement a function sort_binary_list(lst) that takes a binary list of numbers and returns a sorted list.

Input#
A list having binary numbers

Output#
A sorted binary list

Sample input#
lst = [1, 0, 1, 0, 1, 1, 0, 0]
Sample output#
result = [0, 0, 0, 0, 1, 1, 1, 1]

Since the list is iterated only once, the time complexity is O(n)

"""
def sort_binary_list(lst):
    j = 0
    for i in range(len(lst)):
        if lst[i] < 1:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
    return lst

# Driver to test above code
if __name__ == '__main__':

    lst = [1, 0, 1, 0, 1, 0, 1, 0]
    result = sort_binary_list(lst)

    print(result)
