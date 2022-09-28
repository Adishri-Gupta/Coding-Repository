class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = -1
        prefixSum=[0]*len(nums)
        prefixSum[0]=nums[0]
        sumVal=sum(nums)
        for i in range(1,len(nums)):
            prefixSum[i]=prefixSum[i-1]+nums[i]
        for i in range(len(nums)):
            if (prefixSum[i-1] if i>0 else 0) == sumVal-prefixSum[i]:
                pivot = i
                break
        
        return pivot