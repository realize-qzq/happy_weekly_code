class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(word1)
        n=len(word2)
        if m==0 or n==0:
            return m+n
        dp=[[float('inf')]*n for i in range(m)]#用word1去追word2，word2为目标（因为结果值肯定是互易的）
        for j in range(n):
            s2=word2[j]
            for i in range(m):
                s1=word1[i]
                if i==0 and j==0:
                    dp[i][j]=0 if s1==s2 else 1
                    continue
                elif i==0:
                    if s1 in word2[:j+1]:
                        dp[i][j]=j
                    else:
                        dp[i][j]=j+1
                    continue
                elif j==0:
                    if s2 in word1[:i+1]:
                        dp[i][j]=i
                    else:
                        dp[i][j]=i+1
                    continue
                else:
                    temp=0
                    if s1==s2:
                        temp=dp[i-1][j-1]#继承上一个
                    else:
                        temp=dp[i-1][j-1]+1#改
                    #增进
                    add=dp[i][j-1]+1
                    #删除
                    delete=dp[i-1][j]+1
                    dp[i][j]=min(dp[i][j],temp,add,delete)
        return dp[-1][-1]