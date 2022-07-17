"""

    Input: 123
    Output: "123"
    Input: -123
    Output: "-123"

"""
def int_to_str(input):
    if input < 0:
        is_negative = True
        input *= -1
    else:
        is_negative = False
    output = []
    if input == 0:
        output.append('0')
    else:
        while input > 0:
            output.append(chr(ord('0') + input % 10))
            input //= 10
        output = output[::-1]
    output = ''.join(output)
    if is_negative:
        return '-' + output
    else:
        return output

input_int = 123
print(input_int)
print(type(input_int))

output_str = int_to_str(input_int)
print(output_str)
print(type(output_str))
