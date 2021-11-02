from collections import defaultdict, deque
from typing import List
import heapq


def parallelCourses(n : int, relations: List[List[int]], time: List[int]) -> int:
    graph = defaultdict(list)
    for prev, nex in relations:
        graph[prev].append(nex)

    incoming = defaultdict(int)
    for node in graph.keys():
        incoming[node]
        for neighbor in graph[node]:
            incoming[neighbor] += 1

    maxWait = defaultdict(int)    
    def bfs():
        nonlocal graph, incoming
        queue = deque()

        for node in incoming:
            if incoming[node] == 0:
                queue.append(node)
    
        while queue:
            current = queue.popleft()

            for neighbor in graph[current]:
                incoming[neighbor] -= 1
                maxWait[neighbor] = max(maxWait[neighbor], maxWait[current])
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
    bfs()
    return max(maxWait.values())

def parallelCourses(n : int, relations: List[List[int]], time: List[int]) -> int:
    graph = defaultdict(list)
    incoming = defaultdict(int)
    for prev, nex in relations:
        graph[prev].append(nex)
        incoming[nex] += 1
    
    print(incoming)
    def bfs(graph, incoming):
 
        queue = [(time[node-1], node) for node in range(1, n+1) if incoming[node] == 0]
        heapq.heapify(queue)
        
        maxElapsedMonth = 0
        print(graph, time, incoming, queue, sep='\n')

        while queue:
            elapsedMonth, current = heapq.heappop(queue)
            maxElapsedMonth = max(elapsedMonth, maxElapsedMonth)
            for neighbor in graph[current]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    print("here")
                    heapq.heappush(queue, (elapsedMonth + time[neighbor - 1], neighbor))
        
        return maxElapsedMonth
    return bfs(graph, incoming)


n = 3
relations = [[1,3],[2,3]]
# relations = [[1,3], [1,2], [2,3]]
# relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
time = [3,2,5]

print(parallelCourses(n, relations, time))