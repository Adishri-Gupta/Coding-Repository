class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_Reach=0
        for i in range(len(nums)):
            if i+nums[i]>max_Reach:
                max_Reach=i+nums[i]
            if i==max_Reach:
                break
        return max_Reach>=len(nums)-1