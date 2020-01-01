class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(nums)
        buy=[float('-inf')]*n
        sell=[float('-inf')]*n
        maxs=0
        if n==0:
            return 0
        for i in range(n):
            if i==0:
                buy[i]=0-nums[i]
                sell[i]=0
            elif i==1:
                buy[i]=max(buy[i-1],-nums[i])
                sell[i]=max(buy[i-1]+nums[i],sell[i-1])
            else:
                buy[i]=max(buy[i-1],sell[i-2]-nums[i])#buy[i]里max的分别是今天买或者不买（利润自然和昨天一样，buy[i])
                sell[i]=max(buy[i-1]+nums[i],sell[i-1])#sell[i]里max的分别是今天卖或者不卖（利润自然和昨天一样，sell[i])
        return sell[-1]