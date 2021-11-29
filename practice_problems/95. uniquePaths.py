from collections import defaultdict

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.path = [(0, 1), (1, 0)]
        return self.countPath((0, 0), (m - 1, n - 1), defaultdict(int))

    def fitsBoundary(self, point, boundary):
        x, y = point
        a, b = boundary
        return 0 <= x < a and 0 <= y < b
    
    def countPath(self, src, dst, memo):
        final_x, final_y = dst
        if src in memo:
            return memo[src]
        if src == (final_x, final_y):
            return 1
        curr_x, curr_y = src
        count = 0
        for path_x, path_y in self.path:
            next_x, next_y = path_x + curr_x, path_y + curr_y
            if self.fitsBoundary((next_x, next_y), (final_x + 1, final_y + 1)):
                count += self.countPath((next_x, next_y), dst, memo)
        memo[(curr_x, curr_y)] = count
        return memo[src]
print(Solution().uniquePaths(100, 100))

                    