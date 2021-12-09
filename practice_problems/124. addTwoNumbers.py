# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()

        head, temp = dummy, 0

        while l1 and l2:
            dummy.next, temp = ListNode((l1.val + l2.val + temp)%10), ListNode((l1.val + l2.val + temp)//10)
            l1, l2, dummy = l1.next, l2.next, dummy.next
        
        while l1:
            dummy.next, temp = ListNode((l1.val + temp)%10), ListNode((l1.val + temp)//10)
            l1, dummy = l1.next, dummy.next
        
        while l2:
            dummy.next, temp = ListNode((l2.val + temp)%10), ListNode((l2.val + temp)//10)
            l2, dummy = l2.next, dummy.next
        
        if temp:
            dummy.next = ListNode(temp)
            
        return head.next