def sumTill(num):
    if num == 1:
        return num
    else:
        return num + sumTill(num-1)


# Driver Code
targetNumber = 5
print(sumTill(targetNumber))
