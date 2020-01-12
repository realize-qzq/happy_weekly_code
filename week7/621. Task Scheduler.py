from heapq import *
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        pq=[]
        mydict={}
        for x in tasks:
            mydict[x]=mydict.get(x,0)+1
        for key in mydict:
            heappush(pq,(-mydict[key],[key,mydict[key]]))

        cnt=0
        while pq!=[]:
            addedkey=[]
            for i in range(n+1):
                if len(pq)>0:#必须满足这个，步满足这个进入等待时间
                    item=heappop(pq)[1]#下一个是除自己以外的数目最多的
                    key,val=item[0],item[1]
                    if val>1:
                        mydict[key] = mydict[key] - 1
                        addedkey.append(key)
                    else:
                        mydict.pop(key)
                        pass
                cnt+=1
                if pq==[] and len(mydict)==0:
                    return cnt
            for key in addedkey:#不能用mydict，因为当n=0时候，会插入没有使用的值，因为n=0，一次只用1个值
                val=mydict[key]
                heappush(pq, (-val , [key, val ]))
        return cnt

if __name__=="__main__":
    sol=Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    cnt=sol.leastInterval(tasks,n)
    print(cnt)