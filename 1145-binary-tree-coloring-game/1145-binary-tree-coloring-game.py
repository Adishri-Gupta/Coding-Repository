# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        node_dict = {}
        self.helper(root, None, node_dict)
        x_node = node_dict[x]
        
        y_cap_par, y_cap_l, y_cap_r = 0, 0, 0
        # if we capture parent
        if x_node.parent:
            y_cap_par = n - x_node.cnt
            
        # if we capture left_child
        if x_node.left:
            y_cap_l = x_node.left.cnt
            
        # if we capture right_child
        if x_node.right:
            y_cap_r = x_node.right.cnt
        
        
        y_cap_max = max(y_cap_par, y_cap_l, y_cap_r)
        
        print(y_cap_max)
        
        return y_cap_max>n//2
            
    def helper(self, node, p, nd):
        if not node: return 0
        
        node.parent = p
        
        l_cnt = self.helper(node.left, node, nd)
        r_cnt = self.helper(node.right, node, nd)
        
        node.cnt = l_cnt+r_cnt+1
        
        nd[node.val] = node
        return node.cnt