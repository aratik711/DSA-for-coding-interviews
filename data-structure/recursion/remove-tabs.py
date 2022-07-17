def remove(str):
    if not str:
        return ""
    if str[0] == "\t" or str[0] == " ":
        return remove(str[1:])
    else:
        return str[0] + remove(str[1:])

# Driver Code
print(remove("Hello\tWorld"))
