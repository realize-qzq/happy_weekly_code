class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n=len(people)
        people=sorted(people,key=lambda comp:[-comp[0],comp[1]])#优先比较数字的大小，大的在前，然后同数字按照ind升序
        res=[]
        for i,x in enumerate(people):
            value,ind=x[0],x[1]
            res.insert(ind,[value,ind])#动态插入的方法
        return res