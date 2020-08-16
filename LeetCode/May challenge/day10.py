class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        l1=[l[0] for l in trust]
        l2=[l[1] for l in trust]
        num=list(range(1,N+1))
        if len(l1)==N:
            return -1
        suspects=list(set(num).difference(set(l1)))
        for i in suspects:
            if l2.count(i)==N-1:
                return i
        return -1