class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach=0
        
        for i in range(len(nums)):
            if i+nums[i]>maxReach:
                maxReach=i+nums[i]
            if i==maxReach:
                break
                
    
        return maxReach>=len(nums)-1
            
        