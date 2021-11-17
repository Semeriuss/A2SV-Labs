from collections import deque

def armChairs(seats):
    ones, zeros = [], []
    for i, seat in enumerate(seats):
        if seat == 1:
            ones.append(i)
        else:
            zeros.append(i)
    
    def dfs(graph, source, visited):
        if source >= len(graph) or source < 0:
            return float("inf")
        if source not in visited and graph[source] == 0:
            visited.add(source)
            return source
        right = dfs(graph, source + 1, visited)
        left = dfs(graph, source - 1, visited)
        if right < left:
            visited.remove(left)
            return right
        else:
            visited.remove(right)
            return left
    
    minutes = 0
    visited = set()
    for one in ones:
        minutes += abs(one - dfs(seats, one, visited))
    
    return minutes


if __name__ == "__main__":
    n = int(input())
    seats = list(map(int, input().split()))
    print(armChairs(seats))
    