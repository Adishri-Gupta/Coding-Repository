class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n=len(grid)   
        def dfs(i,visited,grid):
            for j in range(n):
                if grid[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j,visited,grid)
            
            
            
        
        visited=set()
        res=0
        for i in range(n):
            if i not in visited:
                res+=1
                visited.add(i)
                dfs(i,visited,grid)
        return res
            
  
       