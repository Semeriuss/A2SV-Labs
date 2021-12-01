from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for post, pre in prerequisites:
            graph[pre].append(post)
            indegree[post] += 1

        queue = deque()
        for course, degree in enumerate(indegree): 
            if degree == 0:
                queue.append(course) 
                
        while queue:
            current_course = queue.popleft()
            for course in graph[current_course]:
                indegree[course] -= 1
                if not indegree[course]:
                    queue.append(course)
        
        for degree in indegree:
            if degree:
                return False
        return True

numCourses = 2
prerequisites = [[1,0]]

numCourses = 2
prerequisites = [[1,0], [0,1]]

numCourses = 2
prerequisites = [[0,1]]
print(Solution().canFinish(numCourses, prerequisites))
            

        