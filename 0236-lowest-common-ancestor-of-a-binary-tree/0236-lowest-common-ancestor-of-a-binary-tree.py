# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res=None
        def helper(node):
            nonlocal res
            if not node:
                return [False,False]
            lp,lq=helper(node.left)
            
            rp,rq=helper(node.right)
            
            cp=node==p or lp or rp
            cq=node==q or lq or rq
          
            if cp and cq and not res:
                res=node
            return [cp,cq]
        helper(root)
        return res
            
                
            
            