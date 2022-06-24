class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            maxSum = max(maxSum, sum1)
            if sum1 < 0:
                sum1 = 0
        return maxSum
            
            
            
                