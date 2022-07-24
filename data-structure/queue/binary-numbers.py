"""

The time complexity of this solution is in O(n)

"""

from Queue import MyQueue


def find_bin(num):
    binary = []
    bin_queue = MyQueue()
    bin_queue.enqueue(1)
    for i in range(num):
        binary.append(str(bin_queue.dequeue()))
        s1 = binary[i] + "0"
        s2 = binary[i] + "1"
        bin_queue.enqueue(s1)
        bin_queue.enqueue(s2)
    return binary

print(find_bin(3))
print(find_bin(5))
