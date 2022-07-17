def sort(arr, length):
    if length <= 1:
        return
    sort(arr, length - 1)
    lastElement = arr[length-1]
    temp = length - 2
    while (temp >= 0 and arr[temp] > lastElement):
        arr[temp+1] = arr[temp]
        temp = temp - 1
    arr[temp+1] = lastElement



# Driver Code
testVariable = [5, 4, 2, 3, 1]
print("Original Array ---> " + str(testVariable))

sort(testVariable, len(testVariable))
print("Modified Array ---> " + str(testVariable))
