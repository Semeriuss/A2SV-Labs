from typing import List

# 4 tries -> 20 minutes


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        def getSlope(point1, point2):
            
            x1, y1 = point1
            x2, y2 = point2
            
            if x2 -x1 == 0:
                return float("-inf")

            return (y2 - y1)/(x2 - x1)
        
        first_slope = getSlope(tuple(coordinates[0]), tuple(coordinates[1]))
        current_slope = first_slope
        for i in range(1, len(coordinates) - 1):
            current_slope = getSlope(tuple(coordinates[i]), tuple(coordinates[i+1]))
            if current_slope != first_slope:
                return False
        
        return True
            
            
            
            
print(Solution().checkStraightLine([[0,0],[0,5],[5,5],[5,0]]))