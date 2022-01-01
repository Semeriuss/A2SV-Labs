# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        org = head
        count = 1
        while head:
            temp_count = count
            if count % 2 != 0:
                while head and temp_count:
                    head = head.next
                    temp_count -= 1
                count += 1
            else:
                rev = None
                temp_count = count
                while head and temp_count:
                    print("rev", rev, "rev.next", "and", head.val)
                    rev, rev.next, head = head, rev, head.next
                    print("rev", rev, "rev.next after", rev.next, "and", head.val)
                    temp_count -= 1
                count += 1
        
        while org:
            print(org.val, end=" ")
            org = org.next

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        org = head
        count = 1
        while head:
            temp_count = count
            if count % 2 != 0:
                while head and temp_count:
                    head = head.next
                    temp_count -= 1
                count += 1
            else:
                rev = None
                temp_count = count
                while head and temp_count:
                    print("rev", rev, "rev.next", "and", head.val)
                    rev, rev.next, head = head, rev, head.next
                    print("rev", rev, "rev.next after", rev.next, "and", head.val)
                    temp_count -= 1
                count += 1
        
        while org:
            print(org.val, end=" ")
            org = org.next
# head = [1,1,0,6]
head = ListNode(5, ListNode(2, ListNode(6, ListNode(3, ListNode(9, ListNode(1, ListNode(7, ListNode(3, ListNode(8, ListNode(4))))))))))
head = ListNode(5, ListNode(2, ListNode(6)))
Solution().reverseEvenLengthGroups(head)