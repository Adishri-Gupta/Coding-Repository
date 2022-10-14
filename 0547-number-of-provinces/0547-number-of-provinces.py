class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n=len(grid)   
        visited=set()
        res=0
        q=deque()
            
        for i in range(n):
            if i not in visited:
                visited.add(i)
                q.append(i)
                while q:
                    s=q.popleft()
                
                    for j in range(n):
                        if grid[s][j] and j not in visited:
                            q.append(j)
                    visited.add(s)
                res+=1
        return res
            
  
       