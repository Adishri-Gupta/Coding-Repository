# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sumVal=0
        self.helper(root,0)
        
        # for i in range(len(self.res)):
        #     sumVal+=int(self.res[i])
        # return sumVal
        return self.sumVal
    
    def helper(self,node,currNum):
        
        if not node:
            return 
        currNum=currNum*10+node.val
        if not node.left and not node.right:
            self.sumVal+=currNum
            return
       
        self.helper(node.left,currNum)
        
        self.helper(node.right,currNum)
        
        