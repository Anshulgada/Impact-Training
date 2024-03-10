import heapq

def shortest_path(graph):
    num_nodes = int(graph[0])
    nodes = graph[1:num_nodes + 1]
    conn = graph[num_nodes + 1:]

    adj_list = {node: [] for node in nodes}
    for conns in conn:
        source, dest, weight = conns.split('|')
        adj_list[source].append((dest, int(weight)))

    pq = [(0, nodes[0], [])]
    visited = set()

    while pq:
        dist, node, path = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == nodes[-1]:
                return '-'.join(path)
            for neighbor, weight in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (dist + weight, neighbor, path))

    return -1

graph_input = input()
graph = graph_input.split(',')

print(shortest_path(graph))