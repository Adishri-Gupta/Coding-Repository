# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        curr=head
        prev=None
        nex=head.next
        
        while curr:
            curr.next=prev
            
            prev=curr
            curr=nex
            if nex:
                nex=nex.next
        
        head=prev
        return head
        