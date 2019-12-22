class Solution:
    def make(self,nums):
        n=len(nums)
        if n==0:
            return None
        elif n==1:
            return TreeNode(nums[0])
        elif n==2:
            n1,n2=TreeNode(nums[0]),TreeNode(nums[1])
            n2.left=n1
            return n2
        else:
            root=TreeNode(nums[n//2])
            left_tree=self.make(nums[:n//2])
            right_tree=self.make(nums[n//2+1:])
            root.left=left_tree
            root.right=right_tree
            return root
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.make(nums)