"""

A string containing a postfix mathematic expression. Each digit is considered to be a separate number, i.e., there are no double digit numbers.

Output#
A result of the given postfix expression.

Sample Input#
exp = "921 * - 8 - 4 +" # 9 - 2 * 1 - 8 + 4
Sample Output#
3

The time complexity for this algorithm is O(n).
"""
from stack import Stack


def evaluate_post_fix(exp):
    num_stack = Stack()
    #exp_stack = Stack()
    exp_str = "*-+/"
    for i in exp:
        if i.isdigit():
            num_stack.push(i)
        elif i in exp_str:
            if num_stack.size() >= 2:
                val1 = num_stack.pop()
                val2 = num_stack.pop()
                num_stack.push(str(eval(val2 + i +  val1)))
            else:
                return "Invalid Expression"
    if num_stack.size() != 1:
        return "Invalid Expression"
    return num_stack.pop()


if __name__ == "__main__" :
    print("Result of expression (921*-8-4+) : " + str(evaluate_post_fix("921*-8-4+")))
    print("Result of expression (921*-8--4+) : " + str(evaluate_post_fix("921*-8--4+")))
