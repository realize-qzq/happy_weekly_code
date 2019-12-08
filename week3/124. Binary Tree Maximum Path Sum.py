class Solution(object):
    def dfs(self,root):
        if root is None:
            return 0
        left=self.dfs(root.left)
        right=self.dfs(root.right)
        self.maxs=max(self.maxs,root.val+left+right)
        return max(0,root.val+left,root.val+right)
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxs=float('-inf')
        self.dfs(root)
        return self.maxs
        