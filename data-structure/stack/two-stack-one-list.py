class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.size = size
        self.items = [0] * size
        self.top1 = -1
        self.top2 = self.size

    # Insert Value in First Stack
    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.items[self.top1] = value
        else:
            print("Stack Overflow")

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.items[self.top2] = value
        else:
            print("Stack Overflow")

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.top1 >= 0:
            value = self.items[self.top1]
            self.top1 -= 1
            return value
        else:
            print("Stack Underflow")

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.top2 < self.size:
            value = self.items[self.top2]
            self.top2 += 1
            return value
        else:
            print("Stack Underflow")

    def print_list(self):
        val = "["
        for item in self.items:
            val += str(item)
            val += ", "
        val += "]"
        return val

if __name__ == "__main__" :
    stack = TwoStacks(10)
    stack.push1(20)
    stack.push2(10)
    print(stack.pop1())
    stack.push1(100)
    print(stack.pop2())
