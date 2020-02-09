class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        self.quicksort(points,0,len(points)-1,K)
        return points[:K]
    def quicksort(self,points,i,j,K):
        if i>=j:
            return
        index=self.partition(points,i,j)
        if index==K:
            return
        elif index>K:
            self.quicksort(points,i,index-1,K)#如果不减1，会陷入无限递归，如果index==j且index>k
        else:
            self.quicksort(points,index+1,j,K)
    def partition(self,nums,s,e):
        start=s-1
        for j in range(s,e):
            x=nums[j]
            y=nums[e]
            xx=x[0]*x[0]+x[1]*x[1]
            yy=y[0]*y[0]+y[1]*y[1]
            if xx<yy:
                start+=1
                nums[start],nums[j]=nums[j],nums[start]
        nums[start+1],nums[e]=nums[e],nums[start+1]
        return start+1