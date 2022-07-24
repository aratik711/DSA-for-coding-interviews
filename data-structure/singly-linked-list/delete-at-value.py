"""

The time complexity will be O(n).

"""

from node import Node
from node import LinkedList

def insertAtTail(lst, value):
    if lst.head is None:
        new_node = Node(value)
        lst.head = new_node
    else:
        new_node = Node(value)
        curr_node = lst.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.next = None

def delete(lst, value):
    curr_node = lst.head
    if curr_node and curr_node.data == value:
        lst.head = lst.head.next
        curr_node = None
        return True
    curr_node = curr_node.next
    prev_node = None
    while curr_node is not None:
        if curr_node.data == value:
            prev_node.next = curr_node.next
            curr_node = None
            return True
        prev_node = curr_node
        curr_node = curr_node.next
    return False


lst = LinkedList()
insertAtTail(lst, 0)
insertAtTail(lst, 1)
insertAtTail(lst, 2)
insertAtTail(lst, 3)
lst.print_list()
print(delete(lst, 0))
print(delete(lst, 1))
print(delete(lst, 8))
print(delete(lst, 2))
print(delete(lst, 4))
lst.print_list()
