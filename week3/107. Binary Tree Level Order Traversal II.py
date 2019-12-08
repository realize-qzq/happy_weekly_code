# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans=[]
        curlevel=[root]
        nextlevel=[]
        while curlevel!=[]:
            temp=[]
            for node in curlevel:
                temp.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            ans=[temp]+ans
            curlevel=nextlevel
            nextlevel=[]
        return ans