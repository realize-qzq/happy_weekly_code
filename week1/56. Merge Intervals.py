class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals==[] or intervals ==[[]]:
            return []
        intervals.sort(key=lambda x:x[0])
        prev=[intervals[0][0],intervals[0][1]]
        ans=[prev[:]]
        for i,x in enumerate(intervals):
            #相交
            s0,e0=prev
            s1,e1=x
            if s1<=e0:
                end=max(e0,e1)
                start=s0
                ans[-1]=[start,end]
            elif s1>e0:
                #相离
                start,end=s1,e1
                ans.append([start,end])
            else:
                print("no")
            prev=ans[-1]
        return ans