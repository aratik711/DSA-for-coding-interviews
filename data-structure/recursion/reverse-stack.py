import stack as s:

def insertAtBottom(stack, item):
    if s.isEmpty(stack):
        s.push(stack, item)
    else:
        temp = s.pop(stack)
        insertAtBottom(stack, item)
        s.push(stack, temp)

def reverse(var):
    if not s.isEmpty(var):
        temp = s.pop(var)
        reverse(var)
        insertAtBottom(var, temp)

# Driver Code
myStack = s.createStack()
s.push(myStack, str(8))
s.push(myStack, str(5))
s.push(myStack, str(3))
s.push(myStack, str(2))

print("Original Stack")
s.printStack(myStack)

reverse(myStack)

print("\n\nReversed Stack")
s.printStack(myStack)
