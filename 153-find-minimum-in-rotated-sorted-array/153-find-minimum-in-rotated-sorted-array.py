class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        if nums[l]<nums[r]:
            return nums[l]
        
        
        while(l<=r):
            m = (l+r)//2
            
            if m-1>-1 and nums[m-1]>nums[m]:
                return nums[m]
            
            if m+1<=r and nums[m]>nums[m+1]:
                return nums[m+1]
            
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m-1
            
        
        return nums[0]
        