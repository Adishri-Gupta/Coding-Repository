class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        maxI=nums.index(max(nums))
        minI=nums.index(min(nums))
        n=len(nums)
        
        res=min(max(maxI,minI)+1,
                max(n-maxI,n-minI),
                maxI+1+n-minI,
                minI+1+n-maxI)
        
        return res