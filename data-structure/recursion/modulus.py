def mod(dividend, divisor):
    if divisor == 0:
        print("Divisor 0")
        return 0
    if dividend < divisor:
        return dividend
    else:
        return mod(dividend-divisor, divisor)

# Driver Code
print(mod(10, 4))
