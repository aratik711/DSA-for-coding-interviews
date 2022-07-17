def count(array, key):
    if array == []:
        return 0
    if array[0] == key:
        return 1 + count(array[1:], key)
    else:
        return count(array[1:], key)


# Driver Code
array = [1, 2, 1, 4, 5, 1]
key  = 1
print(count(array, key))
