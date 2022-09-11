class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res=[]
        self.helper(k,n,[],1)
        return self.res
    def helper(self,k,remain,currComb,start):
        if remain==0 and len(currComb)==k :
            self.res.append(list(currComb))
            return
        elif remain<0 or len(currComb)==k:
            return
        
        for i in range(start,10):
            self.helper(k,remain-i,currComb+[i],i+1)