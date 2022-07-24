"""

Input #
A linked list.

Output #
A list with all the duplicates removed.

Sample Input #
LinkedList = 1->2->2->2->3->4->4->5->6
Sample Output #
LinkedList = 1->2->3->4->5->6

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

def remove_duplicates(lst):
    visited = []
    curr_node = lst.head
    prev_node = None
    while curr_node:
        if curr_node.data in visited:
            prev_node.next = curr_node.next
            curr_node = None
        else:
            visited.append(curr_node.data)
            prev_node = curr_node
        curr_node = prev_node.next

lst = LinkedList()
insertAtTail(lst, 0)
insertAtTail(lst, 1)
insertAtTail(lst, 2)
insertAtTail(lst, 2)
insertAtTail(lst, 3)
insertAtTail(lst, 3)
insertAtTail(lst, 0)
insertAtTail(lst, 4)
lst.print_list()
remove_duplicates(lst)
lst.print_list()
lst2 = LinkedList()
insertAtTail(lst2, 0)
insertAtTail(lst2, 1)
insertAtTail(lst2, 2)
insertAtTail(lst2, 3)
insertAtTail(lst2, 4)
lst2.print_list()
remove_duplicates(lst2)
lst2.print_list()
