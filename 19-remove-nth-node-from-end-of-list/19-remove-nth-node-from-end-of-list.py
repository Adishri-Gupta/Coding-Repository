# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pnt1=head
        pnt2=head
       
        for _ in range(n):
            pnt2=pnt2.next
        if pnt2 is None:
            return head.next
        while pnt2.next is not None:
            pnt1=pnt1.next
            pnt2=pnt2.next
        
        val=pnt1.next.next
        pnt1.next=val
        return head
       