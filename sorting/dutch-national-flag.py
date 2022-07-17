"""

Implement a function that sorts a list of 0s
0s
, 1s
1s
 and 2s
2s
. This is called the Dutch National Flag Problem. Since the number O
O
 can be represented by the blue color, 1
1
 by the white color, and 2
2
 as the red color, the task is to transform the list input to the Dutch flag.

Try solving this problem in-place and in linear time without using any extra space.

Input#
An array of 0s, 1s, 2s

Output#
An array where the numbers 0
0
, 1
1
, and 2
2
 are sorted

Sample input#
lst = [2, 0, 0, 1, 2, 1, 0]
Sample output#
result = [0, 0, 0, 1, 1, 2, 2]

Since we are arranging the elements of the list in a single iteration, the complexity is O(n)

"""
def dutch_national_flag(lst):
    size = len(lst)
    i = 0
    mid = 0
    j = size - 1
    while mid <= j:
        if lst[mid] == 0:
            lst[i], lst[mid] = lst[mid], lst[i]
            i += 1
            mid += 1
        elif lst[mid] == 2:
            lst[mid], lst[j] = lst[j], lst[mid]
            j -= 1
        elif lst[mid] == 1:
            mid += 1
    return lst


# Driver to test above code
if __name__ == '__main__':

    lst = [2, 0, 0, 1, 2, 1]

    print(dutch_national_flag(lst))
