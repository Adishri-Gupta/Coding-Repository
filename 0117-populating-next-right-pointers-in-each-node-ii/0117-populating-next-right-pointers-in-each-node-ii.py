"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        q=deque()
        q.append(root)
        while q:
            currSize=len(q)
            
            while currSize>0:
                ele=q.popleft()
                
                currSize-=1
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                if currSize!=0:
                    ele.next=q[0]
        return root
                
                