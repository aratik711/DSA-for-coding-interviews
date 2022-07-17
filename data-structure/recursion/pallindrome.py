def isPalindrome(var):
    if len(var) <= 1:
        return True
    length = len(var)
    if var[0] == var[length - 1]:
        return isPalindrome(var[1:length-1])
    return False


# Driver Code
print(isPalindrome("madam"))
