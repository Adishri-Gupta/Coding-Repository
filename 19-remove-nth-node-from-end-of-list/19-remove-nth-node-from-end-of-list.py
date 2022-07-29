# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pnt1=head
        pnt2=head
        pnt2 = pnt1 = dummy = ListNode(0)
        dummy.next = head
       
        for _ in range(n):
            pnt2=pnt2.next
       
        while pnt2 and pnt2.next is not None:
            pnt1=pnt1.next
            pnt2=pnt2.next
        
        val=pnt1.next.next
        pnt1.next=val
        return dummy.next
       