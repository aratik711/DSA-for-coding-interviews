"""

Your task is to implement an algorithm to determine if a string has all unique characters.

"""
def is_unique_1(str):
    d = dict()
    for i in str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

def is_unique_2(str):
    return len(set(str)) == len(str)

def is_unique_3(str):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    for i in str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True

unique_str = "AbCDefG"
non_unique_str = "non UniqueSTR"

print("Unique String")
print(unique_str)
print("Non-Unique String")
print(non_unique_str, "\n")

print("Solution 1 where input string is unique string")
print(is_unique_1(unique_str))
print("Solution 1 where input string is non-unique string")
print(is_unique_1(non_unique_str), "\n")


print("Solution 2 where input string is unique string")
print(is_unique_2(unique_str))
print("Solution 2 where input string is non-unique string")
print(is_unique_2(non_unique_str), "\n")

print("Solution 3 where input string is unique string")
print(is_unique_3(unique_str))
print("Solution 3 where input string is non-unique string")
print(is_unique_3(non_unique_str))
