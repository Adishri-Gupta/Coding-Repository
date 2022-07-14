class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF=2147483647
        m=len(rooms)
        n=len(rooms[0])
        def dfs(i,j,path):
            if i<0 or j>=n or j<0 or i>=m or (rooms[i][j]<=path and path!=0):
                return
            rooms[i][j]=path
            dfs(i+1,j,path+1)
            dfs(i,j+1,path+1) 
            dfs(i-1,j,path+1)
            dfs(i,j-1,path+1)                
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    dfs(i,j,0)
            
        