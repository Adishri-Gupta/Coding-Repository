class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n=len(grid)   
        parent=[i for i in range(n)]
        rank=[1]*n
       
        def convert(a):
            adjList = defaultdict(list)
            for i in range(len(a)):
                for j in range(len(a[i])):
                               if a[i][j]== 1:
                                   adjList[i].append(j)
            return adjList
     
        
        def find(n1):
            parValue=n1
            
            while parValue!=parent[parValue]:
                parValue=parent[parent[parValue]]
                parValue=parent[parValue]
                
            return parValue
            
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1 == p2:
                return 0
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return 1
        
        edges=convert(grid)
        result=n
        for n1 in edges:
            for n2 in edges[n1]:
                result-=union(n1,n2)
        return result
 
       