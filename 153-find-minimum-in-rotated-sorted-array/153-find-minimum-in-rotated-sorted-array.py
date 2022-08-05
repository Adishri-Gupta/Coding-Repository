class Solution:
    def findMin(self, nums: List[int]) -> int:
        minEl=nums[0]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                minEl = min(minEl, nums[i+1])
        return minEl
        
        