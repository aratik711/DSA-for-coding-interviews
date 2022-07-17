"""

Every positive fraction can be represented as the sum of its unique unit fractions. A fraction is a unit fraction, if the numerator is 1 and the denominator is a positive integer. For example, 1/3 is a unit fraction. Such a representation is called an Egyptian Fraction.

Input#
Two variables numerator and denominator

Output#
A list in the format [d1, d2, ..., dn]

Sample input#
  numerator = 2
  denominator = 3
Sample output#
  result = [2, 6]

The time complexity is O(log n)
, because a fraction is always reduced to a form where the denominator is greater than the numerator and the numerator doesn’t divide the denominator.



"""
import math
def egyptian_fraction(numerator, denominator):
    lst_denominator = []
    while numerator != 0:
        x = math.ceil(denominator/numerator)
        lst_denominator.append(x)
        numerator = x * numerator - denominator
        denominator = denominator * x
    return lst_denominator


# Driver code to test above function
if __name__ == '__main__':

    print(egyptian_fraction(6, 14))
    print(egyptian_fraction(2, 3))
