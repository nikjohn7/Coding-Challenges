class Solution:
    def firstUniqChar(self, s: str) -> int:
        lis=list(s)
        d={}
        for i in lis:
            if i in d:
                d[i]=1
            else:
                d[i]=0
        for i in lis:
            if d[i]==0:
                return lis.index(i)
        return -1