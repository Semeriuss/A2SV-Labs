from typing import List
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ROW = len(rowCosts)
        COL = len(colCosts)
        sx, sy = startPos
        ex, ey = homePos

        spx, epx = min(sx, ex), max(sx, ex)
        spy, epy = min(sy, ey), max(sy, ey)
        minimumCost= 0
        for i in range(spx, epx + 1):
            minimumCost += rowCosts[i]
        for j in range(spy, epy + 1):
            minimumCost += colCosts[j]
        
        minimumCost -= rowCosts[sx]
        minimumCost -= colCosts[sy]
        return minimumCost

        
start = [1, 0]
end = [2, 3]
rowcost = [5, 4, 3]
colcost = [8, 2, 6, 7]

start = [1,2]
end = [3,3]
rowcost = [10,1,2,3]
colcost = [10,7,8,9]

start = [45,70]
end = [32,35]
rowcost = [4,10,5,8,0,10,5,9,10,2,7,7,7,6,1,1,5,1,5,9,7,1,0,3,1,2,6,4,6,4,2,4,1,1,5,2,3,9,3,9,8,4,1,4,6,6728,8650,6586,9762,9034,9246,5033,9632,6907,7237,6422,5603,6062,5033,5109,8118,7210,9672,8268,5157,5854,7723,8101]
colcost = [7,8,9,8,10,3,10,4,8,10,7,5,5,9,7,5,7,10,8,6,2,2,4,10,7,3,6,2,1,8,1,6,5,5,1,9,10,6,3,2,8,6,3,0,10,4,5,4,6,2,1,6,8,9,3,0,5,6,8,3,8,6,10,4,6,4,3,3,6,3,6893,9916,9592,7854,8030,6396,8904,5191,9514,9417,9701,9840,9194,6515,5643,7804,9768,8898,6735,8548,6859,6024,9551,9520,5537,5135]

start = [4,1]
end = [0,2]
rowcost = [6,3,0,8,19,21,10]
colcost = [0,7,23,15,13,19,12,14]\

start = [5,5]
end = [5,2]
rowcost = [7,1,3,3,5,3,22,10,23]
colcost = [5,5,6,2,0,16]
print(Solution().minCost(tuple(start), tuple(end), rowcost, colcost))

