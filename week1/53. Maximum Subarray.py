class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs=float('-inf')
        n=len(nums)
        sums=0
        for i in range(n):
            x=nums[i]
            sums+=x
            maxs=max(maxs,sums)
            if sums<0:
                sums=0
        return maxs