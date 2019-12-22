class Solution:
    def dfs(self,root):
        if root is None:
            return None,None
        l_head,l_tail=self.dfs(root.left)
        r_head,r_tail=self.dfs(root.right)
        root.left=None
        if l_head is None and l_tail is None:
            l_head=root
            l_tail=root
        elif l_head is None:
            root.right=l_tail
    
        elif l_tail is None:
            root.right=l_head

            l_tail=l_head#给l_tail一个不None，给后面r_head用
        else:
            root.right=l_head
            
        
        
        if r_head is None and r_tail is None:
            l_tail.right=None
            return root,l_tail
        elif r_head is None:
            l_tail.right=r_tail
           
            return root,r_tail
        elif r_tail is None:
            l_tail.right=r_head
           
            return root,r_head
        else:
            l_tail.right=r_head
            return root,r_tail
               
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #靠，不需要root.left接上一个，只需要一直管right就行了
        self.dfs(root)
        