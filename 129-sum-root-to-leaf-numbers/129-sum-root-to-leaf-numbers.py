# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res=[]
        self.helper(root,str(root.val))
        sumVal=0
        for i in range(len(self.res)):
            sumVal+=int(self.res[i])
        return sumVal
    
    def helper(self,node,currComb):
        
        if not node:
            return 
        
        if not node.left and not node.right:
            self.res.append(currComb)
            return
        if node.left:
            self.helper(node.left,currComb+str(node.left.val))
        if node.right:
            self.helper(node.right,currComb+str(node.right.val))
        
        