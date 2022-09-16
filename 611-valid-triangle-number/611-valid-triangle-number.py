class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        if not nums or len(nums)<3:
            return 0
        for i in range(len(nums)):
            l,r=0,i-1
            while l<=r:
                if nums[l]+nums[r]>nums[i]:
                    count+=r-l
                    r-=1
                else:
                    l+=1
        return count