import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def helper(node):
            if not node:
                return [math.inf,-math.inf,True]
            
            minl,maxl,isValidL=helper(node.left)
            minr,maxr,isValidR=helper(node.right)
            
            isValidNode=isValidL and isValidR and maxl<node.val<minr
            minNode=min(minl, node.val)
            maxNode=max(maxr, node.val)
            
            return [minNode,maxNode,isValidNode]
        
        return True if helper(root)[2] else False
        
        
        
            
        