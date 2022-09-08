class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapVal={}
        for i in range(len(nums)):
            val=target-nums[i]
            if val in mapVal:
                return [i,mapVal[val]]
            mapVal[nums[i]]=i
        return