class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        listEdges=defaultdict(list)
        self.n=n
        
        if len(edges)!=n-1: 
            return False
        
        for edge in edges:
            [i,j]=edge
            listEdges[i].append(j)
            listEdges[j].append(i)
        return self.isConnected(listEdges)
    def isConnected(self,listEdges):
        visited=set()
        queue=deque([0])
        visited.add(0)
        while queue:
            ele=queue.popleft()
            for nei in listEdges[ele]:
                if nei in visited:
                    continue
                visited.add(nei)
                queue.append(nei)
        return len(visited)== self.n
    
       
                