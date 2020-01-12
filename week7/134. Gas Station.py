class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        start=0
        sums=0
        localsum=0
        res=0
        for i,g in enumerate(gas):
            x=g-cost[i]
            sums+=x
            localsum+=x
            if localsum<0:
                localsum=0
                start=(i+1)%n
        if sums>=0:
            return start
        else:
            return -1