class Solution:
    def modifyString(self, s: str) -> str:
        
        ques=[]
        alpha='abcdefghijklmnopqrstuvwxyz'
        st,e = 0, 0
        while e<len(s):
            if s[e] == '?':
                e+=1      
            else:
                if st!=e:
                    ques.append((st,e-1))
                e+=1
                st=e
        
        if st!=e:
            ques.append((st,e-1))        
        for q in ques:
            l,r=q
            
            if l == 0 and r == len(s)-1:
                q = (r-l+1)//26
                rem = (r-l+1)%26
                s = q*alpha + alpha[:rem]
            elif l==0:
                cr=s[r+1]
                ar=ord(cr)-ord('a')
                alphaMod= alpha[:ar] + alpha[ar+1:]
                s = alphaMod[0:r+1] + s[r+1:]
            elif r==len(s)-1:
                cl=s[l-1]
                al=ord(cl)-ord('a')
                alphaMod=alpha[0:al]+alpha[al+1:]
                s=s[:l]+alphaMod[0:r-l+1]
            else:
                cl = s[l-1]
                cr = s[r+1]


                al,ar = ord(cl)-ord('a'), ord(cr)-ord('a')

                al, ar = min(al, ar), max(al, ar)

                alphaMod= alpha[0:al] + alpha[al+1:ar] + alpha[ar+1:]
                s = s[:l] + alphaMod[0:r-l+1] + s[r+1:]
            
            
            
            
            
            
            
           
        return s
            