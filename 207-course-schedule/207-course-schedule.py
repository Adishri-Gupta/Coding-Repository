class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        
        for course,pre in prerequisites:
            preMap[course].append(pre)
        
        visited = set()
        def dfs(crs):
          
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            
            visited.add(crs)
            for prereq in preMap[crs]:
                if not dfs(prereq): return False
            visited.remove(crs)
            preMap[crs]=[]
            return True
        
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True