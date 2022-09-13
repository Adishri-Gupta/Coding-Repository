# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mapVal={}
        for desc in descriptions:
            [par, child, left]=desc
            
            
            if par in mapVal:
                node = mapVal[par]
            else:
                node = TreeNode(par)
                mapVal[par]=node
                
            if child in mapVal:
                childNode = mapVal[child]
            else:
                childNode = TreeNode(child)
                mapVal[child]=childNode
                
            if left ==1:
                node.left=childNode
            else:
                node.right=childNode
                
        for desc in descriptions:
            del mapVal[desc[1]]
        
        return list(mapVal.values())[0]
            
            
            