class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.valMap=defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.valMap[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        
        minS=math.inf
        
        lword1=self.valMap[word1]
        lword2=self.valMap[word2]
        l1=0
        l2=0
        while l1<len(lword1) and l2<len(lword2):
            
            minS=min(abs(lword1[l1]-lword2[l2]),minS)
            if lword1[l1]<lword2[l2]:
                l1+=1
            else:
                l2+=1
        return minS
            
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)