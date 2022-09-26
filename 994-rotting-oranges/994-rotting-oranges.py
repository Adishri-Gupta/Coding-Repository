class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        count=0
        time=0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append([i,j])
                elif grid[i][j]==1:
                        count+=1
        if count == 0:
            return 0
        
        while queue:
            l = len(queue)
            
            while l:
                i,j=queue.popleft()
                directions=[[-1,0],[0,-1],[1,0],[0,1]]
                for d in directions:
                    newr=i+d[0]
                    newc=j+d[1]
                    if newr>=0 and newc>=0 and newr<m and newc<n and grid[newr][newc]==1:
                        grid[newr][newc]=2
                        queue.append([newr,newc])
                        count-=1
                l-=1
            time+=1
            
        return time-1 if count==0 else -1