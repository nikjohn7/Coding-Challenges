class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def factors(n):
            yield 1
            for i in range(2, int(math.sqrt(n)) + 1):
                if not n % i:
                    yield i
                    if i * i != n:
                        yield n // i
                        
        nums.sort()                        
        d = {}            
        for n in nums:
            for f in factors(n):
                tmp = d.get(f, []) + [n]
                d[n] = tmp if len(d.get(n, [])) < len(tmp) else d.get(n, [])
        return nums and max(d.values(), key=len)