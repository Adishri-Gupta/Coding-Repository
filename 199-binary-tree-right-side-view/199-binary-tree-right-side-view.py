# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans

        # Initialize queue 
        queue = collections.deque()
        queue.append(root)

        # Iterate over the queue until it's empty
        while queue:
            # Check the length of queue
            currSize = len(queue)
            currList = []

            while currSize > 0:
                # Dequeue element
                currNode = queue.popleft()
                currList.append(currNode.val)
                currSize -= 1

                # Check for left child
                if currNode.left is not None:
                    queue.append(currNode.left)
                # Check for right child
                if currNode.right is not None:
                    queue.append(currNode.right)

            # Append the currList to answer after each iteration
            ans.append(currList[-1])
        return ans
        
        