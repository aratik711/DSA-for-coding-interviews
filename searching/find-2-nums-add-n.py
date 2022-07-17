"""

In this problem, you have to implement the find_sum(lst, n) function which will take a list lst and number n as inputs and return two numbers from the list that add up to n.

Input#
A list and a number n

Output#
A list with two integers a and b that add up to n

Sample input#
lst = [1, 21, 3, 14, 5, 60, 7, 6]
n = 81
Sample output#
result = [21, 60]

The time complexity of the solution above is in O(n)

"""
def find_sum(lst, n):
    found_values = set()
    for ele in lst:
        if n - ele in found_values:
            return [ele, n-ele]
        found_values.add(ele)
    return False

# Driver to test above code
if __name__ == '__main__':

  print(find_sum([1, 3, 2, 4], 6))
