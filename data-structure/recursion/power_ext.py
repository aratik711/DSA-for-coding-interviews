def power(N, P):
    if (P==0):
        result=1
    elif (P==1):
        result=N
    elif (P>0 and P%2==0):
        result = power(N, P/2)
        return result*result
    elif (P>0 and P%2!=0):
        result = power(N, P-1)
        return N*result
    elif (P<0):
        result = 1/power(N, abs(P))
    return result

print(power(2,-2))
