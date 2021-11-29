from typing import List
from collections import deque


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = deque()
        inserted = False
        for interval in intervals:
            if not inserted and newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
                output.append([min(interval[0], newInterval[0]), max(interval[1], newInterval[1])])
                inserted = True
            elif inserted and interval[0] <= output[-1][1]:
                output[-1][1] = max(interval[1], output[-1][1])
            elif not inserted and newInterval[0] < interval[0] and newInterval[1] < interval[1]:
                inserted = True
                output.append(newInterval)
                output.append(interval)
            else:
                output.append(interval)
        
        if not inserted: output.append(newInterval)
        return list(output)


intervals = [[1,3],[6,9]]
newInterval = [2,5]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

intervals = []
newInterval = [5,7]

intervals = [[1,5]]
newInterval = [2,3]

intervals = [[1,5]]
newInterval = [2,7]

intervals = [[1, 5]]
newInterval = [0, 0]

intervals = [[3,5],[12,15]]
newInterval = [6,6]

intervals = [[1, 1], [12, 15]]
newInterval = [16, 16]

intervals = [[1, 1], [12, 15]]
newInterval = [0, 0]

intervals = [[1, 6], [12, 15]]
newInterval = [2, 11]

intervals = [[1, 6], [12, 15]]
newInterval = [6, 999]
print(Solution().insert(intervals, newInterval))