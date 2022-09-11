# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        headOld=head
        headNew=head
        lenOfList=1
        if head is None:
            return None
        if head.next is None:
            return head
        while headOld.next:
            headOld=headOld.next
            lenOfList+=1
        headOld.next=head
        
        k=k%lenOfList
        newTail=head
        for i in range(lenOfList-k-1):
            newTail=newTail.next
        headNew=newTail.next
            
        newTail.next=None
        return headNew
            