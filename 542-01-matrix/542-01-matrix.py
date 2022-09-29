class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        visited=set()
        queue=deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    visited.add((i,j))
                    queue.append([i,j])
        while queue:
            i,j=queue.popleft()
            directions=[[-1,0],[0,1],[1,0],[0,-1]]
            for r,c in directions:
                xx=i+r
                yy=j+c
                
                if xx<m and xx>=0 and yy<n and yy>=0 and (xx,yy) not in visited:
                    mat[xx][yy]=mat[i][j]+1
                    visited.add((xx,yy))
                    queue.append([xx,yy])
                    
        return mat