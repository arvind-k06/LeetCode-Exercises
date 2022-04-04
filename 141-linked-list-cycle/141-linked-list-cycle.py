# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        s = set()
        # s.add(head)
        d = head
        
        while(d):
            if d in s:
                return True
            s.add(d)
            d = d.next
        
        return False
        f = s = head
        while(s and f and f.next):
            s = s.next
            f = f.next.next
            if s == f:
                return True
        
        return False
        
        