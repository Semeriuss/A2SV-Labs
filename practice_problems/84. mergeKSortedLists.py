from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(a, b):
            if not a or b and a.val > b.val:
                a, b = b, a
            if a:
                a.next = mergeTwoLists(a.next, b)
            return a
    
        res = None
        for i in range(len(lists)):
            a = lists[i]
            res = mergeTwoLists(a, res)
        return res
            