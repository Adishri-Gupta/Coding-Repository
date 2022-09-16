"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        finalMax=-math.inf
        if not root:
            return 0
        if root.children==[]:
            return 1
        for c in root.children:
            maxD=self.maxDepth(c)
            finalMax=max(maxD,finalMax)
        return finalMax+1
        