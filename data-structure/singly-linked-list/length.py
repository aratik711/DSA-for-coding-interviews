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

def get_length(lst):
    curr_node = lst.head
    count = 0
    while curr_node is not None:
        count += 1
        curr_node = curr_node.next
    return count


lst = LinkedList()
insertAtTail(lst, 0)
insertAtTail(lst, 1)
insertAtTail(lst, 2)
insertAtTail(lst, 3)
lst.print_list()
print(get_length(lst))
