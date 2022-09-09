class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        longCon=1
        maxLen=0
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                longCon+=1
            else:
                maxLen=max(longCon,maxLen)
                longCon=1
        return max(longCon,maxLen)
            