class Solution:
    def countBits(self, num: int) -> List[int]:
        d = {0: 0, 1: 1, 2: 1}
        if num == 1:
            return [0, 1]
        if num == 0:
            return [0]
        for x in range(3, num+1):
            quotient, reminder = divmod(x, 2)
            d[x] = d[quotient] + d[reminder]
        return list(d.values())