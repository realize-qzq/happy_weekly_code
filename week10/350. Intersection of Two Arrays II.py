from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c=Counter(nums1)
        ans=[]
        for x in nums2:
            if x in c and c[x]>0:
                ans.append(x)
                c[x]-=1
        return ans