class WordDistance:

    def __init__(self, wordsDict: List[str]):
        
        self.valMap=defaultdict(list)
        for i,words in enumerate(wordsDict):
            self.valMap[words].append(i)
    def shortest(self, word1: str, word2: str) -> int:
        minD=math.inf
        for i in self.valMap[word1]:
            for j in self.valMap[word2]:
                minD=min(minD,abs(j-i))
        return minD
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)