class Solution:
    def __init__(self, w: List[int]):
        self.w=w
        self.prefix_sum = [0]*len(w)
        self.prefix_sum[0]=w[0]
        for i in range(1,len(w)):
            self.prefix_sum[i]=self.prefix_sum[i-1]+w[i]
        
       
    def pickIndex(self) -> int:
       
        find=random.random()*self.prefix_sum[-1]
        lo,hi=0,len(self.w)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if find>self.prefix_sum[mid]:
                lo=mid+1
            else:
                hi=mid-1
        return lo
        
        
        
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()