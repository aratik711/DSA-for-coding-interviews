def replace(arr, currentIndex):
    if currentIndex < len(arr):
        if arr[currentIndex] < 0:
            arr[currentIndex] = 0
        replace(arr, currentIndex + 1)
    return


# Driver Code
array = [2, -3, 4, -1, -7, 8]
print("Original Array --> " + str(array))
replace(array, 0)
print("Modified Array --> " + str(array))
