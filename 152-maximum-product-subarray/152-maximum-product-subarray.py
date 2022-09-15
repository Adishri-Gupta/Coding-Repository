class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        res = nums[0]
        
        maxFar=nums[0]
        
        minFar=nums[0]
        
        for i in range(1,len(nums)):
            
            
            maxFar, minFar = max(maxFar*nums[i] ,minFar*nums[i] ,nums[i]), min(maxFar*nums[i] ,minFar*nums[i] ,nums[i])

            res=max(maxFar,res)
        
        # print(res)
        return res