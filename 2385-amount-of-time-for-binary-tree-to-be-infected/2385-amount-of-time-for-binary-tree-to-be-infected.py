# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
    
        conn = collections.defaultdict(list)
        def connect(parent, child):
     
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
     
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
       
        connect(None, root)
        print(conn)
        q=deque()
       
        visited=set()
        q.append(start)
        visited.add(start)
        d=-1
        print(q,visited)
        while q:
            currSize=len(q)
            while currSize>0:
                ele=q.popleft()
                currSize-=1

                for nei in conn[ele]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            d+=1
            
        return d
            
            
            
            