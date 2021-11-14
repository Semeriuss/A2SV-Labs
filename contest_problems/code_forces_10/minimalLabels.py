from collections import defaultdict, deque
import heapq

def minimalLabels(graph, indegree):

    queue = []
    n = len(indegree)

    label = [0] * (n)   
    for node in range(1, n):
        if indegree[node] == 0:
            heapq.heappush(queue, node)

    rank = 1
    while queue:
        current = heapq.heappop(queue)
        label[current] = str(rank)
        rank += 1
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(queue, neighbor)

    return " ".join(label[1:])       

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = defaultdict(list)
    for _ in range(m):
        edge1, edge2 = map(int, input().split())
        graph[edge1].append(edge2)
        indegree[edge2] += 1
    print(minimalLabels(graph, indegree))

