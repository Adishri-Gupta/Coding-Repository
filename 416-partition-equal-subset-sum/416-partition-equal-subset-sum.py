class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumVal=sum(nums)
        if sumVal%2!=0:
            return False
        target=sumVal//2
        if self.subsetSum(nums,target):
            return True
        
    def subsetSum(self, nums, target):
        n=len(nums)
        dp=[[False]*(target+1) for _ in range(n+1)]
        dp[0][0]=True
        for i in range(1,n+1):
            for j in range(target+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
        
   