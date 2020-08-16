class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        temp1=A.copy()
        temp2=A.copy()
        f=0
        for i in range(1,len(A)):
            if temp1[i-1]>0:     #find max one without circular
                temp1[i]+=temp1[i-1]
                f=1
            if temp2[i-1]<0:     #find min one without circular
                temp2[i]+=temp2[i-1]
        if f==0:
            return max(A)
        return max(max(temp1),(sum(A)-min(temp2)))