"""

Implement a function that returns the number of nodes at a given level starting from a root node of a directed graph.

Try modifying the breadth-first traversal algorithm to achieve this goal.

To solve this problem, all the previously-implemented data structures will be available to us.

Input#
An undirected graph represented as an adjacency list, and the level whose number of nodes we need to find

Output#
The number of nodes returned as a simple integer

The solution above modifies the visited list to store the level of each node. Later, count the nodes with the same level.

In this code, while visiting each node, the level of that node is set with an increment in the level of its parent node, i.e.,

       visited[child] = visited[parent] + 1


the time complexity is O(V+E)

"""
from graph import Graph
def number_of_nodes(my_graph, level):
    source = 0
    visited = [0] * len(my_graph.graph)
    queue = []
    result = ""
    queue.append(source)
    visited[source] = 1
    while queue:
        source = queue.pop(0)
        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if visited[data] == 0:
                queue.append(data)
                visited[data] = visited[source] + 1
            my_graph.graph[source] = my_graph.graph[source].next
    result = 0
    for i in range(len(my_graph.graph)):
        if visited[i] == level:
            result += 1
    return result

# Main to test above function
if __name__ == "__main__":

    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(number_of_nodes(g, 2))
