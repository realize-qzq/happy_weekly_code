class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        buy=[0]*n
        sell=[0]*n
        buy[0]=-prices[0]
        for i,x in enumerate(prices):
            if i==0:
                continue
            else:
                buy[i]=max(sell[i-1]-x,buy[i-1])
                sell[i]=max(buy[i-1]+x-fee,sell[i-1])
        return max(buy[-1],sell[-1])