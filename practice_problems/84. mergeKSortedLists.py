from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(a, b):
            if not a or (b and a.val > b.val):
                a, b = b, a
            if a:
                a.next = mergeTwoLists(a.next, b)
            return a
        
        while len(lists) > 1:
            res = []
            for i in range(0, len(lists) - 1, 2):
                res.append(mergeTwoLists(lists[i], lists[i + 1]))
            
            if len(lists) % 2 == 1:
                res.append(lists[-1])
            lists = res
        
        return lists[0] if len(lists) else None
