"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldMapNew={None:None}
        curr=head
        while curr is not None:
            copy=Node(curr.val)
            oldMapNew[curr]=copy
            curr=curr.next
        curr=head
        while curr is not None:
            copy=oldMapNew[curr]
            copy.next=oldMapNew[curr.next]
            copy.random=oldMapNew[curr.random]
            curr=curr.next
            
        return oldMapNew[head]