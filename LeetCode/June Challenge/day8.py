class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bins=bin(n).replace("0b", "")
        bins=list(bins)
        if bins.count('1')==1 and n>0:
            return True
        return False