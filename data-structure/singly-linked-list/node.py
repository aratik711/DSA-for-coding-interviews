class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end="->")
            cur_node = cur_node.next
        print("None")
    def get_head(self):
        return self.head
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None
    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return
            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1
            if cur_node is None:
                return
            prev.next = cur_node.next
            cur_node = None
    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            count += 1
        return count
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        if not curr_1 or not curr_2:
            return
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)
        self.head = _reverse_recursive(cur=self.head, prev=None)
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        self.head = new_head
        return self.head
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()
        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next
    def print_nth_from_last(self, n):
        p = self.head
        q = self.head
        if n > 0:
            count = 0
            while q:
                count += 1
                if count >= n:
                    break
                q = q.next
            if not q:
                print(str(n) + "is greater than number of nodes")
                return
            while p and q.next:
                p = p.next
                q = q.next
            return p.data
        else:
            return None
    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)
    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0
            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev
            q.next = self.head
            self.head = p.next
            p.next = None
    def is_palindrome(self):
        if self.head:
            p = self.head
            q = self.head
            prev = []
            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]
            count = 1
            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True
    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next
            last.next = self.head
            second_to_last.next = None
            self.head = last
    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        sum_llist = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        return sum_llist

#llist = LinkedList()
#llist.append("A")
#llist.append("B")
#llist.append("C")


#llist.insert_after_node(llist.head.next, "D")
#llist.append("E")
#llist.delete_node("B")
#llist.delete_node("E")
#llist.delete_node_at_pos(0)

#llist.print_list()
#print("The length of the linked list calculated recursively is:")
#print(llist.len_recursive(llist.head))
#print("The length of the linked list calculated iteratively is:")
#print(llist.len_iterative())

#llist.append("F")
#llist.append("G")
#llist.swap_nodes("B", "C")
#print("Swapping nodes B and C that are not head nodes")
#llist.print_list()

#llist.swap_nodes("A", "B")
#print("Swapping nodes A and B where key_1 is head node")
#llist.print_list()

#llist.swap_nodes("D", "B")
#print("Swapping nodes D and B where key_2 is head node")
#llist.print_list()

#llist.swap_nodes("C", "C")
#print("Swapping nodes C and C where both keys are same")
#llist.reverse_recursive()
#llist.print_list()
#llist_1 = LinkedList()
#llist_2 = LinkedList()

#llist_1.append(1)
#llist_1.append(5)
#llist_1.append(7)
#llist_1.append(9)
#llist_1.append(10)

#llist_2.append(2)
#llist_2.append(3)
#llist_2.append(4)
#llist_2.append(6)
#llist_2.append(8)

#llist_1.merge_sorted(llist_2)
#llist_1.print_list()
# llist = LinkedList()
# llist.append(1)
# llist.append(6)
# llist.append(1)
# llist.append(4)
# llist.append(2)
# llist.append(2)
# llist.append(4)
#
# print("Original Linked List")
# llist.print_list()
# print("Linked List After Removing Duplicates")
# llist.remove_duplicates()
# llist.print_list()
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
#
# print(llist.print_nth_from_last(4))
# print(llist.print_nth_from_last(4))
# llist_2 = LinkedList()
# llist_2.append(1)
# llist_2.append(2)
# llist_2.append(1)
# llist_2.append(3)
# llist_2.append(1)
# llist_2.append(4)
# llist_2.append(1)
# print(llist_2.count_occurences_recursive(llist_2.head, 1))
# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)
#
# llist.rotate(4)
# llist.print_list()
# llist = LinkedList()
#
#
# llist_2 = LinkedList()
# llist_2.append("A")
# llist_2.append("B")
# llist_2.append("C")
#
# print(llist.is_palindrome())
# print(llist_2.is_palindrome())
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
#
# llist.print_list()
# llist.move_tail_to_head()
# print("\n")
# llist.print_list()
# llist1 = LinkedList()
# llist1.append(5)
# llist1.append(6)
# llist1.append(3)
#
# llist2 = LinkedList()
# llist2.append(8)
# llist2.append(4)
# llist2.append(2)
#
# print(365 + 248)
# print((llist1.sum_two_lists(llist2)).print_list())
