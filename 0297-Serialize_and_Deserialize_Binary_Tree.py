# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        ret = []

        while q:
            node = q.popleft()
            if node is None:
                ret.append(None)
            else:
                ret.append(node.val)
                q.extend([node.left, node.right])
        
        # remove redundancy None
        while ret and ret[-1] is None:
            ret.pop()

        return str(ret)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = deque(eval(data))
        if len(data) == 0:
            return None
            
        root = TreeNode(data.popleft())
        q = deque([root])

        while q:
            node = q.popleft()
            if data:
                val = data.popleft()
                node.left = TreeNode(val) if val is not None else None
            
            if data:
                val = data.popleft()
                node.right = TreeNode(val) if val is not None else None
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
