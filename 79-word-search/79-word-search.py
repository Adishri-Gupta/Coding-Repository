class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        def helper(i,j,pos):
            if pos==len(word):
                return True
            if (i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[pos] or (i,j) in visited):
                return False
            visited.add((i,j))
            res=(helper(i+1,j,pos+1) or 
                 helper(i,j+1,pos+1) or 
                 helper(i-1,j,pos+1) or 
                 helper(i,j-1,pos+1))
            visited.remove((i,j))
            return res
            
                
            
            
        for i in range(len(board)):
                for j in range(len(board[0])):
                    if helper(i,j,0): return True
        return False
        
                