def merge(s1, s2):
    if s1 == "":
        if s2 == "":
            return ""
        return s2
    elif s2 == "":
        return s1
    elif s1[0] > s2[0]:
        return s2[0] + merge(s1, s2[1:])
    return s1[0] + merge(s1[1:], s2)


# Driver Code
string1 = "acu"
string2 = "bst"
print(merge(string1, string2))
