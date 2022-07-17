def avg(arr, currentIndex = 0):
    if currentIndex == len(arr) - 1:
        return arr[currentIndex]
    if currentIndex == 0:
        return ((arr[currentIndex] + avg(arr, currentIndex+1))/len(arr))
    return (arr[currentIndex] + avg(arr, currentIndex+1))


# Driver code
arr = [10, 2, 3, 4, 8, 0]
print(avg(arr))
