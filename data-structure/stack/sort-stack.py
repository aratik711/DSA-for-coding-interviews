"""

A stack of integers.

Output#
The stack with all its elements sorted in descending order.

Sample Input#
stack = [23, 60, 12, 42, 4, 97, 2]
Sample Output#
result = [97, 60, 42, 23, 12, 4, 2]
## 2 was the value last pushed

Time complexity O(n^2)
"""
from stack import Stack

def sort_stack(stack):
    if not stack.is_empty():
        value = stack.pop()
        sort_stack(stack)
        insert(stack, value)

def insert(stack, value):
    if stack.is_empty() or value < stack.peek():
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)


if __name__ == "__main__" :
    # Creating and populating the stack
    stack = Stack()
    stack.push(2)
    stack.push(97)
    stack.push(4)
    stack.push(42)
    stack.push(12)
    stack.push(60)
    stack.push(23)
    # Sorting the stack
    sort_stack(stack)
    # Printing the sorted stack
    print("Stack after sorting")
    print([stack.pop() for i in range(stack.size())])
