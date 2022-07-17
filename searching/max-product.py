"""

Implement a function find_max_prod(lst) that takes a list of numbers and returns a maximum product pair.

Input#
A list of integer numbers

Output#
Two integers

Sample input#
lst = [1, 3, 5, 2, 6]
Sample output#
result1, result2 = 5, 6

We have traversed the list in a single loop. So, the time complexity is O(n)
"""
from decimal import Decimal

def find_max_prod(lst):
    max1 = lst[0]
    max2 = Decimal('-Infinity')
    min1 = lst[0]
    min2 = Decimal('Infinity')
    for number in lst:
        if number > max1:
            max2 = max1
            max1 = number
        elif number > max2:
            max2 = number
        if number < min1:
            min2 = min1
            min1 = number
        elif number < min2:
            min2 = number

    if max1*max2 > min1*min2:
        return max2, max1
    else:
        return min2, min1


# Driver to test above code
if __name__ == '__main__':

    lst = [1, 3, 5, 2, 6]
    num1, num2 = find_max_prod(lst)
    print(num1, num2)

    lst = [1, -3, -5, 2, 6]
    num1, num2 = find_max_prod(lst)
    print(num1, num2)
