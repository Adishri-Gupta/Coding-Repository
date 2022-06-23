class Solution:
    def judgeCircle(self, moves: str) -> bool:
        currx, curry=0,0
        for c in moves:
            if c == 'U':
                curry+=1
            elif c == 'R':
                currx+=1
            elif c == 'L':
                currx-=1
            elif c == 'D':
                curry-=1
        if currx==0 and curry==0:
            return True
        else: return False
        