class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h=len(heights)
        w=len(heights[0])
        pac=set()
        at=set()
        if h==0 or w==0:
            return []
        
        def dfs(i,j,reachable):
            reachable.add((i,j))
            for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
                          row=i+r
                          col=j+c
                          if row<0 or row>=h or col<0 or col>=w:
                                continue
                          if (row,col) in reachable:
                                continue
                          if heights[row][col]<heights[i][j]:
                                continue
                          dfs(row,col,reachable)
            
        for c in range(w):
            dfs(0,c,pac)
            dfs(h-1,c,at)
        for r in range(h):
            dfs(r,0,pac)
            dfs(r,w-1,at)
        
        
        return list(pac.intersection(at))