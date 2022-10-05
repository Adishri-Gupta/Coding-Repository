"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head != None: self.flatten_rec(head)
        return head
        
    def flatten_rec(self, head):
        curr, tail = head, head
        while curr != None:
            child, next = curr.child, curr.next
            if child != None:
                _tail = self.flatten_rec(child)
                _tail.next = next
                if next != None: next.prev = _tail
                curr.next = child
                curr.child = None
                child.prev = curr
                curr = _tail
            else:
                curr = next
            if curr != None: tail = curr
        
        return tail