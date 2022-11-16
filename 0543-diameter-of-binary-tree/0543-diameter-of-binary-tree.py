# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d=0
        self.diameter(root)
        return self.d
    def diameter(self,node):
        if not node:
            return -1
        left=self.diameter(node.left)
        right=self.diameter(node.right)
        
        
        self.d=max(self.d,left+right+2)
        return max(left,right)+1