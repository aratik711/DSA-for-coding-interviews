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

def attach_to_head(lst, src_value):
    if lst.head is None:
        new_node = Node(src_value)
        lst.head = new_node
    else:
        new_node = Node(src_value)
        curr_node = lst.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.next = lst.head

def detect_loop(lst):
    if lst.head is None:
        return False
    else:
        curr_node = lst.head
        while curr_node.next is not None:
            if curr_node.next.data == lst.head.data:
                return True
            curr_node = curr_node.next
        return False


lst = LinkedList()
insertAtTail(lst, 0)
insertAtTail(lst, 1)
insertAtTail(lst, 2)
insertAtTail(lst, 3)
lst.print_list()
print(detect_loop(lst))
lst2 = LinkedList()
insertAtTail(lst2, 0)
insertAtTail(lst2, 1)
insertAtTail(lst2, 2)
insertAtTail(lst2, 3)
attach_to_head(lst2, 4)
print(detect_loop(lst2))
