from collections import Counter
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nc1=Counter(nums1)
        kong=set()
        for x in nums2:
            if x in nc1 and x not in kong:
                kong.add(x)
        return list(kong)