class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        lenVal=1
        flag=None
        if len(nums)<2:
            return lenVal
        
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 0 and (flag == "UP" or flag == None):
                flag = "DOWN"
                lenVal += 1
            elif nums[i] - nums[i-1] < 0 and (flag == "DOWN" or flag == None):
                flag = "UP"
                lenVal += 1
        
        
        
        return lenVal
    