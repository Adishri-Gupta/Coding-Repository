class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if len(digits)==0:
            return []

        
        mapD = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z'],
        }
        
        
        def helper(currComb,i):
            if len(currComb)==len(digits):
                res.append(currComb)
                return

            for c in mapD[digits[i]]:
                helper(currComb+c,i+1)
        helper('',0)
        return res
