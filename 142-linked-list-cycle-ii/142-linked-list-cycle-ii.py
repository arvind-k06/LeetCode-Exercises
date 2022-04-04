# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        s = f = head
        
        while(s and f and f.next):
            s = s.next
            f = f.next.next
            
            if s == f:
                break
        else:
            return None
        
        while(head != s):
            s = s.next
            head = head.next
        return head
        