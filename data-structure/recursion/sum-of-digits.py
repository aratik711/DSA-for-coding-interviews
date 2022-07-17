def sumDigits(var):
    if var == "":
        return 0
    else:
        return int(var[0]) + sumDigits(var[1:])


# Driver Code
print(sumDigits("345"))
