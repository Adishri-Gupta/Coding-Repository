# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph=defaultdict(list)
        def graph_build(parent,child):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
                
            if child.left:
                graph_build(child,child.left)
            if child.right:
                graph_build(child,child.right)
        graph_build(None,root)
  
        
    
        q=deque()
        visited=set()
        dist=0
        ans=[]
        q.append((target.val,0))
        visited.add(target.val)
     
        while q:
            ele,dist=q.popleft()
           
            if dist==k:
                ans.append(ele)
            for nei in graph[ele]:
                if nei in visited:
                    continue
                visited.add(nei)
                q.append((nei,dist+1))

                    
        return ans
                    