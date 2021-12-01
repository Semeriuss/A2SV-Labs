import sys
from typing import Dict, List
from collections import defaultdict
sys.setrecursionlimit(3000)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for post, pre in prerequisites:
            graph[pre].append(post)
            indegree[post] += 1
        
        def dfs(graph: Dict, indegree: List[int], course: int, schedule: List[int]):
            if indegree[course]:
                return 
            
            schedule.append(course)
            for course in graph[course]:
                indegree[course] -= 1
                dfs(graph, indegree, course, schedule)

        takeableCourse = [course for course, degree in enumerate(indegree) if not degree]
        schedule = []
        for course in takeableCourse:
            dfs(graph, indegree, course, schedule)
        
        for degree in indegree:
            if degree:
                return []
        return schedule

numCourses = 2
prerequisites = [[1,0]]
print(Solution().findOrder(numCourses, prerequisites))