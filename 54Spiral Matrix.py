class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rs,rn=0,len(matrix)-1
        if rn<rs:
            return []
        cs,cn=0,len(matrix[0])-1
        if cn<cs:
            return []
        #row start, row end
        #column start, column end
        sp=0
        ans=[]
        while rs<=rn and cs<=cn:
            if sp==0:
                for j in range(cs,cn+1):
                    item=matrix[rs][j]
                    ans.append(item)
                rs+=1
            elif sp==1:
                for i in range(rs,rn+1):
                    item=matrix[i][cn]
                    ans.append(item)
                cn-=1
            elif sp==2:
                for j in range(cn,cs-1,-1):
                    item=matrix[rn][j]
                    ans.append(item)
                rn-=1
            else:
                for i in range(rn,rs-1,-1):
                    item=matrix[i][cs]
                    ans.append(item)
                cs+=1
            sp+=1
            sp%=4
        return ans