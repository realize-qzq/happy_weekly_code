class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        if len(nums)<=1:
            return
        kong=[]

        if len(nums)%2==1:
            i1=len(nums)//2
        else:
            i1=len(nums)//2-1
        mid=i1
        i2=len(nums)-1
        #小大小
        #小大小大
        #所以前面的更长
        #而且是2边都是倒着的，不然都往前走的话会有4，5，5，6反例
        while i2>mid:
            x1,x2=nums[i1],nums[i2]
            kong.append(x1)
            kong.append(x2)
            i1-=1
            i2-=1
        while len(kong)<len(nums):
            x1=nums[i1]
            kong.append(x1)
            i1-=1
        for i,x in enumerate(kong):
            nums[i]=x