mods=1000000007
# Write your code here
cl, amount = map(int, input().split())
arr=list(map(int, input().split()))
dp=[[0 for i in range(amount+1)] for j in range(cl)]

for i in range(cl):
    dp[i][0]=1

for i in range(cl):
    for j in range(1, amount+1):
        a = dp[i-1][j] if i>0 else 0
        b = dp[i][j-arr[i]] if (j-arr[i])>=0 else 0
        dp[i][j]=a+b

print(dp[cl-1][amount]%mods)