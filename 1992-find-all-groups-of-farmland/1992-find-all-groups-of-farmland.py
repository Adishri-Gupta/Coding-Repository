class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        m=len(land)
        n=len(land[0])
        res=[]
        cache = {}
        
        def dfs(i,j,endi,endj):
            k = (i,j,endi,endj)
            
            if k in cache:
                return cache[k]
            if i<0 or j<0 or i>=len(land) or j>=len(land[0]) or land[i][j]!=1:
                return [endi,endj]
      
            
            land[i][j]=-1
            
            endir, endjr = dfs(i+1,j,endi,endj)
            endil, endjl = dfs(i-1,j,endi,endj)
            endiu, endju = dfs(i,j+1,endi,endj)
            endid, endjd = dfs(i,j-1,endi,endj)
            
            endi = max(endir,endil,endiu,endid,i)
            endj = max(endjr,endjl,endju,endjd,j)
            cache[k] = [endi,endj] 
            
            return cache[k]
            
        for i in range(m):
            for j in range(n):
                if land[i][j]==1:

                    endi,endj=dfs(i,j,i,j)
                    
                    res.append([i,j,endi,endj])
        return res