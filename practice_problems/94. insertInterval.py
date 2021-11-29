from typing import List
from collections import deque


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for interval in intervals:
            if interval[0] < e:
                left.append(interval)
            elif interval[1] > s:
                right.append(interval)
            else:
                s = min(s, interval[0])
                e = max(e, interval[1])
        return left + [[s, e]] + right


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