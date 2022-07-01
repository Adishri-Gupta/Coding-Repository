class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        solution = []
        def helper(subset,index,total,target,array,solution):
            
            if index >= len(array):
                if total == target:
                    solution.append(subset[:])
                    return
                
                return
                    
            if total > target:
                return
            
            helper(subset,index+1,total,target,array,solution)
            

            helper(subset+[array[index]],index,total+array[index],target,array,solution)

            
              
            return 
        

        helper([],0,0,target,candidates,solution)
        return solution