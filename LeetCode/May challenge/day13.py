class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        for d in num:
            while k and res and res[-1] > d:
                res.pop()
                k -= 1
            res.append(d)
        return ''.join(res[:-k or None]).lstrip('0') or '0'    