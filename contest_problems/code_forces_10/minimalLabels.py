from collections import defaultdict
import heapq

def minimalLabels(graph, outdegree):

    queue = []
    n = len(outdegree)

    label = [0] * (n)   
    for node in range(1, n):
        if outdegree[node] == 0:
            heapq.heappush(queue, -node)

    rank = n - 1
    while queue:
        current = heapq.heappop(queue)
        label[abs(current)] = str(rank)
        rank -= 1
        for parent in graph[current]:
            outdegree[abs(parent)] -= 1
            if outdegree[abs(parent)] == 0:
                heapq.heappush(queue, parent)

    return " ".join(label[1:])       

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    outdegree = [0] * (n + 1)
    graph = defaultdict(list)
    for _ in range(m):
        edge1, edge2 = map(int, input().split())
        graph[-edge2].append(-edge1)
        outdegree[abs(edge1)] += 1
    print(minimalLabels(graph, outdegree))

