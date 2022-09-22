# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        self.findDia(root)
        return self.d
        
    def findDia(self, node:TreeNode):
        
        if not node: return -1
        
        left=self.findDia(node.left)
        right=self.findDia(node.right)
        
        self.d=max(self.d,left+right+2)
        
        return max(left,right)+1