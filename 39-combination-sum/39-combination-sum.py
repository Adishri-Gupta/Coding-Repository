class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.helper(candidates,target,[],0)
        return self.res
    def helper(self,candidates,target,path,start):
        if target<0:
            return
        if target==0:
            self.res.append(list(path))
            return
        for i in range(start, len(candidates)):
            self.helper(candidates,target-candidates[i],path+[candidates[i]],i)
        
        