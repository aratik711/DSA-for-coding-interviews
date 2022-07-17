"""

    "123" -> 123
    "-12332" -> -12332
    "554" -> 554

"""
def str_to_int(input):
    output = 0
    if input[0] == '-':
        id = 1
        is_negative = True
    else:
        id = 0
        is_negative = False
    for i in range(id, len(input)):
        place = 10**(len(input) - (i+1))
        digit = ord(input[i]) = ord('0')
        output += place*digit
    if is_negative:
        return -1 * output
    else:
        return output


s = "554"
x = str_to_int(s)
print(type(x))

s = "123"
print(str_to_int(s))

s = "-123"
print(str_to_int(s))
