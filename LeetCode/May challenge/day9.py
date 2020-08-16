class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        if n<2:
            return True
        l,r=2,(n//2)
        while l<=r:
            mid=(l+r)//2
            sq=mid*mid

            if sq==n:
                return True
            elif sq<n:
                l=mid+1
            else:
                r=mid-1
        return False