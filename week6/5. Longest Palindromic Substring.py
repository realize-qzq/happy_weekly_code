class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.longstr=""
        self.maxs=0
        #中心外扩，并且分为奇数长度和偶数长度2种,可以提前终止，虽然O(N*N)，但是剪枝了很多
        for i,x in enumerate(s):
            self.helper(s,i,i)#奇数长度
            self.helper(s,i,i+1)
        return self.longstr
    def helper(self,s,low,high):
        lowbias=0
        highbias=len(s)-1
        while low>=lowbias and high<=highbias:
            if s[low]==s[high]:
                cur=high-low+1;
                if cur>=self.maxs:
                    self.longstr=s[low:high+1]
                    self.maxs=cur
                low-=1
                high+=1
            else:
                break
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n=len(s)
#         dp=[[0]*n for i in range(n)]
#         maxs=[0,[0,0]]
#         for k in range(n):
#             for i in range(n-k):
#                 j=i+k;
#                 dp[j][j] = 1;#不能在外循环里加，不然i=0,j=3的时候，没有经过dp[2][2]
#                 if j==i:
#                     pass
#                 elif k==1:
#                     if s[i]==s[j]:
#                         dp[i][j]=1
#                 else:
#                     if s[i]==s[j] and dp[i+1][j-1]==1:
#                         dp[i][j]=1
#                 if dp[i][j]==1 and j-i>=maxs[0]:
#                     maxs=[j-i,[i,j]]
#         ii,jj=maxs[1]
#         return s[ii:jj+1]
#
# if __name__=="__main__":
#     sol=Solution()
#     s="aaaa"
#     ans=sol.longestPalindrome(s)
#     print(ans)