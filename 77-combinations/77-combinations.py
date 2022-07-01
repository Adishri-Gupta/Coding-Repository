class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res=[]
        self.helper(1,[],k,n)
        return self.res
    def helper(self,i,path,k,n):
        
        if len(path)==k:
            self.res.append(list(path))
            return
        for i in range (i,n+1):
            
            self.helper(i+1,path+[i],k,n)