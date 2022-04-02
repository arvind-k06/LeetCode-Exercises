# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d ={}
        def traverse(node, level):
            if node:
                if level not in d:
                    d[level] = []
                d[level].append(node.val)
                traverse(node.left, level+1)
                traverse(node.right, level+1)
        
        traverse(root,0)
        
        return [d[i] for i in d]
        