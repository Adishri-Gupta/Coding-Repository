class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len,reverse=True)
        n=len(words)
        encodingStr=""
        for i in range(0,n):
            if words[i]+"#" not in encodingStr:
                encodingStr+=words[i]+"#"
                
        return len(encodingStr)
        