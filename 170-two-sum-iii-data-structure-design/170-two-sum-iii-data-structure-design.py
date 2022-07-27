class TwoSum:

    def __init__(self):
        self.nums=[]

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        mapDiff={}
        for i in range(len(self.nums)):
            
            val=value-self.nums[i]
            if val in mapDiff:
                return True
            mapDiff[self.nums[i]]=i
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)