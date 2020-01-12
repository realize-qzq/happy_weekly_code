class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==0 or n==1:
            return 0
        ans=0
        for i,x in enumerate(prices):
            if i==0:
                continue
            else:
                if x>prices[i-1]:
                    ans=ans+(x-prices[i-1])#因为没有冷冻周期，利益最大就是把所有相邻2个上升的作为差
        return ans