class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res=[]
        changed.sort()
        mapFreq=defaultdict()
        zeroCount=0
        if len(changed)%2!=0:
            return []
        for i in changed:
            if i in mapFreq:
                mapFreq[i]+=1
            else:
                mapFreq[i]=1
                
        if 0 in mapFreq and mapFreq[0]%2!=0:
            return []
            
        if len(changed)==1:
            return []
        for i in changed:
     
            if i in mapFreq and mapFreq[i]>0:
                mapFreq[i]-=1
                j=i*2
                # print(j)
                if j in mapFreq and mapFreq[j] > 0:
                    res.append(i)
                    mapFreq[j]-=1
      

    
        return res if len(res)==len(changed)//2 else []
        