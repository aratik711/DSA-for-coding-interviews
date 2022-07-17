def decimalToBinary(var):
    if var <= 1:
        return str(var)
    else:
        return decimalToBinary(var//2) + decimalToBinary(var%2)


# Driver Code
testVariable = 11
print(decimalToBinary(testVariable))
