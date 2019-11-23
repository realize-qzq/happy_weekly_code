class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Time O(N)
        seen_items=dict()
        for i,x in enumerate(nums):
            if target-x in seen_items:
                return [seen_items[target-x],i]
            else:
                seen_items[x]=i