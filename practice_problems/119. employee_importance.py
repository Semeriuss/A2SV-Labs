
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
        e_map = {e.id : e for e in employees}
        def dfs(eid):
            employee = e_map[eid]
            return employee.importance + sum(dfs(sub) for sub in employee.subordinates)
        return dfs(id)