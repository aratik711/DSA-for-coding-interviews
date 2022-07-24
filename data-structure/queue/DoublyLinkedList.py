class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def get_head(self):
        if self.head != None:
            return self.head.data
        else:
            return False
    def is_empty(self):
        if self.head is None:
            return True
        return False
    def insert_tail(self, data):
        temp_node = Node(data)
        if self.is_empty():
            self.head = temp_node
            self.tail = temp_node
        else:
            self.tail.next = temp_node
            temp_node.prev = self.tail
            self.tail = temp_node
        self.length += 1
        return temp_node
    def remove_head(self):
        if self.is_empty():
            return False
        node_to_del = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = node_to_del.next
            self.head.prev = None
            node_to_del.next = None
        self.length -= 1
        return node_to_del.data
    def tail_node(self):
        if self.head != None:
            return self.tail.data
        return False
    def __str__(self):
        val = ""
        if self.is_empty():
            return ""
        temp = self.head
        val = "[" + str(temp.data) + ", "
        temp = temp.next
        while temp.next:
            val += str(temp.data) + ", "
            temp = temp.next
        val += str(temp.data) + "]"
        return val
    def __str2__(self):
        val = ""
        if self.is_empty():
            return ""
        temp = self.head
        val = str(temp.data)
        while temp.next:
            val += str(temp.data)
            temp = temp.next
        val += str(temp.data)
        return val
