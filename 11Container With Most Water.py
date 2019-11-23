class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        i,j=0,n-1
        maxs=0
        while i<j:
            x1,x2=height[i],height[j]
            cur=min(x1,x2)*(j-i)
            maxs=max(maxs,cur)
            if x1<x2:
                i+=1
            else:
                j-=1
        return maxs