# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Solution 1
    def longestUnivaluePath1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        sub = max( self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right) )
        return max( sub, self.helper(root.left, root.val) + self.helper(root.right, root.val))

    def helper(self, node, parentVal):
        if( node is None or node.val != parentVal ):
            return 0

        return 1 + max(self.helper(node.left, node.val), self.helper(node.right, node.val))

    # Solution 2
    def longestUnivaluePath2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def arrow_length(node):
            if not node:
                return 0

            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)

            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1

            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1

            self.ans = max(self.ans, left_arrow + right_arrow)

            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
