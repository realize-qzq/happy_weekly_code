class Solution:
    def dfs(self,root,num=1):
        if root is None:
            self.maxs=max(self.maxs,num)
            return
        #这里不能写if root.left 因为叶子节点进不去下面2个dfs，就不能进入if root is None
        self.dfs(root.left,num+1)
        self.dfs(root.right,num+1)
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.maxs=0
        self.dfs(root,0)
        return self.maxs