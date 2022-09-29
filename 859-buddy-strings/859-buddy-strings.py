class Solution:
    
    #1 - if both strings length not matching, return false
    #2 - if both strings are equal, but have any character repeating more than once, its swappable so return true
    #3 - if more than 2 diffs, it won't match by swapping twice, so return false
    #4 - When the diff is exactly two, for it to be swappable, the sorted values of both diffs should match up and return true, else false.
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        
        if s==goal and len(set(s))!=len(s):
            return True
        diff=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                diff.append(i)
        if len(diff)>2:
            return False
        if len(diff)==2:
            i,j=diff[0],diff[1]
            if s[i]!=goal[j] or s[j]!=goal[i]:
                return False
            else:
                return True
        return False
                
        