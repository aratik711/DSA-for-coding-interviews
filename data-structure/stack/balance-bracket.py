"""

A balanced set of brackets is one where the number and type of opening and closing brackets match and that is also properly nested within the string of brackets.

"""
from stack import Stack
def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False

def is_paren_balanced(str):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(str) and is_balanced:
        paren = str[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))
