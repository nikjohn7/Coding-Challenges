class Solution:

    def __init__(self, w: List[int]):
        self.cdf = [0]
        for weight in w:
            self.cdf.append(self.cdf[-1] + weight)

    def pickIndex(self) -> int:
        rand = random.randint(1, self.cdf[-1])
        idx = bisect.bisect_left(self.cdf, rand)
        return idx - 1