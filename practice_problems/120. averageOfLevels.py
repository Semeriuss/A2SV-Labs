# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque([root])
        res = []
        while que:
            summation, k = 0, len(que)
            for _ in range(len(que)):
                curr_node = que.popleft()
                summation += curr_node.val
                if curr_node.left: que.append(curr_node.left)
                if curr_node.right: que.append(curr_node.right)
            res.append(summation/k)
        return res
                
