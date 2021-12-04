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
        level = 0
        while que:
            temp = deque()
            for _ in range(len(que)):
                curr_node = que.popleft()
                if level % 2:
                    temp.appendleft(curr_node.val)
                else:
                    temp.append(curr_node.val)

                if curr_node.left:
                    que.append(curr_node.left)
                if curr_node.right:
                    que.append(curr_node.right)
            result.append(temp)
            level += 1
            
        
        return result
            
                
            
            
                    
            