class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h=len(heights)
        w=len(heights[0])
        pac=set()
        at=set()
        q1=deque()
        q2=deque()
        
        
        
        
        for j in range(w):
            q1.append((0,j))
            
            q2.append((h-1,j))
            pac.add((0,j))
            at.add((h-1,j))
        for i in range(h):
            
            q1.append((i,0))
            q2.append((i,w-1))
            pac.add((i,0))
            at.add((i,w-1))
        while q1:
            x,y=q1.popleft()
            directions=[[-1,0],[1,0],[0,1],[0,-1]]
            for d in directions:
                newx=x+d[0]
                newy=y+d[1]
                if (newx,newy) in pac:
                    continue
                if 0<=newx<h and 0<=newy<w and heights[newx][newy]>=heights[x][y]:
                    q1.append((newx,newy))
                    pac.add((newx,newy))
        while q2:
            x,y=q2.popleft()
            directions=[[-1,0],[1,0],[0,1],[0,-1]]
            for d in directions:
                newx=x+d[0]
                newy=y+d[1]
                if (newx,newy) in at:
                    continue
                if 0<=newx<h and 0<=newy<w and heights[newx][newy]>=heights[x][y]:
                    q2.append((newx,newy))
                    at.add((newx,newy))
        return list(pac.intersection(at))
            