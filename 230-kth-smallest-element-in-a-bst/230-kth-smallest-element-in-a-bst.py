# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = self.inorder(root)
        return order[k-1]
    def inorder(self, node):
        if not node:
            return []
        l=self.inorder(node.left)
        r=self.inorder(node.right)
        return l + [node.val] + r
    
        