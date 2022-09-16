class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if target>nums[mid]:
                lo=mid+1
            else:
                hi=mid-1
        return lo
        
                
        