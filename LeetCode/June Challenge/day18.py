class Solution:
    def hIndex(self, citations):
        if not citations:
            return 0
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if citations[m] >= n - m:
                r = m - 1
            else:
                l = m + 1
        return n - r - 1