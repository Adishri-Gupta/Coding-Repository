class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent=[i for i in range(n)]
        rank=[1]*n
        
        def find(n1):
            parValue=n1
            
            while parValue!=parent[parValue]:
                parValue=parent[parent[parValue]]
                parValue=parent[parValue]
                
            return parValue
            
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1 == p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return True
        if len(edges) != n - 1: return False
        for n1,n2 in edges:
            if not union(n1,n2):
                return False
        return True