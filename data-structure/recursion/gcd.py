def gcd(var1, var2):
    if var1 == var2:
        return var1
    if var1 > var2:
        return gcd(var1-var2, var2)
    else:
        return gcd(var1, var2-var1)


# Driver Code
number1 = 6
number2 = 9
print(gcd(number1, number2))
