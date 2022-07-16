class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n=len(nums)
        for i in range(len(nums)):
            if i%2!=0:
                if i+1<n:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
        