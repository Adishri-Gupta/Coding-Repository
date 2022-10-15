class Solution:
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m=len(grid2)
        n=len(grid2[0])
        
        
        def findIslands(grid):
            islands=[]
            visited=set()
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1 and (i,j) not in visited:
                        islands.append(bfs(i,j,grid,visited))
            return islands        
                    
        def bfs(i,j,grid,visited):
            q=deque()
            q.append((i,j))
            island=[]
            directions=[[-1,0],[1,0],[0,-1],[0,1]]
            while q:
                x,y=q.popleft()
                
                if (x,y) in visited: continue
                
                visited.add((x,y))
                
                island.append((x,y))
                
                for d in directions:
                    newx=x+d[0]
                    newy=y+d[1]
                    if newx<0 or newy<0 or newx>=m or newy>=n or grid[newx][newy]!=1:
                        continue
                    q.append((newx,newy))
            
            return island
        
        
        cnt = 0
        islands2=findIslands(grid2)
        
        for i2 in islands2:
            flag = True
            for (x,y) in i2:
                if grid1[x][y] == 0:
                    flag = False
                    break
            cnt += (1 if flag else 0)
        
        return cnt