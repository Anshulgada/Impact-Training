graph = {
    '5' : ['3', '7'],
    '3': ['3', '7'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []    # List for visited nodes
queue = []      # Q Init

def BFS(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:                # Loop to traverse each node
        m = queue.pop(0)
        print(m, end = ' -> ')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
print("Following is Breadth-First Search: ")
BFS(visited, graph, '5')