class Solution:
    def minSwaps(self, data: List[int]) -> int:
        count = sum(data)
        l=0
        r=count
        zero=0
    
        for i in range(r):
            if data[i] == 0:
                zero += 1
        zeroVal=zero
        while r<len(data):
            if data[l]==0:
                zero-=1
            l+=1
            
            if data[r]==0:
                zero+=1
            r+=1
                
            zeroVal=min(zero,zeroVal)
        return zeroVal
            
  