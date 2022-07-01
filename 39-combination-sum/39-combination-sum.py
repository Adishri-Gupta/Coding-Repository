class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        
        def helper(target, path,c, start):

            if target<0:
                return

            if target==0:
                res.append(list(path))
                return

            for i in range(start, len(c)):
                path.append(c[i])
                helper(target-c[i],path,c,i)
                path.pop()
        
        helper(target,[],candidates, 0)
        return res