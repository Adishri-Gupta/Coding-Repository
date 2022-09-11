class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res=[]
        self.helper(k,[],1,n)
        return self.res
    def helper(self,k,currComb,start,n):
        if len(currComb)==k:
            self.res.append(list(currComb))
        for i in range(start,n+1):
            self.helper(k,currComb+[i],i+1,n)
  