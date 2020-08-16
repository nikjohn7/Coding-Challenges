class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [0] * (len(B) + 1)
        for i in range(len(A)):
            for j in range(len(B))[::-1]:
                if A[i] == B[j]: dp[j + 1] = dp[j] + 1
            for j in range(len(B)):
                dp[j + 1] = max(dp[j + 1], dp[j])
        return dp[len(B)]