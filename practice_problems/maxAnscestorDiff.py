# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.v = 0
        minval = float("inf")
        minlevel = None
        dq = deque([(0, root)])
        
        while dq:            
            temp = dq.copy()
            dq.clear()
            while temp:
                curlevel, curnode = temp.popleft()
                if curnode.val < minval:
                    minval = curnode.val
                    minlevel = curlevel
                    
                if curnode.left:
                    dq.append((curlevel + 1, curnode.left))
                if curnode.right:
                    dq.append((curlevel + 1, curnode.right))
            
            if dq:
                curlevel = dq[0][0]
                curval = max([node.val for _, node in dq])
            
                if curlevel != minlevel:
                    self.v = max(self.v, abs(curval - minval))
        return self.v