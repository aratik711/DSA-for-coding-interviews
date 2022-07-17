"""

Given a tall skyscraper and a few eggs, write a function to figure out how many tries it would take to find which floor of the skyscraper from which the eggs can be safely dropped without breaking. Here are some rules;

An egg that survives a fall can be used again. A broken egg must be discarded
The effect of a fall is the same for all eggs
If an egg breaks when dropped, then, it would break if dropped from a higher floor
If an egg survives a fall, then it would survive a shorter fall
Input#
Two integers that represent the number of stories of the skyscraper and number of eggs respectively

Output#
The least number of egg-droppings to figure out the critical floor

Sample input#
eggs = 6
floors = 15
Sample output#
result = 4

The time complexity of this code is in O(eggs*log(floors))
"""
def binomial_coeff(x, n, k):
    """
    Find sum of binomial coefficients xCi (where i varies from 1 to n).
    If the sum becomes more than K
    :param x: Mid point
    :param n: Eggs
    :param k: Floor
    :return: Binomial Coefficient
    """
    sum = 0
    term = 1
    for i in range(1, n+1):
        if sum < k:
            term *= x - i + 1
            term //= i
            sum += term
    return sum

def egg_drop(eggs, floors):
    if eggs <= 0:
        return 0
    if floors == 1 or floors == 0:
        return floors
    if eggs == 1:
        return floors
    low = 1
    high = floors
    while low < high:
        mid = (low+high)//2
        if binomial_coeff(mid, eggs, floors) < floors:
            low = mid + 1
        else:
            high = mid
    return low
# Driver code to test the above function
if __name__ == '__main__':

    print(egg_drop(2, 13))
