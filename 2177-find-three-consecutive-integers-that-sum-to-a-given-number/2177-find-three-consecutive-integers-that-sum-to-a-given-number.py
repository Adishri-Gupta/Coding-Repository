class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res=[]
        val=num%3
        valDi=num//3
        if val!=0:
            return res
        else:
            res.append(valDi-1)
            res.append(valDi)
            res.append(valDi+1)
        return res
        