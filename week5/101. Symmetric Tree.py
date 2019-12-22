class Solution:
    def dfs(self,n1,n2):
        if n1 is None and n2 is None:
            return True
        elif n1 is not None and n2 is not None:
            if n1.val!=n2.val:
                return False
            else:
                temp_flag1=self.dfs(n1.left,n2.right)
                if temp_flag1 is False:
                    return False
                temp_flag2=self.dfs(n1.right,n2.left)
                if temp_flag2 is False:
                    return False
                return True
        else:
            return False
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root,root)