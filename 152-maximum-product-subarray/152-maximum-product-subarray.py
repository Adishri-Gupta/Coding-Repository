class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxPro=nums[0]
        minPro=nums[0]
        res=maxPro
        for i in range(1,len(nums)):
            tempMax=max(nums[i],maxPro*nums[i],minPro*nums[i])
            minPro=min(nums[i],maxPro*nums[i],minPro*nums[i])
            maxPro=tempMax
            res=max(res,maxPro)
        return res
        