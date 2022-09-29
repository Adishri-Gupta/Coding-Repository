class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            return max(self.houseRobber(nums[0:n-1]),self.houseRobber(nums[1:n]))
        
    def houseRobber(self,arr):
        dp=[0]*len(arr)
        
        dp[0]=arr[0]
        dp[1]=max(arr[0],arr[1])
        
        for i in range(2,len(arr)):
            dp[i]=max(dp[i-2]+arr[i],dp[i-1])
        return dp[-1]
        