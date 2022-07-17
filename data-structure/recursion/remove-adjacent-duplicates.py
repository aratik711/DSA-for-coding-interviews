def removeDuplicates(str):
    if not str:
        return ""
    elif len(str) == 1:
        return str
    elif str[0] == str[1]:
        return removeDuplicates(str[1:])
    return str[0] + removeDuplicates(str[1:])


# Driver Code
print(removeDuplicates('Hellloo')) #returns Helo
