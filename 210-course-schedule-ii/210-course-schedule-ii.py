class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        final = []
        for course,pre in prerequisites:
            preMap[course].append(pre)
        
        visit,cycle = set(), set()
        def dfs(crs):
          
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for prereq in preMap[crs]:
                if not dfs(prereq): return False
            cycle.remove(crs)
            visit.add(crs)
            final.append(crs)
            return True
        
        
        for course in range(numCourses):
            if not dfs(course): return []
        return final