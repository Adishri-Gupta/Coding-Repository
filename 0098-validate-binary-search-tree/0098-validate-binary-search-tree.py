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
                return [-math.inf,math.inf,True]
            maxl,minl,isValidl=helper(node.left)
            maxr,minr,isValidr=helper(node.right)
            
            isValidNode=isValidl and isValidr and maxl<node.val<minr
            maxVal=max(maxr,node.val)
            minVal=min(minl,node.val)
            
            return [maxVal,minVal,isValidNode]
        
        return True if helper(root)[2] else False
        
            
        