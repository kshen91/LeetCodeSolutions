# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack = [root]
        visited = []
        ret = []
        
        while stack:
            node = stack[-1]
            
            if node.right is not None and node.right not in visited:
                stack.append(node.right)
                
            if node.left is not None and node.left not in visited:
                stack.append(node.left)
            
            if (node.left is None or node.left in visited) and (node.right is None or node.right in visited):
                node = stack.pop()
                ret.append(node.val)
                visited.append(node)
            
        return ret  
