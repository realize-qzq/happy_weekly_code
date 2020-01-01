class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            pass
        dps=[0]*(n+1)
        dps[1]=1
        dps[2]=2
        for i in range(3,n+1):
            dps[i]=dps[i-1]+dps[i-2]
        return dps[-1]