"""

The time complexity for this algorithm is O(n).

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

def search(lst, value):
    curr_node = lst.head
    while curr_node is not None:
        if curr_node.data == value:
            return True
        curr_node = curr_node.next
    return False



lst = LinkedList()
insertAtTail(lst, 0)
insertAtTail(lst, 1)
insertAtTail(lst, 2)
insertAtTail(lst, 3)
insertAtTail(lst, 4)
insertAtTail(lst, 5)
insertAtTail(lst, 6)
lst.print_list()
print(search(lst, 3))
print(search(lst, 20))
print(search(lst, 1))
