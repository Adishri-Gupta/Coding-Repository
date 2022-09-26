class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapR=defaultdict(list)
        inDeg=defaultdict(int)
        ans=[]
        for pre in prerequisites:
            x=pre[0]
            y=pre[1]
       
            mapR[y].append(x)
            
            inDeg[x]+=1
            
    
            
        q=deque()
        for i in range(numCourses):
            if inDeg[i]==0:
                q.append(i)
            
        while q:
            curr=q.popleft()
            ans.append(curr)
            for nei in mapR[curr]:
                inDeg[nei]-=1
                if inDeg[nei]==0:
                    q.append(nei)
        return len(ans)==numCourses 
        