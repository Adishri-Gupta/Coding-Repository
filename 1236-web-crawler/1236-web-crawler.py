# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        q=deque()
        q.append(startUrl)
        visited=set()
        ans=[startUrl]
        visited.add(startUrl)
        domain = startUrl.split("http://")[1].split("/")[0]
        while q:
            url = q.popleft()
           
         
            
            urlList = htmlParser.getUrls(url)
            for u in urlList:
                if u in visited:
                    continue
                if u.split("http://")[1].split("/")[0]!=domain:
                    continue
                q.append(u)
                ans.append(u)
                visited.add(u)
        
        return ans
            
            
            
        