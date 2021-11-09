
from collections import defaultdict, deque
import collections

n = int(input())
employees = []
for i in range(n):
    employees.append(int(input()))

def groupEmployees(employees):
    graph = defaultdict(list)
    indegree = [0 for _ in range(len(employees))]
    for i in range(len(employees)):
        if employees[i] != -1:
            graph[employees[i]].append(i + 1)
            indegree[i] += 1
 
    queue = deque()

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i + 1)
    
    groups = 0
    while queue:
        groups += 1

        tempQueue = deque()
        while queue:
            currEmployee = queue.popleft()
            for subordinates in graph[currEmployee]:
                indegree[subordinates - 1] -= 1
                if indegree[subordinates - 1] == 0:
                    tempQueue.append(subordinates)
            
        queue.extend(tempQueue)
    
    return groups

print(groupEmployees(employees))

