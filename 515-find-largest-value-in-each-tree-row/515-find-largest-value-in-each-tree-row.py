# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)
        
        while len(q) > 0:
            cnt = len(q)
            row = [] 
            while cnt>0:
                ele = q.popleft()
                row.append(ele.val)
                if ele.left: q.append(ele.left)
                if ele.right: q.append(ele.right)
                cnt-=1
            res.append(max(row))
        
        return res