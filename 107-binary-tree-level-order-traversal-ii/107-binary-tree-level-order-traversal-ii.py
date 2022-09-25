# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return []
        queue=deque()
        queue.append(root)
        
        while queue:
            currSize=len(queue)
            currList=[]
            while currSize>0:
                ele=queue.popleft()
                currList.append(ele.val)
                currSize-=1
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            ans.append(currList)
        return reversed(ans)
        