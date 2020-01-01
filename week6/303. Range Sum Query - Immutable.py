class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.dp=[0]*(self.n+1)
        for i,x in enumerate(nums):
            self.dp[i+1]=self.dp[i]+x
    def sumRange(self, i: int, j: int) -> int:
        a=self.dp[j+1]
        b=self.dp[i]
        return a-b


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)