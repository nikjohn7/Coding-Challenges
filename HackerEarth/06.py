arr=[]
n=int(input())
for _ in range(n):
    arr.append(int(input()))
dp=[1]*n
# print(dp, arr)
for i in range(1,n):
    if arr[i]>arr[i-1]:
        dp[i]=dp[i-1]+1
for i in range(n-2, -1, -1):
    if arr[i]>arr[i+1] and dp[i]<=dp[i+1]:
        dp[i]=dp[i+1]+1
print(sum(dp))