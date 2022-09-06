class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longCon=1
        lenVal=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if nums[i]==nums[i-1]+1:
                    lenVal+=1
                else:
                    longCon=max(lenVal,longCon)
                    lenVal=1
        return max(longCon,lenVal)