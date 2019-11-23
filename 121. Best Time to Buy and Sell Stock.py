class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n=len(prices)
        mins=float('inf')
        maxs=0
        for i,x in enumerate(prices):
            mins=min(mins,x)
            if i==0:
                continue
            delta=x-mins
            maxs=max(maxs,delta)
        return maxs