n,k=map(int,input().split())
mods=1000000007
dp=[0]*n
for i in range(1,k+1):
    dp[i]=2**(i-1)
for i in range(k+1,n):
    for j in range(1,k+1):
        dp[i]+=dp[i-j]
print(dp[-1]%mods)