class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        
        while(l<r):
            sumVal = numbers[l]+numbers[r]
            if(sumVal==target):
                return ([l+1,r+1])
            elif(sumVal<target):
                l+=1
            else:
                r-=1
                
        return [-1,-1]
        
            