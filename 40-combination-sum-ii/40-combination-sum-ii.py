class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        candidates.sort()
        self.helper(candidates,target,0,[])
        return self.res
    def helper(self,candidates,target,start,path):
        if target<0:
            return
      
        if target==0:
            self.res.append(list(path))
        
        for i in range(start, len(candidates)):
            if i>start and candidates[i]==candidates[i-1]:
                continue
            self.helper(candidates,target-candidates[i],i+1,path+[candidates[i]])
        
        