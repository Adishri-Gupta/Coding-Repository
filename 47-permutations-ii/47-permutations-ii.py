class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        self.res=[]
        counter=Counter(nums)
        
        self.helper([],counter,nums)
        return self.res
    def helper(self,currComb,counter,nums):
        n=len(nums)
        
    
        if len(currComb)==n:
            self.res.append(list(currComb))
            return
        for i in counter:
            if counter[i]>0:
                counter[i]-=1
                self.helper(currComb+[i],counter,nums)
                counter[i]+=1  
            