# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        
        def helper(node):
            if not node:
                return ''
                
            
            l = helper(node.left)
            r = helper(node.right)
            if not l and r:
                l='()'
            return '('+str(node.val) + l + r + ')' 
       
        res=helper(root)
        return res[1:-1]

        
        