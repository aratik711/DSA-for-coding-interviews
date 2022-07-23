"""

Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

Input:#
A list of numbers (could be floating points or integers)

Output:#
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input#
arr = [1,2,3,4]
Sample Output#
arr = [24,12,8,6]

Since this algorithm only traverses over the list twice, it’s in linear time, O(n)
"""
def find_product(lst):
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i]*right
        right = right * lst[i]
    return product

print(find_product([0, 1, 2, 3]))
