# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        res=[]
        maxRow=-1
        if not root:
            return 
        queue.append(root)
        
        while queue:
            currSize=len(queue)
            currList=[]
            while currSize>0:
                node=queue.popleft()
                currList.append(node.val)
                currSize-=1
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(max(currList))
        return res
        
        
            
            