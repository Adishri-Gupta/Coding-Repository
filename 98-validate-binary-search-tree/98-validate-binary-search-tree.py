import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.minMax(root)[0]
    
    def minMax(self,node):
        if not node.left and not node.right:
            return [True, node.val, node.val]
        
        is_left_valid, is_right_valid = True, True
        
        left_max, right_max = -math.inf, -math.inf
        
        left_min, right_min = math.inf, math.inf
        
        if node.left:
            [is_left_valid, left_min, left_max]=self.minMax(node.left)
        if node.right:
            [is_right_valid, right_min, right_max]=self.minMax(node.right)

        if not is_left_valid or not is_right_valid:
            return [False, math.inf, -math.inf]
        
        is_valid = left_max<node.val<right_min
        
        min_val = min(left_min, right_min, node.val)
        max_val = max(left_max,right_max, node.val)
        
        return [is_valid, min_val, max_val]