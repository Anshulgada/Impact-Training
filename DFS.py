graph = {
    '5' : ['3', '7'],
    '3': ['3', '7'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []

def DFS(visited, graph, node):
    if node not in visited:
        print(node, end = ' -> ')
        visited.append(node)

        for neighbour in graph[node]:
            DFS(visited, graph, neighbour)

# Driver Code
print("Following is Depth-First Search: ")
DFS(visited, graph, '5')