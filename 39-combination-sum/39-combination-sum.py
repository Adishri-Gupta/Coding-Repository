class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.helper(target,[],candidates, 0)
        return self.res
        
    def helper(self, target, path,c, start):

        if target<0:
            return

        if target==0:
            self.res.append(list(path))
            return

        for i in range(start, len(c)):
            path.append(c[i])
            self.helper(target-c[i],path,c,i)
            path.pop()
    