class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        curmaxs=0
        for i,x in enumerate(nums):
            curmaxs=max(curmaxs,i+x)
            if curmaxs>=n-1:
                return True
            if curmaxs<=i:
                return False
        return curmaxs>=n