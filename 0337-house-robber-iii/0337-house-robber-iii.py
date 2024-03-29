# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
#         if parent not robbed:
#             rob=node.val+helper(node.left)+helper(node.right)
        
#         if parent is robbed:
#             notrob=helper(node.left.left) + helper(node.right.right)
        
        def helper(node):
            
            if not node:
                return [0,0]
            
            left=helper(node.left)
            right=helper(node.right)
            rob=node.val+left[1]+right[1]
            not_rob=max(left)+max(right)
            
            return [rob,not_rob]
        money=helper(root)
        
        return max(money)