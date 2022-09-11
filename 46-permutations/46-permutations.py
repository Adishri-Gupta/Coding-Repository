class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.helper(nums,[],0,set())
        return list(self.res)
        
    def helper(self,nums,currComb,start,visited):
        n=len(nums)
        if len(currComb)==n:
            self.res.append(list(currComb))
            return
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            self.helper(nums,currComb+[nums[i]],i+1,visited)
            visited.remove(nums[i])