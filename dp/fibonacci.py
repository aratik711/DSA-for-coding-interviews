def fib(num):
    if num <= 1:
        return num
    second_last = 0
    last = 1
    current = 0
    for i in range(2, num+1):
        current, second_last = second_last + last, last
        last = current
    return current


# Driver code to test above function
if __name__ == '__main__':
  num = 6
  print(fib(num))
