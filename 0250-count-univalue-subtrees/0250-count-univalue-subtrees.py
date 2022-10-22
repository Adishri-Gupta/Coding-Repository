# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return True
            isSameL=helper(node.left)
            isSameR=helper(node.right)
            
            
            if (isSameL and isSameR and (node.left is None or node.left.val==node.val) and (node.right is None or node.right.val==node.val)):
                self.cnt+=1
                return True
            else:
                return False
          
        self.cnt=0
        helper(root)
        return self.cnt