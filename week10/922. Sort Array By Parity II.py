class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even=0
        odd=1
        while even<len(A):
            even_val=A[even]
            if even_val%2==1:
                odd_val=A[odd]
                while odd_val%2==1:#找到第一个奇数位上的偶数，和它换
                    odd+=2
                    odd_val=A[odd]
                A[even],A[odd]=A[odd],A[even]
            even+=2
        return A