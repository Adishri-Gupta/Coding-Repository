# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res=None
        
        def helper(node):
            if not node:
                return [False,False]
            lp,lq=helper(node.left)
            rp,rq=helper(node.right)
            
            cp=node==p or lp or rp
            cq=node==q or lq or rq
            
            if cp and cq and not self.res:
                self.res=node
                
            return [cp,cq]
        helper(root)
        return self.res