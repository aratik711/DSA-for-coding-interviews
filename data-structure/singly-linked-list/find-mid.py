"""

Input#
A singly linked list.

Output#
The integer value of the middle node.

Sample Input#
LinkedList = 7->14->10->21
Sample Output#
14

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

def find_mid(lst):
    # Sol 1
    # length = get_length(lst) - 1
    # diff = length // 2
    # count = 0
    # curr_node = lst.head
    # while count < diff:
    #     curr_node = curr_node.next
    #     count += 1
    # return curr_node.data
    # Sol 2
    curr_node = lst.head
    if curr_node.next is None:
        return curr_node.data
    mid_node = curr_node
    curr_node = curr_node.next.next
    while curr_node:
        mid_node = mid_node.next
        curr_node = curr_node.next
        if curr_node:
            curr_node = curr_node.next
    if mid_node:
        return mid_node.data
    return -1

lst = LinkedList()
insertAtTail(lst, 0)
insertAtTail(lst, 1)
insertAtTail(lst, 2)
insertAtTail(lst, 3)
lst.print_list()
print(find_mid(lst))
lst2 = LinkedList()
insertAtTail(lst2, 0)
insertAtTail(lst2, 1)
insertAtTail(lst2, 2)
insertAtTail(lst2, 3)
insertAtTail(lst2, 4)
lst2.print_list()
print(find_mid(lst2))
