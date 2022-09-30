class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        self.helper(nums,0,[],set())
        return self.ans
    def helper(self,nums,start,currComb,visited):
        if len(currComb)==len(nums):
            self.ans.append(list(currComb))
            
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            currComb.append(nums[i])
            self.helper(nums,i+1,currComb,visited)
            currComb.pop()
            visited.remove(nums[i])
        
            