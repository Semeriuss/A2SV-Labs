from collections import defaultdict, deque
import heapq

def smallestLexicographicSequence(graph, minNode):
    
    queue = []
    visited = set()
    heapq.heappush(queue, minNode)
    visited.add(minNode)
    label = []
    while queue:
        current = heapq.heappop(queue)
        label.append(str(current))
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(queue, neighbor)
                visited.add(neighbor)
    
    return " ".join(label)

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    if n == 1:
        print(1)
    else:
        minNode = min(graph.keys())
        print(smallestLexicographicSequence(graph, minNode))
