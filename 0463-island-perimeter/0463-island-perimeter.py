class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        self.total=0
        self.visited=set()
        def dfs(i,j):
            
            edges=4
            directions=[[-1,0],[1,0],[0,-1],[0,1]]
            for d in directions:
                newx=i+d[0]
                newy=j+d[1]
                if 0<=newx<len(grid) and 0<=newy<len(grid[0]) and grid[newx][newy]==1:
                    edges-=1
                    if (newx,newy) not in self.visited:
                        self.visited.add((newx,newy))
                        dfs(newx,newy)
            self.total+=edges
        
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.visited.add((i,j))
                    dfs(i,j)
                    return self.total