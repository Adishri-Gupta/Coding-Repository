class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        final=[]
        l,r=0,len(products)-1
        for i in range(len(searchWord)):
            c=searchWord[i]
            
            while l<=r and (len(products[l])<=i or products[l][i]!=c):
                l+=1
            while l<=r and (len(products[r])<=i or products[r][i]!=c):
                r-=1
            final.append([])
            for k in range(min(3,r-l+1)):
                final[-1].append(products[l+k])
                    
        return final