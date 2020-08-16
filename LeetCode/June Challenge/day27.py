class Solution:
    def numSquares(self, n):
        while n%4 ==0: 
            n = n // 4
        if n % 8 == 7: 
            return 4

        if int(math.sqrt(n)) ** 2 == n: 
            return 1

        i = 1
        while i**2 <= n:
            j = math.sqrt(n - i**2)
            if int(j) == j: return 2
            i += 1

        return 3  
        while n%4 ==0: n = n // 4
        if n % 8 == 7: return 4

        if int(math.sqrt(n)) ** 2 == n: return 1

        i = 1
        while i**2 <= n:
            j = math.sqrt(n - i**2)
            if int(j) == j: return 2
            i += 1

        return 3