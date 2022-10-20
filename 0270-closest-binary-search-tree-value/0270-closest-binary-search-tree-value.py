# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.ans=[]
        
        def helper(node):
            if not node:
                return None
            
            l=helper(node.left)
            self.ans.append(node.val)
            r=helper(node.right)
            
        helper(root)
        return min(self.ans, key=lambda x:abs(x-target))