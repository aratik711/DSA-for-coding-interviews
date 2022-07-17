"""

A girl lost the key to her locker (note: The key is only numeric). She remembers the number of digits N as well as the sum S of all the digits of her password. She also knows that her password is the largest number of N digits that can be possible with a given sum S.

Implement a function that would help her retrieve her key.

Input#
The number of digits and the sum of those digits

Output#
The largest number that can be created (or the key) as a list

Sample input#
sum_of_digits = 20
number_of_digits = 3
Sample output#
result = [9, 9, 2]

The time complexity is O(n)
 because we can simply find the solution in one iteration.
"""

def find_largest_number(digits, sum):
    if sum == 0:
        if digits == 1:
            return [0]
        else:
            return [-1]
    if sum > 9 * digits:
        return [-1]
    result = [0] * digits
    for i in range(digits):
        if sum >= 9:
            result[i] = 9
            sum -= 9
        else:
            result[i] = sum
            sum = 0
    return result

# Driver code to test above function
if __name__ == '__main__':

    sum_of_digits = 20
    number_of_digits = 3

    print(find_largest_number(number_of_digits, sum_of_digits))

    sum_of_digits = 100
    number_of_digits = 2

    print(find_largest_number(number_of_digits, sum_of_digits))
