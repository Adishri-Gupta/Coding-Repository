class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        indegree=defaultdict(int)
        q=deque()
        res=[]
        for pre in prerequisites:
            a=pre[0]
            b=pre[1]
            
            graph[b].append(a)
            indegree[a]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            ele=q.popleft()
            res.append(ele)
            for value in graph[ele]:
                indegree[value]-=1
                if indegree[value]==0:
                    q.append(value)
        return True if len(res)==numCourses else False
            
        