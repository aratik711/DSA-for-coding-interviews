"""

Input

The profit that can be gained by each piece of the jewelry
The number of pieces of jewelry
The weight of each piece of jewelry
The maximum weight that the knapsack can hold
The length of the array
Output#
The maximum profit that can be returned

Sample input#
    profit = [60, 100, 120]
    profits_length = 3
    weight = [10, 20, 30]
    capacity = 50 # knapsack weight

Sample output#
    result = 220

While the time complexity remains the same, i.e., O(N*C)
, the space complexity of this solution is brought down to O(C)
, where ‘N’ represents total items and ‘C’ is the maximum capacity.



"""
def knap_sack(profits, profits_length, weights, capacity):
    weights_length = profits_length
    if capacity <= 0 or profits_length == 0:
        return 0
    lookup_table = [0 for x in range(capacity+1)]
    for i in range(1, profits_length):
        if weights[0] <= i:
            lookup_table[i] = profits[0]
    for i in range(1, profits_length):
        for j in reversed(range(capacity + 1)):
            profit1 = 0
            profit2 = 0
            if weights[i] <= j:
                profit1 = profits[i] + lookup_table[j-weights[i]]
            profit2 = lookup_table[j]
            lookup_table[j] = max(profit1, profit2)
    return lookup_table[capacity]

# Driver code to test the above function
if __name__ == '__main__':
    profits = [1, 6, 10, 16]  # The values of the jewelry
    weights = [1, 2, 3, 5]  # The weight of each
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 7))
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 6))
