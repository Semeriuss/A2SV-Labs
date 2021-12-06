
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

from collections import deque
from typing import List
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        que =deque()
        importance = 0
        for employee in employees:
            if employee.id == id:
                importance += employee.importance
                for subordinate_id in employee.subordinates:
                    que.append(subordinate_id)
                break
        
        while que:
            curr_employee_id = que.popleft()
            for employee in employees:
                if employee.id == curr_employee_id:
                    importance += employee.importance
                    for subordinate_id in employee.subordinates:
                        que.append(subordinate_id)
        return importance
                