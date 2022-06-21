class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while(l<r):
                sumVal=nums[i]+nums[l]+nums[r]
                if sumVal==0:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                    
                elif sumVal<0:
                    l+=1
                else:
                    r-=1

        return res