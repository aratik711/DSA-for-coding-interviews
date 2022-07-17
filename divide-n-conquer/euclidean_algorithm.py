"""

Given two integers x and y, calculate the largest number that divides both of them without leaving a remainder.

Input#
Two integers x and y

Output#
An integer which will be x and y's GCD

Sample input#
x = 1071
y = 462
Sample output#
result = 21

The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger value of the two is replaced by the difference between both numbers.

The time complexity of this solution is O(log min(x, y))

"""
def euclidean_algorithm(x, y):
    print(x, y)
    if x == 0:
        return y
    return euclidean_algorithm(y%x, x)

# Driver code to test above function
if __name__ == '__main__':

    num1 = 1071
    num2 = 462

    result = euclidean_algorithm(num1, num2)
    print('The GCD of ', num1, 'and ', num2, 'is ', result)
