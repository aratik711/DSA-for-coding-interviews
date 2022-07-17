def findSquare(num):
    if num == 0:
        return 0
    else:
        return findSquare(num-1) + (2*num) - 1


# Driver Code
targetNumber = 5
print(findSquare(targetNumber))
