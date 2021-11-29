from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [(1, 0), (0, 1)]

        def fitsBoundary(point):
            row, col = point
            return 0 <= row < m and 0 <= col < n

        def bfs(src, dst):
            queue = deque()
            visited = set()
            queue.append(src)
            ways = 0
            way = []
            while queue:
                curr_x, curr_y = queue.popleft()
                if (curr_x, curr_y) == dst:
                    ways += 1
                    break
                for x, y in path:
                    next_x, next_y = x + curr_x, y + curr_y
                    if (next_x, next_y) not in visited and fitsBoundary((next_x, next_y)):
                        if (next_x, next_y) == dst:
                            ways += 1
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))
            return ways
        return bfs((0,0), (m-1, n-1))

print(Solution().uniquePaths(3, 7))

                    