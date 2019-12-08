class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        left_node = self.invertTree(root.left)
        right_node = self.invertTree(root.right)
        root.left = right_node
        root.right = left_node
        return root