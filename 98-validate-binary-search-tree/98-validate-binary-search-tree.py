import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.validate(root,-math.inf,math.inf)
        
        
    def validate(self,node,low,high):
        if not node:
            return True
        
        if node.val<=low or node.val>=high:
            return False
        
        return self.validate(node.right,node.val,high) and self.validate(node.left,low,node.val)
        
        
        
            
        