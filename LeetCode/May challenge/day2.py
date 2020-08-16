class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d=dict()
        sums=0
        for i in S:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in J:
            if i in d:
                sums+=d[i]
        return sums