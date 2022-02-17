# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        t = head
        
        # if n ==1: return 
        c=0
        while(t):
            t=t.next
            c+=1
        # if n==2 and 
        v = c-n+1
        if v == 1:
            return head.next
        print(v)
        p1 = head
        p2 = head.next

        for i in range(v-2):
            p1, p2 = p1.next, p2.next

        temp = p2.next
        p1.next = temp
        
        return head
        # print(p1,"ndnjnfdfdf", p2)
    