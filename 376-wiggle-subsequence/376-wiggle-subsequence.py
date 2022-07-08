class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = 1
        next_expected = None

        if len(nums) < 2:
            return length

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0 and (next_expected == "UP" or next_expected == None):
                next_expected = "DOWN"
                length += 1
            elif nums[i] - nums[i-1] < 0 and (next_expected == "DOWN" or next_expected ==None):
                next_expected = "UP"
                length += 1
        return length
    