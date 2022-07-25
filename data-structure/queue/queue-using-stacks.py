"""

Input#
enqueue( ): A value to insert into the queue

dequeue( ): Does not require any input

Output#
enqueue( ): Does not return anything

dequeue( ): Pops out and returns the oldest value in the queue

Sample Input#
value = 5 # [1, 2, 3, 4]
enqueue(value)
dequeue()
Sample Output#
True # [1, 2, 3, 4, 5]
1 # [2, 3, 4, 5]


enqueue: O(1)
dequeue is O(n)
"""
from Stack import MyStack

class NewQueue:
    def __init__(self):
        self.enqueue_stack = MyStack()
        self.dequeue_stack = MyStack()
    def enqueue(self, value):
        self.enqueue_stack.push(value)
    def dequeue(self):
        while self.enqueue_stack.is_empty() is False:
            self.dequeue_stack.push(self.enqueue_stack.pop())
        value = self.dequeue_stack.pop()
        while self.dequeue_stack.is_empty() is False:
            self.enqueue_stack.push(self.dequeue_stack.pop())
        return value



queue = NewQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())
