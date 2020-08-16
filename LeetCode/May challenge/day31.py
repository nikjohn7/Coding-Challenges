class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        if M * N == 0:
            return M + N
        dp = [[0] * (N + 1) for i in range(M + 1)]

        for i in range(M + 1):
            dp[i][0] = i
        for i in range(N + 1):
            dp[0][i] = i
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]))
        return dp[M][N]