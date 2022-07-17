"""

A list of duplicate integers

Note: All the integers are less than the size of the list.

Output#
A list with the duplicates if they exist, and an empty list if they don’t

Sample input#
  lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
Sample output#
  result = [1, 3, 7]

Since the list is traversed only once and removing duplication also takes O(n)
 time, the overall time complexity of this solution is O(n)

"""
def find_duplicates(lst):
    seen = {}
    dups = []
    for x in lst:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dups.append(x)
            seen[x] += 1
    return dups


# Driver to test above code
if __name__ == '__main__':

    lst = [1, 2, 5, 1, 4, 2, 1, 1]

    result = find_duplicates(lst)
    print (result)
