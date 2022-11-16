class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapVal={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in mapVal:
                return [mapVal[rem],i]
            
            mapVal[nums[i]]=i
