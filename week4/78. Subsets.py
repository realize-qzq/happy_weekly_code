class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #奇怪的回溯法
        #https://leetcode.com/problems/subsets/discuss/429534/General-Backtracking-questions-solutions-in-Python-for-reference-%3A
        self.n=len(nums)
        self.ans=[]
        self.dfs(nums,0,[])
        return self.ans
    def dfs(self,nums,ind,cur):
        self.ans.append(cur[:])
        for i in range(ind,self.n):
            x=nums[i]
            self.dfs(nums,i+1,cur+[x])