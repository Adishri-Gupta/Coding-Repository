class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        # for i in range(len(s)-1,0,-1):
        #     word.append(s[i])
        #     if s[i]==' ':
        #         res.append(reverse)
        word=s.split()
        word.reverse()
        return ' '.join(word)
                
                
            
            