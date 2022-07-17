def printPascal(var):
    if var == 0:
        return [1]
    else:
        line = [1]
        previousLine = printPascal(var-1)
        for i in range(len(previousLine)-1):
            line.append(previousLine[i] + previousLine[i+1])
        line += [1]
    return line


# Driver Code
testVariable = 5
print(printPascal(testVariable))
