import sys

# Providing the graph
vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]

# Find which vertex is to be visited next
def to_be_visited():
    global visited_and_distance
    v = -10
    for index in range(num_of_vertices):
        # If the vertex has not been visited and is the smallest unvisited distance
        if visited_and_distance[index][0] == 0 \
                and (v < 0 or visited_and_distance[index][1] <=
                     visited_and_distance[v][1]):
            v = index
    return v

num_of_vertices = len(vertices[0])

visited_and_distance = [[0, 0]]
# Initializing distances with infinity for all vertices except the source vertex
for i in range(num_of_vertices - 1):
    visited_and_distance.append([0, sys.maxsize])

# Iterating through each vertex
for vertex in range(num_of_vertices):
    # Find next vertex to be visited
    to_visit = to_be_visited()
    # Iterating through neighbors of the current vertex
    for neighbor_index in range(num_of_vertices):
        # Updating new distances
        if vertices[to_visit][neighbor_index] == 1 and \
                visited_and_distance[neighbor_index][0] == 0:
            new_distance = visited_and_distance[to_visit][1] \
                           + edges[to_visit][neighbor_index]
            # Update distance if it's smaller than the current known distance
            if visited_and_distance[neighbor_index][1] > new_distance:
                visited_and_distance[neighbor_index][1] = new_distance
        # Mark the current vertex as visited
        visited_and_distance[to_visit][0] = 1

# Printing the distance from the source vertex to each vertex
i = 0
for distance in visited_and_distance:
    print("Distance of ", chr(ord('a') + i),
          " from source vertex: ", distance[1])
    i = i + 1
