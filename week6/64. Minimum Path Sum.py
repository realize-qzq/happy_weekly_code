class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        dp = [[float('inf')] * n for i in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if j!=0:
                    left = dp[i][j - 1]#不能用try ,except，因为dp[-1]没有违规，马德
                else:
                    left = float('inf')
                if i!=0:
                    top = dp[i - 1][j]
                else:
                    top = float('inf')
                dp[i][j] = min(dp[i][j], left, top) + grid[i][j]
        return dp[-1][-1]
if __name__=="__main__":
    grid=[[1,3,1],[1,5,1],[4,2,1]];
    sol=Solution()
    ans=sol.minPathSum(grid)
    print(ans)