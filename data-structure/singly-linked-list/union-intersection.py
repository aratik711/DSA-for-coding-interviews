"""

Input #
Two linked lists.

Output #
A list containing the union of the two lists.
A list containing the intersection of the two lists.
Sample Input #
list1 = 10->20->80->60
list2 = 15->20->30->60->45
Sample Output #
union = 10->20->80->60->15->30->45
intersection = 20->60

Union:
If we did not have to care for duplicates, The runtime complexity of this algorithm would be O(m) where m is the size of the first list. However, because of duplicates, we need to traverse the whole union list. This increases the time complexity to O(l^2)
 where l = m + n. Here, m is the size of the first list, and n is the size of the second list.


Intersection:
The time complexity will be max(O(mn), O(min(m,n)^2))
 where m is the size of the first list and n is the size of the second list.

The term O(mn) comes from the lines 85-95. We traverse the two lists searching the elements of list1 in list2, and generate an intermediate list of size min(m, n)

Next, we remove the duplicates using the remove_duplicates method that takes quadratic time. Hence the term, min(m, n)^2

.

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

def union(lst1, lst2):
    lst1_curr_node = lst1.head
    while lst1_curr_node.next is not None:
        lst1_curr_node = lst1_curr_node.next
    lst1_curr_node.next = lst2.head
    remove_duplicates(lst1)

def intersection(lst1, lst2, lst3):
    lst1_curr_node = lst1.head
    visited = []
    while lst1_curr_node:
        if lst1_curr_node.data not in visited:
            visited.append(lst1_curr_node.data)
        lst1_curr_node = lst1_curr_node.next
    lst2_curr_node = lst2.head
    lst3_curr_node = None
    while lst2_curr_node:
        if lst2_curr_node.data in visited:
            if lst3.head is None:
                lst3.head = Node(lst2_curr_node.data)
                lst3.head.next = None
                lst3_curr_node = lst3.head
            else:
                lst3_curr_node.next = Node(lst2_curr_node.data)
                lst3_curr_node = lst3_curr_node.next
                lst3_curr_node.next = None
        lst2_curr_node = lst2_curr_node.next
    remove_duplicates(lst3)
    return lst3



lst = LinkedList()
insertAtTail(lst, 15)
insertAtTail(lst, 8)
insertAtTail(lst, 22)
lst.print_list()
lst2 = LinkedList()
insertAtTail(lst2, 7)
insertAtTail(lst2, 14)
insertAtTail(lst2, 21)
lst2.print_list()
union(lst, lst2)
lst.print_list()
lst3 = LinkedList()
insertAtTail(lst3, 15)
insertAtTail(lst3, 22)
insertAtTail(lst3, 14)
lst3.print_list()
lst4 = LinkedList()
insertAtTail(lst4, 15)
insertAtTail(lst4, 14)
insertAtTail(lst4, 21)
lst4.print_list()
lst5 = LinkedList()
lst5 = intersection(lst3, lst4, lst5)
lst5.print_list()
