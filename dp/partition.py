"""
Given a list of integers, write a function to find if any two subsets of the input list exist—such that the sum of both subsets is equal. You can assume that the list will only consist of positive integers.

Input#
A list of positive integers

Output#
A boolean. True if such subsets exist and False if they do not

Sample input#
 set = [1, 2, 3, 4]
Sample output#
result = True # (The 2 subsets will be 1,4 & 2,3)

We are trying to populate our lookup_table list in a bottom-up fashion. Essentially, we want to see if we can make all possible sums with every subset. This means, lookup_table[i][j] will be 1 if we can make a sum j from the first i numbers.

So, for each number at index i (0 <= i < set_length) and sum j (0 <= j <= S/2), we have two options:

Exclude the number. In this case, we will see if we can get j from the subset excluding this number: lookup_table[i - 1][j]
Include the number if its value is not more than j. In this case, we will see if we can find a subset to get the remaining sum: lookup_table[i - 1][j - set[i]]
If either of the two above scenarios is true, we can find a subset of numbers with a sum equal to j.

The above solution has time and space complexity of O(N*S)
, where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.


"""
def can_partition(set):
    set_length = len(set)
    sum = 0
    for i in set:
        sum += i
    if sum %2 != 0:
        return False
    sum //= 2
    lookup_table = [[0 for x in range(sum+1)] for y in range(set_length)]
    # populate the sum = 0 columns, as we can always for '0' sum with an empty set
    for i in range(set_length):
        lookup_table[i][0] = True
    for i in range(1, set_length):
        for j in range(1, sum+1):
            if lookup_table[i-1][j]:
                lookup_table[i][j] = lookup_table[i-1][j]
            elif j >= set[i]:
                lookup_table[i][j] = lookup_table[i-1][j-set[i]]
    return lookup_table[set_length-1][sum]


# Driver code to test the above function
if __name__ == '__main__':
    set1 = [1, 2, 3, 4]
    print(can_partition(set1))

    set2 = [1, 1, 3, 4, 7]
    print(can_partition(set2))

    set3 = [2, 3, 4, 6]
    print(can_partition(set3))
