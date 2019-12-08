# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res=[]
        cur=[root]
        while cur:
            head=cur.pop(0)
            res.append(head.val)  
            if head.right:
                cur.insert(0,head.right)
            if head.left:
                cur.insert(0,head.left)
        return res
