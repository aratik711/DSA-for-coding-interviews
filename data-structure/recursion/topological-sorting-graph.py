import graph as g
def helperFunction(myGraph, current, visited, result):
    visited[current] = True
    for i in myGraph.graph[current]:
        if visited[i] == False:
            helperFunction(myGraph, i, visited, result)
    result.insert(0, current)


def topologicalSort(myGraph):
    visited = [False] * myGraph.vertices
    result = []
    for current in range(myGraph.vertices):
        if visited[current] == False:
            helperFunction(myGraph, current, visited, result)
    return result


# Driver code
# Create a graph given in the above diagram
myGraph = g.Graph(5)
myGraph.addEdge(0, 1)
myGraph.addEdge(0, 3)
myGraph.addEdge(1, 2)
myGraph.addEdge(2, 3)
myGraph.addEdge(2, 4)
myGraph.addEdge(3, 4)

print("Topological Sort")
print(topologicalSort(myGraph))
