class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans=[]
        for n_hour in range(num+1):
            n_min=num-n_hour
            self.hours=[]
            self.mins=[]
            self.hour_back(n_hour,0,0,0)
            self.min_back(n_min,0,0,0)
            for h in self.hours:
                for m in self.mins:
                    if m<10:
                        temp=str(h)+":"+"0"+str(m)
                    else:
                        temp=str(h)+":"+str(m)
                    ans.append(temp[:])
        return ans
    def min_back(self,n,on_led,cur_min,ind):
        if cur_min>59:
            return
        if ind>=6:
            if on_led==n:
                self.mins.append(cur_min)
            return
        else:
            if on_led==n:
                self.mins.append(cur_min)
                return
            else:
                pass
        for i in range(2):
            if i==1:
                self.min_back(n,on_led+1,cur_min+2**ind,ind+1)
            else:
                self.min_back(n,on_led,cur_min,ind+1)
    def hour_back(self,n,on_led,cur_hour,ind):
        if cur_hour>11:
            return
        if ind>=4:
            if on_led==n:
                self.hours.append(cur_hour)
            return
        else:
            if on_led==n:
                self.hours.append(cur_hour)
                return
            else:
                pass
        for i in range(2):
            if i==1:
                self.hour_back(n,on_led+1,cur_hour+2**ind,ind+1)
            else:
                self.hour_back(n,on_led,cur_hour,ind+1)