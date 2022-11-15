# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node,ans):
            if not node:
                return True
            lleaf=helper(node.left,ans)
        
            rleaf=helper(node.right,ans)
            
            if not node.left and not node.right:
                ans.append(node.val)
            
            return ans
        
        
        seq1=helper(root1,[])
        seq2=helper(root2,[])
        print(seq1,seq2)
        return True if seq1==seq2 else False
            