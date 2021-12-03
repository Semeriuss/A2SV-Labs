from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root: return result
        
        que = deque([root])
        k = 0
        while que:
            if k % 2:
                temp = [node.val for node in reversed(que)]
            else:
                temp = [node.val for node in que]
            result.append(temp)
            for _ in range(len(que)):
                curr_node = que.popleft()
                if curr_node.left:
                    que.append(curr_node.left)
                if curr_node.right:
                    que.append(curr_node.right)
            k += 1
            
        
        return result
            
                
            
            
                    
            