import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)
        
    
    def helper(self, node: TreeNode):
        if not node:
            return [math.inf, -1*math.inf]
        
        left = self.helper(node.left)
        
        right = self.helper(node.right)
        
        if not left or not right:
            return False
        
        if node.val <= left[1] or node.val >= right[0]:
            return False
        
        return [min(left[0], right[0], node.val), max(left[1], right[1], node.val)]
        
            
        