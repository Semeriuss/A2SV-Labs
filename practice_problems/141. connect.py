# Definition for a Node.
from typing import Optional
from collections import dedq

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return 
        dq, prelevel, prenode = dedq([(1, root)]), 0, Node 
        
        while dq:
            level, node = dq.popleft()
            if level == prelevel:
                prenode.next = node
                prenode = node
            else:
                prelevel, prenode = level, prenode
            
            if node.left:
                dq.append((level + 1, node.left))
                dq.append((level + 1, node.right))
        return root
            
                