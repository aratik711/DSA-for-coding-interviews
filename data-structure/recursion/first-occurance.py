"""

Input#
A variable arr that contains the array that will be searched.
A variable testVariable, being the number that will be searched.
A variable currentIndex that contains the starting index of the arr array.
Output#
Index of the first occurrence of testVariable in arr

Sample Input#
arr = [9, 8, 1, 8, 1, 7]
targetNumber = 1
currentIndex = 0
Sample Output#
2

"""
def firstIndex(arr, var, currentIndex):
    if len(arr) == currentIndex:
        return -1
    if arr[currentIndex] == var:
        return currentIndex
    return firstIndex(arr, var, currentIndex+1)


# Driver Code
arr = [9, 8, 1, 8, 1, 7]
testVariable = 1
currentIndex = 0

print(firstIndex(arr, testVariable, currentIndex))
