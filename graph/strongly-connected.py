"""

Implement a function that tells us whether a graph is strongly connected or not.

A directed graph is strongly connected if there is a path between any two pairs of vertices.

Input#
A directed graph and its source

Output#
True if it’s a strongly connected graph but False otherwise

the time complexity is O(V+E)
"""

from graph import *

def dfs(my_graph, source):
    visited = [False] * len(my_graph.graph)
    stack = []
    result = ""
    stack.append(source)
    while stack:
        source = stack.pop()
        if not visited[source]:
            result += str(source)
            visited[source] = True
        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            my_graph.graph[source] = my_graph.graph[source].next
    return result

def transpose(my_graph):
    new_graph = Graph(my_graph.V)
    for source in range(my_graph.V):
        while my_graph.graph[source] is not None:
            destination = my_graph.graph[source].vertex
            new_graph.add_edge(destination, source)
            my_graph.graph[source] = my_graph.graph[source].next
    return new_graph

def is_strongly_connected(graph1):
    result1 = dfs(graph1, 0)
    if graph1.V != len(result1):
        return False
    graph2 = transpose(graph1)
    result2 = dfs(graph2, 0)
    if graph2.V != len(result2):
        return False
    return True

# Main program to test the above code
if __name__ == "__main__":

    V = 5
    g1 = Graph(V)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(3, 0)
    g1.add_edge(4, 2)
    print("Yes" if is_strongly_connected(g1) else "No")

    g2 = Graph(V)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(2, 4)
    print ("Yes" if is_strongly_connected(g2) else "No")
