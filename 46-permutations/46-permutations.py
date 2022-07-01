class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        
        self.helper(0,nums,[],set())
        return self.res
    def helper(self,start,nums,path, visited):
        if len(list(path))==len(nums):
            self.res.append(list(path))
            return
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            self.helper(start+1,nums,path+[nums[i]], visited)
            visited.remove(nums[i])
        
            
        