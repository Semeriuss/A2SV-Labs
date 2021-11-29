from collections import defaultdict, deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rPath = [(-1, 0), (0, -1)]

        def fitsBoundary(point):
            row, col = point
            return 0 <= row < m and 0 <= col < n

        def countPath(dst, memo):
            if dst in memo:
                return memo[dst]
            if dst == (0, 0):
                return 1
            count = 0
            if fitsBoundary(dst):
                x, y = dst
                for path in rPath:
                    path_x, path_y = path
                    next_x, next_y = x + path_x, y + path_y
                    if fitsBoundary((next_x, next_y)):
                        count += countPath((next_x, next_y), memo)
                    memo[(x, y)] = count
            return count
        return countPath((m - 1, n - 1), defaultdict(int))
print(Solution().uniquePaths(100, 100))

                    