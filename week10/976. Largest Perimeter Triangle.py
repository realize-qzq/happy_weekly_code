class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        j=len(A)-1
        while j>1:
            x3=A[j]
            x2=A[j-1]
            x1=A[j-2]
            if x1+x2<=x3:
                j-=1
            else:
                return x1+x2+x3
        return 0