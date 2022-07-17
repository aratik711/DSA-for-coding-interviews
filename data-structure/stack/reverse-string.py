from stack import Stack
def reverse_string(stack ,str):
    for i in range(len(str)):
        stack.push(str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))
