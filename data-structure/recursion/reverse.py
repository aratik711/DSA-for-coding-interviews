def reverse(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    return [arr[len(arr) - 1]] + reverse(arr[:len(arr) - 1])


# Driver Code
array = [1, 2, 3, 4]
print(reverse(array))
