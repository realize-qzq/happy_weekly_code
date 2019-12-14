class Solution:
    def back(self, nums, cur):
        if nums == []:
            self.ans.append(cur[:])
            return
        for i, x in enumerate(nums):
            self.back(nums[:i] + nums[i + 1:], cur + [x])

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.back(nums, [])
        return self.ans