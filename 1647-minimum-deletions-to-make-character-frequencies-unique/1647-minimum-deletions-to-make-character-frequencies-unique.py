class Solution:
    def minDeletions(self, s: str) -> int:
        uniFreq=set()
        counter=Counter(s)
        
        sortedFreq=dict(sorted(counter.items(), key = lambda x: x[1], reverse = True))
        Nodel=0
        for l in sortedFreq.values():
            
            while l and l in uniFreq:
                Nodel+=1
                l-=1
            
            uniFreq.add(l)
        return Nodel
        
        