# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        tmpnodes = []
        swapnodes = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            tmpnodes.append(node)
            if len(tmpnodes) > 2:
                del tmpnodes[0]
            if len(tmpnodes) == 2 and tmpnodes[0].val > tmpnodes[1].val:
                if len(swapnodes) == 0:
                    swapnodes.append(tmpnodes[0])
                    swapnodes.append(tmpnodes[1])
                else:
                    swapnodes[1] = tmpnodes[1]

            inorder(node.right)

        inorder(root)

        swapnodes[0].val, swapnodes[1].val = swapnodes[1].val, swapnodes[0].val
