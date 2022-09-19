class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastZero=0
        for i in nums:
            if i !=0:
                nums[lastZero]=i
                lastZero+=1
        for i in range(lastZero, len(nums)):
            nums[i]=0
        
        return nums