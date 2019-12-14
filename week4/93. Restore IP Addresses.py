class Solution:
    def back(self,ind,s,cur,seg_ind):
        if seg_ind>=4:
            if ind>=len(s):
                self.ans.append(".".join(cur))
                return
            else:
                return
        for seg_long in range(1,4):
            if ind+seg_long>len(s):
                return
            x=s[ind:ind+seg_long]
            if len(x)!=1:
                start_ind=ind
                while start_ind<ind+seg_long:
                    temp=s[start_ind]
                    if temp!="0":
                        if start_ind==ind:
                            break
                        else:
                            return#过滤"1.01.3.2"
                    start_ind+=1
                if start_ind==ind+seg_long:#过滤"1.00.3.2"
                    return
            if int(x)<=255:
                self.back(ind+seg_long,s,cur+[x],seg_ind+1)
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans=[]
        self.back(0,s,[],0)
        return self.ans