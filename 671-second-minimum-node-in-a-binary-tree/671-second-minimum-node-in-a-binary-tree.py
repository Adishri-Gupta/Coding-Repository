# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.smallest=root.val
        self.res=math.inf
        
        self.updateMin(root)
        if self.res<math.inf:
            return self.res
        else:
            return -1
    def updateMin(self,node):
        
        if node:
            if self.smallest<node.val<self.res:
                self.res=node.val
            self.updateMin(node.left)
            self.updateMin(node.right)