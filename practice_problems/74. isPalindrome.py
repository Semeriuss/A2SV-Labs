# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def isPalindrome(head: 'ListNode') -> bool:
    slow = fast = head
    rev = None
    while fast and fast.next:
        rev, rev.next, slow, fast = slow, rev, slow.next, fast.next.next
    
    if fast:
        slow = slow.next
    
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    return not rev
