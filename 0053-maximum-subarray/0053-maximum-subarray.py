class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=[0 for i in range(len(nums))]
        maxSub[0]=nums[0]
        for i in range(1,len(nums)):
            maxSub[i]=max(maxSub[i-1]+nums[i],nums[i])
        return max(maxSub)
            
            
            
            
                