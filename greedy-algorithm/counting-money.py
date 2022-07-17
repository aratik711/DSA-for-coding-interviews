"""

Given an infinite number of quarters (25 cents)
(25cents)
, dimes (10 cents)
(10cents)
, nickels (5 cents)
(5cents)
, and pennies (1 cent)
(1cent)
, implement a function to calculate the minimum number of coins to represent v
v
 cents.

Input#
A variable v (total money to convert to coins) and a list of available coins

Output#
The minimum number of coins among the available coins that add up to the original number v, i.e., the coins represent v cents

Sample input#
v = 19
available_coins = [1, 5, 10, 25]
Sample output#
result = [10, 5, 1, 1, 1, 1]

Time complexity O(n^2)
"""
def find_min_coins(v, coins_available):
    result = []
    n = len(coins_available)
    for i in reversed(range(n)):
        while v >= coins_available[i]:
            v -= coins_available[i]
            result.append(coins_available[i])
    return result
# Main program to test the above code
if __name__ == "__main__":

    coins_available = [1, 5, 10, 25] # The available coins are in increasing order
    print(find_min_coins(19, coins_available))
