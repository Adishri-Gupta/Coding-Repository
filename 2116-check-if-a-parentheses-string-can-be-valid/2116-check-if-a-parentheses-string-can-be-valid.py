class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        bal=0
        flip_open, flip_close = 0, 0
        if n%2!=0:
            return False
        for i in range(len(s)):
            ch=s[i]
            if locked[i] == '0':
                if ch=='(': flip_open+=1
                else: flip_close+=1
            if ch=='(':
                bal+=1
            else:
                bal-=1
            if bal<0:
                if flip_close:
                    bal+=2
                    flip_close-=1
                else:
                    return False
            flip_open = min(bal//2, flip_open)

        return bal-2*flip_open==0