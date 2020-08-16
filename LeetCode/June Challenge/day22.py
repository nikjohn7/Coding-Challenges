from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=Counter(nums)
        return (list(d.keys())[list(d.values()).index(1)]) 