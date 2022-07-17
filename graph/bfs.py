"""

You have to implement the breadth-first traversal in Python.

To solve this problem, the previously implemented Graph class is already prepended.

Input#
A graph represented as an adjacency list and a starting vertex

Output#
A string containing the vertices of the graph listed in the correct order of traversal

Let E
 be the set of all edges in the connected component visited by the algorithm. For each edge {u, v}
 in E
 the algorithm makes two while loop iteration steps: one time when the algorithm visits the neighbors of u
 and one time when it visits the neighbors of v
Hence, the time complexity is 
O(|V| +|E|).

"""
from graph import Graph

def bfs(my_graph, source):
    visited = [False] * (len(my_graph.graph))
    queue = []
    result = ""
    queue.append(source)
    visited[source] = True
    while queue:
        source = queue.pop(0)
        result += str(source)
        temp = my_graph.graph[source]
        while temp is not None:
            data = temp.vertex
            if not visited[data]:
                queue.append(data)
                visited[data] = True
            temp = temp.next
    return result


# Main to test the above program
if __name__ == "__main__":

    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(bfs(g, 0))
