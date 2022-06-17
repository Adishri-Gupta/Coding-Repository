class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        area = 0
        
        
        def dfs(i,j):   
            if i<0 or j<0 or i>=row or j>=col or grid[i][j]!=1: return 0
            l,r,u,d=0,0,0,0
            grid[i][j] = 0
            l=dfs(i+1,j)
            r=dfs(i-1,j)
            u=dfs(i,j-1)
            d=dfs(i,j+1)
            return l + r + u + d + 1
            
            
            
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    
                    area = max (area, dfs(i,j))
        return area