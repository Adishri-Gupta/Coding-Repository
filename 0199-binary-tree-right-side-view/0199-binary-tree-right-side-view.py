# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        ans=[]
        if not root:
            return []
        q.append(root)
        while q:
            currSize=len(q)
            currList=[]
            
            while currSize>0:
                
                node=q.popleft()
                currList.append(node.val)
                currSize-=1
                
                if node.left is not None:
                    q.append(node.left)
                    
                if node.right is not None:
                    q.append(node.right)
            ans.append(currList[-1])
        return ans
            
        
        