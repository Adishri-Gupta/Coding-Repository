class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s)==0:
            return 0
        temp='0'
        res=0
        i=0
        
        if s[0]=='-' or s[0]=='+':
            temp=s[0]
            i=1
        minInt=-2**31
        maxInt=2**31-1
        for i in range(i,len(s)):
            if s[i].isdigit():
                temp+=s[i]
            else:
                break
       
        if len(temp)>1:
            res=int(temp)
        if res>maxInt:
            return maxInt
        elif res<minInt:
            return minInt
        else:
            return res
            
            