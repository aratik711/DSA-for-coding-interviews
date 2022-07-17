"""

You have to implement the depth-first traversal in Python.

To solve this problem, the previously implemented graph class is already prepended.

Input#
A graph represented as an adjacency list and a starting vertex

Output#
A string containing the vertices of the graph listed in the correct order of traversal

Let E
 be the set of all edges in the graph. The algorithm makes two calls to DFS for each edge \{u, v\}
 in E
: one time when the algorithm visits the neighbors of u
 and one time when it visits the neighbors of v.

Hence, the time complexity of the algorithm is O(V + E)


"""
from graph import Graph

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

# Main to test the above program
#if __name__ == "__main__":

#    V = 5
#    g = Graph(V)
#    g.add_edge(0, 1)
#    g.add_edge(0, 2)
#    g.add_edge(1, 3)
#    g.add_edge(1, 4)

#    print(dfs(g, 0))
