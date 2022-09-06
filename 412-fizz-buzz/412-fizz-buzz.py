class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        while n>0:
            if n%3==0 and n%5==0:
                res.append("FizzBuzz")
            elif n%3==0:
                res.append("Fizz")
            elif n%5==0:
                res.append("Buzz")
            else:
                res.append(str(n))
            n-=1
        return reversed(res)