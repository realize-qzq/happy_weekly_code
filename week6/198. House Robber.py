class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            pass
        theals = [0] * (n + 1)
        theals[1] = nums[0]
        for i, x in enumerate(nums):
            if i < 1:
                continue
            j = i + 1
            theals[j] = max(theals[j - 1], theals[j - 2] + x)
        return theals[-1]
