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
            temp = [node.val for node in que]
            res.append(sum(temp)/len(temp))
            for _ in range(len(que)):
                curr_node = que.popleft()
                temp.append(curr_node.val)
                if curr_node.left:
                    temp.append(curr_node.left.val)
                    que.append(curr_node.left)
                if curr_node.right:
                    temp.append(curr_node.right.val)
                    que.append(curr_node.right)
        return res
                
