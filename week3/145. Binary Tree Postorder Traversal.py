# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        cur=[root]
        ans=[]
        while cur:
            head=cur[0]
            if head.left is None and head.right is None:
                ans.append(head.val)
                head.val=float('inf')
                cur.pop(0)
            elif head.left is None and head.right.val!=float('inf'):
                cur.insert(0,head.right)
            elif head.right is None and head.left.val!=float('inf'):
                cur.insert(0,head.left)
            else:
                if (head.left and head.left.val==float('inf')) or (head.right and head.right.val==float('inf')):
                    ans.append(head.val)
                    head.val = float('inf')
                    cur.pop(0)
                else:
                    cur.insert(0,head.right)
                    cur.insert(0,head.left)
        return ans


