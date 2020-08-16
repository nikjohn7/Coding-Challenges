inf=10**10
N=int(input())
H=list(map(int,input().split()))
dp = [inf for _ in range(N)]
dp[0]=0
for i in range(N):
    if i+1<N:
        dp[i+1] = min(dp[i+1],dp[i]+abs(H[i+1]-H[i]))
    if i+2<N:
        dp[i+2] = min(dp[i+2],dp[i]+abs(H[i+2]-H[i]))
print(dp[N-1])