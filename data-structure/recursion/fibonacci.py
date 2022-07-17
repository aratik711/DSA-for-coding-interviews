def fibonacci(var):
    if var <= 1:
        return var
    return fibonacci(var-1) + fibonacci(var-2)

# Driver Code
testVariable = 7
print(fibonacci(testVariable))
