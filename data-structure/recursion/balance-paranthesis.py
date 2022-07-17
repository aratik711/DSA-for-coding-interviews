def balanced(arr, start = 0, currentIndex = 0):
    if start == len(arr):
        return currentIndex == 0
    if currentIndex < 0:
        return False
    if arr[start] == "(":
        return balanced(arr, start + 1, currentIndex + 1)
    elif arr[start] == ")":
        return balanced(arr, start + 1, currentIndex - 1)


# Driver Code
testVariable = ["(", "(", ")", ")", "(", ")"]
print(balanced(testVariable))
