"""

Implement the function reverseK(queue, k) which takes a queue and a number “k” as input and reverses the first “k” elements of the queue. An illustration is also provided for your understanding.

Output#
The queue with first “k” elements reversed. Remember to return the queue itself!

In case the value of “k” is larger than the size of the queue, is smaller than 0, or if the queue is empty, simply return None instead.

Sample Input#
Queue = [1,2,3,4,5,6,7,8,9,10], k = 5
Sample Output#
Queue = [5,4,3,2,1,6,7,8,9,10]

The time complexity of this function is O(n)
"""
from Queue import MyQueue
from Stack import MyStack


def reverseK(queue, k):
    if queue.size() < k or k < 1:
        return None
    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())
    for i in range(k):
        queue.enqueue(stack.pop())
    for i in range(queue.size() - k):
        queue.enqueue(queue.dequeue())

if __name__ == "__main__" :
    # testing our logic
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
    print("the queue before reversing:")
    print(queue.items)
    reverseK(queue, 5)
    print("the queue after reversing:")
    print(queue.items)
