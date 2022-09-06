class RandomizedSet:

    def __init__(self):
        self.valList=[]
        
    def insert(self, val: int) -> bool:
        if val in self.valList:
            return False
        self.valList.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.valList:
            self.valList.remove(val)
            return True
        else:
            return False
    def getRandom(self) -> int:
        return choice(self.valList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()