from collections import defaultdict
import sys

input = sys.stdin.readline
n = int(input())

reposts = []
for i in range(n):
    reposts.append(input().rstrip())

def maxChain(reposts):
    
    graph = defaultdict(list)
    for repost in reposts:
        name1, label, name2 = repost.split()
        graph[name2.lower()].append(name1.lower())
    
    def dfs(graph, source, count, visited):
        if source not in graph:
            return count
        
        visited.add(source)
        count += 1
        current_count = count
        for friend in graph[source]:
            if friend not in visited:
                count = max(dfs(graph, friend, current_count, visited), count)
        return count

    return dfs(graph, 'polycarp', 1, set())

print(maxChain(reposts))