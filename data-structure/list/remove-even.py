# Time complexity - O(n)
def remove_even(lst):
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in lst if number % 2 != 0]


print(remove_even([3, 2, 41, 3, 34]))
