# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        nums=list(range(1,n+1));
        self.ans=[]
        if n==0: return []
        return self.gen(nums)
    def gen(self,nums):
        result=[]
        n=len(nums)
        if n==0:
            return [None]
        for i in range(n):
            lefts=nums[:i]
            rights=nums[i+1:]
            rleft=self.gen(lefts)
            rright=self.gen(rights)
            i1,j1=len(rleft),len(rright)
            for x in rleft:
                for y in rright:
                    root=TreeNode(nums[i])
                    root.left=x
                    root.right=y
                    result.append(root)
        return result