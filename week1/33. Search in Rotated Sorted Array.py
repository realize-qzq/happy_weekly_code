from bisect import bisect_left as bl
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #[末前，末尾]+[起始,中间]  先寻求末尾最大数的索引
        n=len(nums)
        if n==0:
            return -1
        i,j=0,n-1
        while i<j:
            mid=(i+j)//2
            x=nums[mid]
            if target==x:
                return mid
            if x<nums[i]:
                j=mid-1
            elif x>nums[i]:
                i=mid
            else:
                #相等，即[nums[i],nums[j]]只有这2个元素了,j=i+1的情况
                if nums[j]>nums[i]:
                    i=j
                else:
                    j=i
        #最后i代表了末尾最大数的索引
        maxs=nums[i]
        if target>maxs:
            return -1
        ind=None
        if i==n-1:#没有旋转的数组
            if target<nums[0]:
                return -1
            else:
                ind=bl(nums,target)
        else:#有旋转的数组
            if target<=nums[n-1]:
                ind=bl(nums[i+1:],target)
                ind=ind+i+1
            else:
                ind=bl(nums[0:i+1],target)
        if ind>=n or nums[ind]!=target:
            return -1
        else:
            return ind
if __name__=="__main__":
    sol=Solution()
    nums=[4,5,6,7,0,1,2]
    nums=[3,5,1]
    target = 3
    ans=sol.search(nums,target)
    print(ans)