# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res=[]
        self.helper(root,'')
        return self.res
    def helper(self,root,currPath):
        if not root:
            return 
        currPath += str(root.val)
        if not root.left and not root.right:
            self.res.append(currPath)
            return
        currPath+='->'
        self.helper(root.left,currPath)
        self.helper(root.right,currPath)
        
        
        