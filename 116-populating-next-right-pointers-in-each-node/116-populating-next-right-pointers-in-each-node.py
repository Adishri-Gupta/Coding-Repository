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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        lqueue=collections.deque()
        lqueue.append(root)
        lastPopped=root
        while lqueue:
            
            currSize=len(lqueue)
            currList=[]
            while currSize>0:
                currNode=lqueue.popleft()
               
                currSize-=1

                if currNode.left:
                    lqueue.append(currNode.left)
                if currNode.right:
                    lqueue.append(currNode.right)
                    
                if currSize!=0:
                    currNode.next=lqueue[0]
            

        return root
        
            