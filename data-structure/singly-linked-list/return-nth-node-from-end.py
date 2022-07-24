"""

Input #
A linked list and a position N.

Output #
The value of the node n positions from the end. Returns -1 if n is out of bounds.

Sample Input #
LinkedList = 22->18->60->78->47->39->99 and n = 3
Sample Output #
47

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


def find_nth(lst, n):
    length = get_length(lst)
    if length < n or length == 0:
        return -1
    elif length == 1 and n != 1:
        return -1
    curr_node = lst.head
    count = 1
    while count != n:
        curr_node = curr_node.next
        count += 1
    nth_node = lst.head
    while curr_node.next is not None:
        curr_node = curr_node.next
        nth_node = nth_node.next
    return nth_node.data



lst = LinkedList()
insertAtTail(lst, 15)
insertAtTail(lst, 22)
insertAtTail(lst, 8)
insertAtTail(lst, 7)
insertAtTail(lst, 14)
insertAtTail(lst, 21)
lst.print_list()
print(find_nth(lst, 4))
print(find_nth(lst, 5))
print(find_nth(lst, 8))
print(find_nth(lst, 2))
