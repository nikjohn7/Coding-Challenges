from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        st=''
        for w in sorted(d, key=d.get, reverse=True):
            st+=w*d[w]
        return st