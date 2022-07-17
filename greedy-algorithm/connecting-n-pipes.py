"""

Implement a function that connects n pipes of different lengths, into one pipe. You can assume that the cost to connect two pipes is equal to the sum of their lengths. We need to connect the pipes with minimum cost.

Input#
A list containing lengths of n pipes

Output#
The total cost of connecting the pipes

Sample input#
pipes = [4, 3, 2, 6]
Sample output#
result = 29

The time complexity for this solution is O(nlogn)
 because both the push and pop operations of the priority queue take O(logn) time.

"""
import heapq
def min_cost(pipes):
    heapq.heapify(pipes)
    cost = 0
    while(len(pipes) > 1):
        first = heapq.heappop(pipes)
        second = heapq.heappop(pipes)
        cost += first + second
        heapq.heappush(pipes, first+second)
    return cost

# Main program to test above function
if __name__ == "__main__":

    pipes = [4, 3, 2, 6]

    print(min_cost(pipes))
