# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root:
            return []
        q=deque()
        ans=[]
        q.append(root)
        flag=True
        while q:
            currSize=len(q)
            currList=[]
            
            while currSize>0:
                
                currVal=q.popleft()
                currList.append(currVal.val)
                currSize-=1
                
                if currVal.left:
                    q.append(currVal.left)
                if currVal.right:
                    q.append(currVal.right)
            if flag:
                ans.append(currList)
            else:
                ans.append(currList[::-1])
            flag=not flag
        return ans
                    
            
                
            