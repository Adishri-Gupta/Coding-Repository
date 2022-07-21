class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        valSum=0
        l=0
        r=0
        mapS=set()
        erasure=0
        while r<len(nums):
            right=nums[r]
            while right in mapS:
                left=nums[l]
                valSum -= left
                mapS.remove(left)
                l += 1
            valSum += right
            mapS.add(right)
            r+=1
            erasure = max(erasure, valSum)

        return erasure