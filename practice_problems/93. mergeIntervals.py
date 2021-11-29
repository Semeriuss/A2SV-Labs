from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        for interval in sorted(intervals, key=lambda interval : interval[0]):
            if output and interval[0] <= output[-1][1]:
                output[-1][1] = max(interval[1], output[-1][1])
            else:
                output.append(interval)
        return output

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals =  [[1,4],[4,5]]
intervals = [[5, 11], [2, 5], [6, 12]]
intervals = [[0, 1]]
intervals = [[4, 7], [3, 11], [5, 6], [10, 45], [47, 55], [44, 46]]
intervals = [[1, 4], [0, 4]]
intervals = [[1, 4], [2, 3]]
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
intervals = [[2,3],[4,5]]
intervals = [[6,7],[8,9]]
intervals = [[2,3],[4,5],[0, 2],[6,7],[8,9],[1,10]]
print(Solution().merge(intervals))