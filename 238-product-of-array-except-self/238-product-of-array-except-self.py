class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lArray=[1]*n
        rArray=[1]*n
        for i in range(1,n):
            lArray[i]=lArray[i-1]*nums[i-1]
        for i in reversed(range(0,n-1)):
            rArray[i]=rArray[i+1]*nums[i+1]
        for i in range(n):
            nums[i]=lArray[i]*rArray[i]
        return nums
        