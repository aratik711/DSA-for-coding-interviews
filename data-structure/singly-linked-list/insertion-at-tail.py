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



lst = LinkedList()
insertAtTail(lst, 0)
insertAtTail(lst, 1)
insertAtTail(lst, 2)
insertAtTail(lst, 3)
lst.print_list()
