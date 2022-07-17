import linkedList as l
def length(var, head):
    if not head:
        return 0
    else:
        return 1 + length(var, head.next)


# Driver Code
myLinkedList = l.LinkedList()
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(7)
myLinkedList.append(11)

print(length(myLinkedList, myLinkedList.head))
