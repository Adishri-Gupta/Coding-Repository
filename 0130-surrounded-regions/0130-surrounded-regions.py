class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q=deque()
        visited=set()
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j]=='O':
                    q.append((i,j))
                    visited.add((i,j))
        while q:
            x,y=q.popleft()
            directions=[[-1,0],[0,1],[1,0],[0,-1]]
            for d in directions:
                newx=x+d[0]
                newy=y+d[1]
                if (newx,newy) not in visited and 0<=newx<m and 0<=newy<n and board[newx][newy]=='O':
                    q.append((newx,newy))
                    visited.add((newx,newy))
        print(visited)
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    board[i][j]='X'
                    
        return board
                    
                    