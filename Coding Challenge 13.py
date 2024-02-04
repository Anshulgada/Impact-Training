import heapq

def OrderDelivery(cityNodes, cityFrom, cityTo, company):

    graph = { }

    for i in range(len(cityFrom)):
        if cityFrom[i] not in graph:
            graph[cityFrom[i]] = [ ]

        if cityTo[i] not in graph:
            graph[cityTo[i]] = [ ]

        graph[cityFrom[i]].append((cityTo[i], i + 1))
        graph[cityTo[i]].append((cityFrom[i], i + 1))

    distances  = {city: float('inf') for city in range(1, cityNodes + 1)}
    distances[company] = 0

    heap = [(0, company)]
    heapq.heapify(heap)

    while heap:
        currentDistance, currentCity = heapq.heappop(heap)

        for neighbor, indexOfRoad in graph[currentCity]:
            nextDistance = currentDistance + 1

            if nextDistance < distances[neighbor]:
                distances[neighbor] = nextDistance
                heapq.heappush(heap, (nextDistance, neighbor))

    resultSet = []

    for distance in sorted(distances.keys(), key = lambda x: (distances[x], x)):
        if distance != company:
            resultSet.append(distance)

    return resultSet

if __name__ == '__main__':
    cityNodes, n = map(int, input().split())
    cityFrom = [ ]
    cityTo = [ ]

    for _ in range(n):
        From, To = map(int, input().split())
        cityFrom.append(From)
        cityTo.append(To)

    company = int(input())
    result = OrderDelivery(cityNodes, cityFrom, cityTo, company)

    for city in result:
        print(city)