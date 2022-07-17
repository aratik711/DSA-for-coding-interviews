def recursiveLength(var):
    if var == "":
        return 0
    else:
        return 1 + recursiveLength(var[1:])

# Driver Code
testVariable = "Educative"
print (recursiveLength(testVariable))
