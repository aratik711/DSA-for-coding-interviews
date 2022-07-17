"""

Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write some code to calculate the number of ways to represent n cents.

Input#
The values of the coins available to represent the cents with (the denominations), the number of denominations, and the number of cents

Output#
The number of ways that the given number of cents can be represented

Sample input#
amount = 10 # num of cents
denoms = [25, 10, 5, 1]
denomsLength = 4
Sample output#
result = 4 # num of ways to make change for 10 cents
The change for 10 cents can be made in the following 4 ways:

{1,1,1,1,1,1,1,1,1,1}

{5,1,1,1,1,1}

{5,5}

{10}


We first create a lookup table of length amount + 1 and set the first value of the lookup table to 1. You’ll see why we do that in a bit.

Each index in the lookup table represents an amount and the number of ways to represent that amount using the given denomination. So, in the end, the value in lookup_table[3] would have the number of ways to represent the amount 3

The code then iterates through the given denominations. It starts with the first denomination, which is 25
 in our given example, and checks if it’s less than or equal to the given amount. If that is the case, we continue; otherwise, we move on to the next denomination.

Let’s suppose we continue. We then add the number of ways to represent j - denoms[i] coins to j coins, where j is the denomination in the first iteration, which puts j - denoms[i] at 0


Then, we add the value of lookup_table[0] to the value of lookup_table[j]. This is why we set the first value of the lookup table to 0. This process continues until each index has the correct amount. In the end, we return the value in the lookup table at the index amount.

The crux of the code is that the number of ways there are to represent the amount x is the number of ways to represent the amount y-n where y = x-n.

The time complexity is O(amount*denomslength)
. However, the space complexity is reduced to O(amount)
 in this case.
"""
def count_change(denoms, denoms_length, amount):
    if denoms_length <= 0 or amount <= 0:
        return 0
    lookup_table = [0] * (amount+1)
    lookup_table[0] = 1
    # Pick all coins one by one and update the lookup_table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(denoms_length):
        for j in range(denoms[i], amount+1):
                lookup_table[j] += lookup_table[j - denoms[i]]
    return lookup_table[amount]

# Driver code to test the above function
if __name__ == '__main__':

    denoms = [25, 10, 5, 1]
    print(count_change(denoms, len(denoms), 10))
