class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappedDiff = {}
        
        for i in range(len(nums)):
            val = target - nums[i]
            if val in mappedDiff:
                return [i,mappedDiff[val]]
            mappedDiff[nums[i]] = i
        return 
        