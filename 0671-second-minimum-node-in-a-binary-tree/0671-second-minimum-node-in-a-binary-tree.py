# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        order=set()
        ans=math.inf
        self.helper(root,order)
        for ele in order:
            if root.val<ele<ans:
                ans=ele
        return ans if ans<math.inf else -1
    def helper(self,node, order):
        if not node:
            return
        self.helper(node.left,order)
        order.add(node.val)
        self.helper(node.right,order)